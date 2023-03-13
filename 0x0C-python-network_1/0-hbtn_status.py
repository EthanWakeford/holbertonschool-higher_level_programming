#!/usr/bin/python3
'''reads from a webpage.'''


if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(type(page), page,
                               page.decode('utf8')))
