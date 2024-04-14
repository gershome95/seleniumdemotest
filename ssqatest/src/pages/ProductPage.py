import time

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.ProductPageLocators import ProductPageLocators
from ssqatest.src.helpers.config_helpers import get_base_url
from selenium.webdriver.support.ui import Select

class ProductPage(ProductPageLocators):



    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_product_page(self, product_slug):
        base_url = get_base_url()
        product_page_url = f"{base_url}/product/{product_slug}"
        self.driver.get(product_page_url)

    def get_displayed_product_name(self):
        return self.sl.wait_and_get_text(self.PRODUCT_TITLE)

    def get_url_of_displayed_main_image(self):
        image_elm = self.sl.wait_until_element_is_visible(self.PRODUCT_IMAGE_MAIN)
        src = image_elm.get_attribute('data-src')
        return src

    def get_url_of_displayed_alternate_images(self):
        image_elements = self.sl.wait_until_elements_are_visible(self.PRODUCT_ALTERNATE_IMAGES)
        srcs = [elem.get_attribute('src') for elem in image_elements]
        return srcs

    def get_product_type_text(self):
        return self.sl.wait_and_get_text(self.PRODUCT_TYPE_TEXT)


    def get_displayed_product_price_inner_html(self):
        elem = self.sl.wait_and_get_elements(self.PRODUCT_PRICE)[0]
        return elem.get_attribute('innerHTML')

    def get_displayed_product_price(self):

        return self.sl.wait_and_get_text(self.PRODUCT_PRICE)

    def get_add_to_cart_button_element(self):
        return self.sl.wait_until_element_is_visible(self.ADD_TO_CART_BUTTON)

    def click_add_to_cart_button(self):
        add_cart_btn = self.get_add_to_cart_button_element()
        add_cart_btn.click()

    def get_view_cart_btn_on_add_to_cart_success_message_box(self):
        return self.sl.wait_until_element_is_visible(self.VIEW_CART_BTN_IN_SUCCESS_MESSAGE)

    def click_view_cart_btn_on_add_to_cart_success_message_box(self):
        view_cart_btn = self.get_view_cart_btn_on_add_to_cart_success_message_box()
        view_cart_btn.click()

    def get_quantity_field_element(self):
        return self.sl.wait_until_element_is_visible(self.PRODUCT_PAGE_QUANTITY_FIELD)

    def get_displayed_sku_and_label(self):
        return self.sl.wait_and_get_text(self.PRODUCT_PAGE_SKU_AND_LABEL)

    def get_displayed_category_and_label(self):
        return self.sl.wait_and_get_text(self.PRODUCT_PAGE_CATEGORY_AND_LABEL)

    def get_displayed_product_description(self):
        return self.sl.wait_and_get_text(self.PRODUCT_DESCRIPTION)

    def get_displayed_product_description_header(self):
        return self.sl.wait_and_get_text(self.PRODUCT_DESCRIPTION_HEADER)

    def get_related_products_section_header(self):
        return self.sl.wait_and_get_text(self.RELATED_PRODUCTS_SECTION_HEADER)

    def get_related_products_elements_list(self):
        related_products_list = self.sl.wait_until_elements_are_visible(self.RELATED_PRODUCTS_LIST)
        return related_products_list

    def get_left_nav_tab_elements(self):
        return self.sl.wait_until_elements_are_visible(self.LEFT_NAV_TABS)

    def get_labels_of_left_nav_tabs(self):
        tabs_elements = self.get_left_nav_tab_elements()
        return [i.text for i in tabs_elements]

    def get_label_for_color_attribute_dropdown(self):
        return self.sl.wait_and_get_text(self.VARIABLE_PRODUCT_COLOR_ATTRIBUTE_LABEL)

    def get_label_for_logo_attribute_dropdown(self):
        return self.sl.wait_and_get_text(self.VARIABLE_PRODUCT_LOGO_ATTRIBUTE_LABEL)

    def get_color_dropdown_options_elements(self):
        return self.sl.wait_until_elements_are_visible(self.VARIABLE_PRODUCT_COLOR_ATTRIBUTE_OPTIONS)

    def get_logo_dropdown_options_elements(self):
        return self.sl.wait_until_elements_are_visible(self.VARIABLE_PRODUCT_LOGO_ATTRIBUTE_OPTIONS)


    def get_color_dropdown_options_values_and_text(self):
        options_elements = self.get_color_dropdown_options_elements()

        value_and_text = []
        for element in options_elements:
            self.sl.wait_until_element_is_visible(element)
            value_and_text.append({'value': element.get_attribute('value'), 'text': element.text})

        return value_and_text

    def get_logo_dropdown_options_values_and_text(self):
        options_elements = self.get_logo_dropdown_options_elements()

        value_and_text = []
        for element in options_elements:
            self.sl.wait_until_element_is_visible(element)
            value_and_text.append({'value': element.get_attribute('value'), 'text': element.text})

        return value_and_text

    def select_color_option_by_visible_text(self, color):
        color_dropdown = self.sl.wait_until_element_is_visible(self.VARIABLE_PRODUCT_COLOR_ATTRIBUTE_DROPDOWN)
        select = Select(color_dropdown)
        select.select_by_visible_text(color)

    def select_logo_option_by_visible_text(self, logo_option):
        logo_dropdown = self.sl.wait_until_element_is_visible(self.VARIABLE_PRODUCT_LOGO_ATTRIBUTE_DROPDOWN)
        select = Select(logo_dropdown)
        select.select_by_visible_text(logo_option)

    def click_reset_variations_btn(self):
        self.sl.wait_and_click(self.RESET_VARIATIONS_BTN)

    def get_selected_color_option(self):
        color_dropdown = self.sl.wait_until_element_is_visible(self.VARIABLE_PRODUCT_COLOR_ATTRIBUTE_DROPDOWN)
        select = Select(color_dropdown)
        return select.first_selected_option

    def get_selected_logo_option(self):
        logo_dropdown = self.sl.wait_until_element_is_visible(self.VARIABLE_PRODUCT_LOGO_ATTRIBUTE_DROPDOWN)
        select = Select(logo_dropdown)
        return select.first_selected_option

    def select_color_option_and_verify(self, color_to_select):
        self.select_color_option_by_visible_text(color_to_select)
        selected_option = self.get_selected_color_option()
        # verify the selection was successful
        assert selected_option.text == color_to_select, f"Expected '{color_to_select}' to be selected but found '{selected_option.text}'"

    def select_logo_option_and_verify(self, logo_to_select):
        self.select_logo_option_by_visible_text(logo_to_select)
        selected_option = self.get_selected_logo_option()
        # verify the selection was successful
        assert selected_option.text == logo_to_select, f"Expected '{logo_to_select}' to be selected but found '{selected_option.text}'"
