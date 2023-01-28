from faker import Faker
import time


class BaseContact:
    def __init__(self, name, family, phone, email):
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email


    def __str__(self):
        return f"{self.name} {self.family} - {self.email}"


    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.family}")


    @property
    def label_length(self):
        return len(self.name) + len(self.family) + 1


class BusinessContact(BaseContact):
    def __init__(self, role, company, workphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role
        self.company = company
        self.workphone = workphone


    def contact(self):
        print(f"Wybieram numer {self.workphone} i dzwonię do {self.name} {self.family}")


def create_contact(typ, ilosc):
    lista = []
    for _ in range(ilosc):
        if typ == "basic":
            random_name = fake.first_name()
            random_family = fake.last_name()
            random_number = fake.phone_number()
            semi_random_mail = f"{random_name}{random_family}@gmail.com"
            lista.append(BaseContact(random_name, random_family, random_number, semi_random_mail))
        if typ == "business":
            random_name = fake.first_name()
            random_family = fake.last_name()
            random_number = fake.phone_number()
            semi_random_mail = f"{random_name}{random_family}@gmail.com"
            random_role = fake.job()
            random_company = fake.company()
            random_workphone = fake.phone_number()
            lista.append(BusinessContact(random_role, random_company, random_workphone, random_name, random_family, random_number, semi_random_mail))
    return lista


if __name__ == "__main__":
    fake = Faker()
    starttime = time.time()
    test = create_contact("business", 5)
    endtime = time.time()
    print(endtime - starttime)
    print(test[1])
    print(test[1].label_length)
