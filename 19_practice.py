spamWords = ['buy now', 'subscribe now', 'click this']

email = input("Enter the email: ")
spam = False

if ('buy now' in email):
    spam = True

    if ('subscribe now' in email):
    spam = True

    if ('click this' in email):
    spam = True

    print("spam is", spam)
