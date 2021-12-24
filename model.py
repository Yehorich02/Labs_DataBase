import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from DB_lab3 import Base, Session, engine


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class Provider(Base):
    __tablename__ = 'Provider'
    provider_id = Column(Integer, primary_key=True)
    title = Column(String)
    address = Column(String)
    sob = relationship("Supplier_order_base")
    phone_numbers = relationship("Phone_numbers")

    def __init__(self, provider_id, title, address):
        self.provider_id = provider_id
        self.title = title
        self.address = address

    def __repr__(self):
        return "{:>10}{:>35}{:>35}" .format(self.provider_id, self.title, self.address)


class Phone_numbers(Base):
    __tablename__ = "Phone numbers"
    phone_number = Column(Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey('Provider.provider_id'))
    mobile_operator = Column(String)

    def __init__(self, phone_number, provider_id, mobile_operator):
        self.phone_number = phone_number
        self.provider_id = provider_id
        self.mobile_operator = mobile_operator

    def __repr__(self):
        return "{:>10}{:>10}{:>20}" .format(self.phone_number, self.provider_id, self.mobile_operator)


class Pharmacy(Base):
    __tablename__ = "Pharmacy"
    pharmacy_id = Column(Integer, primary_key=True)
    pharmacy_title = Column(String)
    phone_num = Column(Integer)
    address = Column(String)
    sob = relationship("Supplier_order_base")

    def __init__(self, pharmacy_id, pharmacy_title, phone_num, address):
        self.pharmacy_id = pharmacy_id
        self.pharmacy_title = pharmacy_title
        self.phone_num = phone_num
        self.address = address

    def __repr__(self):
        return "{:>10}{:>30}{:>10}{:>40}" .format(self.pharmacy_id, self.pharmacy_title, self.phone_num, self.address)


class Medicine(Base):
    __tablename__ = "Medicine"
    medicine_id = Column(Integer, primary_key=True)
    medicine_title = Column(String)
    manufacturer = Column(String)
    sob = relationship("Supplier_order_base")

    def __init__(self, medicine_id, medicine_title, manufacturer):
        self.medicine_id = medicine_id
        self.medicine_title = medicine_title
        self.manufacturer = manufacturer

    def __repr__(self):
        return "{:>10}{:>30}{:>30}" .format(self.medicine_id, self.medicine_title, self.manufacturer)


