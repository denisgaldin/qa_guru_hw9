from pages.registration_page import RegistrationPage


def test_automation_form():
    page = RegistrationPage()
    (
        page.open_browser()
        .fill_name('Denis')
        .fill_last_name('Galdin')
        .fill_email('denisgaldin@mail.ru')
        .fill_gender('Male')
        .fill_user_number('1234567890')
        .data_birth('27', 'September', '1997')
        .subjects('English')
        .hobbies('Sports')
        .upload_picture('111.jpg')
        .fill_user_address('Vladimir street 12')
        .choice_state()
        .choice_city()
        .submit()
        .should_user(
            'Denis Galdin',
            'denisgaldin@mail.ru',
            'Male',
            '1234567890',
            '27 September,1997',
            'English',
            'Sports',
            '111.jpg',
            'Vladimir street 12',
            'Uttar Pradesh Agra')

        )