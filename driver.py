from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver():
    # Classe singleton que instancia o navegador 

    __driver = None

    def __new__(self):
        if Driver.__driver is None:
            self.__initDriver(self)
        return Driver.__driver
    
    def __initDriver(self):
        chrome_options = Options()  
        #chrome_options.add_argument("--headless") 
        self.__driver = webdriver.Chrome(chrome_options=chrome_options)

    def init(self):
        pass

    def close_driver(self):
        self.__driver.quit()