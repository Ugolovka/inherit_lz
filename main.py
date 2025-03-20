from authorization import Authorization
from authorization import Login

def main():
    user = Authorization("Ivan", "Petrov", "ivanp", "my_secure_pass")
    print("Is employee:", Login.is_employee(employees, user.login))

if __name__ == "__main__":
    employees = ["user123", "admin", "johndoe"]
    user = Authorization("John", "Doe", "johndoe", "securepassword")
    print(user.info())
    print("Is employee:", Login.is_employee(employees, user.login))