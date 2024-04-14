
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions

import os
import allure



@pytest.fixture(scope="class")
def init_driver(request):

    driver = webdriver.Chrome()
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'headlessfirefox':
        ff_options = FFOptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)
    else:
        print(browser)
        breakpoint()

    request.cls.driver = driver
    yield
    driver.quit()

import pytest_html


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         xfail = hasattr(report, "wasxfail")
#         # check if test failed
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception("Environment variable 'RESULTS_DIR' must be set")
#                 screen_shot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save.screenshot(screen_shot_path)
#
#
#             # only add additional html on failure
#             # extras.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
#             extras.append(pytest_html.extras.html.image(screen_shot_path))
#         report.extras = extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        # check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")

                screen_shot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save.screenshot(screen_shot_path)
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)

# UNCOMMENT THIS
# ## FOR: generating only pytest-html report
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         xfail = hasattr(report, "wasxfail")
#         # check if test failed
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception("Environment variable 'RESULTS_DIR' must be set.")
#
#                 screen_shot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save_screenshot(screen_shot_path)
#                 # only add additional html on failure
#                 # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
#                 extra.append(pytest_html.extras.image(screen_shot_path))
#
#         report.extra = extra


# #========
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         # check if test failed
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception("Environment variables 'RESULTS_DIR' must be set")
#                 screenshot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver = driver_fixture.cls.driver.save_screenshot(screenshot_path)
#             # only add additional html on failure
#             # extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#             # extra.append(pytest_html.extras.image("/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/image.jpeg"))
#             extra.append(pytest_html.extras.image("screenshot_path"))
#
#         report.extra = extra
