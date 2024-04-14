
import time

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.components.NotificationBarLocators import NotificationBarLocators


class NotificationBar(NotificationBarLocators):



    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_notification_bar_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.NOTIFICATION_BAR_TEXT)

    def verify_text_on_notification_bar(self, expected_text):
        self.verify_notification_bar_is_displayed()
        self.sl.wait_until_element_contains_text(self.NOTIFICATION_BAR_TEXT, expected_text)

    def verify_notification_bar_is_not_displayed(self):

        # we know the notification bar has setting to showsup after a delay.
        # so lets just wait few seconds before checking it is displayed or not
        try:
            self.sl.wait_until_element_is_visible(self.NOTIFICATION_BAR_TEXT, timeout=3)
            raise Exception("The 'Notification Bar' should not have been displayed on 'Checkout' page but it is")
        except:
            pass