import requests
#notify
def notification():
    report = {}
    requests.post("https://maker.ifttt.com/trigger/fall_detect/with/key/bGFMBXIHS7wlWDwvdiG7lZ", data=report)