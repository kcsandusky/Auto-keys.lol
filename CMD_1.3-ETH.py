import urllib.request
import time
import sys
import os
import re
import threading

pages = 0
print("Loaded Auto keys.lol ethereum CMD VERSION 1.3")
threadCount = input('How many threads to run: ')
print("Started search...")


def run():
    try:
        while 5 > 1:
            webUrl = urllib.request.urlopen('https://keys.lol/ethereum/random')
            time.sleep(10)
            data = webUrl.read()
            result = re.findall("[+-]?\d+\.\d+", str(data))
            for i in result:
                if str(i) + " eth" in str(data):
                    if float(i) > 0:
                        with open('ValidWalletsETH.txt', 'a') as appendFile:
                            appendFile.write('{} eth\n'.format(str(i)))
                            appendFile.write('{}\n'.format(webUrl.geturl()))
            global pages
            pages = pages + 1
            sys.stdout.write("\rPages read: {}".format(str(pages)))
            sys.stdout.flush()
    except TimeoutError:
        os.execv(sys.executable, ['python'] + sys.argv)


for i in range(int(threadCount)):
    thread = threading.Thread(target=run)
    thread.start()
