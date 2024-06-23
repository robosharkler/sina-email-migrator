import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Ensure DISPLAY environment variable is set
os.environ['DISPLAY'] = ':0'

# Set up Firefox options
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "/home/shark/Downloads/sinaEmails")
options.set_preference("browser.download.improvements_to_download_panel", False);
options.set_preference("browser.download.useDownloadDir", True);
options.set_preference("browser.download.viewableInternally.enabledTypes", "");
options.set_preference("browser.helperApps.alwaysAsk.force", False);
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "Thunderbird Document, blob: ,application/vnd.protonmail.v1+json, application/json, json, media-src,blob,message, message/rfc6532,message/partial, message/external-body, message/rfc822, application/octet-stream, text/plain, application/download, application/octet-stream, binary/octet-stream, application/binary, application/x-unknown, texto/html");
options.set_preference("pdfjs.disabled", True);

# Start Firefox with the specified options
driver = webdriver.Firefox(options=options)

try:
    # Open the URL
    driver.get("https://m0.mail.sina.com.cn/classic/index.php#action=maillist&fid=new&title=%25E6%2594%25B6%25E4%25BB%25B6%25E5%25A4%25B9&pagecount=0&pageno=1&order=htime&sorttype=desc&type=0&tag=-1")
    
    # Loop through the list
    for index in range(1, 6):  # Loop from 1 to 5 (inclusive)
        print(f"This is loop number {index}")
        
        # Construct the CSS selector
        selector = f".classData:nth-child(2) .listrow:nth-child({index}) > .eveRow"
        print(selector)
        
        # Click on the element
        element = driver.find_element(By.CSS_SELECTOR, selector)
        element.click()
        
        # Wait for the page to load
        time.sleep(3)
        
        # Click on the download button
        download_button = driver.find_element(By.CSS_SELECTOR, ".mailPubButStyle:nth-child(10) .mailPubText")
        download_button.click()
        
        # Wait for the dropdown to appear and click on the download link
        time.sleep(2)
        download_link = driver.find_element(By.LINK_TEXT, "下载EML文件")
        download_link.click()
        
        # Wait for the download to complete
        time.sleep(5)
    
    # Click on the next page button if needed
    # next_page_button = driver.find_element(By.CSS_SELECTOR, "#listpage1 > .inBlock:nth-child(3)")
    # next_page_button.click()
    # Add more logic if you need to handle pagination
    
finally:
    # Close the browser
    driver.quit()
