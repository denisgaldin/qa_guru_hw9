from pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()

    registration_page.open() \
        .fill_first_name('Denis') \
        .fill_last_name('Galdin') \
        .fill_email('testqa@mail.ru') \
        .select_gender('Male') \
        .fill_user_number('9009009000') \
        .select_date_of_birth(27, 8, 1997) \
        .select_subjects([
        ('E', 'English'),
        ('A', 'Arts')
    ]) \
        .select_hobby('Sports') \
        .upload_picture('pic.jpg') \
        .fill_current_address('9153 Jerry Dr, Juneau, Alaska 99801, USA') \
        .select_location('Uttar Pradesh', 'Lucknow') \
        .submit()

    registration_page.should_have_registered(
        student_name='Denis Galdin',
        student_email='testqa@mail.ru',
        gender='Male',
        mobile='9009009000',
        dob='27 September,1997',
        subjects='English, Arts',
        hobbies='Sports',
        picture='pic.jpg',
        address='9153 Jerry Dr, Juneau, Alaska 99801, USA',
        location='Uttar Pradesh Lucknow'
    )
