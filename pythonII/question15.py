# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Banking:
    def __init__(self, id, full_name, email, contact, phone, permanent_address, temporary_address, birth_of_date, citizenship_no):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.contact = contact
        self.phone = phone
        self.permanent_address = permanent_address
        self.temporary_address = temporary_address
        self.birth_of_date = birth_of_date
        self.citizen_no = citizenship_no

    def information(self):
        pass

    def user_transaction(self):
        pass


