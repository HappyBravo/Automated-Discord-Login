import time
import undetected_chromedriver.v2 as uc

#also, a Chrome-Shortcut Desktop icon may be created

chrome_sel_path = 'path where you saved Selenium chromedriver.exe'

driver = uc.Chrome()
driver.implicitly_wait(5)

driver.get('https://discord.com/login')

driver.implicitly_wait(30)


u_email = "Your Email/mobile no"
u_pass = "Your account Password"

print("started")

time.sleep(10)  #sleep timer depending on how much time it takes to load the page.

#finding the email box with : driver.find_element_by_name('email')
driver.find_element_by_name('email').send_keys(u_email)

#finding the password box with : driver.find_element_by_name('password')
driver.find_element_by_name('password').send_keys(u_pass)

#Login Button's class name :
cla = "marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN"
cla = ".".join(cla.split())
#print(cla)

time.sleep(1)   #this sleep was done for just seeing if it works, you can remove it if you want.

driver.find_element_by_class_name(cla).click()

### if you remembered the login credentials correctly, then its done ###
print("found")

#simply putting a while loop so that the Chrome do not exits, else after the execution of the program, the Chrome browser exits.
while True:
    time.sleep(10)
    if input("Turn it off ? : ").lower() == 'y':    #if you want to close the program/Chrome, you can make use of this statement
        break
    pass

'''
### RAW ###
try:
    print("started")
    time.sleep(10)
    #email_box = driver.find_element_by_name('email')
    driver.find_element_by_name('email').send_keys(u_email)
    #pass_box = driver.find_element_by_name('password')
    driver.find_element_by_name('password').send_keys(u_pass)
    ''
    for i in u_email:
        email_box.send_keys(i)
        time.sleep(random.uniform(0,1))
    print("Email Done !!!")
    time.sleep(10)
    for j in u_pass:
        pass_box.send_keys(j)
        time.sleep(random.uniform(0,1))
    print("Password Done !!!")
    ''
    cla = "marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN"
    cla = ".".join(cla.split())
    print(cla)
    time.sleep(1)
    driver.find_element_by_class_name(cla).click()
    #time.sleep(10)
    print("found")
except:
    print("cant find")
'''

#driver.close()



