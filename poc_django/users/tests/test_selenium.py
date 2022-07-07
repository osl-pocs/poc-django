# ref: https://ordinarycoders.com/blog/article/testing-django-selenium
import chromedriver_binary
from django.test import LiveServerTestCase
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys


class LoginTest(LiveServerTestCase):
    def test_login(self):
        selenium = webdriver.Chrome(chromedriver_binary.chromedriver_filename)
        assert selenium
        # Choose your url to visit
        # selenium.get('http://127.0.0.1:8000/')
        # #find the elements you need to submit form
        # player_name = selenium.find_element_by_id('id_name')
        # player_height = selenium.find_element_by_id('id_height')
        # player_team = selenium.find_element_by_id('id_team')
        # player_ppg = selenium.find_element_by_id('id_ppg')
        # submit = selenium.find_element_by_id('submit_button')
        # #populate the form with data
        # player_name.send_keys('Lebron James')
        # player_team.send_keys('Los Angeles Lakers')
        # player_height.send_keys('6 feet 9 inches')
        # player_ppg.send_keys('25.7')
        # #submit form
        # submit.send_keys(Keys.RETURN)
        # #check result; page source looks at entire html document
        # assert 'Lebron James' in selenium.page_source
