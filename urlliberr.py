import urllib.request
from http import HTTPStatus

def main():
    url = 'https://httpbin.org/html'
    # url = 'https://httpbin.org/status/404'
    # url = 'https://no-such-server.org'

    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(HTTPStatus)
        print(result.read().decode('UTF-8'))

if __name__ == '__main__':
    main()
