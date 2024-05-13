import requests
import geocoder

USER = "uyscddawqhg16xwezfqn4wrtnnceww"
API = "asjgx3ytj5xn5gsrqhrosaukzrrb9v"

def send_message():
    g = geocoder.ip('me')
    msg = f"Person may be sleepy at geo location: {g.latlng}"
    payload = {"message": msg, "user": USER, "token": API }
    r = requests.post('https://api.pushover.net/1/messages.json', data=payload, headers={'User-Agent': 'Python'})
    return r