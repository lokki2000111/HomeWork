from authenticator import Authenticator
from exeptions import AuthorizationError, RegistrationError


def successful_action(func):
    def wrapper():
        var = True
        while var:
            try:
                func()
            except (AuthorizationError, RegistrationError) as e:
                continue
            var = False

    return wrapper


@successful_action
def main():
    authenticator = Authenticator()
    # понять когда вызвать авторизацию , а когда регистрацию
    # при успешной регистрации или авторизации завершить цикл
    # вывести имя и кол-во ошибок
    if authenticator.login == None:
        print("Несуществующий логин , пройдите регистрацию")

    if authenticator.login:
        print("Введите логин и пароль")

    login = input("Введите лолгин: ")
    password = input("Введите пароль: ")

    if authenticator.login is None:
        authenticator.registrate(login, password)

    authenticator.authorize(login, password)


if __name__ == "__main__":
    main()
