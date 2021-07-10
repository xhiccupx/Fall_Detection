#code to send sms using ifttt web hooks and sms service
import requests
#notify
def notification():
    report = {}
    requests.post("https://maker.ifttt.com/trigger/<event name>/with/key/<enter your ifttt web hook key id>", data=report)
