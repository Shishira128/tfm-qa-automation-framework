from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):

    # First product in product listing page
    FIRST_PRODUCT = (
        By.XPATH,
        "(//a[@data-testid='product-image'])[1]"
    )

    # Add to cart button on product details page
    ADD_TO_CART = (
        By.XPATH,
        "//button[@data-testid='add-to-cart']"
    )

    def select_first_product(self):

        # Wait for page load
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # Close popup if it appears
        self.close_marketing_popup()

        # Wait until product appears in DOM
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_PRODUCT)
        )

        # Click first product
        self.click(self.FIRST_PRODUCT)

    def add_to_cart(self):

        # Wait for product details page to load
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # Close popup again if it appears
        self.close_marketing_popup()

        # Click Add to Cart
        self.click(self.ADD_TO_CART)