from faker import Faker

fake = Faker()
lista = []

class BaseContact:
    def __init__(self, name, family, phone, email):
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.contact_phone = self.phone

    def __str__(self):
        return f"{self.name} {self.family} - {self.email}"

    def contact(self):
        print(f"Wybieram numer {self.contact_phone} i dzwonię do {self.name} {self.family}")

    @property
    def label_length(self):
        return f"{len(self.name)} {len(self.family)}"

class BusinessContact(BaseContact):
    def __init__(self, role, company, wphone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.role = role
       self.company = company
       self.wphone = wphone
       self.contact_phone = self.wphone
    
def create_contact(typ, ilosc):
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

create_contact("business", 3)
lista[0].contact()
print(lista[0].email)
print(lista[0].label_length)