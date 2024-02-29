import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options
def get_leave_city_list(bro):
    ans_list=[]
    classify_lis=[]
    leave_city_button=bro.find_element(By.XPATH,'//*[@id="fromStationText"]')
    leave_city_button.click()
    tmp=bro.find_elements(By.XPATH,'//*[@id="abc"]/li')
    for i in tmp:
        classify_lis.append(i)
    for li in classify_lis:
        li.click()
        while bro.find_element(By.XPATH,'')
        lst=bro.find_elements(By.XPATH,'//*[@id="ul_list2"]/ul[1]/li')
        for ele in lst:
            ans_list.append(ele.text)
    print(ans_list)

option=Options()
# option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_experimental_option('excludeSwitches',['enable-automation'])
bro=webdriver.Edge(options=option)
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
action=ActionChains(bro)
username_input=bro.find_element(By.ID,'J-userName')
pwd_input=bro.find_element(By.ID,'J-password')
submit=bro.find_element(By.ID,'J-login')
username_input.send_keys('')
pwd_input.send_keys('')
submit.click()
script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
bro.execute_script(script)
time.sleep(2)
slip=bro.find_element(By.ID,'nc_1_n1z')
action.click_and_hold(slip)
for i in range(8):
    action.move_by_offset(40,0).perform()
action.release().perform()
time.sleep(1)
index_button=bro.find_element(By.XPATH,'//*[@id="J-index"]')
time.sleep(1)
index_button.click()
#查询车票
get_leave_city_list(bro)
arrive_city_list=[]
leave_city_list=[]
leave_place=''
arrive_place=''
leave_date=''
type=input('您要查询单程票和往返?(单程/往返）')
while not (type=='单程' or type=='往返'):
    print('输入错误','请再输入一次')
    type = input('您要查询单程票和往返?(单程/往返）')
leave_place=input('请输入出发地')
arrive_place=input('请输入到达地')
leave_date=input('请输入出发日期')
# if type=='单程'
input()
