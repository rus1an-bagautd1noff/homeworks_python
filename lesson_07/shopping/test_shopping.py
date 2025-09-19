import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.usefixtures("setup_driver")
def test_shopping_scenario(setup_driver):
    driver = setup_driver

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_tshirt()
    main_page.add_onesie()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")

    total_amount = checkout_page.get_total_amount()
    assert total_amount == "$58.29"

    driver.quit()
