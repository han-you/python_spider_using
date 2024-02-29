import time
import requests
import ddddocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

times = 1.25
username = ''
password = ''
# times=float(input('请输入显示windows缩放比例'))
# username=input('请输入用户名')
# password=input('请输入密码')
# driver_path=input('请输入浏览器驱动位置（必须是绝对路径，用/分隔）')

ErrorXpath = '//*[@id="native"]/div[1]'


def getpicture(bro):
    bro.save_screenshot('aa.png')
    code_img_ele = bro.find_element(By.XPATH, '/html/body/div/div/form[1]/a/img')
    location = code_img_ele.location
    print('location', location)
    size = code_img_ele.size
    print('size', size)

    # rangle=(
    #     location['x']*times,location['y']*times,location['x']*times+size['width']*times,location['y']*times+size['height']*times
    # )
    rangle = (
        location['x'] * 1.25, location['y'] * 1.25, location['x'] * 1.25 + size['width'] * 1.25,
        location['y'] * 1.25 + size['height'] * 1.25
    )

    i = Image.open('aa.png')
    code_img_name = 'aa.png'
    frame = i.crop(rangle)
    frame.save(code_img_name)
    fp = open('aa.png', 'rb')
    OCR = ddddocr.DdddOcr()
    ans = OCR.classification(fp.read())
    print(ans)
    return ans


def tips_exits(bro):
    try:
        tips_button = bro.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a')
        return True
    except:
        return False


def click_tips_ckick(bro):
    if tips_exits(bro):
        tips_button = bro.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a')
        tips_button.click()

def op_1():
    '''仅实现反检测'''
    options = EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-outomation'])
    return options


# 捕获异常
def NodeExists(xpath, bro):
    try:
        bro.find_element(By.XPATH, xpath)
        return True
    except:
        return False

def action(bro):
    try:
        # 打分
        input_button = bro.find_element(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[2]/td/div/input')
        input_button.send_keys(100)
        # 单选2
        click_button = bro.find_element(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[4]/td/div[1]/label')
        click_button.click()
        # 单选3
        click_button = bro.find_element(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[6]/td/div[1]/label')
        click_button.click()
        # 单选4
        click_button = bro.find_element(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[8]/td/div[1]/label')
        click_button.click()
        # 单选5
        click_button = bro.find_element(By.XPATH,
                                        '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[10]/td/div[1]/label')
        click_button.click()
        # 多选6
        click_list = bro.find_elements(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[12]/td/div')
        for button in click_list:
            button.click()
        # 单选7
        click_button = bro.find_element(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[14]/td/div[1]')
        click_button.click()
        #    对话框8
        text_list = bro.find_element(By.XPATH, '//*[@id="saveEvaluation"]/div/div/table/tbody/tr[16]/td/div/textarea')
        text_list.send_keys('无')
        # 提交
        submit_button = bro.find_element(By.XPATH, '//*[@id="save"]')
        submit_button.click()
        return True
    except:
        return False
op = op_1()

# 登录
# bro=webdriver.Edge(executable_path=driver_path,options=op)
bro = webdriver.Edge(executable_path='C:/Users/Lenovo/Desktop/code/python/爬虫/第七章：动态加载数据处理/msedgedriver.exe',options=op)
while True:
    bro.get('http://zhjw.scu.edu.cn/login')
    username_input = bro.find_element(By.ID, 'input_username', )
    pwd_input = bro.find_element(By.ID, 'input_password')
    code_input = bro.find_element(By.ID, 'input_checkcode')
    submit_button = bro.find_element(By.ID, 'loginButton')
    time.sleep(1)

    # username_input.send_keys(username)
    username_input.send_keys('2021141460330')

    username_input.send_keys()

    time.sleep(1)
    bro.find_element(By.ID, 'input_password').click()
    time.sleep(1)

    # bro.find_element(By.ID,'input_password').send_keys(password)
    bro.find_element(By.ID, 'input_password').send_keys('Chenyu&20021122')

    ans = getpicture(bro)
    code_input.send_keys(ans)
    submit_button.click()
    if not NodeExists(ErrorXpath, bro):
        break;
# 进入评教页面
bro.get('http://zhjw.scu.edu.cn/')
menu_button = bro.find_element(By.ID, 'menu-toggler')
time.sleep(1)
menu_button.click()
comment_button = bro.find_element(By.ID, '125803523')
comment_button.click()
comment_page_url = bro.find_element(By.XPATH, '//*[@id="125803539"]/a').get_attribute('href')
bro.get(comment_page_url)
click_tips_ckick(bro)

finial_term_button=bro.find_element(By.XPATH,'//*[@id="myTab"]/li[2]/a')
finial_term_button.click()
time.sleep(5)
issues_list = bro.find_elements(By.XPATH, '//*[@id="codeTable"]/tbody/tr')
issues_list_len=len(issues_list)
for index in range(issues_list_len):
    time.sleep(3)
    pos=format('//*[@id="codeTable"]/tbody/tr[%d]/td[2]'%(index+1))
    button=bro.find_elements(By.XPATH,pos+'/button')
    if len(button)==1:
        button[0].click()
        time.sleep(5)
        action(bro)
        bro.get('http://zhjw.scu.edu.cn/student/teachingEvaluation/newEvaluation/index')
        click_tips_ckick(bro)
        finial_term_button = bro.find_element(By.XPATH, '//*[@id="myTab"]/li[2]/a')
        finial_term_button.click()
input()
