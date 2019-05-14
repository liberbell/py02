import urllib.request

def main():
    url = 'https://httpbin.org/xml'

    result = urllib.request.urlopen(url)
    print(result.status)

if __name__ == '__main__':
    main()
