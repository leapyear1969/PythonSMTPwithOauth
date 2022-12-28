import msal
import smtplib
import base64
import logging


# Get a token by msal
client_id = '5c26ecdb-07d5-419a-a073-ed041ded6144'
username = 'jason@majun.fun'
scopes=["https://partner.outlook.cn/SMTP.Send"]
redirect_uri ='http://localhost'
app = msal.PublicClientApplication(client_id,authority='https://login.partner.microsoftonline.cn/d7125684-0e28-40b5-aba2-ea9580f2a204')

result = None
accounts = app.get_accounts(username=username)
if accounts:
    logging.info("Account(s) exists in cache, probably with token too. Let's try.")
    print("Account(s) already signed in:")
    for a in accounts:
        print(a["username"])
    chosen = accounts[0]  # Assuming the end user chose this one to proceed
    print("Proceed with account: %s" % chosen["username"])
    # Now let's try to find a token in cache for this account
    result = app.acquire_token_silent(scopes,account=chosen)
if not result:
    logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
    print("A local browser window will be open for you to sign in. CTRL+C to cancel.")
    result = app.acquire_token_interactive(scopes)

if "access_token" in result:
    print(result["access_token"])
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))

print("result: " , result)
token = result["access_token"]

user = 'jason@majun.fun'
xoauth = "user=" + user + "\x01auth=Bearer " + token + "\x01\x01"
print("之前的样子: "+xoauth)
xoauth = xoauth.encode('ascii')
xoauth = base64.b64encode(xoauth)
xoauth = xoauth.decode('ascii')
print(xoauth)

