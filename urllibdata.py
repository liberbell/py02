import urllib.request

def main():
    url = 'https://httpbin.org/get'


    result = urllib.request.urlopen(url)

    print('Result code: {0}'.format(result.status))

    print('Headers ------------')

    print('Returned data ------')


if __name__ == '__main__':
    main()
