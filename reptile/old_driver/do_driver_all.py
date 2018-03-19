import threading

import time

from reptile.old_driver.do_requests import driver

for i in range(96, 236):
    url = "https://www.llss.fun/wp/page/" + str(i)
    filename = "page" + str(i) + ".json"
    threading.Thread(target=driver, args=(url, filename,)).start()
    print(url + " in " + filename)

time.sleep(60)
