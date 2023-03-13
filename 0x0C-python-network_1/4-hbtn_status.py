#!/usr/bin/python3
"""handles errors"""


if __name__ == "__main__":
    import requests

    r = requests.get("https://intranet.hbtn.io/status")

    print("""Body response:
\t- type: {}
\t- content: {}""".format(type(r.text), r.text))
