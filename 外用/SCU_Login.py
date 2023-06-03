#/*******************************************************************
#使用前请确保输入的学科名和课程号正确


import time
import requests
import ddddocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
chosen_scores_name=''   #输入课程号
chosen_scores_id=''     #输入课程号
times='xxx'             #输入数字 设置->系统->屏幕 中的缩放与布局中更改文本、应用等项目的大小
username=''             #输入用户名
password=''             #输入密码
# times=float(input('请输入显示windows缩放比例'))
# ErrorXpath='//*[@id="native"]/div[1]'
# username=input('请输入用户名')
# password=input('请输入密码')
# driver_path=input('请输入浏览器驱动位置（必须是绝对路径，用/分隔）')
ErrorXpath='//*[@id="native"]/div[1]'
def getpicture(bro,path):
    bro.save_screenshot('aa.png')
    code_img_ele=bro.find_element(By.XPATH,path)
    location=code_img_ele.location
    print('location',location)
    size=code_img_ele.size
    print('size',size)
    rangle=(
        location['x']*times,location['y']*times,location['x']*times+size['width']*times,location['y']*times+size['height']*times
    )
    i=Image.open('aa.png')
    code_img_name='aa.png'
    frame=i.crop(rangle)
    frame.save(code_img_name)
    fp=open('aa.png', 'rb')
    OCR = ddddocr.DdddOcr()
    ans=OCR.classification(fp.read())
    print(ans)
    return ans
def login(bro):
    while True:
        bro.get('http://zhjw.scu.edu.cn/login')
        username_input = bro.find_element(By.ID, 'input_username', )
        pwd_input = bro.find_element(By.ID, 'input_password')
        code_input = bro.find_element(By.ID, 'input_checkcode')
        submit_button = bro.find_element(By.ID, 'loginButton')
        time.sleep(1)
        username_input.send_keys(username)
        time.sleep(1)
        bro.find_element(By.ID, 'input_password').click()
        time.sleep(1)
        bro.find_element(By.ID, 'input_password').send_keys(password)
        ans = getpicture(bro,'/html/body/div/div/form[1]/a/img')
        code_input.send_keys(ans)
        submit_button.click()
        if not NodeExists(ErrorXpath, bro):
            break;
def to_free_select(bro):
    bro.get('http://zhjw.scu.edu.cn/')
    menu_button = bro.find_element(By.ID, 'menu-toggler')
    time.sleep(1)
    menu_button.click()
    time.sleep(1)
    select_class_li = bro.find_element(By.ID, '82020')
    select_class_li.click()
    time.sleep(1)
    select_class_control = bro.find_element(By.ID, '1293220')
    select_class_control.click()
    url = bro.find_element(By.XPATH, '//*[@id="1293218"]/a').get_attribute('href')
    bro.get(url)
    free_select = bro.find_element(By.XPATH, '//*[@id="zyxk"]/a')
    free_select.click()
#进入自由选课后
def get_class_id(txt):
    tmp=txt.split('(')
    rec_index=0;
    ans=""
    while rec_index!=len(tmp) :
        if(tmp[rec_index]!="" and "1"<=tmp[rec_index][0]<="9"):
            ans = tmp[rec_index].split(')')[0]
        rec_index+=1
    return ans
def start_select(bro):
    time.sleep(1)
    judge=False
    iframe=bro.find_element(By.XPATH,'//*[@id="ifra"]')
    bro.switch_to.frame(iframe)
    input_text = bro.find_element(By.XPATH, '//*[@id="kcm"]')
    input_text.send_keys(chosen_scores_name)
    bro.switch_to.default_content()
    while True:
        if judge==False:
            iframe = bro.find_element(By.XPATH, '//*[@id="ifra"]')
            bro.switch_to.frame(iframe)
            judge=True
        inquiry_button=bro.find_element(By.XPATH,'//*[@id="queryButton"]')
        inquiry_button.click()
        time.sleep(1)
        class_list=bro.find_elements(By.XPATH,'/html/body/div[1]/div/table/tbody/tr')
        Flag=True
        for item in class_list:
            txt=item.find_element(By.XPATH,'./td[3]').text
            class_id=get_class_id(txt)
            if(class_id==chosen_scores_id):
                chose_button=item.find_element(By.XPATH,'./td[1]/input')
                chose_button.click()
                while True:
                    if judge==True:
                        bro.switch_to.default_content()
                        judge=False
                    time.sleep(1)
                    ans_input = bro.find_element(By.XPATH, '//*[@id="submitCode"]')
                    ans_input.click()
                    ans_input.clear()
                    pic=getpicture(bro,'/html/body/div[3]/div[2]/div[2]/div/div/div/h4/span/div/img')
                    print(pic)
                    ans_input.send_keys(pic)
                    submit_button=bro.find_element(By.XPATH,'//*[@id="submitButton"]')
                    submit_button.click()
                    time.sleep(2)
                    if NodeExists('//*[@id="304042030_01"]/span',bro) and bro.find_element(By.XPATH,'//*[@id="304042030_01"]/span').text=='选课成功！':
                        print('选课成功')
                        exit(0)
                        #//*[@id="314044020_01"]/span     选课时间冲突
                    else:
                        if NodeExists('//*[@id="ifra"]',bro):
                            continue
                        else:
                            time.sleep(2)
                            print('这里是冲突的处理')
                            url = bro.find_element(By.XPATH, '//*[@id="1293218"]/a').get_attribute('href')
                            bro.get(url)
                            free_select = bro.find_element(By.XPATH, '//*[@id="zyxk"]/a')
                            free_select.click()
                            judge = False
                            iframe = bro.find_element(By.XPATH, '//*[@id="ifra"]')
                            bro.switch_to.frame(iframe)
                            input_text = bro.find_element(By.XPATH, '//*[@id="kcm"]')
                            input_text.send_keys(chosen_scores_name)
                            bro.switch_to.default_content()
                            Flag=False
                            break
                if not Flag:
                    break



def op_1():
    '''仅实现反检测'''
    options = EdgeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-outomation'])
    return options
#捕获异常
def NodeExists(xpath,bro):
   try:
      bro.find_element(By.XPATH,xpath)
      return True
   except:
      return False

op=op_1()
bro=webdriver.Edge(options=op)
#登录
login(bro)
#自由选课按钮
to_free_select(bro)
#循环选课
start_select(bro)
input()
