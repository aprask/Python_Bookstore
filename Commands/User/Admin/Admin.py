class Admin:
    ADMIN_PASSWORD = 'project2'

    def did_pass(self):
        attempts = 5
        while attempts > 0:
            password_attempt = input("Enter a password: ")
            if password_attempt.__eq__(self.ADMIN_PASSWORD):
                return True
            attempts -= 1
        return False
