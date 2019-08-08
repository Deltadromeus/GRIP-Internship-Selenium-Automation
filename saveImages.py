
                                              #      Downloading search results of google images search automatically using selenium web driver

from selenium import webdriver
import os
import json
import urllib.request
import time


os.environ["PATH"] += os.pathsep + os.getcwd()
download_path = "C:/Users/Saundarya/Downloads/Pictures"

def main():
    searchtext = input("Enter the search text for images ...")
    num_requested = int(input("Enter the number of search results you want ..."))


    if not os.path.exists(download_path + searchtext.replace(" ", "_")):
        os.makedirs(download_path + searchtext.replace(" ", "_"))

    url = "https://www.google.co.in/search?q=" + searchtext + "&source=lnms&tbm=isch"
    driver = webdriver.Chrome(r"C:\Users\Saundarya\Documents\Python Scripts\chromedriver.exe")
    driver.implicitly_wait(12)
    driver.maximize_window()
    driver.get(url)

    headers = {}
    headers[
        'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    extensions = {"jpg", "jpeg", "png", "gif"}


    img_count = 0                                   # initial image count
    downloaded_img_count = 0                        # initial downloaded image count

    images = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')        # uses xpath to find images
    print("Total images:" , len(images) , "\n")
    for img in images:
        img_count += 1
        img_url = json.loads(img.get_attribute('innerHTML'))["ou"]                     # load json strings -- url and type
        img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
        print("Downloading the images ",img_count,": ", img_url)
        try:
            if img_type not in extensions:
                img_type = "jpg"
            req = urllib.request.Request(img_url, headers=headers)                     # request for opening and reading image file
            opener= urllib.request.build_opener()                                             # open the file
            raw_img = opener.open(req).read()                                          # store the file in raw_img
            f = open(download_path + searchtext.replace(" ", "_") + "/" + str(downloaded_img_count) + "." + img_type,
                     "wb")
            f.write(raw_img)                                                           # write in the download folder

            downloaded_img_count += 1                                                  # file successfully downloaded
            print("download complete")
        except Exception as e:
            print("Download failed:",e)

        if downloaded_img_count >= num_requested:
            break

    print("Total downloaded: ",downloaded_img_count,"/", img_count)
    time.sleep(2)


if __name__ == "__main__":
    main()