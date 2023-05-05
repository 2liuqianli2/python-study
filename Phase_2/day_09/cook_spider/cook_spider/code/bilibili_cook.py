from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=WebDriver()

def do_login(url,password,username):
    driver.get(url)
    sleep(2)
    login_page=driver.find_element(By.CLASS_NAME,"header-login-entry")
    login_page.click()
    sleep(2)
    username_butn=driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入账号"]')
    password_butn=driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入密码"]')
    username_butn.send_keys(username)
    password_butn.send_keys(password)
    sleep(1)
    login_butn=driver.find_element(By.CLASS_NAME,'btn_primary ')
    login_butn.click()
    # print(login_butn)

    WebDriverWait(driver,30,0.5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"header-entry-mini")))


    cooks=driver.get_cookies()
    driver.close()
    return cooks




if __name__ == '__main__':
    url="https://www.bilibili.com/"
    password="123plm123plm"
    username="19967628490"
    cooks=do_login(url,password,username)
    print(cooks)