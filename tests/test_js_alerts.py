from faker import Faker

from pages.alert_page import AlertMessages, AlertPage, ResultMessages
from pages.context_menu_page import ContextAlertMessage, ContextMenuPage

fake = Faker()


def test_js_alerts_page(page, base_url):
    alert_page = AlertPage(page)
    alert_page.action.goto(f"{base_url}/javascript_alerts")
    received_alert_msg = alert_page.receive_msg_from_alert_btn()
    assert received_alert_msg == AlertMessages.ALERT_MSG, (
        f"Expected message {AlertMessages.ALERT_MSG} but got {received_alert_msg}"
    )
    received_alert_result = alert_page.result_text.get_inner_text()
    assert received_alert_result == ResultMessages.ALERT_RESULT, (
        f"Expected result {ResultMessages.ALERT_RESULT} but got {received_alert_result}"
    )

    received_confirm_msg = alert_page.receive_msg_from_confirm_btn()
    assert received_confirm_msg == AlertMessages.CONFIRM_MSG, (
        f"Expected message {AlertMessages.CONFIRM_MSG} but got {received_confirm_msg}"
    )
    received_confirm_result = alert_page.result_text.get_inner_text()
    assert received_confirm_result == ResultMessages.CONFIRM_RESULT_OK, (
        f"Expected result {ResultMessages.CONFIRM_RESULT_OK} but got {received_confirm_result}"
    )

    random_word = fake.word()
    received_prompt_msg = alert_page.receive_msg_from_prompt_btn(random_word)
    assert received_prompt_msg == AlertMessages.PROMPT_MSG, (
        f"Expected message {AlertMessages.PROMPT_MSG} but got {received_prompt_msg}"
    )
    received_prompt_result = alert_page.result_text.get_inner_text()
    assert received_prompt_result == (ResultMessages.PROMPT_RESULT + random_word), (
        f"Expected result {(ResultMessages.PROMPT_RESULT + random_word)} but got {received_prompt_result}"
    )


def test_context_area_page(page, base_url):
    context_menu_page = ContextMenuPage(page)
    context_menu_page.actions.goto(f"{base_url}/context_menu")
    received_message = context_menu_page.click_on_context_area()
    assert ContextAlertMessage.ALERT_MSG == received_message, (
        f"Expected message {ContextAlertMessage.ALERT_MSG} but got {received_message}"
    )
