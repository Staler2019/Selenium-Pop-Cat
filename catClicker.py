from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge("msedgedriver.exe")
driver.get(
    "https://popcat.click/?fbclid=IwAR0XlDcofkycLI1bMB66ekXM_yLnTnX8RSC-X1AES--iK5rKjPIt_NIrVkg"
)

action = ActionChains(driver)
action.click(driver.find_element_by_xpath('//*[@id="app"]/div'))

while 1:
    action.perform()

driver.quit()
