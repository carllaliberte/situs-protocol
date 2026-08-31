"""python -m situs_filtre.cli "J'ai mal à la poitrine"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from situs_filtre.router import route


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        print("usage: python -m situs_filtre.cli <message>")
        return 2
    print(json.dumps(route(" ".join(args)), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
