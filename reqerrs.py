import requests
from requests import HTTPError

def main():
    url = 'https://httpbin.org/status/404'
    result = requests.get(url)
    printResult(result)


def printResult(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers ------------')
    print(resData.headers)
    print('\n')

    print('Returned data ------')
    print(resData.text)

if __name__ == '__main__':
    main()
