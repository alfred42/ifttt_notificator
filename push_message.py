import requests
import sys

KEY = ""
EVENT_NAME = ""

def push_message(key, event_name, message):
    try:
        r = requests.post("https://maker.ifttt.com/trigger/" + event_name + "/with/key/" + key, json={"value1": message})
        if r.status_code != 200:
            sys.exit(-1)
    except Exception:
        sys.exit(-1)


if __name__ == '__main__':
    push_message(KEY, EVENT_NAME, sys.argv[1])
