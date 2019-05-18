import requests
from requests import HTTPError

def main():
    url = 'https://httpbin.org/status/404'
    try:
        result = requests.get(url)
        printResult(result)
    except HTTPError as err:
        print('Error: {0}'.format(err))

def printResult(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    # print('Headers ------------')
    # print(resData.headers)
    # print('\n')

    print('Returned data ------')
    print(resData.text)

if __name__ == '__main__':
    main()
