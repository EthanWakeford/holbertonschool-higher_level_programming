#!/usr/bin/python3
"""sends a post response and checks for json validity"""


def main(argv):
    import requests

    data = {}
    if len(argv) > 1:
        data['q'] = argv[1]
    else:
        data['q'] = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        j = r.json()
        if j.get('id') is None:
            print("No result")
        else:
            print("[{}] {}".format(j.get('id'), j.get('name')))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    from sys import argv
    main(argv)
