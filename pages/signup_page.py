from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignupPage(BasePage):

    # Top user icon
    USER_ICON = (By.XPATH, "//div[@data-testid='login-account']")

    # Create account button inside login modal
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(),'Create Account')]")

    # Create with Email Instead button
    CREATE_WITH_EMAIL_BTN = (By.XPATH, "//button[contains(text(),'Create with Email Instead')]")

    # Close (X) button inside modal
    CLOSE_MODAL_BTN = (
    By.XPATH,
    "//div[contains(@class,'mb-2') and contains(@class,'cursor-pointer')]"
)

    def signup(self):
        self.driver.get("https://dev.trulyfree.com/")

        # Click user icon
        self.click(self.USER_ICON)

        # Click Create Account
        self.click(self.CREATE_ACCOUNT_BTN)

        # Wait for Create Account modal
        self.wait.until(
            EC.visibility_of_element_located(self.CREATE_WITH_EMAIL_BTN)
        )

    def close_modal(self):
     close_btn = self.wait.until(
        EC.visibility_of_element_located(self.CLOSE_MODAL_BTN)
    )

     self.driver.execute_script("arguments[0].click();", close_btn)

     self.wait.until(
        EC.invisibility_of_element_located(self.CREATE_WITH_EMAIL_BTN)
    )