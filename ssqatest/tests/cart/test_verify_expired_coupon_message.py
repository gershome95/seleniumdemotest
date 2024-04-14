
import pytest
from ssqatest.src.helpers.api_helpers import create_coupon, delete_coupon_by_coupon_code
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header

@pytest.mark.usefixtures("init_driver")
class TestCartExpiredCoupon:

    @pytest.fixture(scope='class')
    def setup(self, request):
        expired_coupon = create_coupon(expired=True)
        request.cls.expired_coupon = expired_coupon
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield
        delete_coupon_by_coupon_code(expired_coupon)

    @pytest.mark.tcid66
    def test_expired_coupon_message(self, setup):
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        self.cart.apply_coupon(self.expired_coupon, expect_success=False)
        notice = self.cart.get_displayed_error()
        assert notice == 'This coupon has expired.', "Expired coupon error not displayed."
