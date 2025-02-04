import time
import threading
import win32com.client
import win10toast

# Initialize speaker and notifier
speaker = win32com.client.Dispatch("SAPI.SpVoice")
show_notification = win10toast.ToastNotifier()

# Function to handle quitting
quit_program = False

def quit_listener():
    global quit_program
    while not quit_program:
        speaker.Speak("Type 'quit' or 'q' to stop the reminders: ")
        user_input = input("\nType 'quit' or 'q' to stop the reminders: ").strip().lower()
        if user_input == "quit" or 'q':
            quit_program = True
            print("Stopping the reminder...")
            speaker.Speak("Stopping the reminder...")

# Input the notification message
notification = input("Enter the notification you want to be reminded about: ")

print("SET THE TIMER:")
hour = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
# Clculate the total time interval
time_interval = seconds + (minutes * 60) + (hour * 3600)

if time_interval <= 0:
    print("Time interval must be greater than zero.")
    speaker.Speak("Time interval must be greater than zero.")
    exit()

print(f"Reminder set for {hour} hours, {minutes} minutes, and {seconds} seconds.")
speaker.Speak(f"Reminder set for {hour} hours, {minutes} minutes, and {seconds} seconds.")
# Start the quit listener in a separate thread
listener_thread = threading.Thread(target=quit_listener, daemon=True)
listener_thread.start()

# Start the reminder loop
while not quit_program:
    time.sleep(time_interval)
    if quit_program:  # Check if user quit before triggering the reminder
        break
    speaker.Speak(notification)
    show_notification.show_toast("Reminder", notification, duration=10)

print("Reminder program has exited.")
speaker.Speak("Reminder program has exited.")