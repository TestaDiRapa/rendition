from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from character import Character 

class Roll20Driver:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.characters = dict()

    def login(self, username, password):
        self.driver.get("https://app.roll20.net/login")
        login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "login")))
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.withad")))

    def list_games(self):
        ret = list()
        self.driver.get("https://app.roll20.net/campaigns/search/")
        page_index = 1
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.campaigns")))
        campaigns = self.driver.find_elements_by_css_selector("h3.campaignname a")
        while len(campaigns) > 0:
            for c in campaigns:
                url = c.get_attribute("href")
                game_id = re.search(r'[0-9]{6,}', url)
                ret.append((c.text, game_id.group()))
            page_index += 1
            self.driver.get(f"https://app.roll20.net/campaigns/search/?p={page_index}")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pull-right")))
            campaigns = self.driver.find_elements_by_css_selector("h3.campaignname a")
        return ret

    def list_characters(self, game_id):
        ret = list()
        self.driver.get(f"https://app.roll20.net/editor/setcampaign/{game_id}")
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_css_selector("a[href='#journal']").click()
        characters = self.driver.find_elements_by_css_selector("li.journalitem.dd-item.character.ui-draggable")
        for c in characters:
            soup = BeautifulSoup(c.get_attribute('innerHTML'), 'lxml')
            name = soup.find("div", {"class": "namecontainer"}).text
            self.characters[name] = c
            ret.append(name)
        return ret

    def get_character(self, name):
        self.characters[name].click()
        character_id = self.characters[name].get_attribute("data-itemid")
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, f"iframe[name='iframe_{character_id}']")))
        self.driver.implicitly_wait(5)
        c = Character(self.driver.page_source)
        c.save_to_txt()
        self.driver.switch_to.default_content()
