

import pytest
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.CartPage import CartPage


# test data
# hard coding a product that has these variations
PRODUCT_SLUG = 'hoodie'



@pytest.mark.usefixtures("init_driver")
class TestVariableProductAddToCartFromPDP:

    @pytest.fixture(scope="function")
    def go_to_pdp_setup(self, request):
        request.cls.product_page = ProductPage(self.driver)
        request.cls.product_page.go_to_product_page(PRODUCT_SLUG)
        request.cls.cart_page = CartPage(self.driver)

    @pytest.mark.tcid96
    def test_variable_product_pdp_select_options_add_to_cart(self, go_to_pdp_setup):
        # test data
        color_to_select = 'Blue'
        logo_to_select = 'Yes'
        expected_name_in_cart = 'Hoodie - Blue, Yes'

        # select color
        self.product_page.select_color_option_and_verify(color_to_select)

        # select logo
        self.product_page.select_logo_option_and_verify(logo_to_select)

        # click the 'Add to cart button
        self.product_page.click_add_to_cart_button()

        # go to cart by clicking the button in the success message
        self.product_page.click_view_cart_btn_on_add_to_cart_success_message_box()

        # verify cart page is loaded
        self.cart_page.verify_cart_page_url()

        # verify the correct product is added in cart
        products_in_cart = self.cart_page.get_all_product_names_in_cart()
        assert expected_name_in_cart in products_in_cart, f"After adding to cart unable to find product in the cart." \
                                                          f"Expected product name in cart: {expected_name_in_cart}," \
                                                          f"Actual name in cart: {products_in_cart}"


