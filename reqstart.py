import requests

def main():
    url = 'https://httpbin.org/xml'
    result = requests.get(url)
    printResult(result)


def printResult(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers ------------')
    print(resData.headers)
    print('\n')

    print('Returned data ------')
    print(resData.content)

if __name__ == '__main__':
    main()
