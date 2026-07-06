"""Thin Wikidata helpers: name folding, SPARQL, and the entity search/get APIs.

Standard-library only. All requests carry a descriptive User-Agent per the
Wikimedia API etiquette.
"""

import json
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "bamboo-filing-cabinet-vietnam-elections-wikidata/0.1 (https://github.com/bamboo-filing-cabinet/vietnam-elections-wikidata)"
SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
API_ENDPOINT = "https://www.wikidata.org/w/api.php"

# Position: member of the National Assembly of Vietnam (verified 2026-07-04).
POSITION_MEMBER_NA = "Q10841192"


def fold(name: str) -> str:
    """Lowercase, strip Vietnamese diacritics, collapse whitespace.

    Handles đ/Đ explicitly since NFD does not decompose them.
    """
    if not name:
        return ""
    name = name.replace("đ", "d").replace("Đ", "D")
    decomposed = unicodedata.normalize("NFD", name)
    stripped = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    return " ".join(stripped.lower().split())


_last_request_at = 0.0
MIN_INTERVAL = 0.35  # seconds between requests, to stay polite / avoid 429


def _get(url: str, retries: int = 5) -> bytes:
    global _last_request_at
    last_err = None
    for attempt in range(retries):
        gap = MIN_INTERVAL - (time.monotonic() - _last_request_at)
        if gap > 0:
            time.sleep(gap)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code == 429:
                retry_after = e.headers.get("Retry-After")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else 5.0 * (attempt + 1)
                time.sleep(delay)
            else:
                time.sleep(2.0 * (attempt + 1))
        except Exception as e:  # noqa: BLE001 - retry any transient failure
            last_err = e
            time.sleep(2.0 * (attempt + 1))
        finally:
            _last_request_at = time.monotonic()
    raise last_err


def sparql(query: str) -> list[dict]:
    """Run a SPARQL query, return the bindings list."""
    url = SPARQL_ENDPOINT + "?" + urllib.parse.urlencode({"query": query, "format": "json"})
    data = json.loads(_get(url))
    return data["results"]["bindings"]


def search_entities(term: str, language: str = "vi", limit: int = 10) -> list[str]:
    """Return candidate QIDs for a label search via wbsearchentities."""
    url = API_ENDPOINT + "?" + urllib.parse.urlencode(
        {
            "action": "wbsearchentities",
            "search": term,
            "language": language,
            "uselang": language,
            "type": "item",
            "limit": str(limit),
            "format": "json",
        }
    )
    data = json.loads(_get(url))
    return [r["id"] for r in data.get("search", [])]


def get_entities(qids: list[str]) -> dict[str, dict]:
    """Fetch full entity JSON for up to 50 QIDs per call (wbgetentities)."""
    out: dict[str, dict] = {}
    for i in range(0, len(qids), 50):
        batch = qids[i : i + 50]
        url = API_ENDPOINT + "?" + urllib.parse.urlencode(
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "labels|aliases|claims",
                "languages": "vi|en",
                "format": "json",
            }
        )
        data = json.loads(_get(url))
        out.update(data.get("entities", {}))
        time.sleep(0.2)
    return out


def entity_dob(entity: dict) -> str | None:
    """Extract the P569 date of birth as ISO 'YYYY-MM-DD' (day precision only)."""
    claims = entity.get("claims", {}).get("P569", [])
    for c in claims:
        try:
            val = c["mainsnak"]["datavalue"]["value"]
            precision = val.get("precision", 0)
            # 11 = day precision. Lower precision (year/month) is not a safe DOB match.
            if precision >= 11:
                # time looks like "+1962-04-19T00:00:00Z"
                return val["time"][1:11]
        except (KeyError, TypeError):
            continue
    return None


def entity_is_human(entity: dict) -> bool:
    for c in entity.get("claims", {}).get("P31", []):
        try:
            if c["mainsnak"]["datavalue"]["value"]["id"] == "Q5":
                return True
        except (KeyError, TypeError):
            continue
    return False


def entity_names(entity: dict) -> set[str]:
    """All folded labels + aliases (vi, en) for an entity."""
    names: set[str] = set()
    for lang_map in (entity.get("labels", {}), *(v for v in [entity.get("aliases", {})])):
        for lang in ("vi", "en"):
            v = lang_map.get(lang)
            if isinstance(v, dict):
                names.add(fold(v["value"]))
            elif isinstance(v, list):
                for a in v:
                    names.add(fold(a["value"]))
    return {n for n in names if n}
