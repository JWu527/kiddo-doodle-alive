#!/usr/bin/env python3
"""Fail if SKILL.md frontmatter is missing required fields."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
text = (root / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"\A---\n(.*?)\n---", text, re.S)
if not m:
    sys.exit("missing YAML frontmatter")
fm = m.group(1)
for key in ("name:", "description:", "license:"):
    if key not in fm:
        sys.exit(f"missing {key}")
if "version:" not in fm:
    sys.exit("missing metadata.version")
print("frontmatter ok")
