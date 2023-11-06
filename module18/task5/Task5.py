import re

import requests
from requests import Response

H3_PATTERN = re.compile(r"<h3.*>(.*)</h3>")


def get_page(path: str) -> Response:
    return requests.get(url=path)


def main():
    response = get_page("http://www.columbia.edu/~fdc/sample.html")

    if response.status_code == 200:
        print(re.findall(H3_PATTERN, response.text))


if __name__ == '__main__':
    main()
