from old_driver.do_requests import driver

for i in range(1, 500):
    url = "https://www.llss.fun/wp/page/" + str(i)
    filename = "info/"+"page" + str(i) + ".json"
    # threading.Thread(target=driver, args=(url, filename,)).start()
    driver(url, filename)
