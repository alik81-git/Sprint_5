import random as r
import uuid


class TestData:
    @staticmethod
    def random_email():
        generated_uuid = uuid.uuid4()
        username = str(generated_uuid).split("-")[0]
        random_email = f"test_{username}@yandex.ru"
        return random_email

    @staticmethod
    def user_data():

        user_data = {
            "email": "qa_python_25@mail.ru",
            "unsupported_email": "qa_python_25@test.ru",
            "password": "qa_python_25",
            "title": "New Item" + str(r.randint(1000, 9999)),
            "description": f"New Item Description{r.randint(11, 99)}",
            "price": str(r.randint(100, 1000)),
            "base_url": "https://qa-desk.stand.praktikum-services.ru/",
        }
        return user_data
