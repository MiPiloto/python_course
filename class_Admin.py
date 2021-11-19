from class_User import User
from class_Privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, age, id, password):
        super().__init__(first_name, last_name, age, id, password)
        self.privileges = Privileges()

    def describe_user(self):
        print("Administrator is registered by:\n" + "First name: " + self.first_name.title() + "\n" + 
        "Last name: " + self.last_name.title() + "\n" + 
        "Age: " + str(self.age) + "\n" + 
        "ID number: " + str(self.id) + "\n" + 
        "Password: " + str(self.password) + ".")


director = Admin("bruce","wayne",62,34679,"joker")
print(director.describe_user())
director.privileges.show_privileges()
director.privileges.upgrade_privileges("kill villain")
director.privileges.show_privileges()