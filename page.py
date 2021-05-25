from driver import Driver
from selenium.common.exceptions import NoSuchElementException

class Page():   

    def __init__(self,url):
        self.driver=Driver()   
        self.driver.get(url)   

    def name_is_there(self,full_name):
        try:
            self.driver.find_element_by_xpath("//*[text()='"+full_name+"']")
            return True
        except NoSuchElementException:
            return False

    def close(self):
        self.driver.close_driver()