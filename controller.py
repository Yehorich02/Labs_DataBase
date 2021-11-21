import psycopg2
from psycopg2 import Error
import model
import view
import datetime
import time


class Controller:
    def __init__(self):
        self.v = view.View()
        self.m = model.Model()

    def print(self, table_name):
        name = self.v.valid.check_table_name(table_name)
        if name:
            if name == 'Pharmacy':
                self.v.print_pharmacy(self.m.print_pharmacy())
            elif name == 'Medicine':
                self.v.print_medicine(self.m.print_medicine())
            elif name == 'Provider':
                self.v.print_provider(self.m.print_provider())
            elif name == "Phone_numbers":
                self.v.print_phone_numbers(self.m.print_phone_numbers())
            elif name == 'Supplier_order_base':
                self.v.print_supplier_order_base(self.m.print_supplier_order_base())

    def delete(self, table_name, key_name: str, value):
        table_name_ = self.v.valid.check_table_name(table_name)
        key_name_ = self.v.valid.check_key_names(table_name_, key_name)
        if table_name_ and key_name_:
            count = self.m.find(table_name_, key_name, value)
            key_value = self.v.valid.check_pkey(value, count)
            if key_value:
                if table_name_ == 'Provider' or table_name_ == 'Pharmacy' or table_name_ == 'Medicine':
                    count_sob = self.m.find('Supplier order base', key_name, value)[0]
                    if count_sob:
                        self.v.not_delete()
                    else:
                        try:
                            self.m.delete_data(table_name, key_name, key_value)
                        except(Exception, Error) as ex:
                            self.v.sql_error(ex)
                elif table_name_ == 'Provider':
                    count_p = self.m.find('Phone numbers', key_name, key_value)[0]
                    if count_p:
                        self.v.not_delete()
                    else:
                        try:
                            self.m.delete_data(table_name, key_name, key_value)
                        except (Exception, Error) as ex:
                            self.v.sql_error(ex)
                else:
                    try:
                        self.m.delete_data(table_name, key_name, key_value)
                    except (Exception, Error) as ex:
                        self.v.sql_error(ex)
            else:
                self.v.deletion_error()

    def update_pharmacy_table(self, pharmacy_id: str, pharmacy_title: str, phone_num: str, address: str):
        id_value = None
        if self.v.valid.check_keys('Pharmacy', 'pharmacy_id', pharmacy_id):
            count_id = self.m.find('Pharmacy', 'pharmacy_id', int(pharmacy_id))
            id_value = self.v.valid.check_pkey(pharmacy_id, count_id)

        if id_value and self.v.valid.check_keys('Pharmacy', 'pharmacy_title', pharmacy_title) \
                and self.v.valid.check_keys('Pharmacy', 'phone_num', phone_num) \
                and self.v.valid.check_keys('Pharmacy', 'address', address):
            try:
                self.m.update_pharmacy_data(id_value, pharmacy_title, int(phone_num), address)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.updation_error()

    def update_provider_table(self, provider_id: str, title: str, address: str):
        id_value = None
        if self.v.valid.check_keys('Provider', 'provider_id', provider_id):
            count_id = self.m.find('Provider', 'provider_id', int(provider_id))
            id_value = self.v.valid.check_pkey(provider_id, count_id)
        if id_value and self.v.valid.check_keys('Provider', 'title', title) \
                and self.v.valid.check_keys('Provider', 'address', address):
            try:
                self.m.update_provider_data(id_value, title, address)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.updation_error()

    def update_medicine_table(self, medicine_id: str, medicine_title: str, manufacturer: str):
        id_value = None
        if self.v.valid.check_keys('Medicine', 'medicine_id', medicine_id):
            count_id = self.m.find('Medicine', 'medicine_id', int(medicine_id))
            id_value = self.v.valid.check_pkey(medicine_id, count_id)
        if id_value and self.v.valid.check_keys('Medicine', 'medicine_title', medicine_title) \
                and self.v.valid.check_keys('Medicine', 'manufacturer', manufacturer):
            try:
                self.m.update_medicine_data(id_value, medicine_id, manufacturer)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.updation_error()

    def update_phone_numbers_table(self, provider_id: str, phone_num: str, mobile_operator: str):
        id_value = None
        num_value = None
        if self.v.valid.check_keys('Phone numbers', 'provider_id', provider_id):
            count_id = self.m.find('Phone numbers', 'provider_id', int(provider_id))
            id_value = self.v.valid.check_pkey(provider_id, count_id)
        if self.v.valid.check_keys('Phone numbers', 'phone_num', phone_num):
            count_num = self.m.find('Phone numbers', 'phone_num', int(phone_num))
            num_value = self.v.valid.check_pkey(phone_num, count_num)
        if id_value and num_value and self.v.valid.check_keys('Phone numbers', 'mobile_operator', mobile_operator):
            try:
                self.m.update_phone_numbers_data(num_value, id_value, mobile_operator)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.updation_error()

    def update_supplier_order_base_table(self, supplier_order_id: str, provider_id: str, pharmacy_id: str,
                                         medicine_id: str, number: str, order_date: str):
        id_value = None
        provider_id_value = None
        pharmacy_id_value = None
        medicine_id_value = None
        if self.v.valid.check_keys('Supplier order base', 'supplier_order_id', supplier_order_id):
            count_id = self.m.find('Supplier order base', 'supplier_order_id', int(supplier_order_id))
            id_value = self.v.valid.check_pkey(supplier_order_id, count_id)
        if self.v.valid.check_keys('Supplier order base', 'provider_id', provider_id):
            count_provider_id = self.m.find('Supplier order base', 'provider_id', int(provider_id))
            provider_id_value = self.v.valid.check_pkey(provider_id, count_provider_id)
        if self.v.valid.check_keys('Supplier order base', 'pharmacy_id', pharmacy_id):
            count_pharmacy_id = self.m.find('Supplier order base', 'pharmacy_id', int(pharmacy_id))
            pharmacy_id_value = self.v.valid.check_pkey(pharmacy_id, count_pharmacy_id)
        if self.v.valid.check_keys('Supplier order base', 'medicine_id', medicine_id):
            count_medicine_id = self.m.find('Supplier order base', 'medicine_id', int(medicine_id))
            medicine_id_value = self.v.valid.check_pkey(medicine_id, count_medicine_id)
        if id_value and provider_id_value and pharmacy_id_value and medicine_id_value \
                and self.v.valid.check_keys('Supplier order base', 'number', number) \
                and self.v.valid.check_keys('Supplier order base', 'order_date', order_date):
            try:
                date_info = [int(a) for a in order_date.split(sep='.')]
                self.m.update_supplier_order_base_data(id_value, provider_id_value, pharmacy_id_value,
                                                       medicine_id_value, int(number),
                                                       datetime.datetime(date_info[0], date_info[1], date_info[2],
                                                                         date_info[3], date_info[4], date_info[5]))
            except(Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.updation_error()

    def insert_pharmacy(self, pharmacy_id: str, pharmacy_title: str, phone_num: str, address: str):
        count_id = None
        if self.v.valid.check_keys('Pharmacy', 'pharmacy_id', pharmacy_id):
            count_id = self.m.find('Pharmacy', 'pharmacy_id', int(pharmacy_id))[0]
        if(not count_id or count_id == (0,)) and self.v.valid.check_keys('Pharmacy', 'pharmacy_id', pharmacy_id):
            try:
                self.m.insert_pharmacy_data(int(pharmacy_id), pharmacy_title, int(phone_num), address)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.insertion_error()

    def insert_provider(self, provider_id: str, title: str, address: str):
        count_id = None
        if self.v.valid.check_keys('Provider', 'provider_id', provider_id):
            count_id = self.m.find('Provider', 'provider_id', int(provider_id))[0]
        if (not count_id or count_id == (0,)) and self.v.valid.check_keys('Provider', 'provider_id', provider_id):
            try:
                self.m.insert_provider_data(int(provider_id), title, address)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.insertion_error()

    def insert_medicine(self, medicine_id: str, medicine_title: str, manufacturer: str):
        count_id = None
        if self.v.valid.check_keys('Medicine', 'medicine_id', medicine_id):
            count_id = self.m.find('Medicine', 'medicine_id', int(medicine_id))[0]
        if (not count_id or count_id == (0,)) and self.v.valid.check_keys('Medicine', 'medicine_id', medicine_id):
            try:
                self.m.insert_medicine_data(int(medicine_id), medicine_title, manufacturer)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.insertion_error()

    def insert_phone_numbers(self, provider_id: str, phone_num: str, mobile_operator: str):
        provider_id_value = None
        count_num = None
        if self.v.valid.check_keys('Phone numbers', 'phone_num', phone_num):
            count_num = self.m.find('Phone numbers', 'phone_num', int(phone_num))[0]
        if self.v.valid.check_keys('Provider', 'provider_id', provider_id):
            count_id = self.m.find('Provider', 'provider_id', int(provider_id))
            provider_id_value = self.v.valid.check_pkey(provider_id, count_id)

        if(not count_num or count_num == (0,)) and provider_id_value \
                and self.v.valid.check_keys('Phone numbers', 'phone_num', phone_num):
            try:
                self.m.insert_phone_numbers_data(int(phone_num), int(provider_id), mobile_operator)
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.insertion_error()

    def insert_supplier_order_base(self, supplier_order_id: str, provider_id: str, pharmacy_id: str, medicine_id: str,
                                   number: str, order_date: str):
        count_sob = None
        count_med = None
        provider_id_value = None
        pharmacy_id_value = None
        if self.v.valid.check_keys('Supplier order base', 'supplier_order_id', supplier_order_id):
            count_sob = self.m.find('Supplier order base', 'supplier_order_id', int(supplier_order_id))[0]
        if self.v.valid.check_keys('Supplier order base', 'medicine_id', medicine_id):
            count_med = self.m.find('Supplier order base', 'medicine_id', int(medicine_id))[0]
        if self.v.valid.check_keys('Provider', 'provider_id', provider_id):
            count_provider_id = self.m.find('Provider', 'provider_id', int(provider_id))
            provider_id_value = self.v.valid.check_pkey(provider_id, count_provider_id)
        if self.v.valid.check_keys('Pharmacy', 'pharmacy_id', pharmacy_id):
            count_pharmacy_id = self.m.find('Pharmacy', 'pharmacy_id', int(pharmacy_id))
            pharmacy_id_value = self.v.valid.check_pkey(pharmacy_id, count_pharmacy_id)

        if (not count_sob or count_sob == (0,)) and (not count_med or count_med == (0,)) \
                and provider_id_value and pharmacy_id_value \
                and self.v.valid.check_keys('Supplier order base', 'supplier_order_id', supplier_order_id) \
                and self.v.valid.check_keys('Supplier order base', 'number', number) \
                and self.v.valid.check_keys('Supplier order base', 'order_date', order_date):
            try:
                arr = [int(a) for a in order_date.split(sep='.')]
                self.m.insert_supplier_order_base_data(int(supplier_order_id), int(medicine_id), int(provider_id),
                                                       int(pharmacy_id), int(number),
                                                       datetime.datetime(arr[0], arr[1], arr[2],
                                                                         arr[3], arr[4], arr[5]))
            except (Exception, Error) as ex:
                self.v.sql_error(ex)
        else:
            self.v.insertion_error()

    def generate(self, table_name: str, n: int):
        t_name = self.v.valid.check_table_name(table_name)
        if t_name:
            if t_name == 'Pharmacy':
                self.m.pharmacy_data_generator(n)
            elif t_name == 'Provider':
                self.m.provider_data_generator(n)
            elif t_name == 'Medicine':
                self.m.medicine_data_generator(n)
            elif t_name == 'Phone numbers':
                self.m.phone_numbers_data_generator(n)
            elif t_name == 'Supplier order base':
                self.m.supplier_order_base_data_generator(n)

    def search_in_one_table(self, table1_name: str, search: str):
        t1_n = self.v.valid.check_table_name(table1_name)
        if t1_n:
            start_time = time.time()
            result = self.m.search_data_one_table(table1_name, search)
            self.v.time_output(start_time)
            self.v.print_search(result)

    def search_in_two_tables(self, table1_name: str, table2_name: str, table1_key: str, table2_key: str, search: str):
        t1_n = self.v.valid.check_table_name(table1_name)
        t2_n = self.v.valid.check_table_name(table2_name)
        if t1_n and self.v.valid.check_key_names(t1_n, table1_key) and t2_n \
                and self.v.valid.check_key_names(t2_n, table2_key):
            start_time = time.time()
            result = self.m.search_data_two_tables(table1_name, table2_name, table1_key, table2_key, search)
            self.v.time_output(start_time)
            self.v.print_search(result)
