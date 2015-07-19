
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # checkout the home page
        self.browser.get("http://localhost:8000")
        
        # notice the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")
    # enter a to-do item straight away


    # types "Buy peacock feathers" into a text box

    # when hits enter, the page update, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # there is still a text box inviting to add another item. 
    # Enter "Use peacock feathers to make a fly"

    # the page updates again, and now show both items on her list


    # that site has generated a unique URL for her -- there is some
    # explanatory text to that effect

    # Visits that URL - her to-do list is still there


    # satisfied, goes back to sleep

if __name__ == "__main__":
    unittest.main(warnings='ignore')
