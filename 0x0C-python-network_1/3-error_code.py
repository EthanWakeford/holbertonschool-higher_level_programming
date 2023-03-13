#!/usr/bin/python3
"""handles errors"""


if __name__ == "__main__":
    from urllib import request, error
    import urllib.request
    from sys import argv

    url = argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as repsonse:
            print(repsonse.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
