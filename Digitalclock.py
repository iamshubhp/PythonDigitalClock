# Import necessary PyQt5 modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

# Define the DigitalClock class, inheriting from QWidget


class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()  # Initialize the parent QWidget class

        # Create a QLabel to display the time
        self.time_label = QLabel(self)

        # Create a QTimer to update the clock every second
        self.timer = QTimer(self)

        # Initialize the UI components
        self.initUI()

    def initUI(self):
        """Sets up the user interface for the digital clock."""
        self.setWindowTitle("Digital Clock")  # Set window title
        self.setGeometry(600, 400, 300, 100)  # Set window size and position

        # Create a vertical layout and add the time label
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Set font size and color of the time display
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")

        # Set background color of the window
        self.setStyleSheet("background-color: black;")

        # Load and apply the custom digital font
        font_id = QFontDatabase.addApplicationFont("DS-DIGIB.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # Connect the timer to the update_time function and start it
        self.timer.timeout.connect(self.update_time)
        # Update time every 1000 milliseconds (1 second)
        self.timer.start(1000)

        # Display the initial time immediately
        self.update_time()

    def update_time(self):
        """Updates the time label with the current time every second."""
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    clock = DigitalClock()  # Create an instance of DigitalClock
    clock.show()  # Display the clock window
    sys.exit(app.exec_())  # Execute the application event loop
