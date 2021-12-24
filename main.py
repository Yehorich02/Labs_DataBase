import controller as con
import sys

c = con.Controller()

try:
    command = sys.argv[1]
except IndexError:
    c.v.no_command()
else:
    if command == 'print_table':
        try:
            name = sys.argv[2]
        except IndexError:
            c.v.argument_error()
        else:
            c.print(name)
    elif command == 'delete_record':
        try:
            args = {"table_name": sys.argv[2], "value": sys.argv[3]}
        except IndexError:
            c.v.arg_error()
        else:
            c.delete(args["table_name"], args["value"])
    elif command == 'insert_record':
        try:
            args = {"table_name": sys.argv[2], "key": sys.argv[3]}
            if args["table_name"] == 'Medicine':
                args["title"], args["manufacturer"] = sys.argv[4], sys.argv[5]
            elif args["table_name"] == 'Provider':
                args["title"], args["address"] = sys.argv[4], sys.argv[5]
            elif args["table_name"] == 'Phone_numbers':
                args["provider_id"], args["mobile_operator"] = sys.argv[4], sys.argv[5]
            elif args["table_name"] == 'Pharmacy':
                args["title"], args["phone_num"], args["address"] = sys.argv[4], sys.argv[5], sys.argv[6]
            elif args["table_name"] == 'Supplier_order_base':
                args["provider_id"], args["pharmacy_id"], args["medicine_id"], args["number"], args["order_date"] =\
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]
        except IndexError:
            c.v.wrong_table()
        else:
            if args["table_name"] == 'Medicine':
                c.insert_medicine(args["key"], args["title"], args["manufacturer"])
            elif args["table_name"] == 'Provider':
                c.insert_provider(args["key"], args["title"], args["address"])
            elif args["table_name"] == 'Pharmacy':
                c.insert_pharmacy(args["key"], args["title"], args["phone_num"], args["address"])
            elif args["table_name"] == 'Phone_numbers':
                c.insert_phone_numbers(args["key"], args["provider_id"], args["mobile_operator"])
            elif args["table_name"] == 'Supplier_order_base':
                c.insert_supplier_order_base(args["key"], args["provider_id"], args["pharmacy_id"], args["medicine_id"],
                                             args["number"], args["order_date"])
    elif command == 'update_record':
        try:
            args = {"table_name": sys.argv[2], "key": sys.argv[3]}
            if args["table_name"] == 'Medicine':
                args["title"], args["manufacturer"] = sys.argv[4], sys.argv[5]
            elif args["table_name"] == 'Provider':
                args["title"], args["address"] = sys.argv[4], sys.argv[5]
            elif args["table_name"] == 'Phone_numbers':
                args["provider_id"], args["mobile_operator"] = sys.argv[4], sys.argv[5]
            elif args["table_name"] == 'Pharmacy':
                args["title"], args["phone_num"], args["address"] = sys.argv[4], sys.argv[5], sys.argv[6]
            elif args["table_name"] == 'Supplier_order_base':
                args["provider_id"], args["pharmacy_id"], args["medicine_id"], args["number"], args["order_date"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]
        except IndexError:
            c.v.wrong_table()
        else:
            if args["table_name"] == 'Medicine':
                c.update_medicine_table(args["key"], args["title"], args["manufacturer"])
            elif args["table_name"] == 'Provider':
                c.update_provider_table(args["key"], args["title"], args["address"])
            elif args["table_name"] == 'Pharmacy':
                c.update_pharmacy_table(args["key"], args["title"], args["phone_num"], args["address"])
            elif args["table_name"] == 'Phone_numbers':
                c.update_phone_numbers_table(args["key"], args["provider_id"], args["mobile_operator"])
            elif args["table_name"] == 'Supplier_order_base':
                c.update_supplier_order_base_table(args["key"], args["provider_id"], args["pharmacy_id"],
                                                   args["medicine_id"], args["number"], args["order_date"])
    elif command == 'generate_records':
        try:
            args = {"table_name": sys.argv[2], "value": int(sys.argv[3])}
        except (Exception, IndexError):
            print(Exception, IndexError)
        else:
            c.generate(args["table_name"], args["value"])
    elif command == "search_records":
        while True:
            search_num = c.v.get_search_num()
            try:
                search_num = int(search_num)
            except ValueError:
                c.v.invalid_search_num()
            else:
                if search_num in [2, 3, 4]:
                    break
                else:
                    c.v.invalid_search_num()
        if search_num == 2:
            c.search_in_two_tables()
        elif search_num == 3:
            c.search_in_three_tables()
        elif search_num == 4:
            c.search_in_all_tables()
    elif command == 'help':
        c.v.print_help()
    else:
        c.v.wrong_command()
