"""Load vietnam-elections data from the sibling checkout or published exports.

Prefers ../vietnam-elections/public/data/elections/<cycle>/ when running
inside the monorepo; falls back to the GitHub Pages exports.
"""

from pathlib import Path

SIBLING_ROOT = Path(__file__).resolve().parents[2] / "vietnam-elections" / "public" / "data" / "elections"
HTTP_ROOT = "https://bamboo-filing-cabinet.github.io/vietnam-elections/data/elections"


def load_results(cycle: str = "na15-2021") -> dict:
    """Return the parsed results.json for a cycle."""
    raise NotImplementedError


def load_winners(cycle: str = "na15-2021") -> list[dict]:
    """Return person records for winners (statuses containing 'won')."""
    raise NotImplementedError
