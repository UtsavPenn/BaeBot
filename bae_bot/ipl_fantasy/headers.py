import os


def get_headers_from_chrome(text):
    lines = [line for line in text.splitlines() if not line.startswith(":")]

    _k = lambda line: line.split()[0][:-1]
    _v = lambda line: " ".join(line.split()[1:])
    return {_k(line): _v(line) for line in lines}


API_HEADERS = get_headers_from_chrome(
    """:authority: 2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com
:method: GET
:scheme: https
accept: application/json,
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
accesstoken: {}
origin: https://fantasy.iplt20.com
referer: https://fantasy.iplt20.com/tournament
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
userid: tarunreddy.bethi@gmail.com""".format(os.environ['IPL_ACCESS_TOKEN']))
