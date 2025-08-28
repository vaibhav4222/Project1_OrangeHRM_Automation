import allure
from allure_commons.types import AttachmentType

def attach_screenshot(driver, name="screenshot"):
    allure.attach(driver.get_screenshot_as_png(),
                  name=name,
                  attachment_type=AttachmentType.PNG)
