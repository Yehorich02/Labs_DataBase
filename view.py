import validator
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
            print(row)

    @staticmethod
    def print_medicine(table):
        print('----Medicine table----')
        print("%12s%30s%30s" % ("medicine_id", "medicine_title", "manufacturer"))
        for row in table:
            print(row)

    @staticmethod
    def print_provider(table):
        print('----Provider table----')
        print("%10s%35s%35s" % ("provider_id", "title", "address"))
        for row in table:
            print(row)

    @staticmethod
    def print_phone_numbers(table):
        print('----Phone numbers table----')
        print("%10s%10s%20s" % ("phone_number", "provider_id", "mobile_operator"))
        for row in table:
            print(row)

    @staticmethod
    def print_supplier_order_base(table):
        print('----Supplier order base----')
        print("%10s%10s%10s%10s%10s%20s" % ("supplier_order_id", "provider_id", "mobile_operator"))
        for row in table:
            print(row)

    def print_search(self, res):
        print('----Search results----')
        for row in res:
            print(row)

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

    @staticmethod
    def get_search_num():
        return input('Specify the number of tables which you`d to find: ')

    @staticmethod
    def invalid_search_num():
        print('The number should be different from 2 to 4: ')

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
