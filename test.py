from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

# driver = webdriver.Chrome('/opt/homebrew/Caskroom/chromedriver')
driver = webdriver.Chrome()
driver.get("https://www.stealmylogin.com/demo.html")
print(driver.title)

driver.find_element(By.NAME, 'username').send_keys("abc@gmail.com")
driver.find_element(By.NAME, 'password').send_keys("your_password")
# driver.find_element(By.NAME("user_password")).sendKeys("your_password")
driver.find_element(By.XPATH, "//input[@value='login']").click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
except:
    driver.quit()


# driver.quit()
