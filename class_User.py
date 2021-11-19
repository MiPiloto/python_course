class User():

    def __init__(self, first_name, last_name, age, id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print("User is registered by:\n" + "First name: " + self.first_name.title() + "\n" + 
        "Last name: " + self.last_name.title() + "\n" + 
        "Age: " + str(self.age) + "\n" + 
        "ID number: " + str(self.id) + "\n" + 
        "Password: " + str(self.password) + ".")

    def greet_user(self):
        print("Welcome, " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user01 = User("jack","sparrow",57,45671,"rum")
print(user01.first_name)
print(user01.last_name)
print("\n")

user01.describe_user()
user01.greet_user()

user01.increment_login_attempts()
user01.increment_login_attempts()
print(user01.login_attempts)

user01.reset_login_attempts()
print(user01.login_attempts)





