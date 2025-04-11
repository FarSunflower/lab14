from Apps import *
from playwright.sync_api import sync_playwright, expect
class Task1LocatorsAndVariables:

    date_picker = "2025-03-19"
    date_time_picker = "2025-03-19T14:00"
    email_field = "miray7772@gmail.com"
    month_field = "2025-03" 
    number_field = 7772

    date_xpath = "//input[@id='date-picker']"
    date_time_xpath = "//input[@id='date-time-picker']"
    email_xpath = "//input[@id='email-field']"
    month_xpath = "//input[@id='month-field']"
    number_xpath = "//input[@id='number-field']"

    button_xpath = "//input[@name='submitbutton']"

    value_colour_xpath = "//li[@id='_valuecolour']"
    value_date_xpath = "//li[@id='_valuedate']"
    value_datetime_xpath = "//li[@id='_valuedatetime']"
    value_email_xpath = "//li[@id='_valueemail']"
    value_month_xpath = "//li[@id='_valuemonth']"
    value_number_xpath = "//li[@id='_valuenumber']"

class SearchTask1(Task1App):
    def send_date(self):
        return self.page.locator(Task1LocatorsAndVariables.date_xpath).fill(Task1LocatorsAndVariables.date_picker)
    def send_datetime(self):
        return self.page.locator(Task1LocatorsAndVariables.date_time_xpath).fill(Task1LocatorsAndVariables.date_time_picker)
    def send_email(self):
        return self.page.locator(Task1LocatorsAndVariables.email_xpath).fill(Task1LocatorsAndVariables.email_field)
    def send_month(self):
        return self.page.locator(Task1LocatorsAndVariables.month_xpath).fill(Task1LocatorsAndVariables.month_field)
    def send_number(self):
        return self.page.locator(Task1LocatorsAndVariables.number_xpath).fill(str(Task1LocatorsAndVariables.number_field))
    def click_button(self):
        return self.page.locator(Task1LocatorsAndVariables.button_xpath).click()
    def text_colour_displayed(self):
        return self.page.locator(Task1LocatorsAndVariables.value_colour_xpath).is_visible()
    def text_date_displayed(self):
        return self.page.locator(Task1LocatorsAndVariables.value_date_xpath).is_visible()
    def text_datetime_displayed(self):
        return self.page.locator(Task1LocatorsAndVariables.value_datetime_xpath).is_visible()
    def text_email_displayed(self):
        return self.page.locator(Task1LocatorsAndVariables.value_email_xpath).is_visible()
    def text_month_displayed(self):
        return self.page.locator(Task1LocatorsAndVariables.value_month_xpath).is_visible()
    def text_number_displayed(self):
        return self.page.locator(Task1LocatorsAndVariables.value_number_xpath).is_visible()


    
class Task2LocatorsAndVariables:
    username = "andrii"
    password = "123"
    text_area_comment = "hello world"
    filename = "/home/despair/Documents/VSC_projects/lab14/text.txt"

    name_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    comments_xpath = "//textarea[@name='comments']"
    filename_xpath = "//input[@name='filename']"
    checkbox2_xpath = "//input[@value='cb2']"
    checkbox3_xpath = "//input[@value='cb3']"
    radioitem_xpath = "//input[@value='rd3']"
    multivalue_xpath = "//option[@value='ms1']"
    dropdown_xpath = "//select[@name='dropdown']"
    dropdownvalue = "dd6"

    button_xpath = "//input[@value='submit' and @class='styled-click-button']" 

    value_username_xpath = "//li[@id='_valueusername']"
    value_password_xpath = "//li[@id='_valuepassword']"
    value_comments_xpath = "//li[@id='_valuecomments']"
    value_filename_xpath = "//li[@id='_valuefilename']"
    value_hiddenfielad_xpath = "//li[@id='_valuehiddenField']"
    value_checkbox_xpath = "//li[@id='_valuecheckboxes0']"
    value_radioval_xpath = "//li[@id='_valueradioval']"
    value_multi_xpath = "//li[@id='_valuemultipleselect0']"
    value_valdrop_xpath = "//li[@id='_valuedropdown']"

