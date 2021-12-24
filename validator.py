import datetime


class Validator:
    def __init__(self):
        self.error = ''
        self.error_flag = False

    def check_table_name(self, table_name: str):
        if table_name in ['Provider', 'Pharmacy', 'Medicine', 'Phone_numbers', 'Supplier_order_base']:
            return table_name
        else:
            self.error_flag = True
            self.error = f'Table {table_name} does not exist in the database'
            print(self.error)
            return False

    def check_pkey_value(self, key_value: str, min_val: int, max_val: int):
        try:
            value = int(key_value)
        except ValueError:
            self.error_flag = True
            self.error = f'{key_value} is not correct primary key value'
            print(self.error)
            return 0
        else:
            if min_val <= value <= max_val:
                return value
            else:
                self.error_flag = True
                self.error = f'{key_value} is not existing primary key value'
                print(self.error)
                return 0

    def check_pkey_name(self, table_name: str, key_name: str):
        if table_name == 'Provider' and key_name == 'provider_id' \
                or table_name == 'Medicine' and key_name == 'medicine_id' \
                or table_name == 'Pharmacy' and key_name == 'pharmacy_id' \
                or table_name == 'Phone numbers' and key_name == 'phone_num' \
                or table_name == 'Supplier order base' and key_name == 'supplier_order_id and medicine_id':
            return key_name
        else:
            self.error_flag = True
            self.error = f'key {key_name} is not a primary key of table {table_name}'
            return False

    def check_pkey(self, val):
        try:
            value = int(val)
            return value
        except ValueError:
            self.error_flag = True
            self.error = f'{val} is not correct primary key value'
            print(self.error)
            return 0

    def check_key_names(self, table_name: str, key: str):
        if table_name == 'Provider' and key in ['provider_id', 'title', 'address']:
            return True
        elif table_name == 'Phone_numbers' and key in ['phone_num', 'provider_id', 'mobile_operator']:
            return True
        elif table_name == 'Pharmacy' and key in ['pharmacy_id', 'pharmacy_title', 'phone_num', 'address']:
            return True
        elif table_name == 'Medicine' and key in ['medicine_id', 'medicine_title', 'manufacturer']:
            return True
        elif table_name == 'Supplier_order_base' and key in ['supplier_order_id', 'medicine_id', 'pharmacy_id',
                                                             'provider_id', 'number', 'order_date']:
            return True
        else:
            self.error_flag = True
            self.error = f'{key} is not correct name for {table_name} table'
            print(self.error)
            return False

    def check_keys(self, table_name: str, key: str, val: str):
        if table_name == 'Pharmacy':
            if key in ['pharmacy_id']:
                try:
                    value = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key in ['pharmacy_title', 'address']:
                return True
            elif key in ['phone_num']:
                try:
                    number = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible phone number value'
                    print(self.error)
                    return False
                else:
                    return True
            else:
                self.error_flag = True
                self.error = f'{key} is not correct name for Pharmacy table'
                print(self.error)
                return False
        elif table_name == 'Phone numbers':
            if key in ['provider_id', 'phone_num']:
                try:
                    value = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key in ['mobile_operator']:
                return True
            else:
                self.error_flag = True
                self.error = f'{key} is not correct name for Phone numbers table'
                print(self.error)
                return False
        elif table_name == 'Provider':
            if key in ['provider_id']:
                try:
                    value = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key in ['title', 'address']:
                return True
            else:
                self.error_flag = True
                self.error = f'{key} is not correct name for Provider table'
                print(self.error)
                return False
        elif table_name == 'Medicine':
            if key == 'medicine_id':
                try:
                    value = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key in ['medicine_title', 'manufacturer']:
                return True
            else:
                self.error_flag = True
                self.error = f'{key} is not correct name for Medicine table'
                print(self.error)
                return False
        elif table_name == 'Supplier order base':
            if key in ['pharmacy_id', 'medicine_id', 'provider_id', 'supplier_order_id']:
                try:
                    value = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key == 'number':
                try:
                    number = int(val)
                except ValueError:
                    self.error_flag = True
                    self.error = f'{val} is not possible number value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key == 'order_date':
                try:
                    arr = [int(x) for x in val.split(sep='.')]
                    datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
                except TypeError:
                    self.error_flag = True
                    self.error = f'{val} is not correct order date value'
                    print(self.error)
                    return False
                else:
                    return True
            else:
                self.error_flag = True
                self.error = f'{key} is not correct name for Supplier order base table'
                print(self.error)
                return False
