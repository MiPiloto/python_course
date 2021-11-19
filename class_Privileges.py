class Privileges():
    def __init__(self):
        self.privileges = ["add post","delete post","ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(str(privilege.title()))
    
    def upgrade_privileges(self,addon):
        self.addon = addon        
        self.privileges.append(addon)