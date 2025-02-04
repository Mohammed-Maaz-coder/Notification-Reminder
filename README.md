#Notification Reminder 🛎️
A simple Python-based reminder system that provides voice alerts and desktop notifications.

Features
✅ Set custom reminder messages.
✅ Specify the reminder time in hours, minutes, and seconds.
✅ Get voice notifications using Windows' text-to-speech (TTS).
✅ Receive desktop notifications using Win10 Toast Notifier.
✅ Ability to stop reminders by typing "quit" or "q".

Tech Stack
Python 🐍
Libraries Used:
win32com.client (for voice notifications)
win10toast (for desktop notifications)
threading (for non-blocking quit mechanism)
How to Run
Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/notification-reminder.git
Navigate to the project folder:
bash
Copy
Edit
cd notification-reminder
Install dependencies:
bash
Copy
Edit
pip install pywin32 win10toast
Run the script:
bash
Copy
Edit
python reminder.py
Usage
Enter the reminder message when prompted.
Set the time interval (hours, minutes, and seconds).
The system will notify you once the timer expires.
Type "quit" or "q" anytime to stop the reminders.
Contributing
Feel free to fork this repository and contribute! 🚀
