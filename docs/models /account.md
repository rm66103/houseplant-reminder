# Account

`Account` represents a users account in our application. 

## Properties

| property | desc |
| -- | -- |
| email | email address for authentication |
| password | password for authentication |
| phone | phone number for sms reminders |

## Creating an Account

Create an account for a user, or create an account for yourself to use during development.

```
a = Account()
a.email = "foo@bar.com"
a.set_password("<NEW_PASSOWRD>")
a.save()
```

You can use this user to log in to the UI.