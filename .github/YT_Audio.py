from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # type: ignore


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query" + query)
        video = self.driver.find_element(By.XPATH, '//*[@id="dismissable"]')
        video.click()


# assist=music()
# assist.play('yellow tape by chris brown')