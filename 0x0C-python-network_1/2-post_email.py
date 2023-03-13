#!/usr/bin/python3
"""sends a post and prints repsonse"""


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    data = {}
    data['email'] = argv[2]

    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
