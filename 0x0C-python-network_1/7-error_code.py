#!/usr/bin/python3
"""guards for errors"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
