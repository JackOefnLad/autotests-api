import pytest 

@pytest.fixture(scope="session")
def settings():
    print("Seesion.Settings applied")

@pytest.fixture(scope="class")
def user():
    print("Class.Created class fixtures")

@pytest.fixture
def users_client(settings): #Переиспользование фикстуры settings внутри user_client
    print("Function.Fun created")
    #Вложенные фикстуры должны быть либо одного scope, либо в нижнем scope использовать верхний
# class TestUser:
#     def test_user_can_login(self,user, settings, users_client):
#         pass
#     def test_user_create_cours(self, user, settings, users_client):
#         pass

# class TestAccountFlow:
#     def test_user_account(self, user, settings, users_client):
#         pass


@pytest.fixture
def user_data() -> dict: # type: ignore
    print("Создание пользователя(setup)") #До теста
    yield {"username": "test_user", "email":"test@mail.com"} #Выполнение теста
    print("Удаляем пользователя(teardown)") #Завершение теста

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == "test@mail.com"
def test_user_name(user_data: dict):
    print(user_data)
    assert user_data['username'] == 'test_user'


