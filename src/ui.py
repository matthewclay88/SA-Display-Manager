"""
SA Display Manager
ui.py

Main application window.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QCheckBox,
    QGroupBox,
    QStatusBar,
)

import settings
from php_editor import WhiteboardEditor, WhiteboardError


class MainWindow(QWidget):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.dashboard_boxes = {}

        self.editor = WhiteboardEditor(
            settings.DEFAULT_WHITEBOARD_PATH
        )

        self.setWindowTitle(
            f"{settings.APP_NAME} v{settings.APP_VERSION}"
        )

        self.setMinimumWidth(520)
        self.setMinimumHeight(500)

        self.build_ui()
        self.load_whiteboard()

    def build_ui(self):
        """Create the interface."""

        main_layout = QVBoxLayout(self)

        #
        # Whiteboard File
        #
        file_group = QGroupBox("Whiteboard File")
        file_layout = QVBoxLayout()

        self.file_path = QLineEdit()
        self.file_path.setText(settings.DEFAULT_WHITEBOARD_PATH)
        self.file_path.setReadOnly(True)

        file_layout.addWidget(self.file_path)
        file_group.setLayout(file_layout)

        main_layout.addWidget(file_group)

        #
        # Rotation Interval
        #
        interval_group = QGroupBox("Rotation Interval")

        interval_layout = QHBoxLayout()

        self.interval = QSpinBox()
        self.interval.setRange(5, 600)
        self.interval.setValue(settings.DEFAULT_INTERVAL)
        self.interval.setSuffix(" sec")
        self.interval.setMaximumWidth(100)

        interval_layout.addWidget(self.interval)
        interval_layout.addStretch()

        interval_group.setLayout(interval_layout)

        main_layout.addWidget(interval_group)

        #
        # Dashboards
        #
        dashboard_group = QGroupBox("Available Dashboards")

        dashboard_layout = QVBoxLayout()

        for dashboard in settings.DASHBOARDS:

            checkbox = QCheckBox(dashboard)

            if dashboard in settings.DEFAULT_ENABLED:
                checkbox.setChecked(True)

            dashboard_layout.addWidget(checkbox)

            self.dashboard_boxes[dashboard] = checkbox

        dashboard_group.setLayout(dashboard_layout)

        main_layout.addWidget(dashboard_group)

        #
        # Buttons
        #
        button_layout = QHBoxLayout()

        self.restore_button = QPushButton("Restore Defaults")
        self.save_button = QPushButton("Save Changes")

        self.restore_button.clicked.connect(
            self.restore_defaults
        )

        self.save_button.clicked.connect(
            self.save_changes
        )

        button_layout.addStretch()
        button_layout.addWidget(self.restore_button)
        button_layout.addWidget(self.save_button)

        main_layout.addLayout(button_layout)

        #
        # Status Bar
        #
        self.status = QStatusBar()
        self.status.showMessage("Ready")

        main_layout.addWidget(self.status)

    def load_whiteboard(self):
        """Load the current whiteboard settings."""

        try:
            self.editor.load()

            interval = self.editor.get_interval()

            self.interval.setValue(interval)

            urls = self.editor.get_dashboards()

            for name, checkbox in self.dashboard_boxes.items():

                url = settings.DASHBOARDS[name]

                checkbox.setChecked(url in urls)

            self.status.showMessage(
                "Whiteboard loaded."
            )

        except WhiteboardError as error:

            self.status.showMessage(str(error))

    def restore_defaults(self):
        """Restore default settings."""

        self.interval.setValue(
            settings.DEFAULT_INTERVAL
        )

        for name, checkbox in self.dashboard_boxes.items():

            checkbox.setChecked(
                name in settings.DEFAULT_ENABLED
            )

        self.status.showMessage(
            "Defaults restored."
        )

    def save_changes(self):
        """Save changes to the whiteboard."""

        try:
            self.editor.load()

            self.editor.set_interval(
                self.interval.value()
            )

            urls = []

            for name, checkbox in self.dashboard_boxes.items():

                if checkbox.isChecked():

                    urls.append(
                        settings.DASHBOARDS[name]
                    )

            self.editor.set_dashboards(urls)

            self.editor.save()

            self.status.showMessage(
                "Changes saved successfully."
            )

        except WhiteboardError as error:
            self.status.showMessage(str(error))

        except Exception as error:
            self.status.showMessage(
                f"Unexpected error: {error}"
            )
