STYLE_SHEET = """
QMainWindow {
    background-color: #f0f8ff;
}

QLabel {
    color: #2c3e50;
    padding: 10px;
}

QCalendarWidget {
    background-color: white;
    border-radius: 10px;
}

QCalendarWidget QWidget {
    alternate-background-color: #e8f4f8;
}

/* Style for the navigation bar (month/year selection) */
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: #ffffff;
    padding: 4px;
}

/* Style for month/year buttons */
QCalendarWidget QToolButton {
    color: #000000;
    background-color: #ffffff;
    border: 1px solid #bdc3c7;
    border-radius: 5px;
    padding: 8px;
    min-width: 80px;
    font-size: 14px;
    font-weight: bold;
}

QCalendarWidget QToolButton:hover {
    background-color: #e8f4f8;
    border: 1px solid #3498db;
}

QCalendarWidget QToolButton::menu-indicator {
    image: none;  /* Remove default menu indicator */
}

/* Style for month/year dropdown menu */
QCalendarWidget QMenu {
    background-color: white;
    border: 1px solid #bdc3c7;
    padding: 5px;
    color: #000000;
    font-size: 14px;
}

QCalendarWidget QMenu::item:selected {
    background-color: #3498db;
    color: white;
}

QCalendarWidget QSpinBox {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    padding: 3px;
    font-size: 14px;
    color: #000000;
}

/* Style for calendar grid */
QCalendarWidget QTableView {
    border-radius: 5px;
    selection-background-color: #3498db;
    selection-color: white;
    font-size: 13px;
    outline: none;
}

/* Make dates clickable and show hover effect */
QCalendarWidget QTableView::item {
    border-radius: 2px;
    padding: 4px;
}

QCalendarWidget QTableView::item:hover {
    background-color: #e8f4f8;
    border: 1px solid #3498db;
}

/* Style for the selected date */
QCalendarWidget QTableView::item:selected {
    background-color: #3498db;
    color: white;
}

/* Make sure the calendar cells are large enough */
QCalendarWidget QTableView {
    selection-background-color: #3498db;
    selection-color: white;
    min-height: 25px;
}

/* Style for individual day cells */
QCalendarWidget QTableView::item:enabled {
    color: #000000;
    background-color: transparent;
}

QCalendarWidget QTableView::item:disabled {
    color: #808080;
}

/* Ensure the selected date stays highlighted */
QCalendarWidget QTableView::item:selected {
    background-color: #3498db;
    color: white;
    font-weight: bold;
}

/* Style for dates in the calendar */
QCalendarWidget QAbstractItemView:enabled {
    font-size: 13px;
    color: #000000;
    background-color: white;
    selection-background-color: #3498db;
    selection-color: white;
}

/* Style for selected date */
QCalendarWidget QTableView:focus {
    selection-background-color: #2980b9;
    selection-color: white;
}

/* Style for today's date */
QCalendarWidget QTableView:enabled #qt_calendar_dayview[today="true"] {
    background-color: #e8f4f8;
    color: #2980b9;
    font-weight: bold;
}

/* Style for selected date */
QCalendarWidget QTableView:enabled #qt_calendar_dayview[selected="true"] {
    background-color: #3498db;
    color: white;
    font-weight: bold;
}

QCalendarWidget QAbstractItemView:disabled {
    color: #808080;
}

QPushButton {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 30px;
    padding: 15px 25px;
    margin: 15px;
    font-weight: bold;
    text-align: center;
    min-width: 180px;
    letter-spacing: 1px;
}

QPushButton:hover {
    background-color: #2980b9;
    transform: scale(1.02);
}

QPushButton:pressed {
    background-color: #2574a9;
    padding: 17px 25px 13px 25px;
}

QPushButton:disabled {
    background-color: #bdc3c7;
    color: #7f8c8d;
}

/* Make sure text is properly centered and visible */
QPushButton {
    qproperty-alignment: AlignCenter;
    text-align: center;
    line-height: 1.2;
}

QFrame {
    border: 2px solid #bdc3c7;
    border-radius: 10px;
}

/* Style for the year ComboBox */
QComboBox {
    background-color: white;
    border: 2px solid #bdc3c7;
    border-radius: 5px;
    padding: 5px 10px;
    min-width: 100px;
    font-size: 16px;
    color: #2c3e50;
}

QComboBox:hover {
    border-color: #3498db;
}

QComboBox:focus {
    border-color: #3498db;
    background-color: #f8f9fa;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: url(down_arrow.png);
    width: 12px;
    height: 12px;
}

QComboBox QAbstractItemView {
    background-color: white;
    border: 1px solid #bdc3c7;
    selection-background-color: #3498db;
    selection-color: white;
    font-size: 16px;
}

QComboBox QAbstractItemView::item {
    min-height: 30px;
    padding: 5px;
}

QComboBox QAbstractItemView::item:hover {
    background-color: #e8f4f8;
}

QLabel {
    color: #2c3e50;
    font-size: 14px;
    font-weight: bold;
}

/* Update calendar styles for better visibility */
QCalendarWidget QToolButton {
    color: #000000;
    background-color: #ffffff;
    border: 2px solid #bdc3c7;
    border-radius: 5px;
    padding: 8px;
    min-width: 100px;
    min-height: 30px;
    font-size: 16px;
    font-weight: bold;
}

QCalendarWidget QMenu {
    font-size: 16px;
    padding: 5px;
}

QCalendarWidget QSpinBox {
    font-size: 16px;
    padding: 5px;
    min-width: 80px;
    min-height: 30px;
}

/* Make the calendar header more prominent */
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: #f8f9fa;
    min-height: 50px;
    padding: 5px;
}

/* Increase size of date cells */
QCalendarWidget QTableView {
    selection-background-color: #3498db;
    selection-color: white;
    font-size: 14px;
}

QCalendarWidget QTableView::item {
    padding: 8px;
}
""" 