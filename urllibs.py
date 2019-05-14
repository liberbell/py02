import urllib.request

def main():
    url = 'https://httpbin.org/xml'

    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format(result.status))

if __name__ == '__main__':
    main()
