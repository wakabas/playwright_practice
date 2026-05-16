
import faker
from playwright.sync_api import expect


def test_login_page(page):
    fake = faker.Faker()
    base_url = "http://144.31.139.115:5000/"
    page.goto(base_url)
    page.get_by_role("link", name="Login", exact=False).click()
    page.wait_for_url("**/login")
    page.locator("input[name='username']").fill(fake.email())
    page.locator("input[name='password']").fill(fake.password())
    confirm_button = page.get_by_role("button", name="Confirm", exact=False)
    confirm_button.click()
    spinner = page.locator("span[data-testid='login-submit-spinner']")
    spinner.wait_for(state="visible", timeout=2000)
    expect(spinner).to_be_visible()
    expect(page.get_by_text("Invalid login or password.")).to_be_visible()







