from core.templates.unittest.base_unit_case import BaseUnitCase
from datetime import datetime
import time


class TestIntelligentSearch(BaseUnitCase):

    def test_click_search(self, selenium_driver):

        selenium_driver.implicitly_wait(30)

        test_class = selenium_driver.find_element_by_class_name('new-search-con')
        time.sleep(2)

        div = test_class.find_elements_by_tag_name('button')
        self.assertEqual(div[0].get_attribute('innerHTML'), '百度一下', '验证 内容')
