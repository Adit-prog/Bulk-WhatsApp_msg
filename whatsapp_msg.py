#This program is created by Aditya Pandey 
#Reason to create this project is only for fun don't use it for wrong purpose 

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\PythonProjects\Bulk Whatsapp_msg\chromedriver.exe") #Give here you path of where you save this project
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

#After scan the QR code Give victim name , msg you want to send and number of count
name = input("Enter name : ")
msg = input("Enter message : ")
count = int(input("Enter count : "))

input("Enter the anythong after scan QRcode : ")

user =  driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("All msg are send !")

