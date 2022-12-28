# PythonSMTPwithOauth
a demo of python sending emails with Oauth for China Office365.

## Note：
- i'm using python MSAL auth library. https://learn.microsoft.com/en-us/python/api/overview/azure/active-directory?view=azure-python 
- <b>*MUST*</b> replace ``^A`` to ``\x0`` from official docs.[Authenticate an IMAP, POP or SMTP connection using OAuth](https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#authenticate-connection-requests)
```json
base64("user=" + userName + "\x0auth=Bearer " + accessToken + "\x01")    
```
