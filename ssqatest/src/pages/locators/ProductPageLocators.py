
from selenium.webdriver.common.by import By

class ProductPageLocators:

    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.entry-summary h1.product_title.entry-title')
    PRODUCT_IMAGE_MAIN = (By.CSS_SELECTOR, 'div.woocommerce-product-gallery.images figure img.wp-post-image')
    PRODUCT_ALTERNATE_IMAGES = (By.CSS_SELECTOR, 'div.woocommerce-product-gallery.images ol.flex-control-thumbs li img')
    PRODUCT_TYPE_TEXT = (By.CSS_SELECTOR, 'div.entry-summary div.woocommerce-product-details__short-description')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.entry-summary p.price')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'div[class*="add-to-cart"] button[class*="add_to_cart_button"][type="submit"]')
    VIEW_CART_BTN_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.woocommerce-message[role="alert"] a.button.wc-forward')
    PRODUCT_PAGE_QUANTITY_FIELD = (By.CSS_SELECTOR, 'div[class*="add-to-cart"] div.quantity input.input-text.qty')
    PRODUCT_PAGE_SKU_AND_LABEL = (By.CSS_SELECTOR, 'div.product_meta span.sku_wrapper')
    PRODUCT_PAGE_CATEGORY_AND_LABEL = (By.CSS_SELECTOR, 'div.product_meta span.posted_in')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'div#tab-description p')
    PRODUCT_DESCRIPTION_HEADER = (By.CSS_SELECTOR, 'div#tab-description h2')
    RELATED_PRODUCTS_SECTION_HEADER = (By.CSS_SELECTOR, 'section.related.products > h2')
    RELATED_PRODUCTS_LIST = (By.CSS_SELECTOR, 'section.related.products ul li.type-product')
    LEFT_NAV_TABS = (By.CSS_SELECTOR, 'div.woocommerce-tabs ul.tabs.wc-tabs li')
    VARIABLE_PRODUCT_COLOR_ATTRIBUTE_LABEL = (By.CSS_SELECTOR, 'table.variations tr th.label label[for="pa_color"]')
    VARIABLE_PRODUCT_LOGO_ATTRIBUTE_LABEL = (By.CSS_SELECTOR, 'table.variations tr th.label label[for="logo"]')
    VARIABLE_PRODUCT_COLOR_ATTRIBUTE_DROPDOWN = (By.CSS_SELECTOR, 'table.variations tr select[name="attribute_pa_color"]')
    VARIABLE_PRODUCT_COLOR_ATTRIBUTE_OPTIONS = (By.CSS_SELECTOR, 'table.variations tr select[name="attribute_pa_color"] option')
    VARIABLE_PRODUCT_LOGO_ATTRIBUTE_OPTIONS = (By.CSS_SELECTOR, 'table.variations tr select[name="attribute_logo"] option')
    VARIABLE_PRODUCT_LOGO_ATTRIBUTE_DROPDOWN = (By.CSS_SELECTOR, 'table.variations tr select#logo')

    RESET_VARIATIONS_BTN = (By.CSS_SELECTOR, 'table.variations a.reset_variations')

