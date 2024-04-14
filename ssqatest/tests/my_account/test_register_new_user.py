
import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.userfixtures("init_driver")
class TestRegisterNewUser:
    def __init__(self, driver):
        self.driver = driver

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver
                                         )
        # go to my accounnt
        my_account_o.go_to_my_account()
        rand_email = generate_random_email_and_password


        # FILL IN EMAIL
        my_account_o.input_register_email(rand_email["email"])
        # FILL IN PASSWORD
        my_account_o.input_register_password('abcs132')
        # CLICK REGISTER
        my_account_o.click_register_button()
        # VERIFY USER IS REGISTERED
        my_account_i.verify_user_is_signed_in()























# @pytest.mark.usefixtures("init_driver")
# class TestRegisterNewUser:
#
#     @pytest.mark.tcid13
#     def test_register_valid_new_user(self):
#         my_account_o = MyAccountSignedOut(self.driver)
#         my_account_i = MyAccountSignedIn(self.driver)
#
#         my_account_o.go_to_my_account()
#
#         rand_email = generate_random_email_and_password()
#         my_account_o.input_register_email(rand_email["email"])
#         my_account_o.input_register_password('1234abc11!!')
#         my_account_o.click_register_button()
#
#         # verify user is registered
#         my_account_i.verify_user_is_signed_in()