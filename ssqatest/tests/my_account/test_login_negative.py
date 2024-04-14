import pytest
from ssqatest.src.pages.locators.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.userfixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    @pytest.mark.smoke


    def test_login_none_exisiting_user(self):
        print("PASS")
        return

        my_account = MyAccountSignedOut(self.driver) #creating an instance of myaccount

        #go to my account
        my_account.go_to_my_account()

        #type username
        my_account.input_login_username('djfhakj')

        #type password
        my_account.input_login_username('sdfajhsbdfljak')

        #clcik login
        my_account.click_login_button()
        #verify error message
        expected_err = 'Unknown email address. Check again or try your username.'
        my_account.wait_until_error_is_displayed(expected_err)

















# @pytest.mark.usefixtures("init_driver")
# class TestLoginNegative:
#
#     @pytest.mark.tcid12
#     @pytest.mark.smoke
#     def test_login_none_existing_user(self):
#         print("*******")
#         print("TEST LOGIN NON EXISTING")
#         print("*******")
#         my_account = MyAccountSignedOut(self.driver)
#         my_account.go_to_my_account()
#         my_account.input_login_username('adfjladkf')
#         my_account.input_login_password('adfadfadf')
#         my_account.click_login_button()
#
#         # verify error message
#         expected_err = 'Unknown username. Check again or try your email address.'
#         # expected_err = 'ERROR: Invalid username. Lost your password?'
#         my_account.wait_until_error_is_displayed(expected_err)