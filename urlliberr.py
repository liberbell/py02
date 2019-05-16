import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError

def main():
    # url = 'https://httpbin.org/html'
    # url = 'https://httpbin.org/status/404'
    url = 'https://no-such-server.org'

    try:
        result = urllib.request.urlopen(url)
        print('Result code: {0}'.format(result.status))
        if (result.getcode() == HTTPStatus.OK):
            print(result.read().decode('UTF-8'))
    except HTTPError as err:
        print('Error: {0}'.format(err.code))

if __name__ == '__main__':
    main()
