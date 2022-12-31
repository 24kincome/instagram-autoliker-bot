from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AMFBot:
    def __init__(self, like4like_user, like4likepwd, instagram_user, instagram_pwd):
        self.like4like_user = like4like_user
        self.like4likepwd = like4likepwd
        self.instagram_user = instagram_user
        self.instagram_pwd = instagram_pwd
        self.options = Options()
        self.options.add_argument("--lang=en")
        self.bot = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.options)
    
    def open(self):
        bot = self.bot
        bot.maximize_window()
        bot.get("https://www.like4like.org/login/")
        usuario = bot.find_element(By.NAME, 'username')
        senha = bot.find_element(By.NAME, 'password')
        # usuario.clear()
        # senha.clear()
        usuario.send_keys(self.like4like_user)
        senha.send_keys(self.like4likepwd)
        bot.find_element(By.XPATH, '//*[@id="login"]/fieldset/table/tbody/tr[8]/td/span').click()
        time.sleep(5)
        ed.twtlk()
    
    def twtlk(self):
        bot = self.bot
        bot.get("https://www.like4like.org/earn-credits.php?feature=instagramlik")
        time.sleep(5)
        bot.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
        time.sleep(2)
        bot.switch_to.window(bot.window_handles[1])
        #window
        try:
            log_btn = WebDriverWait(bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//a[@role="link"]//div[text()="Log In"]'))
            )
            if log_btn.is_displayed():
                log_btn.click()
                usuario = WebDriverWait(bot, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//main[@role="main"] //input[@type="text"]'))
                )
                
                usuario.send_keys(self.instagram_user)
                senha = bot.find_element(By.XPATH, '//main[@role="main"] //input[@type="password"]')
                senha.send_keys(self.instagram_pwd)
                bot.find_element(By.XPATH, '//main[@role="main"] //button[@type="submit"]').click()
                time.sleep(4)
                bot.find_element(By.XPATH, '//main[@role="main"] //button[@type="button"]').click()
                
                
                like = WebDriverWait(bot, 20).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]'))
                )
                if like.is_displayed():
                    like.click()
                time.sleep(5)
            else:
                like = bot.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]')
                if like.is_displayed():
                    like.click()
                    bot.close()
                time.sleep(5)

        except bot.NoSuchElementException:
            bot.close()
            bot.switch_to.window(bot.window_handles[0])
            time.sleep(5)
            bot.get("https://www.like4like.org/earn-credits.php?feature=instagramlik")
            ed.twttwo()
        
        #window
        bot.close()
        bot.switch_to.window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()
    
    def twttwo(self):
        bot = self.bot
        confirm = bot.find_element(By.CSS_SELECTOR, "a[class^='cursor pulse-checkBox']")
        if confirm.is_displayed():
            confirm.click()
            time.sleep(3)
            bot.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            bot.switch_to.window(bot.window_handles[1])
            #window
        else:
            bot.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            bot.switch_to.window(bot.window_handles[1])
            time.sleep(5)
            #window
        
        try:
            like = WebDriverWait(bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]'))
            )
            if like.is_displayed():
                like.click()
            time.sleep(5)

        except bot.NoSuchElementException:
            bot.close()
            bot.switch_to.window(bot.window_handles[0])
            time.sleep(3)
            bot.get("https://www.like4like.org/earn-credits.php?feature=instagramlik")
            ed.twttwo()

        #window
        bot.close()
        bot.switch_to.window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()


ed = AMFBot('like4likeusername', 'like4likepassword', 'instagramusername', 'instagram password')
ed.open()