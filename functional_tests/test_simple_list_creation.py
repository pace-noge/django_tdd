#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest



class NewVisitorTest(FunctionalTest):   
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # checkout the home page
        self.browser.get(self.server_url)
        
        # notice the page title and header mention to-do lists
        self.assertIn("To-Do lists", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        # types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when hits enter, the page update, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # there is still a text box inviting to add another item. 
        # Enter "Use peacock feathers to make a fly"
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, and now show both items on her list
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        # that site has generated a unique URL for her -- there is some
        # explanatory text to that effect
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Visits that URL - her to-do list is still there
        
        # now new user, Francis, comes along to the site
        
        ## We use a new browser session
        self.browser.quit()
        self.browser = webdriver.Chrome()
        
        # francis visit the home page, Thereis no sign of edith's
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis start new list by entering new item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        # francis get his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # satisfied, goes back to sleep
        #self.fail("Finish the test")
        
    
        
        
