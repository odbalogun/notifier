from notifier.classes import Notification, Alert
import time


def begin():
    # ask user what he wants to do
    print("Welcome to the Notifier...")
    print("What would you like to do?")
    print("1) Create an alert")
    print("2) Exit")


while True:
    begin()
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Invalid selection. Please enter an integer")
        print("="*50)
        print("\n")
        continue

    if option == 1:
        print("Create a notification")
        title = str(input("Title of your notification: "))
        message = str(input("Leave a message: "))
        timer = int(input("How soon do you want to be notified (in seconds)? "))

        notify = Notification(timer=timer, title=title, message=message)
        print("Setting up timer...")

        time.sleep(notify.timer)
        alert = Alert("MAC_OS", notify)
        alert()
        print("You have been notified :)")
        print("\n")
        continue
    elif option == 2:
        print("Bye...")
        time.sleep(1)
        break
    else:
        print("Invalid selection. Please select one of the provided options")
        print("=" * 50)
        print("\n")
        continue
