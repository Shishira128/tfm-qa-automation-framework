from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ==================================
    # Page Utilities
    # ==================================

    def wait_for_page_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    # ==================================
    # Smart Click (React-safe)
    # ==================================

    def click(self, locator):

        for attempt in range(3):  # retry max 3 times
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                # Scroll element to center
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    element
                )

                element.click()
                return

            except StaleElementReferenceException:
                print(f"Element went stale (attempt {attempt+1}), retrying...")
                continue

            except Exception:
                # JS fallback click
                element = self.wait.until(
                    EC.presence_of_element_located(locator)
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )
                return

        raise Exception("Failed to click element after multiple retries")

    # ==================================
    # Typing
    # ==================================

    def type(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    # ==================================
    # Get Text
    # ==================================

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    # ==================================
    # Popup Handler (Marketing Modal)
    # ==================================

    def close_marketing_popup(self):
        try:
            popup_close = (
                By.XPATH,
                "//button[contains(@class,'close') or contains(.,'×')]"
            )

            self.wait.until(
                EC.visibility_of_element_located(popup_close)
            )

            self.driver.find_element(*popup_close).click()

            print("Marketing popup closed")

        except TimeoutException:
            # Popup not present → ignore
            pass