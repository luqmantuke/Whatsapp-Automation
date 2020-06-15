from  selenium import webdriver

url = "https://web.whatsapp.com/"
driver = webdriver.Chrome()
driver.get(url)

scan = input('Press any key to continue after scanning')
print('scanned successfully logged in!')
count = int(input('How many times?: '))
name = input('Enter the name to send to: ')
msg = input('Enter your message: ')


def main():
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    message = driver.find_element_by_class_name('_3uMse')
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    for i in range(count):
        message.send_keys(msg)
        button.click()


main()

driver.quit()
