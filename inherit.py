import bcrypt

list = []

class Login:
    def __init__(self, name, surname, login):
        self.name = name
        self.surname = surname
        self.login = login

    def info(self):
        print(f"Вся информация: ({self.name}, {self.surname}, {self.login})")

    def is_employee(self):
        if self.info in list:
            print("Profil exists in the list")
        else:
            print("Profil does not exist")


class Authorization:
    def __init__(self, password, hash_algorithm, is_hashed, name, surname, login):
        super.__init__(self, name, surname, login)
        self.password = password
        self.hash_algorithm = hash_algorithm
        self.is_hashed = is_hashed

    def info(self):
        print(f"Вся информация: ({self.password}, {self.hash_algorithm}, {self.is_hashed})")

    def hashing_pass(self):
        password = b'GeekPassword'
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        print("Salt :")
        print(salt)
        print("Hashed")
        print(hashed)



login = Login(0, 0, 5)
login.info()
login.is_employee

profil = Authorization(0, 0, 5, 5, 6, 7)
profil.info()
