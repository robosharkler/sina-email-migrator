import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email_per_page = 20
page = 18
download_path = "/Users/sallyp/Downloads/sinaEmails"
downloaded = 0

# Set up Firefox options
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_path)
options.set_preference("browser.helperApps.alwaysAsk.force", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel, application/pdf, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/x-msexcel, application/x-excel, application/excel, application/octet-stream, application/msword, application/csv, text/csv, text/plain, application/vnd.openxmlformats-officedocument.wordprocessingml.document, message/rfc822, message/x-eml, application/x-rar-compressed, application/zip, application/x-7z-compressed")
options.set_preference("browser.helperApps.neverAsk.openFile", "application/vnd.ms-excel, application/pdf, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/x-msexcel, application/x-excel, application/excel, application/octet-stream, application/msword, application/csv, text/csv, text/plain, application/vnd.openxmlformats-officedocument.wordprocessingml.document, message/rfc822, message/x-eml, application/x-rar-compressed, application/zip, application/x-7z-compressed")
options.set_preference("pdfjs.disabled", True)
options.set_preference("browser.download.manager.alertOnEXEOpen", False)
options.set_preference("browser.download.manager.closeWhenDone", True)
options.set_preference("browser.download.manager.showAlertOnComplete", False)
options.set_preference("browser.download.manager.useWindow", False)
options.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)

# Start Firefox with the specified options
driver = webdriver.Firefox(options=options)

try:
    # Open the URL
    driver.get("https://m0.mail.sina.com.cn/classic/index.php#action=maillist&fid=new&title=%25E6%2594%25B6%25E4%25BB%25B6%25E5%25A4%25B9")
    input("Press Enter to continue...")

    # Loop through pages:
    for page in range(0, page):
        for index in range(1, 1 + email_per_page):
            try:
                print(f"This is loop number {index} on page {page + 1}")

                # Construct the CSS selector
                selector = f".classData:nth-child(2) .listrow:nth-child({index}) > .eveRow"
                print(selector)
                
                # Wait for the element to be present and click on it
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                element.click()

                # Wait for the download button to be clickable and click on it
                download_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".mailPubButStyle:nth-child(10) .mailPubText"))
                )
                download_button.click()
                
                # Wait for the dropdown to appear and click on the download link
                download_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//li/a[@value='down_eml']"))
                )
                download_link.click()
                
                # Wait for the download to complete
                time.sleep(5)
                downloaded += 1

                # Check if the network issue popup is present and handle it
                try:
                    popup = driver.find_element(By.CLASS_NAME, "wui-Dialog")
                    if popup.is_displayed():
                        print("Network issue popup detected, page {} index {}. Handling...".format(page + 1, index))
                        # Click on an element inside the popup to dismiss it
                        popup.find_element(By.CSS_SELECTOR, ".mailPubText").click()
                except Exception:
                    pass  # Continue if popup is not found
            except Exception as e:
                print(f"An error occurred on page {page + 1}, index {index}: {str(e)}")
                continue  # Skip to the next email in case of an error
            finally:
                sys.stdout.flush() 
        
        # Click on the next page button if needed
        next_page_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#listpage1 > .inBlock:nth-child(3)"))
        )
        next_page_button.click()
        time.sleep(3)  # Wait for the page to load
finally:
    # Close the browser
    print("DONE! In total {} emails were downloaded!".format(downloaded))
