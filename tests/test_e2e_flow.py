from pages.signup_page import SignupPage
from pages.brand_page import BrandPage
from pages.product_page import ProductPage


def test_complete_e2e_flow(driver):

    # Module 1 – Signup
    signup = SignupPage(driver)
    signup.signup()

    # Module 2 – Select Brand
    brand = BrandPage(driver)
    brand.select_brand()

    # Module 3 – Select Product & Add to Cart
    product = ProductPage(driver)
    product.select_first_product()
    product.add_to_cart()

    # Optional: Add assertion for validation
    # Example: verify cart page opened
    assert "cart" in driver.current_url.lower()