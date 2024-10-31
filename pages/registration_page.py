from selene import browser, have, command


class RegistrationPage:
    def open(self):
        browser.open('automation-practice-form')
        self.remove_unwanted_elements()
        return self

    def remove_unwanted_elements(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def select_gender(self, gender):
        browser.all('[name="gender"]').element_by(have.attribute('value', gender)).element('../label').click()
        return self

    def fill_user_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def select_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def select_subjects(self, subjects):
        for subject in subjects:
            browser.element('#subjectsInput').type(subject[0])
            browser.element('.subjects-auto-complete__menu-list').element(f'//*[text()="{subject[1]}"]').perform(
                command.js.scroll_into_view).click()
        return self

    def select_hobby(self, hobby):
        browser.element(f'//label[text()="{hobby}"]').click()
        return self

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').set_value(path.abspath(path.join(file_name)))
        return self

    def select_location(self, state, city):
        browser.element('#state').click()
        browser.element(f'//*[text()="{state}"]').click()
        browser.element('#city').click()
        browser.element(f'//*[text()="{city}"]').click()
        return self

    def submit(self):
        browser.element('button#submit').click()
        return self

    def should_have_registered(self, student_name, student_email, gender, mobile, dob, subjects, hobbies, picture,
                               address, location):
        assert browser.element('table').should(be.visible)
        assert browser.element('//table//td[text()="Student Name"]/../td[2]').should(have.exact_text(student_name))
        assert browser.element('//table//td[text()="Student Email"]/../td[2]').should(have.exact_text(student_email))
        assert browser.element('//table//td[text()="Gender"]/../td[2]').should(have.exact_text(gender))
        assert browser.element('//table//td[text()="Mobile"]/../td[2]').should(have.exact_text(mobile))
        assert browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(have.exact_text(dob))
        assert browser.element('//table//td[text()="Subjects"]/../td[2]').should(have.exact_text(subjects))
        assert browser.element('//table//td[text()="Hobbies"]/../td[2]').should(have.exact_text(hobbies))
        assert browser.element('//table//td[text()="Picture"]/../td[2]').should(have.exact_text(picture))
        assert browser.element('//table//td[text()="Address"]/../td[2]').should(have.exact_text(address))
        assert browser.element('//table//td[text()="State and City"]/../td[2]').should(have.exact_text(location))
        return self
