"""Create parent class Notification with method send()
Create child classes:

EmailNotification

SMSNotification

WhatsAppNotification
Override send() in each."""

class Notification:
    def send(self):
        print("notification")# we can use pass here becouse parent send(method) unused at this case

class EmailNOtification(Notification):
    def send(self):
        print("Hi...noti,i am send by email")

class WhatsAppNotification(Notification):
    def send(self):
        print("Hi....noti,i ma sending by WhatsApp") 

objs=[EmailNOtification(),WhatsAppNotification()]
# Extra that shows that it also can be possible
class PushNotification(Notification):
    def send(self):
        print("Push notification sent")

objs.append(PushNotification())
for obj in objs:
    obj.send()    #we can use multiple logic here                   


