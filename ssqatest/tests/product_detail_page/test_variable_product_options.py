
import time

import pytest
from ssqatest.src.pages.ProductPage import ProductPage
from selenium.common.exceptions import StaleElementReferenceException


# test data
# hard coding a product that has these variations
PRODUCT_SLUG = 'hoodie'
PRODUCT_ID = 13
COLOR_OPTIONS = ["Blue", "Green", "Red"]
LOGO_OPTIONS = ["Yes", "No"]


@pytest.mark.usefixtures("init_driver")
class TestVariableProductOptionValues:

    @pytest.fixture(scope="function")
    def go_to_pdp_setup(self, request):
        product_page = ProductPage(self.driver)
        product_page.go_to_product_page(PRODUCT_SLUG)
        request.cls.product_page = product_page


    @pytest.mark.tcid97
    def test_variable_product_number_of_options(self, go_to_pdp_setup):

        # verify number of color options
        color_option_elems = self.product_page.get_color_dropdown_options_elements()
        displayed_number_of_color_options = len(color_option_elems)
        expected_number_of_color_options = len(COLOR_OPTIONS) + 1  # +1 because the "Chose an options" option is also in the dropdown
        assert displayed_number_of_color_options == expected_number_of_color_options, \
            f"Expected {expected_number_of_color_options} options for color dropdown but found {displayed_number_of_color_options}"

        # verify number of logo options
        logo_option_elems = self.product_page.get_logo_dropdown_options_elements()
        displayed_number_of_logo_options = len(logo_option_elems)
        expected_number_of_logo_options = len(LOGO_OPTIONS) + 1  # +1 because the "Chose an options" option is also in the dropdown
        assert displayed_number_of_logo_options == expected_number_of_logo_options, \
            f"Expected {expected_number_of_logo_options} options for logo dropdown but found {displayed_number_of_logo_options}"

    @pytest.mark.tcid98
    def test_variable_product_values_of_color_options(self, go_to_pdp_setup):

        # adding retry logic to deal with StaleElementReferenceException
        for i in range(5):
            try:
                value_and_text = self.product_page.get_color_dropdown_options_values_and_text()
                break
            except StaleElementReferenceException:
                time.sleep(1)
                print("WARNING: StaleElementReferenceException. Sleeping for 1 second and retrying.")

        # verify the 'values' are in the expected list
        # first element should have value of ''
        assert value_and_text[0]['value'] == '', f"First element of the colors dropdown should not have a value."
        # first elements text should be 'Choose an option'
        assert value_and_text[0]['text'] == 'Choose an option', f"First element of the colors dropdown should have text 'Choose an option'."

        for i in value_and_text[1:]:
            assert i['value'].capitalize() in COLOR_OPTIONS, f"Color option with value '{i['value']}' in dropdown but not expected."
            # verify the 'text' are in the expected list
            assert i['text'] in COLOR_OPTIONS, f"Logo option with text '{i['text']}' in dropdown but not expected."

    @pytest.mark.tcid99
    def test_variable_product_values_of_logo_options(self, go_to_pdp_setup):

        # adding retry logic to deal with StaleElementReferenceException
        for i in range(5):
            try:
                value_and_text = self.product_page.get_logo_dropdown_options_values_and_text()
                break
            except StaleElementReferenceException:
                time.sleep(1)
                print("WARNING: StaleElementReferenceException. Sleeping for 1 second and retrying.")

        # verify the 'values' are in the expected list
        # first element should have value of ''
        assert value_and_text[0]['value'] == '', f"First element of the logo dropdown should not have a value."
        # first elements text should be 'Choose an option'
        assert value_and_text[0]['text'] == 'Choose an option', f"First element of the logo dropdown should have text 'Choose an option'."

        for i in value_and_text[1:]:
            assert i['value'].capitalize() in LOGO_OPTIONS, f"Logo option with value '{i['value']}' in dropdown but not expected."
            # verify the 'text' are in the expected list
            assert i['text'] in LOGO_OPTIONS, f"Logo option with text '{i['text']}' in dropdown but not expected."

    @pytest.mark.tcid100
    def test_variable_product_clear_selection_btn_when_only_color_is_selected(self, go_to_pdp_setup):

        color_to_select = 'Green'
        self.product_page.select_color_option_by_visible_text(color_to_select)
        selected_option = self.product_page.get_selected_color_option()
        # verify the selection was successful
        assert selected_option.text == color_to_select, f"Expected '{color_to_select}' to be selected but found '{selected_option.text}'"

        # click the reset and validate
        self.product_page.click_reset_variations_btn()
        selected_option = self.product_page.get_selected_color_option()
        assert selected_option.text == 'Choose an option', f"Clear selection button did not clear the color dropdown."

    @pytest.mark.tcid101
    def test_variable_product_clear_selection_btn_when_only_logo_is_selected(self, go_to_pdp_setup):

        logo_to_select = 'No'
        self.product_page.select_logo_option_by_visible_text(logo_to_select)
        selected_option = self.product_page.get_selected_logo_option()
        # verify the selection was successful
        assert selected_option.text == logo_to_select, f"Expected '{logo_to_select}' to be selected but found '{selected_option.text}'"

        # click the reset and validate
        self.product_page.click_reset_variations_btn()
        selected_option = self.product_page.get_selected_logo_option()
        assert selected_option.text == 'Choose an option', f"Clear selection button did not clear the logo dropdown."

    @pytest.mark.tcid102
    def test_variable_product_clear_selection_btn_when_both_color_and_logo_are_selected(self, go_to_pdp_setup):

        # select color
        color_to_select = 'Green'
        self.product_page.select_color_option_by_visible_text(color_to_select)
        selected_option = self.product_page.get_selected_color_option()
        # verify the selection was successful
        assert selected_option.text == color_to_select, f"Expected '{color_to_select}' to be selected but found '{selected_option.text}'"

        # select logo
        logo_to_select = 'No'
        self.product_page.select_logo_option_by_visible_text(logo_to_select)
        selected_option = self.product_page.get_selected_logo_option()
        # verify the selection was successful
        assert selected_option.text == logo_to_select, f"Expected '{logo_to_select}' to be selected but found '{selected_option.text}'"

        # click the reset
        self.product_page.click_reset_variations_btn()

        # verify color is reset
        selected_option = self.product_page.get_selected_color_option()
        assert selected_option.text == 'Choose an option', f"Clear selection button did not clear the color dropdown."

        # verify logo is reset
        selected_option = self.product_page.get_selected_logo_option()
        assert selected_option.text == 'Choose an option', f"Clear selection button did not clear the logo dropdown."

