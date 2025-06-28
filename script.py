import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import requests
import random
import os
import json
import string
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains

import base64
from threading import Thread
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as FirefoxOptions



number_proxy = int(input("Number Proxy= "))
change_ip_ok = int(input("1-No, 2-Change= "))
number_all_theard = 22

sevice_proxy = int(input("1-, 2-= "))
if sevice_proxy == 1:
    arg_out = ""
elif sevice_proxy == 2:
    arg_out = ""
print(arg_out)

number_theard_in_ip = 3
list_all_th = []
list_th = []
for i in range(1, number_all_theard+1):
    list_th.append(i)
    if len(list_th) == number_theard_in_ip:
        list_all_th.append(tuple(list_th))
        list_th = []
print(list_all_th)

wiii = random.randint(320,320)
hiii = random.randint(600,600)


def generate_email_name():
    length = random.randint(15, 18)  # Length between 15 and 18 characters
    email_name = "".join(random.choice(string.ascii_lowercase)
                         for _ in range(length))
    return email_name


def input_text(xpath_s, key_s, time_s, driver):
    element = WebDriverWait(driver, time_s).until(
        EC.presence_of_element_located((By.XPATH, f"{xpath_s}"))
    )
    element.click()
    element.clear()
    element.send_keys(key_s)
    time.sleep(0.5)
def click_xpath(xpath_s, time_s, driver):
    element = WebDriverWait(driver, time_s).until(
        EC.presence_of_element_located((By.XPATH, f"{xpath_s}"))
    )
    element.click()
def wait_xpath(xpath_s, time_s, driver):
    element = WebDriverWait(driver, time_s).until(
        EC.presence_of_element_located((By.XPATH, f"{xpath_s}"))
    )

def SleepT(thrd):
    if thrd % 2 == 0:
        time.sleep(5)
    elif thrd % 3 == 0:
        time.sleep(9)
    else :
        time.sleep(1)

