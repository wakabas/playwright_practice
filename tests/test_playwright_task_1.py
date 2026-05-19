import faker

BASE_URL = "http://144.31.63.127:5000/"
fake = faker.Faker()


def test_login_page(page):
    EXPECTED_ERROR_TEXT = "Invalid login or password."
    page.goto(BASE_URL)
    page.get_by_test_id("nav-login").click()
    page.get_by_test_id("login-username").fill(fake.email())
    page.get_by_test_id("login-password").fill(fake.password())
    confirm_button = page.get_by_test_id("login-submit")
    confirm_button.click()
    spinner = page.get_by_test_id("login-submit-spinner")
    spinner.wait_for(state="visible")
    spinner.wait_for(state="detached")
    login_error = page.get_by_test_id("login-error-inline")
    received_error_text = login_error.inner_text()
    assert received_error_text == EXPECTED_ERROR_TEXT, (
        f"Expected text - {EXPECTED_ERROR_TEXT}, but got {received_error_text}"
    )
