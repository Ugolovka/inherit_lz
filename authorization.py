import hashlib

class Login:
    def __init__(self, name, surname, login):
        self.name = name
        self.surname = surname
        self.login = login

    def info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Login: {self.login}"

    def is_employee(employee_list, login):
        return login in employee_list


class Authorization(Login):
    def __init__(self, name, surname, login, password, hash_algorithm="sha256"):
        super().__init__(name, surname, login)
        self.password = password
        self.hash_algorithm = hash_algorithm
        self.is_hashed = False
        self.hashing_pass()

    def hashing_pass(self):
        if not self.is_hashed:
            hash_func = getattr(hashlib, self.hash_algorithm, hashlib.sha256)
            self.password = hash_func(self.password.encode()).hexdigest()
            self.is_hashed = True

    def info(self):
        if not self.is_hashed:
            self.hashing_pass()
        return (f"Name: {self.name}, Surname: {self.surname}, Login: {self.login}, "
                f"Password: {self.password} (hashed), Algorithm: {self.hash_algorithm}")