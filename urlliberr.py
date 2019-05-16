import urllib.request

def main():
    url = 'https://httpbin.org/html'
    # url = 'https://httpbin.org/status/404'
    # url = 'https://no-such-server.org'

    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format(resutl.status))
    if (result.getcode() == 200):
        print(result.read().decode('UTF-8'))

if __name__ == '__main__':
    main()