#x = 'dXNlcj1qYXNvbkBtYWp1bi5mdW4BYXV0aD1CZWFyZXIgZXlKMGVYQWlPaUpLVjFRaUxDSnViMjVqWlNJNklrbDFaRjlEV0RCbU1ubzVWeTE1VGt0VFFubEVhMEZMVDI4NWQyY3RVWEk0UldZd2RDMUZORk01WmtFaUxDSmhiR2NpT2lKU1V6STFOaUlzSW5nMWRDSTZJbDlEU2tGUGRIbHpXVlp0Tlhoak1WbHZTekJ2VVRkeGVVSkRVU0lzSW10cFpDSTZJbDlEU2tGUGRIbHpXVlp0Tlhoak1WbHZTekJ2VVRkeGVVSkRVU0o5LmV5SmhkV1FpT2lKb2RIUndjem92TDNCaGNuUnVaWEl1YjNWMGJHOXZheTVqYmlJc0ltbHpjeUk2SW1oMGRIQnpPaTh2YzNSekxtTm9hVzVoWTJ4dmRXUmhjR2t1WTI0dlpEY3hNalUyT0RRdE1HVXlPQzAwTUdJMUxXRmlZVEl0WldFNU5UZ3daakpoTWpBeEx5SXNJbWxoZENJNk1UWTNNakU1TmpBNU9Dd2libUptSWpveE5qY3lNVGsyTURrNExDSmxlSEFpT2pFMk56SXhPVGs1T1Rnc0ltRmpjaUk2SWpFaUxDSmhhVzhpT2lKQlZGRkJlUzg0UzBGQlFVRkllRTVaYkRBMVlWWTRNRlZpWjFCUU5qTjRSak5VTlcwM0wxbE1OSEp4ZG5oNmJ6aEJWVzFaTjNSRlJDdDBhbTFHTXpOb1ExUkZkbmRXUjJjMVZGVlBJaXdpWVcxeUlqcGJJbkIzWkNKZExDSmhjSEJmWkdsemNHeGhlVzVoYldVaU9pSndlWFJvYjI1UFlYVjBhQ0lzSW1Gd2NHbGtJam9pTldNeU5tVmpaR0l0TURka05TMDBNVGxoTFdFd056TXRaV1F3TkRGa1pXUTJNVFExSWl3aVlYQndhV1JoWTNJaU9pSXdJaXdpWlc1bWNHOXNhV1J6SWpwYlhTd2labUZ0YVd4NVgyNWhiV1VpT2lMcHFhd2lMQ0puYVhabGJsOXVZVzFsSWpvaTVMLUtJaXdpYVhCaFpHUnlJam9pTVRFeExqRTVNeTQ1T1M0ME55SXNJbTVoYldVaU9pTHBxYXdnNUwtS0lpd2liMmxrSWpvaU1XWmhaVEUxTVRZdE16Z3pZUzAwWmpVekxUazJOVE10TXpJMFlXWmlPV0l3TmpFMklpd2ljSFZwWkNJNklqRXdNRE16TWpNd1F6WTJPRFJCUlRVaUxDSnlhQ0k2SWpBdVFWRkpRV2hHV1ZNeGVXZFBkRlZEY205MWNWWm5VRXRwUVZGSlFVRkJRVUZCVUVWUWVtZEJRVUZCUVVGQlFVRkRRVWxSTGlJc0luTmpjQ0k2SW1aMWJHeGZZV05qWlhOelgyRnpYM1Z6WlhJZ1UwMVVVQzVUWlc1a0lGVnpaWEl1VW1WaFpDSXNJbk5wWjI1cGJsOXpkR0YwWlNJNld5SnJiWE5wSWwwc0luTjFZaUk2SWpOaFVEaG5XRkJKUlRaeVZFeHRVRXBGTW5Od1YxOVhiMFpFV2xBelRTMWlWRjgxYVhoeE1HdE5YMUVpTENKMGFXUWlPaUprTnpFeU5UWTROQzB3WlRJNExUUXdZalV0WVdKaE1pMWxZVGsxT0RCbU1tRXlNREVpTENKMWJtbHhkV1ZmYm1GdFpTSTZJa3BoYzI5dVFHMWhhblZ1TG1aMWJpSXNJblZ3YmlJNklrcGhjMjl1UUcxaGFuVnVMbVoxYmlJc0luVjBhU0k2SWpjd09XSXpSbFk1YURCTFQwbHBlVkF3Y2tkc1FVRWlMQ0oyWlhJaU9pSXhMakFpTENKM2FXUnpJanBiSWpZeVpUa3dNemswTFRZNVpqVXROREl6TnkwNU1Ua3dMVEF4TWpFM056RTBOV1V4TUNJc0ltSTNPV1ppWmpSa0xUTmxaamt0TkRZNE9TMDRNVFF6TFRjMllqRTVOR1U0TlRVd09TSmRmUS51QmNoUXVQdk16eS1wZ3dDVFB5LWYyZnUwWEdyWlBsVS1SenJmZ2Y3c0xCcjNSS01OYlpjUkdib2U1Q1d0RnEwTl9JZlYzRVRQeWlsMDM5amtoY1E1b1JqUUhrNk14dndSVmtaeW0ybWpZZkZVZzBoSmFDaHduNWI5RGtoNW5Tdm83T0ItWDdPeG1sWW5GRE1iVkNhUGZvMVRlbmhZXy1ncWZXMWNfT3lpZmsyVUFnMEhFNVFIdm94VmNCbnZaUTJFa2xjS1gyYVVaNW1zbDF5YXdpLWF1TWpmejdScm9SWHdNSkl3Q1dNTXJabkVGR2xlcXN2a3hJV0ZYYkxrUEtXRjBLZDRQamd1NjVRTlNEN0hCcXJBMGJ0RUREMl9QZkhWcnUxU1owZFItdFhKdEZqN2syVTNBbzA5Z2VSUFRWOU95TjNNS0NQMnhjZzYzNl9Qemc3QWcBAQ=='



smtp_conn = smtplib.SMTP('smtp.partner.outlook.cn',587)
smtp_conn.set_debuglevel(True)
smtp_conn.ehlo()
smtp_conn.starttls()
smtp_conn.ehlo()
smtp_conn.docmd('AUTH', 'XOAUTH2 ' + xoauth)
smtp_conn.sendmail(user, 'someoneelse@some.com', 'cool')






