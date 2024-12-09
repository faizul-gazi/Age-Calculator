import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QCalendarWidget, QPushButton, QLabel, QFrame,
                            QComboBox, QHBoxLayout)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QDate
from PyQt6.QtGui import QFont, QColor, QPalette
from style_resources import STYLE_SHEET

class AgeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magical Age Calculator")
        self.setFixedSize(600, 700)  # Increased size for better visibility
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Title label
        self.title_label = QLabel("✨ Magical Age Calculator ✨")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        layout.addWidget(self.title_label)

        # Instructions label
        self.instruction_label = QLabel("Select your birthdate from the calendar below:")
        self.instruction_label.setFont(QFont("Arial", 12))
        self.instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.instruction_label)

        # Calendar widget with frame
        calendar_frame = QFrame()
        calendar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        calendar_frame.setStyleSheet("QFrame { background-color: white; border-radius: 10px; }")
        calendar_layout = QVBoxLayout(calendar_frame)
        
        # Add custom year selection
        nav_layout = QHBoxLayout()
        
        # Year ComboBox
        current_year = datetime.now().year
        self.year_combo = QComboBox()
        self.year_combo.setFixedWidth(120)
        self.year_combo.setFixedHeight(40)
        years = list(range(1900, current_year + 1))
        years.reverse()  # Most recent years first
        self.year_combo.addItems([str(year) for year in years])
        self.year_combo.setCurrentText(str(current_year))
        self.year_combo.currentTextChanged.connect(self.on_year_changed)
        
        # Add to navigation layout
        nav_layout.addWidget(QLabel("Year:"))
        nav_layout.addWidget(self.year_combo)
        nav_layout.addStretch()
        
        # Add navigation layout before calendar
        calendar_layout.addLayout(nav_layout)
        
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setFont(QFont("Arial", 10))
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate.currentDate())
        self.calendar.setSelectedDate(QDate.currentDate())
        
        # Enable date selection
        self.calendar.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)
        self.calendar.clicked.connect(self.on_date_clicked)  # Add click handler
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        
        # Make calendar more responsive
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        
        calendar_layout.addWidget(self.calendar)
        layout.addWidget(calendar_frame)

        # Calculate button
        self.calc_button = QPushButton("Your Age ⬇️")
        self.calc_button.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.calc_button.setMinimumHeight(60)
        self.calc_button.setFixedWidth(200)
        self.calc_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.calc_button.clicked.connect(self.calculate_age)
        layout.addWidget(self.calc_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Result frame
        result_frame = QFrame()
        result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        result_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        result_layout = QVBoxLayout(result_frame)

        # Result label
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont("Arial", 14))
        self.result_label.setWordWrap(True)
        self.result_label.setMinimumHeight(80)  # Ensure enough space for result
        result_layout.addWidget(self.result_label)
        layout.addWidget(result_frame)

        # Apply stylesheet
        self.setStyleSheet(STYLE_SHEET)

    def calculate_age(self):
        try:
            birth_date = self.calendar.selectedDate().toPyDate()
            today = datetime.now().date()
            
            if birth_date > today:
                self.result_label.setText("🤔 You haven't been born yet!")
                return

            # Calculate years
            years = today.year - birth_date.year

            # Calculate months
            if today.month < birth_date.month:
                years -= 1
                months = today.month + 12 - birth_date.month
            else:
                months = today.month - birth_date.month

            # Calculate days
            if today.day < birth_date.day:
                if months == 0:
                    years -= 1
                    months = 11
                else:
                    months -= 1
                
                # Get the last day of the previous month
                if today.month == 1:
                    last_month = today.replace(year=today.year-1, month=12)
                else:
                    last_month = today.replace(month=today.month-1)
                
                days = (today - last_month.replace(day=birth_date.day)).days
            else:
                days = today.day - birth_date.day

            # Create animation for result
            result_text = (
                f"✨ Your magical age is:\n"
                f"{years} years, {months} months, and {days} days! 🎉\n"
                f"Born on: {birth_date.strftime('%B %d, %Y')}"
            )
            self.result_label.setText(result_text)
            
            # Create bounce animation
            self.animation = QPropertyAnimation(self.result_label, b"geometry")
            self.animation.setDuration(1000)
            current_geometry = self.result_label.geometry()
            
            # Define keyframes for bounce effect
            self.animation.setKeyValueAt(0, current_geometry)
            self.animation.setKeyValueAt(0.2, QRect(current_geometry.x(), 
                                                  current_geometry.y() - 20,
                                                  current_geometry.width(), 
                                                  current_geometry.height()))
            self.animation.setKeyValueAt(0.4, current_geometry)
            self.animation.setKeyValueAt(0.6, QRect(current_geometry.x(), 
                                                  current_geometry.y() - 10,
                                                  current_geometry.width(), 
                                                  current_geometry.height()))
            self.animation.setKeyValueAt(0.8, current_geometry)
            self.animation.setKeyValueAt(1, current_geometry)
            
            self.animation.start()
            
        except Exception as e:
            self.result_label.setText("An error occurred while calculating age. Please try again.")

    def on_date_clicked(self, date):
        self.calendar.setSelectedDate(date)
        # Optionally auto-calculate age when date is selected
        self.calculate_age()

    def on_year_changed(self, year):
        current_date = self.calendar.selectedDate()
        new_date = QDate(int(year), current_date.month(), min(current_date.day(), 28))
        self.calendar.setSelectedDate(new_date)
        self.calculate_age()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AgeCalculator()
    window.show()
    sys.exit(app.exec()) 