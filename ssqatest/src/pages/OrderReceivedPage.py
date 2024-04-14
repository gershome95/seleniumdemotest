
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators

class OrderReceivedPage(OrderReceivedPageLocators):
#gershom's verison

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, 'Order received')

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)








    # def __init__(self, driver):
    #     self.driver = driver
    #     self.sl = SeleniumExtended(self.driver)
    #
    # def verify_order_received_page_loaded(self):
    #     self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, "Order received")
    #
    # def get_order_number(self):
    #     return self.sl.wait_and_get_text(self.ORDER_NUMBER)