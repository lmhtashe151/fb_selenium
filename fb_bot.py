 
from selenium import webdriver
from userPass import username,password
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# .\venv\Scripts\Activate
# class fbBot():
#     def __init__(self):
#         options = Options()
#         options.add_argument("--disable-notifications")
#         self.driver = webdriver.Chrome(options=options)

#     def login(self, username, password):
#         self.driver.get('https://vi-vn.facebook.com/')
#         sleep(2)
#         email_in = self.driver.find_element("xpath", '//*[@id="email"]')
#         email_in.send_keys(username)
#         pass_in = self.driver.find_element("xpath", '//*[@id="pass"]')
#         pass_in.send_keys(password)

#         login_button_selector = 'button[data-testid="royal_login_button"]'
#         login_button = self.driver.find_element("css selector", login_button_selector)
#         login_button.click()

#     def follow(self, username, password):
#         self.login(username, password)
#         sleep(5)
#         self.driver.get('https://www.facebook.com/qcan1501')
#         # theo_doi_button = self.driver.find_element("xpath", '//div[@aria-label="Theo dõi"]')
#         # if theo_doi_button is not None and theo_doi_button.is_displayed():
#         #     theo_doi_button.click()

#     def run(self, account_file):
#         with open(account_file, 'r') as file:
#             for line in file:
#                 username, password = line.strip().split(',')
#                 self.follow(username, password)


# bot = fbBot()
# bot.run('accounts.txt')


class fbBot():
    def __init__(self):
        # self.driver = webdriver.Chrome()
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=options)
    def login(self):
        self.driver.get('https://vi-vn.facebook.com/')
        sleep(2)
        email_in = self.driver.find_element("xpath",'//*[@id="email"]')
        email_in.send_keys(username)
        pass_in = self.driver.find_element("xpath",'//*[@id="pass"]')
        pass_in.send_keys(password)

        login_button_selector = 'button[data-testid="royal_login_button"]'
        login_button = self.driver.find_element("css selector", login_button_selector)
        login_button.click()


        #mount_0_0_hY > div > div:nth-child(1) > div > div:nth-child(3) > div.xds687c.x1pi30zi.x1e558r4.xixxii4.x13vifvy.xzkaem6 > div:nth-child(2) > div > div
        # input_element = self.driver.find_element("xpath",'//input[@aria-label="Tìm kiếm trên Facebook"]')
        # input_element.send_keys("qcan1501")
        # add_con = self.driver.find_element("css selector",'div[aria-label="Tạo bài viết"]')
        # add_con.click()
        # bot.driver.find_element("css selector",'__fb-light-mode')
    # def follow(self):
    #     sleep(5)
    #     self.driver.get('https://www.facebook.com/qcan1501')
    #     theo_doi_button = self.driver.find_element("xpath",'//div[@aria-label="Theo dõi"]')
    #     theo_doi_button.click()

        # logout = bot.driver.find_element("xpath",'//div[@aria-label="Cài đặt và kiểm soát tài khoản"]')
        # logout.click()
    def news(self):
        # Open a new tab
        self.driver.execute_script("window.open('', '_blank');")
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Navigate to the news URL
        news_url = "https://vnexpress.net/podcast"
        self.driver.get(news_url)
        news_c = self.driver.find_element("css selector",'h3.title-news')
        news_c.click()
        sleep(5)
        fb_btn_share = self.driver.find_element("css selector",'a.circle_s.flexbox.fb.btn_share')
        fb_btn_share.click()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        fb_share = self.driver.find_element("xpath",'//button[@name="__CONFIRM__"]/span[text()="Đăng lên Facebook"]/parent::button')
        fb_share.click()
        

#podcast_detail_player > div > div > div.item-news.flexbox > div.social-pop-right.social-com.flexbox > a.circle_s.flexbox.fb.btn_share
bot = fbBot()
bot.login()
bot.news()
# bot.follow()
