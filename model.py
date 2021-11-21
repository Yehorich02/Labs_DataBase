import datetime
import psycopg2 as ps


class Model:
    def __init__(self):
        self.conn = None
        try:
            self.conn = ps.connect(
                database="Pharmacy",
                user="postgres",
                password="1234",
                host="127.0.0.1",
                port="5432",
            )
        except(Exception, ps.DatabaseError) as error:
            print("[INFO] Error when working with PostgreSQL", error)

    def request(self, req: str):
        try:
            cursor = self.conn.cursor()
            print(req)
            cursor.execute(req)
            self.conn.commit()
            return True
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            print(error)
            self.conn.rollback()
            return False

    def get(self, req: str):
        try:
            cursor = self.conn.cursor()
            print(req)
            cursor.execute(req)
            self.conn.commit()
            return cursor.fetchall()
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            print(error)
            self.conn.rollback()
            return False

    def get_el(self, req: str):
        try:
            cursor = self.conn.cursor()
            print(req)
            cursor.execute(req)
            self.conn.commit()
            return cursor.fetchone()
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            print(error)
            self.conn.rollback()
            return False

    def count(self, table_name: str):
        return self.get_el(f"select count(*) from public.\"{table_name}\"")

    def find(self, table_name: str, key_name: str, key_value: int):
        return self.get_el(f"select count(*) from public.\"{table_name}\" where {key_name}={key_value}")

    def min(self, table_name: str, key_name: str):
        return self.get_el(f"select min({key_name}) from public.\"{table_name}\"")

    def max(self, table_name: str, key_name: str):
        return self.get_el(f"select max({key_name}) from public.\"{table_name}\"")

    def print_provider(self) -> None:
        return self.get(f"SELECT * FROM public.\"Provider\"")

    def print_phone_numbers(self) -> None:
        return self.get(f"SELECT * FROM public.\"Phone numbers\"")

    def print_supplier_order_base(self) -> None:
        return self.get(f"SELECT * FROM public.\"Supplier order base\"")

    def print_pharmacy(self) -> None:
        return self.get(f"SELECT * FROM public.\"Pharmacy\"")

    def print_medicine(self) -> None:
        return self.get(f"SELECT * FROM public.\"Medicine\"")

    def update_provider_data(self, provider_id: int, title: str, address: str) -> None:
        self.request(f"UPDATE public.\"Provider\" SET title=\'{title}\', address=\'{address}\' "
                     f"WHERE provider_id={provider_id};")

    def update_phone_numbers_data(self, phone_number: int, provider_id: int, mobile_operator: str) -> None:
        self.request(f"UPDATE public.\"Phone numbers\" SET provider_id={provider_id}, "
                     f"mobile_operator=\'{mobile_operator}\' WHERE phone_number={phone_number};")

    def update_supplier_order_base_data(self, key_value: int, medicine_id: int, provider_id: int, pharmacy_id: int,
                                        number: int, order_date: datetime.datetime) -> None:
        self.request(f"UPDATE public.\"Supplier order base\" SET provider_id={provider_id},"
                     f"pharmacy_id={pharmacy_id}, number={number}, order_date=\'{order_date}\',"
                     f"WHERE supplier_order_id={key_value}, medicine_id={medicine_id};")

    def update_pharmacy_data(self, pharmacy_id: int, title: str, phone_num: int, address: str) -> None:
        self.request(f"UPDATE public.\"Pharmacy\" SET pharmacy_title=\'{title}\', phone_num={phone_num},"
                     f"address=\'{address}\' WHERE pharmacy_id={pharmacy_id};")

    def update_medicine_data(self, medicine_id: int, title: str, manufacturer: str) -> None:
        self.request(f"UPDATE public.\"Medicine\" SET medicine_title=\'{title}\', manufacturer=\'{manufacturer}\'"
                     f"WHERE medicine_id={medicine_id};")

    def insert_provider_data(self, provider_id: int, title: str, address: str) -> None:
        self.request(f"insert into public.\"Provider\" (provider_id, title, address) "
                     f"VALUES ({provider_id}, \'{title}\', {address});")

    def insert_phone_numbers_data(self, phone_number: int, provider_id: int, mobile_operator: str) -> None:
        self.request(f"insert into public.\"Phone numbers\" (phone_num, provider_id, mobile_operator) "
                     f"VALUES ({phone_number}, {provider_id}, \'{mobile_operator}\');")

    def insert_supplier_order_base_data(self, key_value: int, medicine_id: int, provider_id: int, pharmacy_id: int,
                                        number: int, order_date: datetime.datetime) -> None:
        self.request(f"insert into public.\"Supplier order base\" (supplier_order_id, provider_id, pharmacy_id, "
                     f"medicine_id, number, order_date) VALUES ({key_value}, {provider_id}, {pharmacy_id}, "
                     f"{medicine_id}, {number}, \'{order_date}\');")

    def insert_pharmacy_data(self, pharmacy_id: int, title: str, phone_num: int, address: str) -> None:
        self.request(f"insert into public.\"Pharmacy\" (pharmacy_id, pharmacy_title, phone_num, address) "
                     f"VALUES ({pharmacy_id}, \'{title}\', {phone_num}, \'{address}\');")

    def insert_medicine_data(self, medicine_id: int, title: str, manufacturer: str) -> None:
        self.request(f"insert into public.\"Medicine\" (medicine_id, medicine_title, manufacturer) "
                     f"VALUES ({medicine_id}, \'{title}\', \'{manufacturer}\');")

    def delete_data(self, table_name: str, key_name: str, key_value: int) -> None:
        self.request(f"DELETE FROM public.\"{table_name}\" WHERE {key_name}={key_value};")

    def provider_data_generator(self, value: int) -> None:
        for a in range(value):
            self.request("insert into public.\"Provider\" select (SELECT MAX(provider_id)+1 FROM public.\"Provider\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''); ")

    def medicine_data_generator(self, value: int) -> None:
        for a in range(value):
            self.request("insert into public.\"Medicine\" select (SELECT MAX(medicine_id)+1 FROM public.\"Medicine\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(25-10)+10):: integer)), ''); ")

    def pharmacy_data_generator(self, value: int) -> None:
        for a in range(value):
            self.request("insert into public.\"Pharmacy\" select (SELECT MAX(pharmacy_id)+1 FROM public.\"Pharmacy\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(12-4)+4):: integer)), ''), "
                         "FLOOR(RANDOM()*(999999990-1)+1), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(10-3)+3):: integer)), ''); ")

    def phone_numbers_data_generator(self, value: int) -> None:
        for a in range(value):
            self.request("(SELECT provider_id FROM public.\"Provider\" LIMIT 1 OFFSET (round(random() * "
                         "((SELECT COUNT(provider_id) FROM public.\"Provider\")-1)))), "
                         "insert into public.\"Phone numbers\" "
                         "select (SELECT MAX(phone_num)+1 FROM public.\"Phone numbers\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) "
                         "FROM generate_series(1, FLOOR(RANDOM()*(10-3)+3):: integer)), ''); ")

    def supplier_order_base_data_generator(self, value: int) -> None:
        for a in range(value):
            self.request("insert into public.\"Supplier order base\" "
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

    def search_data_one_table(self, table1_name: str, search: str):
        return self.get(f"select * from public.\"{table1_name}\" "
                        f"where {search}")

    def search_data_two_tables(self, table1_name: str, table2_name: str, table1_key, table2_key, search: str):
        table2_name = "Phone numbers"
        return self.get(f"select * from public.\"{table1_name}\" as one inner join public.\"{table2_name}\" as two "
                        f"on one.\"{table1_key}\"=two.\"{table2_key}\" "
                        f"where {search}")
