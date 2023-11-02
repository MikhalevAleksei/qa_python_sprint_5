import random as r


class GenLogin:
    data_name = "Alex"
    gen_email = f'Aleksei_Mikhalev{r.randint(100, 900)}@yandex.ru'
    gen_password = r.randint(123456, 654321)



class User:
    test_name = 'Aleksei'
    empty_fld_name = ''
    test_email = 'Aleksei123@ya.ru'
    test_password = 123456
    wrong_passwords_list = [0, 1, 12345, 5432]
    gen_wrong_password = r.randint(12345, 54321)


