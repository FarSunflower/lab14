from Apps import ItemApp
from playwright.sync_api import sync_playwright, expect

class ItemLocator:
    mp3_button_xpath = "//div[@class='list-group']/a[contains(text(),'MP3 плеєри')]"
    ipod_image_xpath = "//img[@title='iPod Classic']"
    songs_text_xpath = "//p[contains(text(),'songs')]"

class SearchItem(ItemApp):

    def click_button(self):
        # Пошук №1: Клік на кнопку MP3 Players
        return self.page.locator(ItemLocator.mp3_button_xpath).click()
    
    def click_image(self):
        # Пошук №2: Клік на зображення iPod Classic
        return self.page.locator(ItemLocator.ipod_image_xpath).click()
    
    def text_displayed(self):
        # Пошук №3: Перевірка, що текст з "songs" існує
        return self.page.locator(ItemLocator.songs_text_xpath).is_visible()
