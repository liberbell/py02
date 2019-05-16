import urllib.request
import urllib.parse

def main():
    url = 'https://httpbin.org/get'

    args = {
        "name": "Jhon Doe",
        "is_author": True
    }

    data = urllib.parse.urlencode(args)

    result = urllib.request.urlopen(url)

    print('Result code: {0}'.format(result.status))

    print('Headers ------------')

    print('Returned data ------')
    print(result.read().decode('UTF-8'))

if __name__ == '__main__':
    main()
