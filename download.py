import requests
import shutil
import time
import os

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
    
    # check os. if not windows quit
    ops = os.name
    if ops == 'nt':
        pass
    else:
        print('This currently only works for windows!')
        time.sleep(3)
        quit()

    # Startup
    print("""#############################
    #CoinSuplier-File Downloader#
    ############################""")
    print('If you don´t have an license Token consider buying one!')
    key = str(input('Please enter your Token: '))
    print('DISCLAIMER : If you don´t have the macro mod installed all this won´t work!')
    destination = r'%appdata%/.minecraft/liteconfig/common/macros/file.txt'
    #open('', 'wb').write(r.content)

    # url for file 1 
    url = 'https://raw.githubusercontent.com/H3XAbytee/macro-download/main/file1.txt?token=' + key
    print('Sending Request for File1...')
    r = requests.get(url, allow_redirects=False)
    print(r.text)
    if r.status_code == 200:
        print('[*]Key Valid. Copying Files...')
        try:
            w = requests.get('https://link/to/file1')
            open(destination, 'wb').write(r.content)
            print('[+]File1 Copied succesfully!')
            time.sleep(5)
            quit()
        except:
            print('[!]Something went wrong while copying File1!')
            time.sleep(5)
            quit()
    else:
        print('[!]Token Invalid')
        time.sleep(5)
        quit()
    print('[*]Ending')

    
download()