def Main(thrd, proxy_i):
    global error_reg
    
    SleepT(thrd)
    
    host = proxy_i.split(":")[0]
    port = proxy_i.split(":")[1]
    if thrd > 15:
        x = 200*(thrd - 6)
        y = 200
    else:
        x = 333*(thrd - 1)
        y = 0
            
    try:
        today = date.today()
        d1 = today.strftime("%d/%m/%Y") ## dd/mm/YY
        name_file = d1.replace("/", "") + f'outlook_{arg_out}_{thrd}'
        
        print("---", thrd, "---")
        profile_name = str(f"HMail {thrd}" )
        
        # Set up Firefox options if needed
        # firefox_options = Options()
        firefox_options = webdriver.FirefoxProfile() 

        # Définir la préférence pour la langue anglaise
        proxy_address = proxy_i # Replace with your proxy address and port



        firefox_options = FirefoxOptions()
        firefox_proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_address,
        # 'ftpProxy': proxy_address,
        'sslProxy': proxy_address,
        'noProxy': '' # Set this to bypass the proxy for specific addresses
        })



        # Apply the proxy
        firefox_options.proxy = firefox_proxy

        firefox_options.set_preference("intl.accept_languages", "en-us, en")


        # Uncomment the next line if you want to run Firefox in headless mode
        # firefox_options.add_argument('--headless')

        # Specify the path to the Firefox executable
        # Modify this path according to the location of your Firefox installation
        firefox_binary = "C:/Program Files/Mozilla Firefox/firefox.exe"
        firefox_options.binary = firefox_binary

        # Replace with your path to GeckoDriver
        geckodriver_path = 'geckodriver.exe'
        service = Service(geckodriver_path)

        # Use Firefox as the driver
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.set_page_load_timeout(222)
        print('Set size')
        driver.set_window_rect(x, y, width=wiii, height=hiii)            

        
        
        

        # time.sleep(1)
        # driver_len = len(driver.window_handles)
        # if driver_len > 1:
            # for i in range(driver_len - 1, 0, -1):
                # driver.switch_to.window(driver.window_handles[i])
                # driver.close()
                # print("Closed Tab No. ", i)
            # driver.switch_to.window(driver.window_handles[0])
        # else:
            # pass
        ######################################################################################
        driver.get('https://ipv4.icanhazip.com/')
        ippp = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/pre"))
        )
        print(ippp.text)
        main_page = driver.current_window_handle
        ######################################################################################
        for i in range(3):
            driver.get("https://app.suno.ai/")
            time.sleep(1)
            click_xpath("(//button[contains(text(),'Sign up')])[2]", 11, driver)
            time.sleep(1)
            click_xpath("//div//div[@aria-hidden='true']//button[3]", 11, driver)
            time.sleep(1)
            click_xpath("//a[@id='signup']", 11, driver)
            time.sleep(1)
            click_xpath("//a[@id='liveSwitch']", 11, driver)
            time.sleep(1)
            email_name = generate_email_name()
            email_address = f"{email_name}@outlook.com"
            input_text("//input[@id='MemberName']", email_address, 11, driver)
            click_xpath("//input[@id='iSignupAction']", 11, driver)

            time.sleep(1)
            input_text("//input[@id='PasswordInput']", "Lasagaz1!!!", 11, driver)
            click_xpath("//input[@id='iSignupAction']", 11, driver)
            time.sleep(1)

            ngay = random.randint(1,28)
            # click_xpath("//select[@id='BirthDay']", 11, driver)
            click_xpath(f"//select[@id='BirthDay']//option[@value='{ngay}']", 11, driver)
            
            thang = random.randint(1,12)
            # click_xpath(f"//select[@id='BirthMonth']", 11, driver)
            click_xpath(f"//select[@id='BirthMonth']//option[@value='{thang}']", 11, driver)

            nam = random.randint(1988,2003)
            input_text("//input[@id='BirthYear']", nam, 11, driver)
            # click_xpath("//input[@value='Next']", 11, driver)
            click_xpath("//input[@id='iSignupAction']", 11, driver)

            time.sleep(5)
            
            for i in range(33):
                try:
                    WebDriverWait(driver, 0.1).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='enforcementFrame']")))
                    break
                except:
                    pass
                try:
                    wait_xpath("//label[contains(text(),'Phone number')]", 0.1, driver)
                    print("Need Phone")
                    i = 999
                except:
                    pass
                if i > 99:
                    raise Exception("Need Phone")
                time.sleep(1)

            WebDriverWait(driver, 33).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Verification challenge']")))
            WebDriverWait(driver, 33).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Visual challenge']")))
            print("Solve")
            click_xpath("//button[contains(text(),'Next')]", 66, driver)

            start_time = time.time()
            check_status = False
            while True:
                end_time = time.time()
                slvcc = end_time - start_time
                try:
                    click_xpath("//button[contains(text(),'Next')]", 0.1, driver)
                    time.sleep(3)
                except:
                    pass
                try:
                    wait_xpath("//button[contains(text(),'Reload Challenge')]", 0.1, driver)
                    break
                except:
                    pass
                    
                try:
                    text_captcha = WebDriverWait(driver,0.1).until(
                        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Pick the')]"))
                    )
                    text_captcha = text_captcha.text
                    print(text_captcha)
                    try:
                        ... = ....index(text_captcha)
                        ... = ...[...]
                        print(...)
                    except:
                        print("Task Not In List")
                        slvcc = 999
                        raise Exception("Task Not In List")
                    for i in range(22):
                        round_cc = WebDriverWait(driver,1).until(
                            EC.presence_of_element_located((By.XPATH, "//p[@data-theme='tile-game.roundText']"))
                        )
                        round_text = round_cc.text
                        print(round_text)
                        round_text = round_text.split(' of ')

                        img_cc = WebDriverWait(driver,1).until(
                            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Image 1 of 6.']"))
                        )
                        link_img = img_cc.get_attribute("style")
                        # print(link_img)
                        link_img = link_img.split('url("')[1]
                        link_img = link_img.split('");')[0]
                        print(link_img)
                        
                        b64img = get_file_content_chrome(driver, link_img)
                        id_cc = ...(b64img, ...)
                        time.sleep(1)
                        number_click = ...(id_cc)
                        click_xpath(f"//button[@aria-label='Image {number_click} of 6.']", 1, driver)
                        if round_text[0] == round_text[1]:
                            check_status = True
                            break
                        time.sleep(3)
                except:# ZeroDivisionError  as e:
                    pass
                try:
                    text_captcha = WebDriverWait(driver,0.1).until(
                        EC.presence_of_element_located((By.XPATH, "//span[@role='text']"))
                    )
                    text_captcha = text_captcha.text
                    # print(text_captcha)
                    text_captcha = text_captcha.split(". (")[0]
                    print(text_captcha)
                    try:
                        ... = ....index(text_captcha)
                        ... = ...[...]
                        print(...)
                    except:
                        print("Task Not In List")
                        slvcc = 999
                        raise Exception("Task Not In List")

                    for i in range(22):
                        text_captcha = WebDriverWait(driver,1).until(
                            EC.presence_of_element_located((By.XPATH, "//span[@role='text']"))
                        )
                        text_captcha = text_captcha.text
                        text_captcha = text_captcha.split(". (")[1]
                        text_captcha = text_captcha.split(")")[0]
                        print(text_captcha)
                        round_text = text_captcha.split(' of ')

                        img_cc = WebDriverWait(driver,1).until(
                            EC.presence_of_element_located((By.XPATH, "//img[@aria-live='assertive']"))
                        )
                        link_img = img_cc.get_attribute("style")
                        # print(link_img)
                        link_img = link_img.split('url("')[1]
                        link_img = link_img.split('");')[0]
                        print(link_img)
                        
                        b64img = get_file_content_chrome(driver, link_img)
                        id_cc = ...(b64img, ...)
                        time.sleep(1)
                        number_click = ...(id_cc)
                        for i in range(int(number_click)-1):
                            click_xpath(f"//a[@aria-label='Navigate to next image']", 1, driver)
                        click_xpath(f"//button[contains(text(),'Submit')]", 1, driver)
                        if round_text[0] == round_text[1]:
                            check_status = True
                            break
                        time.sleep(3)
                except:# ZeroDivisionError  as e:
                    pass
                if check_status == True:
                    print("Wait Verification complete")
                    try:
                        wait_xpath("//h2[contains(text(),'Verification complete!')]", 6, driver)
                        time.sleep(3)
                        try:
                            wait_xpath("//button[contains(text(),'Next')]", 6, driver)
                            check_status = False
                        except:
                            check_status = 'Done'
                            break
                    except:
                        check_status = False
                try:
                    click_xpath("//button[contains(text(),'Try again')]", 0.1, driver)
                    print("Try Slover")
                except:
                    pass
                time.sleep(3)
                if slvcc > 120:
                    print('Error Captcha')
                    raise Exception("Error Captcha")
            if check_status == 'Done':
                break
        if check_status != 'Done':
            raise Exception("Error Captcha")
        print("Slover Done")
        driver.switch_to.default_content()

        click_xpath("//input[@id='idBtn_Accept']", 33, driver)
        
        wait_xpath("(//a[@data-theme='dark'][normalize-space()='Library'])[2]", 66, driver)
        
        
        ####WRITE
        with open(f"out\\{name_file}.txt","a+") as file_done:
            write_acc= str(email_address)+'|Lasagaz1!!!'+'\n'
            file_done.write(write_acc)
        print("Write TXT Ok")        
        
        error_reg = 0

        driver.quit()
    except:# ZeroDivisionError  as e:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        error_reg += 1
        
        # traceback_str = traceback.format_exc()
        # traceback_str = "".join(traceback_str.split("\n"))
        # with open(f"bug/xxxxxxxxx.txt","a+") as file_traceback:
            # file_traceback.write(traceback_str)
            # file_traceback.write('\n')

        driver.quit()


