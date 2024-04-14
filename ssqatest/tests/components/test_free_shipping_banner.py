
import pytest
import time

from ssqatest.src.pages.components.NotificationBar import NotificationBar
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.notificationbar
@pytest.mark.regression
@pytest.mark.usefixtures('init_driver')
class TestFreeShippingBanner:

    expected_free_shipping_text = "Free shipping on orders over $50"


    @pytest.mark.tcid69
    def test_verify_free_shipping_banner_displayed_in_home_page(self):
        HomePage(self.driver).go_to_home_page()
        NotificationBar(self.driver).verify_text_on_notification_bar(TestFreeShippingBanner.expected_free_shipping_text)

    @pytest.mark.tcid70
    def test_verify_free_shipping_banner_displayed_in_cart_page(self):
        CartPage(self.driver).go_to_cart_page()
        NotificationBar(self.driver).verify_text_on_notification_bar(TestFreeShippingBanner.expected_free_shipping_text)

    @pytest.mark.tcid71
    def test_verify_free_shipping_banner_displayed_in_checkout_page(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()
        CheckoutPage(self.driver).go_to_checkout_page()
        NotificationBar(self.driver).verify_text_on_notification_bar(TestFreeShippingBanner.expected_free_shipping_text)

    @pytest.mark.tcid72
    def test_verify_free_shipping_banner_not_displayed_in_my_account_page(self):
        MyAccountSignedOut(self.driver).go_to_my_account()
        NotificationBar(self.driver).verify_notification_bar_is_not_displayed()

