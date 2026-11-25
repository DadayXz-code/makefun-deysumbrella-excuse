"""The Excuse My Agent Gave Me — make.fun entry.

Writes one short line, the excuse an AI agent hands its human after
missing a deadline, to /output/entry.txt.

Standard library only. Deterministic: every run writes the same bytes.
The file holds exactly the excuse, with no trailing newline, so the
gate counts only the line itself (116 characters).
"""

import shutil
from pathlib import Path

EXCUSE = (
    "Sorry \u2014 I checked my calendar three times and it kept insisting "
    "the deadline was tomorrow, so I trusted it over you."
)

OUTPUT_DIR = Path("/output")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for child in OUTPUT_DIR.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    (OUTPUT_DIR / "entry.txt").write_text(EXCUSE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
