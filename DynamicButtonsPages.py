from Apps import BaseApp
from playwright.sync_api import sync_playwright, expect

class DynamicButtonsLocator:
    locator_button0 = "button00"
    locator_button1 = "button01"
    locator_button2 = "button02"
    locator_button3 = "button03"
    locator_text = "All Buttons Clicked"

class SearchHelper(BaseApp):

    def click_button0(self):
        expect(self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button0}']")).to_be_enabled()
        return self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button0}']").click()
    
    def click_button1(self):
        expect(self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button1}']")).to_be_enabled()
        return self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button1}']").click()
    
    def click_button2(self):
        expect(self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button2}']")).to_be_enabled()
        return self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button2}']").click()
    
    def click_button3(self):
        expect(self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button3}']")).to_be_enabled(timeout=1000000)
        return self.page.locator(f"//button[@id='{DynamicButtonsLocator.locator_button3}']").click()
    
    def text_displayed(self):
        return self.page.get_by_text(DynamicButtonsLocator.locator_text).is_visible()
