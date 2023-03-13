#!/usr/bin/python3
"""sends a post response"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    data = {}
    data['email'] = argv[2]

    r = requests.post(url, data=data)
    print(r.text)
