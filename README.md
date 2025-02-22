**Digital Clock with PyQt5**

This is a simple digital clock application built using Python and PyQt5.

**Features**

Displays the current time in hh:mm:ss AP format.

Uses a custom digital font (DS-DIGIB.TTF).

Green-colored time display on a black background.

Updates every second.

**Installation**

Install the required dependencies:

pip install PyQt5

Clone this repository and navigate to the project directory:

git clone https://github.com/your-username/digital-clock.git
cd digital-clock

Ensure you have the font file (DS-DIGIB.TTF) in the same directory as the script.

**Usage**

Run the script with:

python digital_clock.py

**Code Overview**

The script consists of a DigitalClock class that inherits from QWidget and displays a real-time updating clock.

Key Components:

__init__ Method: Initializes the clock widget and sets up the timer.

initUI Method: Configures the UI layout, font, colors, and timer connection.

update_time Method: Updates the clock display every second.



