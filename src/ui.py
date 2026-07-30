"""
SA Display Manager
ui.py

Main application window.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QCheckBox,
    QGroupBox,
    QStatusBar,
)

import settings


class MainWindow(QWidget):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.dashboard_boxes = {}

        self.setWindowTitle(
            f"{settings.APP_NAME} v{settings.APP_VERSION}"
        )

        self.setMinimumWidth(520)
        self.setMinimumHeight(500)

        self.build_ui()

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

        self.interval = QLineEdit()
        self.interval.setText(str(settings.DEFAULT_INTERVAL))
        self.interval.setMaximumWidth(70)

        seconds = QLabel("seconds")

        interval_layout.addWidget(self.interval)
        interval_layout.addWidget(seconds)
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
