"""
* Notification Factory:
* 		Create a NotificationFactory that generates notification objects (Email, SMS, Push) according to user preferences.
"""

class NotificationFactory:
    def __init__(self):
        pass

    def createNotification(self, notificationType):
        if notificationType == "Email":
            return EmailNotification()
        elif notificationType == "SMS":
            return SMSNotification()
        elif notificationType == "Push":
            return PushNotification()
        else:
            return None


class EmailNotification(NotificationFactory):
    def notify(self, message):
        print(f"Sending email notification: {message}")

class SMSNotification(NotificationFactory):
    def notify(self, message):
        print(f"Sending SMS notification: {message}")

class PushNotification(NotificationFactory):
    def notify(self, message):
        print(f"Sending push notification: {message}")

def main():
    factory = NotificationFactory()

    emailNotification = factory.createNotification("Email")
    smsNotification = factory.createNotification("SMS")
    pushNotification = factory.createNotification("Push")

    notifications = [emailNotification, smsNotification, pushNotification]
    for notification in notifications:
        notification.notify("Hello World!")

if __name__ == "__main__":
    main()