from data.user import User
from pages.registration_page import RegistrationPage


def test_user_form():
    page = RegistrationPage()
    user = User('Denis',
                'Galdin',
                'denisgaldin@mail.ru',
                'Male',
                '1234567890',
                '27',
                'September',
                '1997',
                'English',
                'Music',
                '111.jpg',
                'Vladimir street 12',
                'Uttar Pradesh',
                'Agra'
                )

    page.open_browser()
    page.register_user(user)
    page.submit()
    page.should_user(user)