from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Users\abdul\Desktop\chromedriver-win64\chromedriver.exe")

    def get_info(self,query):
        self.query=query
        self.driver.get(url='https://www.wikipedia.org/')

assist=infow()
assist.get_info("hello") 