from playwright.sync_api import Page
class BaseApp:
    URL = 'https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)
class ItemApp:
    #На момент виконання роботи оригінальна лінка завдання не працювала, в мережі було знайдето схожу модель
    URL = 'https://demo.opencart.ua/desktops'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)
class Task1App:
    URL = 'https://testpages.eviltester.com/styled/html5-form-test.html'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)
class Task2App:
    URL = 'https://testpages.eviltester.com/styled/basic-html-form-test.html'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)
class Task3App:
    URL = 'https://testpages.eviltester.com/styled/auth/basic-auth-test.html'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)
class Task4App:
    URL = 'https://testpages.eviltester.com/styled/file-upload-test.html'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)
class Task5App:
    URL = 'https://testpages.eviltester.com/styled/alerts/alert-test.html'
    def __init__(self, page: Page) -> None:
        self.page = page
    def go_to_site(self) -> None:
        self.page.goto(self.URL)