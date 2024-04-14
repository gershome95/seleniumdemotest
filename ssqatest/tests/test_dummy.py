import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy():
    def test_dummy(self):
        print("I am dummy test 1")
        print("I am dummy test 2")
        self.driver.get("https://supersqa.com")
        import pdb; pdb.set_trace()

    #
# import pytest
#
# @pytest.mark.usefixtures("init_driver")
# class TestDummy():
#
#     @pytest.mark.dummytest
#     def test_dummy_func(self):
#         print("I am dummy test line 1")
#         print("I am dummy test line 2")
#         # self.driver.get("https://supersqa.com")
#         # import pdb; pdb.set_trace()