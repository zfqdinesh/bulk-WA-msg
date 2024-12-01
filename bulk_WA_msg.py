# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Config
login_time = 60               # Time for login (in seconds)
new_msg_time = 15                # TTime for a new message (in seconds)
send_msg_time = 10               # Time for sending a message (in seconds)
country_code = 91               # Set your country code
action_time = 2                 # Set time for button click action
image_path = ("C:/Users/Dell/OneDrive/Pictures/1.jpg",
              "C:/Users/Dell/OneDrive/Pictures/1.jpg"
 ) # Absolute path to you image

pdf_path="C:/Users/Dell/OneDrive/Desktop/Downloads/23EAOCA025.pdf"
 

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text

msg = "hello! check my new product "

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(new_msg_time)
        # Click on button to load the input DOM
        for image in image_path:
            attach_btn = driver.find_element(By.CSS_SELECTOR, "div.x78zum5.x6s0dn4 > button[title='Attach']")
            attach_btn.click()
            time.sleep(action_time)
            # Find and send image path to input
        
        
            msg_input = driver.find_element(By.CSS_SELECTOR, "div.x1i64zmx.x1emribx input")
            msg_input.send_keys(image)
            time.sleep(action_time)
            # Start the action chain to write the message
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(send_msg_time)
        
        
        attach_btn = driver.find_element(By.CSS_SELECTOR, "div.x78zum5.x6s0dn4 > button[title='Attach']")
        attach_btn.click()
        time.sleep(action_time)
        pdf_input = driver.find_element(By.CSS_SELECTOR, "li._aj-r._aj-q._aj-_._ak_v input[type='file']")
        pdf_input.send_keys(pdf_path)
        time.sleep(action_time)
            
        actions = ActionChains(driver)  # Start the action chain to write the message
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)
        

# Quit the driver
driver.quit()