def ChangeCheckObc(proxy):
    proxies = {'https' : f"http://{proxy}"}
    change_ip = f"http://192.168.1.101:6254/reset?proxy={proxy}"
    start_time = time.time()
    try_c = 0
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 666:
            print("Error Change OBC Sleep")
            time.sleep(3333)
        try:
            if try_c == 0:
                ip_1 = requests.get("https://ipv4.icanhazip.com/", timeout=5, proxies=proxies).text.strip()
                ip_2 = ip_1
                print(proxy, ip_1)
            print("Change OBC")
            response = requests.get(change_ip, timeout=5).json()
            print(response)
            stt = response["status"]
            # print(stt)
            time.sleep(9)
            if stt == True:
                print("Change OK Wait")
                for cip in range(9):
                    try:
                        ip_2 = requests.get("https://ipv4.icanhazip.com/", timeout=5, proxies=proxies).text.strip()
                        print(proxy, ip_2)
                        break
                    except:# ZeroDivisionError  as e:
                        print("Check IP Flase")
                        time.sleep(3)
                if ip_1 == ip_2:
                    try_c += 1
                    continue
                elif ip_1 != ip_2:
                    break
            else:
                raise Exception("Error Change")
        except:
            print("Error")
            time.sleep(5)
            continue
            
def (proxy, keypry_i):
    spl = proxy.split(":")
    pyyyy = ''.join(spl[2]+":"+spl[3]+"@"+spl[0]+":"+spl[1])
    proxies = {'https' : f'http://{pyyyy}'}
    start_time = time.time()
    try_c = 0
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 666:
            print("Error Change Sleep")
            time.sleep(3333)
        try:
            if try_c == 0:
                ip_1 = requests.get("https://ipv4.icanhazip.com/", timeout=5, proxies=proxies).text.strip()
                ip_2 = ip_1
                print(proxy, ip_1)
            print("Changer ProxyNo1")
            time.sleep(1)
            ipp_zz = requests.get(f/api/change-key-ip/{keypry_i}").json()
            print(ipp_zz)
            status = int(ipp_zz['status'])
            if status == 0:
                print(status)
                time.sleep(9)
                print("Change OK Wait")
                for cip in range(9):
                    try:
                        ip_2 = requests.get("https://ipv4.icanhazip.com/", timeout=5, proxies=proxies).text.strip()
                        print(proxy, ip_2)
                        break
                    except:# ZeroDivisionError  as e:
                        print("Check IP Flase")
                        time.sleep(3)
                if ip_1 == ip_2:
                    try_c += 1
                    continue
                elif ip_1 != ip_2:
                    return True
            else:
                message = ipp_zz['message']
                message = message.split(" ")[1]
                print(message)
                time.sleep(int(message)+2)
        except:
            print("---Error---")
            time.sleep(5)
            continue

def check_ip_use(proxy):
    print("Wait IP")
    if sevice_proxy == 2:
        spl = proxy.split(":")
        proxy = ''.join(spl[2]+":"+spl[3]+"@"+spl[0]+":"+spl[1])
    proxies = {'https' : f"http://{proxy}"}
    while 1:
        try:
            ip_1 = requests.get("https://ipv4.icanhazip.com/", timeout=5, proxies=proxies).text.strip()
            print(proxy, ip_1)
            break
        except:
            time.sleep(5)
    start_time = time.time()
    while 1:
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 120:
            time.sleep(33)
        try:
            ip_2 = requests.get("https://ipv4.icanhazip.com/", timeout=5, proxies=proxies).text.strip()
        except:
            time.sleep(11)
        if ip_2 != ip_1:
            print(proxy, ip_2)
            return True
        else:
            time.sleep(11)
# Main(1)
# xxxxxxxxxxxxx


error_reg = 0
def MainThead(index_list_all_th):
    global error_reg
    while 1:
        print("INDEX:", index_list_all_th)

        if sevice_proxy == 1:
            with open(f'obc.txt') as f_prx:
                lines_prx = f_prx.readlines()
                proxy_i=lines_prx[index_list_all_th].strip()
                print(proxy_i)
        if sevice_proxy == 2:
            with open(f'.txt') as f_prx:
                lines_prx = f_prx.readlines()
                line=lines_prx[index_list_all_th].strip()
                keypry_i = line.split("|")[0]
                proxy_i = line.split("|")[1]
                print(proxy_i, keypry_i)

        list_thrd = list_all_th[index_list_all_th]
        
        threads = [Thread(target=Main, args=(thrd, proxy_i,)) for thrd in list_thrd]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        if change_ip_ok == 2:
            if wait_ini == 1:
                if sevice_proxy == 1:
                    ChangeCheckObc(proxy_i)
                elif sevice_proxy == 2:    
                    
            elif wait_ini == 2:
                wait_run(wini)
        else:
            check_ip_use(proxy_i)
        print("-"*11)
        print("Error:",error_reg)
        if error_reg > 33:
            print(f"Error {error_reg} Time Sleep 1H")
            time.sleep(3333)
            error_reg = 0

threads = [Thread(target=MainThead, args=(index_list_all_th,)) for index_list_all_th in range(number_proxy)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
