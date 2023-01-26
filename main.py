from faker import Faker
import time

class BaseContact:
    def __init__(self, name, family, phone, email):
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.contact_phone = self.phone 

    def __str__(self):
        return f"{self.name} {self.family} - {self.email}"

    def contact(self): # w 10 linii kodu ustawiam zmienną contact_phone na prywatny numer, w klasie BusinessContact jest na służbowym numerze
        print(f"Wybieram numer {self.contact_phone} i dzwonię do {self.name} {self.family}")

    @property
    def label_length(self):
        return len(self.name) + len(self.family) + 1

class BusinessContact(BaseContact):
    def __init__(self, role, company, workphone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.role = role
       self.company = company
       self.workphone = workphone
       self.contact_phone = self.workphone
    
def create_contact(typ, ilosc):
    lista = []
    for _ in range(ilosc):
        if typ == "basic":
            n = fake.first_name()
            f = fake.last_name()
            p = fake.phone_number()
            e = f"{n}{f}@gmail.com"
            lista.append(BaseContact(n, f, p, e))
        if typ == "business":
            n = fake.first_name()
            f = fake.last_name()
            p = fake.phone_number()
            e = f"{n}{f}@gmail.com"
            r = fake.job()
            c = fake.company()
            wp = fake.phone_number()
            lista.append(BusinessContact(r, c, wp, n, f, p, e))
    return lista        

if __name__ == "__main__":
    fake = Faker()
    starttime = time.time()
    test = create_contact("business", 5)
    endtime = time.time()
    print(endtime - starttime)
    print(test[1])
    print(test[1].label_length)
