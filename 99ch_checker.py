import requests
import time

def check_proxy(proxy):
        try:
            proxies = {"http": "http://{0}".format(proxy),
                       "https": "http://{0}".format(proxy)}
            headers = {'Accept-Encoding': 'identity',
                       'User-Agent': 'Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0'}
            t = requests.get("https://99chan.org/banned.php",
                             proxies=proxies, headers=headers, timeout=2)
            print(t.text)            
            if "Unable to find record of your IP being banned." in t.text:
                print(proxy,"works")
                with open("working.txt", "a") as myfile:
                    myfile.write("{0}".format(proxy))
            else:
                print(proxy,"NOPE")
        except requests.exceptions.RequestException as e:
            print(e)
f = open("proxy_list.txt","r")
for proxy in f:
    derp = proxy.rstrip()
    check_proxy(derp)
    time.sleep(0)
f.close()
