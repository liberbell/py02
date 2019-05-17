import reqests

def main():
    url =


def printResult(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers ------------')
    print(resData.Headers)
    print('\n')

    print('Returned data ------')
    print(resData.contents)

if __name__ == '__main__':
    main()
