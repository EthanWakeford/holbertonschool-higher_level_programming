#!/usr/bin/python3
"""gets the id for the github user"""

if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
