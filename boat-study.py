from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()

options.add_argument('--start-fullscreen')

driver = webdriver.Chrome(options=options)

url = 'https://www.boat-ed.com/accounts/sign_in/'
driver.get(url)

try:
    username = 'Replaceyourusername'
    password = 'Replaceyourpassword!'
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'account[username]')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'account[password]')))
    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Log In"]')
    login_button.click()

    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Continue Where You Left Off')))
    continue_button.click()
    
    while True:
        
        
        try:
            next_button = driver.find_element(By.XPATH, '//a[contains(@class, "btn-success") and contains(text(), "Next")]')
            next_button.click()
            print("Button 'Next' clicked successfully after the timer finished counting.")
        except NoSuchElementException:
            try:
                quiz_button = driver.find_element(By.XPATH, '//button[contains(text(), "Take the Unit")]')
                quiz_button.click()
                print("'Take the Unit  Quiz' button found and clicked. Exiting the program.")
                break  # Exit the loop and the program
            except NoSuchElementException:
                continue


except Exception as e:
    import traceback
    traceback.print_exc()

except KeyboardInterrupt:
        print("Process interrupted by user. Closing the browser...")
finally:
    save_logout_link = driver.find_element(By.XPATH, '//a[contains(@href, "/accounts/sign_out/") and contains(., "Save & Log Out")]')
    save_logout_link.click()

    print("Logged in, 'Continue' button clicked, and button 'Next' clicked successfully after the timer finished counting.")
    driver.quit()