import urllib.request
import time
import sys
import os
import re
import threading

pages = 0
print("Loaded Auto keys.lol CMD VERSION 1.3")
threadCount = input('How many threads to run: ')
print("Started search...")


def run():
    try:
        while 5 > 1:
            webUrl = urllib.request.urlopen('https://keys.lol/bitcoin/random')
            time.sleep(5)
            data = webUrl.read()
            result = re.findall(r"[-+]?\d*\.\d+|\d+", str(data))
            for i in result:
                if str(i) + " btc" in str(data):
                    if float(i) > 0:
                        with open('ValidWallets.txt', 'a') as appendFile:
                            appendFile.write('{} btc\n'.format(str(i)))
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
