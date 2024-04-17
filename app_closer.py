import psutil
import keyboard


def close_application(process_name):
    # Correctly use the 'process_iter' function
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.name() == process_name:
            proc.kill()  # Close the process


# Define the keyboard shortcut and the associated function
keyboard.add_hotkey('f1', close_application, args=('notepad.exe',))  # Change the application you want to close here

# Loop to keep the script listening
print("Press F1 to close notepad...")
keyboard.wait('esc')  # Use the 'esc' key to exit the script
