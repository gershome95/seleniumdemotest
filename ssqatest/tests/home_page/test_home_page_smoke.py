
import pytest

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures('init_driver')
class TestHomePageSmoke:

    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()

        yield

    @pytest.mark.tcid1
    def test_verify_number_of_products_displayed(self, setup):
        expected_number_of_products = 16
        all_product_elements = self.homepage.get_all_product_elements()

        assert len(all_product_elements) == expected_number_of_products, \
            f"Unexpected number of products displayed on home page. " \
            f"Expected: {expected_number_of_products}, Actual: {len(all_product_elements)}"

    @pytest.mark.tcid67
    def test_verify_heading_is_displayed(self, setup):
        expected_heading = 'Shop'
        displayed_heading = self.homepage.get_displayed_heading()
        assert displayed_heading == expected_heading, \
            f"Displayed heading in home page is not as expected. " \
            f"Expected: {expected_heading}, Actual: {displayed_heading}"

    @pytest.mark.tcid68
    def test_verify_header_menu_is_displayed(self, setup):
        self.header.assert_all_menu_items_displayed()
