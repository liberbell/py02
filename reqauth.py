import requests
from requests import HTTPError, Timeout
form requests.auth import HTTPBasicAuth

def main():
    # url = 'https://httpbin.org/status/404'
    url = 'https://httpbin.org/basic-auth/root/pass'

    myCreds = HTTPBasicAuth('root', 'pass')

    result = requests.get(url, auth=myCreds)

    printResult(result)
    # try:
    #     result = requests.get(url, timeout=2)
    #     result.raise_for_status()
    #     printResult(result)
    # except HTTPError as err:
    #     print('Error: {0}'.format(err))
    # except Timeout as err:
    #     print('Request timeout error: {0}',format(err))

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
