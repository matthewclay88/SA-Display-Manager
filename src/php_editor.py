"""
SA Display Manager
php_editor.py

Reads and writes the whiteboard.php slideshow file.
"""

from pathlib import Path
import re
import shutil

import settings


class WhiteboardError(Exception):
    """Raised when the whiteboard file is invalid."""


class WhiteboardEditor:
    """Read, validate, edit and save a whiteboard.php file."""

    def __init__(self, filename):
        self.filename = Path(filename)
        self.content = ""

    # --------------------------------------------------------------
    # File Operations
    # --------------------------------------------------------------

    def load(self):
        """Load the whiteboard file into memory."""

        if not self.filename.exists():
            raise WhiteboardError(
                f"File not found:\n{self.filename}"
            )

        self.content = self.filename.read_text(encoding="utf-8")

        self.validate()

    def validate(self):
        """Verify this is a supported whiteboard.php file."""

        required_patterns = [
            r"\$url\s*=\s*array",
            r'META\s+HTTP-EQUIV="refresh"',
            r"var\s+time\s*=",
        ]

        for pattern in required_patterns:
            if re.search(pattern, self.content, re.IGNORECASE) is None:
                raise WhiteboardError(
                    "This does not appear to be a supported "
                    "whiteboard.php file."
                )

    # --------------------------------------------------------------
    # Interval
    # --------------------------------------------------------------

    def get_interval(self):
        """Return the slideshow interval in seconds."""

        match = re.search(
            r'CONTENT="(\d+);URL=',
            self.content,
            re.IGNORECASE,
        )

        if match is None:
            raise WhiteboardError("Unable to locate refresh interval.")

        return int(match.group(1))

    def set_interval(self, seconds):
        """Update both slideshow timers."""

        milliseconds = int(seconds) * 1000

        self.content = re.sub(
            r'CONTENT="\d+;URL=',
            f'CONTENT="{seconds};URL=',
            self.content,
            count=1,
            flags=re.IGNORECASE,
        )

        self.content = re.sub(
            r"var\s+time\s*=\s*\d+;",
            f"var time = {milliseconds};",
            self.content,
            count=1,
            flags=re.IGNORECASE,
        )

    # --------------------------------------------------------------
    # Dashboards
    # --------------------------------------------------------------

    def get_dashboards(self):
        """Return dashboard URLs currently configured."""

        pattern = r'\$url\[\d+\]\s*=\s*"([^"]+)";'

        return re.findall(pattern, self.content)

    def set_dashboards(self, urls):
        """Replace only the static dashboard list."""

        new_lines = ["$url = array();"]

        for index, url in enumerate(urls):
            new_lines.append(
                f'$url[{index}] = "{url}";'
            )

        replacement = "\n    ".join(new_lines)

        pattern = (
            r"\$url\s*=\s*array\(\);\s*"
            r"(?:\$url\[\d+\]\s*=\s*\".*?\";\s*)+"
        )

        self.content = re.sub(
            pattern,
            replacement + "\n\n    ",
            self.content,
            count=1,
            flags=re.DOTALL,
        )

    # --------------------------------------------------------------
    # Backup
    # --------------------------------------------------------------

    def create_backup(self):
        """Create a .bak copy of the whiteboard."""

        backup = self.filename.with_suffix(
            self.filename.suffix + settings.BACKUP_EXTENSION
        )

        shutil.copy2(self.filename, backup)

    # --------------------------------------------------------------
    # Save
    # --------------------------------------------------------------

    def save(self):
        """Write changes back to disk."""

        self.create_backup()

        self.filename.write_text(
            self.content,
            encoding="utf-8",
        )