class SearchTask2(Task2App):

    def send_username(self):
        return self.page.locator(Task2LocatorsAndVariables.name_xpath).fill(Task2LocatorsAndVariables.username)
    def send_password(self):
        return self.page.locator(Task2LocatorsAndVariables.password_xpath).fill(Task2LocatorsAndVariables.password)
    def send_comments(self):
        return self.page.locator(Task2LocatorsAndVariables.comments_xpath).fill(Task2LocatorsAndVariables.text_area_comment)
    def send_filename(self):
        return self.page.locator(Task2LocatorsAndVariables.filename_xpath).set_input_files(Task2LocatorsAndVariables.filename)
    def click_checkbox2(self):
        return self.page.locator(Task2LocatorsAndVariables.checkbox2_xpath).click()
    def click_checkbox3(self):
        return self.page.locator(Task2LocatorsAndVariables.checkbox3_xpath).click()
    def click_radio(self):
        return self.page.locator(Task2LocatorsAndVariables.radioitem_xpath).click()
    def click_multi(self):
        return self.page.locator(Task2LocatorsAndVariables.multivalue_xpath).click()
    def click_dropdown(self):
        return self.page.locator(Task2LocatorsAndVariables.dropdown_xpath).select_option(Task2LocatorsAndVariables.dropdownvalue)
    def click_button(self):
        return self.page.locator(Task2LocatorsAndVariables.button_xpath).click()
    def username_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_username_xpath).is_visible()
    def password_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_password_xpath).is_visible()
    def comments_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_comments_xpath).is_visible()
    def filename_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_filename_xpath).is_visible()
    def checkbox_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_checkbox_xpath).is_visible()
    def radio_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_radioval_xpath).is_visible()
    def multi_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_multi_xpath).is_visible()
    def dropdown_displayed(self):
        return self.page.locator(Task2LocatorsAndVariables.value_valdrop_xpath).is_visible()

class Task3LocatorsAndVariables:

    username_xpath = "//p[contains(text(),'username')]"
    password_xpath = "//p[contains(text(),'password')]"
    webpage_xpath = "//a[contains(text(),'Basic Auth Protected Page')]"
    finaltext_xpath = "//p[contains(text(), 'You were')]/span[contains(text(), 'Authenticated')]"

class SearchTask3(Task3App):
    def get_credentials(self):
        username_text = self.page.locator(Task3LocatorsAndVariables.username_xpath).text_content()
        password_text = self.page.locator(Task3LocatorsAndVariables.password_xpath).text_content()

        username = username_text.split(":")[1].strip()
        password = password_text.split(":")[1].strip()
        return username, password
    
    def get_auth_url(self):
        href = self.page.locator(Task3LocatorsAndVariables.webpage_xpath).get_attribute("href")
        username, password = self.get_credentials()
        base_url = f"https://{username}:{password}@testpages.eviltester.com"
        return base_url + href
    
    def fullfill(self):
        return self.page.goto(self.get_auth_url())
    
    def text_displayed(self):
        return self.page.locator(Task3LocatorsAndVariables.finaltext_xpath).is_visible()

class Task4LocatorsAndVariables:
    filename = "/home/despair/Documents/VSC_projects/lab14/text.txt"
    fname = "text.txt"

    filename_xpath = "//input[@id='fileinput']"
    itsfile_xpath = "//input[@id='itsafile']"
    button_xpath = "//input[@class='styled-click-button']"
    final_text_xpath = f"//p[contains(text(), '{fname}')]"

class SearchTask4(Task4App):
    def send_filename(self):
        return self.page.locator(Task4LocatorsAndVariables.filename_xpath).set_input_files(Task4LocatorsAndVariables.filename)
    def click_itsfile(self):
        return self.page.locator(Task4LocatorsAndVariables.itsfile_xpath).click()
    def click_button(self):
        return self.page.locator(Task4LocatorsAndVariables.button_xpath).click()
    def text_displayed(self):
        return self.page.locator(Task4LocatorsAndVariables.final_text_xpath).is_visible()

class Task5LocatorsAndVariables:
    alertcheckbox1_xpath = "//input[@id='alertexamples']"
    alertcheckbox2_xpath = "//input[@id='confirmexample']"
    alertcheckbox3_xpath = "//input[@id='promptexample']"

    asserttext1_xpath = "//p[@id='alertexplanation']"
    asserttext2_xpath = "//p[@id='confirmreturn']"
    asserttext3_xpath = "//p[@id='promptreturn']"
    
class SearchTask5(Task5App):
    def click_alertbox(self):
        def handle_dialog(dialog):
            dialog.accept()
        self.page.once("dialog", handle_dialog)
        return self.page.locator(Task5LocatorsAndVariables.alertcheckbox1_xpath).click()
    
    def text1_displayed(self):
        return self.page.locator(Task5LocatorsAndVariables.asserttext1_xpath).is_visible()
    
    def click_confirmbox(self, should_accept=True):
        def handle_confirm_dialog(dialog):
            if should_accept:
                dialog.accept()
            else:
                dialog.dismiss()
        self.page.once("dialog", handle_confirm_dialog)
        return self.page.locator(Task5LocatorsAndVariables.alertcheckbox2_xpath).click()
    
    def text2_displayed(self):
        return self.page.locator(Task5LocatorsAndVariables.asserttext2_xpath).text_content() == "true"
    
    def click_promtbox(self, inputtext):
        def handle_prompt_dialog(dialog):
            dialog.accept(inputtext)
        self.page.once("dialog", handle_prompt_dialog)
        return self.page.locator(Task5LocatorsAndVariables.alertcheckbox3_xpath).click()
    
    def text3_displayed(self, inputtext):
        return self.page.locator(Task5LocatorsAndVariables.asserttext3_xpath).text_content() == inputtext


