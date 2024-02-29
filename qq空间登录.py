from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver import ActionChains
def main():
    bro=webdriver.Edge()
    bro.get('https://qzone.qq.com/')
    bro.switch_to.frame('login_frame')
    select_pwd_login=bro.find_element(By.ID,'switcher_plogin')
    select_pwd_login.click()
    username_input=bro.find_element(By.ID,'u')
    pwd_input=bro.find_element(By.ID,'p')
    username_input.send_keys('') //输入QQ账号
    pwd_input.send_keys('')     //输入QQ密码
    submit=bro.find_element(By.ID,'login_button')
    submit.click()
    input()
if __name__=='__main__':
    main()
