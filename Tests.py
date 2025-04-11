from DynamicButtonsPages import SearchHelper
from PlayerItemPages import SearchItem
from TasksPages import *
from conftest import page

def test_dynamic_buttons(page):
    search = SearchHelper(page)
    search.go_to_site()

    search.click_button0()
    search.click_button1()
    search.click_button2()
    search.click_button3()

    assert search.text_displayed()

def test_player(page):
    search = SearchItem(page)
    search.go_to_site()

    search.click_button()
    search.click_image()
    assert search.text_displayed

def test_task1(page):
    search = SearchTask1(page)
    search.go_to_site()

    search.send_date()
    search.send_datetime()
    search.send_email()
    search.send_month()
    search.send_number()
    search.click_button()
    assert search.text_colour_displayed()
    assert search.text_date_displayed()
    assert search.text_datetime_displayed()
    assert search.text_email_displayed()
    assert search.text_month_displayed()
    assert search.text_number_displayed()

def test_task2(page):
    search = SearchTask2(page)
    search.go_to_site()

    search.send_username()
    search.send_password()
    search.send_comments()
    search.send_filename()
    search.click_checkbox2()
    search.click_checkbox3()
    search.click_radio()
    search.click_multi()
    search.click_dropdown()
    search.click_button()
    assert search.username_displayed()
    assert search.password_displayed()
    assert search.comments_displayed()
    assert search.filename_displayed()
    assert search.checkbox_displayed()
    assert search.radio_displayed()
    assert search.dropdown_displayed()
    assert search.multi_displayed()

def test_task3(page):
    search = SearchTask3(page)
    search.go_to_site()

    search.get_credentials()
    search.get_auth_url()
    search.fullfill()
    assert search.text_displayed()

def test_task4(page):
    search = SearchTask4(page)
    search.go_to_site()

    search.send_filename()
    search.click_itsfile()
    search.click_button()
    assert search.text_displayed()

def test_task5(page):
    search = SearchTask5(page)
    search.go_to_site()

    search.click_alertbox()
    assert search.text1_displayed()
    search.click_confirmbox(should_accept=True)
    assert search.text2_displayed()
    search.click_promtbox(inputtext="Hello!")
    assert search.text3_displayed(inputtext="Hello!")