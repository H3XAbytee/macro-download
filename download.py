import requests
import shutil
import time



def download():
    # Check for Internet Connection
    try:
        requests.get('https://google.com')
    except:
        print('Please check your Internet-Connection! Without an Connection I can´t work!')
        opt = input('(q) to quit | (c) to continue anyways')
        if opt == 'q':
            print('Thanks for stopping by!')
            time.sleep(2)
            quit()
        if opt == 'c':
            pass
        else:
            pass
    print("""##################################
            #CoinSuplier-File Downloader#
            ############################""")
    print('If you don´t have an license Key consider buying one!')
    key = str(input('Please enter your Key: '))
    headers = {'content-type': 'application/json', 'ApiKey': key}
    url = 'http://link/to/file/where/the/key/should/be/included'
    print('Sending Request to File...')
    r = requests.get(url, allow_redirects=False)
    if r.status_code = 200:
        print('[+]Key Valid copying Files...')
        try:
            open('', 'wb').write(r.content)
            print('[+]Files copied!')
        except:
            print('Something went wrong. Try again or speak to an Owner / Mod!')
