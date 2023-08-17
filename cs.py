 
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from selenium import webdriver
from userPass import username, password
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

class fbBot():
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=options)
    
    def login(self):
        self.driver.get('https://vi-vn.facebook.com/')
        time.sleep(2)
        email_in = self.driver.find_element("xpath", '//*[@id="email"]')
        email_in.send_keys(username)
        pass_in = self.driver.find_element("xpath", '//*[@id="pass"]')
        pass_in.send_keys(password)

        login_button_selector = 'button[data-testid="royal_login_button"]'
        login_button = self.driver.find_element("css selector", login_button_selector)
        login_button.click()

    def news(self):
        self.driver.execute_script("window.open('', '_blank');")
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Navigate to the news URL
        news_url = "https://vnexpress.net/podcast"
        self.driver.get(news_url)
        news_c = self.driver.find_element("css selector",'h3.title-news')
        news_c.click()
        time.sleep(3)
        fb_btn_share = self.driver.find_element("css selector",'a.circle_s.flexbox.fb.btn_share')
        fb_btn_share.click()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        fb_share = self.driver.find_element("xpath",'//button[@name="__CONFIRM__"]/span[text()="Đăng lên Facebook"]/parent::button')
        fb_share.click()

def run_bot():
    try:
        bot = fbBot()
        bot.login()
        bot.news()
        messagebox.showinfo("Hoàn thành", "Chương trình đã hoàn thành.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

def start_bot():
    thread = Thread(target=run_bot)
    thread.start()

app = tk.Tk()
app.title("Facebook Bot App")

button = tk.Button(app, text="Chạy chương trình", command=start_bot)
button.pack(pady=20)

app.mainloop()
