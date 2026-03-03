from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class BrandPage(BasePage):

    # Brands menu in header
    BRANDS_MENU = (
        By.XPATH,
        "//span[contains(@class,'menu-title-wrapper') and normalize-space()='Brands']"
    )

    # First brand inside dropdown
    FIRST_BRAND = (
        By.XPATH,
        "(//nav[@data-testid='ecom-wrapper']//a)[1]"
    )

    # First product inside brand page (you may refine later)
    FIRST_PRODUCT = (
        By.XPATH,
        "(//div[contains(@class,'product')])[1]"
    )

    def select_brand(self):

        # 1️⃣ Wait until page fully loads
        self.wait_for_page_load()

        # 2️⃣ Close marketing popup if it appears
        self.close_marketing_popup()

        # 3️⃣ Hover over Brands menu (megamenu needs hover)
        brands_element = self.wait.until(
            EC.visibility_of_element_located(self.BRANDS_MENU)
        )

        ActionChains(self.driver).move_to_element(brands_element).perform()

        # 4️⃣ Wait for dropdown to appear
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_BRAND)
        )

        # 5️⃣ Click first brand
        self.click(self.FIRST_BRAND)

    def select_product(self):

        # Wait for brand page to load
        self.wait_for_page_load()

        # Close popup if any appears
        self.close_marketing_popup()

        # Click first product
        self.click(self.FIRST_PRODUCT)