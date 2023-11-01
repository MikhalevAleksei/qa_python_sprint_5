import random as r


class GenDataLogin:
    data_name = "Alex"
    gen_data_email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'
    gen_data_password = r.randint(123456, 654321)
    gen_wrong_password = r.randint(12345, 54321)