class Supplier_order_base(Base):
    __tablename__ = "Supplier order base"
    supplier_order_id = Column(Integer, primary_key=True)
    medicine_id = Column(Integer, ForeignKey('Medicine.medicine_id'), primary_key=True)
    provider_id = Column(Integer, ForeignKey('Provider.provider_id'))
    pharmacy_id = Column(Integer, ForeignKey('Pharmacy.pharmacy_id'))
    number = Column(Integer)
    order_date = Column(Date)

    def __init__(self, supplier_order_id, medicine_id, provider_id, pharmacy_id, number, order_date):
        self.supplier_order_id = supplier_order_id
        self.medicine_id = medicine_id
        self.provider_id = provider_id
        self.pharmacy_id = pharmacy_id
        self.number = number
        self.order_date = order_date

    def __repr__(self):
        return "{:>10}{:>10}{:>10}{:>10}{:>10}\t\t{}" .format(self.supplier_order_id, self.medicine_id,
                                                              self.provider_id, self.pharmacy_id, self.number,
                                                              self.order_date)


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def find_primary_key_phone_numbers(self, key_value: int):
        return self.session.query(Phone_numbers).filter_by(phone_number=key_value).first()

    def find_foreign_key_phone_number(self, key_value: int, table_name: str):
        if table_name == "Provider":
            return self.session.query(Phone_numbers).filter_by(provider_id=key_value).first()

    def find_primary_key_provider(self, key_value: int):
        return self.session.query(Provider).filter_by(provider_id=key_value).first()

    def find_primary_key_pharmacy(self, key_value: int):
        return self.session.query(Pharmacy).filter_by(pharmacy_id=key_value).first()

    def find_primary_key_medicine(self, key_value: int):
        return self.session.query(Medicine).filter_by(medicine_id=key_value).first()

    def find_primary_key_supplier_order_base(self, key_value: int):
        return self.session.query(Supplier_order_base).filter_by(supplier_order_id=key_value).first()

    def find_foreign_key_supplier_order_base(self, key_value: int, table_name: str):
        if table_name == "Provider":
            return self.session.query(Supplier_order_base).filter_by(provider_id=key_value).first()
        elif table_name == "Pharmacy":
            return self.session.query(Pharmacy).filter_by(pharmacy_id=key_value).first()

    def print_provider(self):
        return self.session.query(Provider).order_by(Provider.provider_id.asc()).all()

    def print_phone_numbers(self):
        return self.session.query(Phone_numbers).order_by(Phone_numbers.phone_number.asc()).all()

    def print_pharmacy(self):
        return self.session.query(Pharmacy).order_by(Pharmacy.pharmacy_id.asc()).all()

    def print_medicine(self):
        return self.session.query(Medicine).order_by(Medicine.medicine_id.asc()).all()

    def print_supplier_order_base(self):
        return self.session.query(Supplier_order_base).order_by(Supplier_order_base.supplier_order_id.asc()).all()

    def delete_data_provider(self, provider_id: int) -> None:
        self.session.query(Provider).filter_by(provider_id=provider_id).delete()
        self.session.commit()

    def delete_data_phone_numbers(self, phone_number: int) -> None:
        self.session.query(Phone_numbers).filter_by(phone_number=phone_number).delete()
        self.session.commit()

    def delete_data_pharmacy(self, pharmacy_id: int) -> None:
        self.session.query(Pharmacy).filter_by(pharmacy_id=pharmacy_id).delete()
        self.session.commit()

    def delete_data_medicine(self, medicine_id: int) -> None:
        self.session.query(Medicine).filter_by(medicine_id=medicine_id).delete()
        self.session.commit()

    def delete_supplier_order_base_data(self, supplier_order_id: int, medicine_id: int) -> None:
        self.session.query(Supplier_order_base).filter_by(supplier_order_id=supplier_order_id,
                                                          medicine_id=medicine_id).delete()
        self.session.commit()

    def update_provider_data(self, provider_id: int, title: str, address: str) -> None:
        self.session.query(Provider).filter_by(provider_id=provider_id) \
            .update({Provider.title: title, Provider.address: address})
        self.session.commit()

    def update_phone_numbers_data(self, phone_number: int, provider_id: int, mobile_operator: str) -> None:
        self.session.query(Phone_numbers).filter_by(phone_number=phone_number) \
            .update({Phone_numbers.provider_id: provider_id, Phone_numbers.mobile_operator: mobile_operator})
        self.session.commit()

    def update_pharmacy_data(self, pharmacy_id: int, title: str, phone_num: int, address: str) -> None:
        self.session.query(Pharmacy).filter_by(pharmacy_id=pharmacy_id) \
            .update({Pharmacy.title: title, Pharmacy.phone_num: phone_num,
                     Pharmacy.address: address})
        self.session.commit()

    def update_medicine_data(self, medicine_id: int, medicine_title: str, manufacturer: str) -> None:
        self.session.query(Medicine).filter_by(medicine_id=medicine_id) \
            .update({Medicine.medicine_title: medicine_title, Medicine.manufacturer: manufacturer})
        self.session.commit()

    def update_supplier_order_base_data(self, supplier_order_id: int, medicine_id: int, provider_id: int,
                                        pharmacy_id: int, number: int, order_date: datetime.datetime) -> None:
        self.session.query(Supplier_order_base).filter_by(supplier_order_id=supplier_order_id,
                                                          medicine_id=medicine_id) \
            .update({Supplier_order_base.provider_id: provider_id,
                     Supplier_order_base.pharmacy_id: pharmacy_id,
                     Supplier_order_base.number: number,
                     Supplier_order_base.order_date: order_date})
        self.session.commit()

    def insert_provider_data(self, provider_id: int, title: str, address: str) -> None:
        provider = Provider(provider_id=provider_id, title=title, address=address)
        self.session.add(provider)
        self.session.commit()

    def insert_phone_numbers_data(self, phone_number: int, provider_id: int, mobile_operator: str) -> None:
        phone_numbers = Phone_numbers(phone_number=phone_number, provider_id=provider_id,
                                      mobile_operator=mobile_operator)
        self.session.add(phone_numbers)
        self.session.commit()

    def insert_pharmacy_data(self, pharmacy_id: int, pharmacy_title: str, phone_num: int, address: str) -> None:
        pharmacy = Pharmacy(pharmacy_id=pharmacy_id, pharmacy_title=pharmacy_title,
                            phone_num=phone_num, address=address)
        self.session.add(pharmacy)
        self.session.commit()

    def insert_medicine_data(self, medicine_id: int, medicine_title: str, manufacturer: str) -> None:
        medicine = Medicine(medicine_id=medicine_id, medicine_title=medicine_title, manufacturer=manufacturer)
        self.session.add(medicine)
        self.session.commit()

    def insert_supplier_order_base_data(self, supplier_order_id: int, medicine_id: int, provider_id: int,
                                        pharmacy_id: int, number: int, order_date: datetime.datetime) -> None:
        sob = Supplier_order_base(supplier_order_id=supplier_order_id, medicine_id=medicine_id,
                                  provider_id=provider_id, pharmacy_id=pharmacy_id, number=number,
                                  order_date=order_date)
        self.session.add(sob)
        self.session.commit()

    def provider_data_generator(self, value: int) -> None:
        for a in range(value):
            self.connection.execute(
                "insert into public.\"Provider\" select (SELECT MAX(provider_id)+1 FROM public.\"Provider\"), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''); ")

    def medicine_data_generator(self, value: int) -> None:
        for a in range(value):
            self.connection.execute(
                "insert into public.\"Medicine\" select (SELECT MAX(medicine_id)+1 FROM public.\"Medicine\"), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''); ")

    def pharmacy_data_generator(self, value: int) -> None:
        for a in range(value):
            self.connection.execute(
                "insert into public.\"Pharmacy\" select (SELECT MAX(pharmacy_id)+1 FROM public.\"Pharmacy\"), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(12-4)+4):: integer)), ''), "
                "FLOOR(RANDOM()*(999999990-1)+1), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(10-3)+3):: integer)), ''); ")

    def phone_numbers_data_generator(self, value: int) -> None:
        for a in range(value):
            self.connection.execute(
                "(SELECT provider_id FROM public.\"Provider\" LIMIT 1 OFFSET (round(random() * "
                "((SELECT COUNT(provider_id) FROM public.\"Provider\")-1)))), "
                "insert into public.\"Phone numbers\" "
                "select (SELECT MAX(phone_num)+1 FROM public.\"Phone numbers\"), "
                "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                "FROM generate_series(1, FLOOR(RANDOM()*(10-3)+3):: integer)), ''); ")

    def supplier_order_base_data_generator(self, value: int) -> None:
        for a in range(value):
            self.connection.execute(
                "insert into public.\"Supplier order base\" "
                "select (SELECT MAX(supplier_order_id)+1 FROM "
                "public.\"Supplier order base\"), "
                "(SELECT provider_id FROM public.\"Provider\" LIMIT 1 OFFSET (round(random() * "
                "((SELECT COUNT(provider_id) FROM public.\"Provider\")-1)))), "
                "(SELECT pharmacy_id FROM public.\"Pharmacy\" LIMIT 1 OFFSET (round(random() * "
                "((SELECT COUNT(pharmacy_id) FROM public.\"Pharmacy\")-1)))), "
                "(SELECT medicine_id FROM public.\"Medicine\" LIMIT 1 OFFSET (round(random() * "
                "((SELECT COUNT(medicine_id) FROM public.\"Medicine\")-1)))), "
                "FLOOR(RANDOM()*(1000-1)+1), "
                "(SELECT to_timestamp(1549634400+random()*70071999));")
