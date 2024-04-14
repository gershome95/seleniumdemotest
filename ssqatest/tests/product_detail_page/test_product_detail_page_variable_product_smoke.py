

import pytest
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.helpers.api_helpers import get_random_products
from ssqatest.src.helpers.generic_helpers import convert_html_to_text
from selenium.webdriver.common.by import By





@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVariableProduct:

    @pytest.fixture(scope='class')
    def setup(self, request):

        random_product = get_random_products(qty=1, type='variable', stock_status='instock')[0]
        request.cls.product_api_data = random_product
        slug = random_product['slug']
        request.cls.product_page = ProductPage(self.driver)
        request.cls.product_page.go_to_product_page(slug)

        yield

    @pytest.mark.tcid80
    def test_variable_product_page_verify_product_name(self, setup):
        displayed_name = self.product_page.get_displayed_product_name()
        assert displayed_name == self.product_api_data['name'], f"Expected product name {self.product_api_data['name']} but was {displayed_name}"

    @pytest.mark.tcid81
    def test_variable_product_page_verify_main_image(self, setup):
        main_image_src = self.product_page.get_url_of_displayed_main_image()
        # create a list of all images in the api response
        images = [i['src'] for i in self.product_api_data['images']]
        assert main_image_src in images, f"The product main image url is not as expected. Expected: {images}. Actual: {main_image_src}"

    @pytest.mark.tcid82
    def test_variable_product_page_verify_extra_images(self, setup):
        all_thumbnails = self.product_page.get_url_of_displayed_alternate_images()
        # create a list of all images in the api response
        images = [i['src'] for i in self.product_api_data['images']]
        for i in all_thumbnails:
            assert i.replace('-100x100.jpg', '.jpg') in images, f"Expected the displayed thumbnail to be in the product info. Thumbnail url: {i}"

    @pytest.mark.tcid83
    def test_variable_product_page_verify_product_type_text(self, setup):
        product_type_text = self.product_page.get_product_type_text()
        assert product_type_text == 'This is a variable product.', f"Unexpected product type text on page." \
                                                                   f"Expected: 'This is a variable product.'" \
                                                                   f"Actual: '{product_type_text}'"

    @pytest.mark.tcid84
    def test_variable_product_page_verify_price_range_before_option_selection(self, setup):
        price_html = self.product_page.get_displayed_product_price()
        api_price_string = convert_html_to_text(self.product_api_data['price_html'])
        assert price_html == api_price_string, f"Expected price_html = {api_price_string}," \
                                              f"Actual: {price_html}"

    @pytest.mark.tcid85
    def test_variable_product_page_verify_add_to_cart_btn_displayed(self, setup):

        add_to_cart_elem = self.product_page.get_add_to_cart_button_element()
        assert add_to_cart_elem.text == 'Add to cart', f"Add to cart button expected to have test 'Add to cart' " \
                                                       f"but was {add_to_cart_elem.text}"

    @pytest.mark.tcid86
    def test_variable_product_page_verify_quantity_field(self, setup):
        qty_field = self.product_page.get_quantity_field_element()
        displayed_value = qty_field.get_attribute('value')
        assert displayed_value == '1', f"Quantity field expected to have default value of '1' but found {displayed_value}"

    @pytest.mark.tcid87
    def test_variable_product_page_verify_sku(self, setup):
        sku_and_label = self.product_page.get_displayed_sku_and_label()
        assert sku_and_label == f'SKU: {self.product_api_data["sku"]}', f"Expected sku info with text 'SKU: {self.product_api_data['sku']}' but found {sku_and_label}"

    @pytest.mark.tcid88
    def test_variable_product_page_verify_category(self, setup):
        category_and_label = self.product_page.get_displayed_category_and_label()
        api_category = self.product_api_data['categories'][0]['name']
        assert category_and_label == f'Category: {api_category}', f"Expected category info with text 'Category: {api_category}' but found {sku_and_label}"

    @pytest.mark.tcid89
    def test_variable_product_page_verify_description(self, setup):
        description_on_page = self.product_page.get_displayed_product_description()

        api_description = self.product_api_data['description']
        string_description_from_api = convert_html_to_text(api_description)
        string_from_api_clean = string_description_from_api.strip()
        assert description_on_page == string_from_api_clean, f"Description on page and from API do not match. \n" \
                                                             f"Description on page: {description_on_page} \n" \
                                                             f"Description from API: {string_from_api_clean}"

    @pytest.mark.tcid90
    def test_variable_product_page_verify_description_header(self, setup):
        description_header = self.product_page.get_displayed_product_description_header()
        assert description_header == 'Description', f"Header for description section expected to be 'Description' but was {description_header}"

    @pytest.mark.tcid91
    def test_variable_product_page_related_items_header(self, setup):
        section_header = self.product_page.get_related_products_section_header()
        assert section_header == 'Related products', f"The related products section header expected to be 'Related products' but was '{section_header}'"

    @pytest.mark.tcid92
    def test_variable_product_page_related_items_list(self, setup):
        related_products_elements = self.product_page.get_related_products_elements_list()
        related_ids = self.product_api_data['related_ids']
        number_of_related = len(related_ids)
        # page is expected to only show 3 even if there are more related
        exp_number_of_related = 3 if number_of_related >= 3 else len(related_ids)
        assert len(related_products_elements) == exp_number_of_related, f"Expected {exp_number_of_related} related products to be displayed but found {len(related_products_elements)}"
        # verify images are displayed
        for i in related_products_elements:
            image_element = i.find_element(By.TAG_NAME, 'img')
            assert image_element.is_displayed(), f"Image for related product is not displayed."
            src = image_element.get_attribute('src')
            assert src.endswith('.jpg'), f"Image for related product does not have 'src' attribute ending with .jpg"

    @pytest.mark.tcid93
    def test_variable_product_page_left_nav_tab_labels(self, setup):
        tab_labels = self.product_page.get_labels_of_left_nav_tabs()
        assert len(tab_labels) == 3, f"Variable product should have 3 tabs on the left nav but found {len(tab_labels)} tabs."
        assert 'Description' in tab_labels, f"Left nav tabs expected to have a tab with label 'Description'."
        assert 'Additional information' in tab_labels, f"Left nav tabs expected to have a tab with label 'Description'."
        rating_count = self.product_api_data['rating_count']
        assert f'Reviews ({rating_count})' in tab_labels, f"Left nav tabs expected to have a tab with label 'Description'."

    @pytest.mark.tcid94
    def test_variable_product_page_color_dropdown_label(self, setup):
        label = self.product_page.get_label_for_color_attribute_dropdown()
        assert label == 'Color', f"Expected label 'Color' for color attribute dropdown."

    @pytest.mark.tcid95
    def test_variable_product_page_logo_dropdown_label(self, setup):
        label = self.product_page.get_label_for_logo_attribute_dropdown()
        assert label == 'Logo', f"Expected label 'Logo' for logo attribute dropdown."
