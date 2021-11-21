import validator
import datetime
import time


class View:
    def __init__(self):
        self.valid = validator.Validator()

    @staticmethod
    def not_delete() -> None:
        print('this record can not delete because it is connected with another table, deleting will be'
              'throw error')

    @staticmethod
    def sql_error(err) -> None:
        print("[INFO] Error in the process of working with PostgreSQL", err)

    @staticmethod
    def insertion_error() -> None:
        print('Something went wrong(Record does not exist in the table)')

    @staticmethod
    def updation_error() -> None:
        print('Something went wrong')

    @staticmethod
    def deletion_error() -> None:
        print('Something went wrong, deletion with such does not exist')

    @staticmethod
    def invalid_interval() -> None:
        print('invalid interval input')

    @staticmethod
    def time_output(start) -> None:
        print("---- %s seconds ----" % (time.time() - start))

    @staticmethod
    def print_pharmacy(table):
        print('----Pharmacy table----')
        for row in table:
            print('pharmacy_id:', row[0], '\tpharmacy_title:', row[1], '\tphone_num:', row[2], '\taddress:', row[3])
            print('_____________________________________')

    @staticmethod
    def print_medicine(table):
        print('----Medicine table----')
        for row in table:
            print('medicine_id:', row[0], '\tmedicine_title:', row[1], '\tmanufacturer:', row[2])
            print('_____________________________________')

    @staticmethod
    def print_provider(table):
        print('----Provider table----')
        for row in table:
            print('provider_id:', row[0], '\ttitle:', row[1], '\taddress:', row[2])
            print('_____________________________________')

    @staticmethod
    def print_phone_numbers(table):
        print('----Phone numbers table----')
        for row in table:
            print('provider_id:', row[0], '\tphone_num:', row[1], '\tmobile_operator:', row[2])
            print('_____________________________________')

    @staticmethod
    def print_supplier_order_base(table):
        print('----Supplier order base----')
        for row in table:
            print('supplier_order_id:', row[0], '\tprovider_id:', row[1], '\tpharmacy_id:', row[2],
                  '\tmedicine_id:', row[3], '\tnumber:', row[4], '\torder_date:', row[5])
            print('_____________________________________')

    def print_search(self, res):
        print('----Search results----')
        for row in res:
            for a in range(0, len(row)):
                print(row[a])
            print('_____________________________________')

    @staticmethod
    def print_help():
        print('print_table - displays the specified table \n'
              '\targument is (table_name)')
        print('delete_record - deletes the specified record from a specific table \n'
              '  arguments dor deletion:\n'
              '\t(table_name, key_name, key_value)')
        print('update_record - adjusts the record with the specified key in a specific table\n'
              '  arguments for Provider table: \n'
              '\t(table_name, provider_id, title, address)\n'
              '  arguments for Pharmacy table: \n'
              '\t(table_name, pharmacy_id, pharmacy_title, phone_num, address)\n'
              '  arguments for Medicine table: \n'
              '\t(table_name, medicine_id, medicine_title, manufacturer)\n'
              '  arguments for Phone_numbers table: \n'
              '\t(table_name, provider_id, phone_num, mobile_operator)\n'
              '  arguments for Supplier_order_base table: \n'
              '\t(table_name, supplier_oder_id, provider_id, pharmacy_id, medicine_id, number, order_date)')
        print('insert_record - enter data in the specified table\n'
              '  arguments for Provider table: \n'
              '\t(table_name, provider_id, title, address)\n'
              '  arguments for Pharmacy table: \n'
              '\t(table_name, pharmacy_id, pharmacy_title, phone_num, address)\n'
              '  arguments for Medicine table: \n'
              '\t(table_name, medicine_id, medicine_title, manufacturer)\n'
              '  arguments for Phone_numbers table: \n'
              '\t(table_name, provider_id, phone_num, mobile_operator)\n'
              '  arguments for Supplier_order_base table: \n'
              '\t(table_name, supplier_oder_id, provider_id, pharmacy_id, medicine_id, number, order_date)')
        print('generate_records - generates n randomized records in the specified table\n'
              '  arguments for generation:'
              '\t(table_name, n)')
        print('search_records - search for records in one table using one or more attributes \n'
              '  arguments for searching\n'
              '\t(table1_name, table1_key)')

    def initiate_search(self, search_number):
        search_value = ''
        for param in range(0, search_number):
            while True:
                search_type = input('Specify the type(date, numeric or string) of data you want to find: ')
                if search_type in ['date', 'numeric', 'string']:
                    break
            key_value = input('Specify the key name by which you`d find(in form key_name if for one table, else - '
                              'table_name.key_name):')
            if search_type == 'numeric':
                left_edge = input('Specify the left edge of search interval:')
                right_edge = input('Specify the right edge of search interval:')
                if search_value == '':
                    search_value = self.numeric_search(left_edge, right_edge, key_value)
                else:
                    search_value += ' and ' + self.numeric_search(left_edge, right_edge, key_value)
            elif search_type == 'string':
                string_value = input('Specify the string which you`d to find: ')
                if search_value == '':
                    search_value = self.string_search(string_value, key_value)
                else:
                    search_value += ' and ' + self.string_search(string_value, key_value)
            elif search_type == 'date':
                date_left = input('Specify the left edge of search interval in form yy.mm.dd: ')
                date_right = input('Specify the left edge of search interval in form yy.mm.dd: ')
                if search_value == '':
                    search_value = self.date_search(date_left, date_right, key_value)
                else:
                    search_value += 'and' + self.date_search(date_left, date_right, key_value)
        return search_value

    def numeric_search(self, left: str, right: str, key: str):
        try:
            left, right = int(left), int(right)
        except ValueError:
            self.invalid_interval()
        else:
            return f"{left} <= {key} and {key} <= {right}"

    def string_search(self, string: str, key: str):
        return f"{key} LIKE \'{string}\'"

    def date_search(self, left: str, right: str, key: str):
        try:
            l_edge = [int(a) for a in left.split(sep='.')]
            r_edge = [int(a) for a in right.split(sep='.')]
        except Exception as e:
            print(e)
            self.invalid_interval()
        else:
            return f"{key} BETWEEN " \
                   f"\'{datetime.datetime(l_edge[0], l_edge[1], l_edge[2])}\' " \
                   f"AND " \
                   f"\'{datetime.datetime(r_edge[0], r_edge[1], r_edge[2])}\'"

    @staticmethod
    def get_search_num():
        return input('Specify the number of attributes which you`d to find: ')

    @staticmethod
    def invalid_search_num():
        print('The number should be different from 0')

    @staticmethod
    def arg_error():
        print('No required arguments specified')

    @staticmethod
    def wrong_table():
        print('Wrong table name')

    @staticmethod
    def wrong_command():
        print('Wrong command, please use Help to see correct commands')

    @staticmethod
    def no_command():
        print('No command, please use Help to see correct commands')