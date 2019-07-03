from selenium import webdriver

prefs = {
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_settings.popups": 0,
}
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("prefs", prefs)


username = "enter your username"
password = "enter your password"
url = "https://www.facebook.com"
driver = webdriver.Chrome("/Users/kartikgupta/Downloads/chromedriver")
driver.get(url)
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
driver.get("https://www.facebook.com/events/birthdays/")
feed = "Happy Birthday Dude!"
element = driver.find_elements_by_xpath(
    "//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']"
)

for el in element:
    cnt += 1
    element_id = str(el.get_attribute("id"))
    print(element_id)
    XPATH = '//*[@id ="' + element_id + '"]'
    post_field = driver.find_element_by_xpath(XPATH)
    post_field.send_keys(feed)

