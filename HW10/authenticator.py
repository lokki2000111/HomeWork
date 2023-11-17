import datetime
from os import path
from exeptions import AuthorizationError,RegistrationError


class Authenticator:

    def __init__(self):
        self.login: str | None = None
        self._password: int | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():
            self._read_auth_file()

    def _is_auth_file_exist(self):
        return path.exists("auth.txt")

    def _read_auth_file(self):
        with open("auth.txt") as f:
            self.login = f.readline().strip()
            self._password = f.readline().strip()
            self.last_success_login_at = f.readline()  # что-то не так
            self.errors_count = int(f.readline())

            print()

            pass

    def authorize(self, login, password):
        if self.login == None:
            self.errors_count += 1
            raise AuthorizationError("нет логина")

        if login == None:
            self.errors_count += 1
            raise AuthorizationError("не передали логин")

        if self.login != login or self._password != password:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError

        if self.login == login and self._password == password:
            self._update_auth_file()



    def _update_auth_file(self):
        """Метод обновление данных в файле.

        В файле обновляется время и количество ошибок.
        """

        with open("auth.txt", "w") as f:
            f.write(f"{self.login}\n")
            f.write(f"{self._password}\n")
            self.last_success_login_at = datetime.datetime.utcnow()
            f.write(f"{self.last_success_login_at.isoformat()}\n")
            f.write(f"{self.errors_count}")

    def registrate(self, login, password):
        if path.exists("auth.txt"):
            raise RegistrationError("Какая-то ошибка регистрации 1")

        if self.login != None:
            raise RegistrationError("Какая-то ошибка регистрации 2")  # возможно дублирующая проверка, как упростить?

        self.login = login
        self._password = password
        self._update_auth_file()



