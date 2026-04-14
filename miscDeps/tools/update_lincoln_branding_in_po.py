#!/usr/bin/env python3
"""One-shot: sync common product-name msgids in all nvda.po files to Lincoln Access Screen Reader.
Clears msgstr for updated entries so gettext falls back to the English msgid until translators refresh."""

import re
import sys
from pathlib import Path

# (old_msgid_line, new_msgid_line) — full logical line without trailing newline in pattern
REPLACEMENTS: list[tuple[str, str]] = [
	('msgid "About NVDA"', 'msgid "About Lincoln Access Screen Reader"'),
	('msgid "Welcome to NVDA"', 'msgid "Welcome to Lincoln Access Screen Reader"'),
	('msgid "Welcome to NVDA!"', 'msgid "Welcome to Lincoln Access Screen Reader!"'),
	('msgid "NonVisual Desktop Access"', 'msgid "Lincoln Access Screen Reader"'),
	('msgid "Exit NVDA"', 'msgid "Exit Lincoln Access Screen Reader"'),
	('msgid "&Install NVDA..."', 'msgid "&Install Lincoln Access Screen Reader..."'),
	('msgid "&Install NVDA on this computer"', 'msgid "&Install Lincoln Access Screen Reader on this computer"'),
	('msgid "NVDA settings"', 'msgid "Lincoln Access Screen Reader settings"'),
	('msgid "American Screen Reader"', 'msgid "Lincoln Access Screen Reader"'),
	(
		'msgid "Please wait while NVDA attempts to fix your system\'s COM registrations..."',
		'msgid "Please wait while Lincoln Access Screen Reader attempts to fix your system\'s COM registrations..."',
	),
]

# After msgid replacement, blank single-line msgstr so catalogs use English msgid as fallback
NEW_MSGIDS_TO_BLANK = [
	"About Lincoln Access Screen Reader",
	"Welcome to Lincoln Access Screen Reader",
	"Welcome to Lincoln Access Screen Reader!",
	"Lincoln Access Screen Reader",
	"Exit Lincoln Access Screen Reader",
	"&Install Lincoln Access Screen Reader...",
	"&Install Lincoln Access Screen Reader on this computer",
	"Lincoln Access Screen Reader settings",
	"Please wait while Lincoln Access Screen Reader attempts to fix your system's COM registrations...",
]


def blank_msgstr_after_msgid(text: str, msgid_content: str) -> str:
	escaped = re.escape(f'msgid "{msgid_content}"')
	# Single-line msgstr only (covers 99% of these entries)
	pat = re.compile(
		"^" + escaped + r"\nmsgstr \"[^\"]*\"\n",
		re.MULTILINE,
	)
	return pat.sub(f'msgid "{msgid_content}"\nmsgstr ""\n', text)


def process_file(path: Path) -> bool:
	raw = path.read_text(encoding="utf-8")
	orig = raw
	for old, new in REPLACEMENTS:
		raw = raw.replace(old, new)
	for mid in NEW_MSGIDS_TO_BLANK:
		raw = blank_msgstr_after_msgid(raw, mid)
	if raw != orig:
		path.write_text(raw, encoding="utf-8")
		return True
	return False


def main() -> int:
	root = Path(__file__).resolve().parents[2] / "source" / "locale"
	changed = 0
	for po in sorted(root.rglob("nvda.po")):
		if process_file(po):
			changed += 1
	print(f"Updated {changed} nvda.po file(s).", file=sys.stderr)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
