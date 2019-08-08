
                    # composing and sending email automatically using selenium web driver

from selenium import webdriver
import time

sender_email = "sksaundarya10@gmail.com"                                                        # sender's email id
email_pass = "spada codatronca"                                                                 # sender's password
receiver_email = "sksaundarya@gmail.com"                                                        # receiver's email id
subject_email = "email automation - test email"                                                 # subject of the email
body_email = "This is a test email sent using selenium web driver"                              # body of the email


driver=webdriver.Chrome(r"C:\Users\Saundarya\Documents\Python Scripts\chromedriver.exe")
driver.maximize_window()
driver.get('http://www.gmail.com')
time.sleep(2)
driver.find_element_by_name("identifier").send_keys(sender_email)                               # email id of sender
driver.find_element_by_id("identifierNext").click()                                             # next button
driver.implicitly_wait(5)                                                                       # wait for browser to load
driver.find_element_by_name("password").send_keys(email_pass)                                   # password
driver.find_element_by_id("passwordNext").click()                                               # next button
driver.find_element_by_css_selector('.aic .z0 div').click()
driver.find_element_by_name("to").send_keys(receiver_email)
driver.implicitly_wait(5)
driver.find_element_by_name("subjectbox").send_keys(subject_email)
driver.implicitly_wait(5)
driver.find_element_by_css_selector(".Ar.Au div").send_keys(body_email)
driver.implicitly_wait(5)
driver.find_element_by_css_selector("tr.btC td:nth-of-type(1) div div:nth-of-type(2)").click();   # btC is class name of row in which the first cell and second divison contains send button
time.sleep(10)


print("The email is sent successfully !!!")


