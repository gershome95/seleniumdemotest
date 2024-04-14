
from selenium.webdriver.common.by import By



class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')

    COUPON_FIELD = (By.ID, 'coupon_code')

    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button[name= "apply_coupon')

    CART_PAGE_MESSAGE = (By.CLASS_NAME, 'woocommerce-message')

    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'a.checkout-button')
# class CartPageLocators:
#
#     PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
#     COUPON_FIELD = (By.ID, 'coupon_code')
#     APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
#
#     CART_PAGE_MESSAGE = (By.CLASS_NAME, 'woocommerce-message')
#     ERROR_BOX = (By.CSS_SELECTOR, 'div.woocommerce-notices-wrapper ul.woocommerce-error')
#
#     PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button')