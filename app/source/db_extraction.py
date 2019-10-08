import pymysql
from source.file_handler import start_dict
from os import environ


def connect_db():
    connection = pymysql.connect(
        environ.get("academyDBhost"),  # host
        environ.get("academyDBuser"),  # username
        environ.get("academyDBpass"),  # password
        environ.get("academyDB"),  # database
        cursorclass=pymysql.cursors.DictCursor # output a dictionary cursor
    )
    return connection


def add_data(table_name, field, data):
    # data is a list of names or drinks, for example
    db = connect_db()

    cursor = db.cursor()

    try:
        for value in data:
            sql_query = f"INSERT INTO {table_name} ({field}) VALUES (%s);"
            cursor.execute(sql_query, (value,))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()
        db.close()


def add_order(person_id, drink_id, round_id):

    db = connect_db()

    cursor = db.cursor()

    try:
        sql_query = f"INSERT INTO orders (person_id, drink_id, round_id) VALUES (%s, %s, %s);"
        cursor.execute(sql_query, (person_id, drink_id, round_id))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()
        db.close()


def update_data(table_name, where_field, field_to_set, new_data):
    # data is a dictionary of the value of the field where you want to set a field value {where_value:added_value}
    db = connect_db()

    cursor = db.cursor()

    try:
        for where_value, added_value in new_data.items():

            sql_query = f"UPDATE {table_name} SET {field_to_set}=%s WHERE {where_field}=%s;"

            cursor.execute(sql_query, (added_value, where_value))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()
        db.close()


def remove_data_by_id(table_name, data):
    # data is a list of names or drinks, for example
    db = connect_db()

    cursor = db.cursor()

    if table_name == "preferences":
        table_name = "person"
        where_field = "preference"
    else:
        where_field = table_name + "_id"

    try:
        for value in data:
            sql_query = f"DELETE FROM {table_name} WHERE {where_field}={value};"
            cursor.execute(sql_query)

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()
        db.close()


def remove_order(person_id, round_id=None):

    db = connect_db()

    cursor = db.cursor()

    try:
        sql_query = f"DELETE FROM orders WHERE round_id = {round_id} AND person_id = {person_id};"
        cursor.execute(sql_query)

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()
        db.close()


def get_preferences():
    pass


def make_person_table_from_file(db, filename):

    people_dictionary = start_dict(filename)

    cursor = db.cursor()

    try:
        for person_id, person_name in people_dictionary.items():
            sql_query = "INSERT INTO person (person_id, name) VALUES (%s, %s);"
            cursor.execute(sql_query, (person_id, person_name))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()


def make_drink_table_from_file(db, filename):
    drinks_dictionary = start_dict(filename)

    cursor = db.cursor()

    try:
        for drink_id, drink_name in drinks_dictionary.items():
            sql_query = "INSERT INTO drink (drink_id, name) VALUES (%s, %s);"
            cursor.execute(sql_query, (drink_id, drink_name))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()


def add_preferences_from_file(db, filename):

    preferences_dictionary = start_dict(filename)

    cursor = db.cursor()

    try:
        for person_id, drink_id in preferences_dictionary.items():
            sql_query = "UPDATE person SET preference=%s WHERE person_id=%s;"
            cursor.execute(sql_query, (drink_id, person_id))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()


def get_table(table_name, field="*"):

    db = connect_db()

    table = []

    cursor = db.cursor()

    try:

        sql_query = f"select {field} from {table_name};"

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        for row in rows:
            table.append(row)

    except Exception as e:
        print(f"The following exception occurred:{e}")

    finally:
        cursor.close()
        db.close()

    return table


def get_round_id():

    db = connect_db()

    table = 0

    cursor = db.cursor()

    try:

        sql_query = f"select round_id from rounds order by round_id desc limit 1;"

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        table = rows[0]['round_id']

    except Exception as e:
        print(f"The following exception occurred:{e}")

    finally:
        cursor.close()
        db.close()

    return table


def table_to_dict(dict_type):
    output_dictionary = {}
    if dict_type == "person":
        people = get_table("person")
        for person in people:
            output_dictionary.update({person["person_id"]: person["name"]})
    elif dict_type == "drink":
        drinks = get_table("drink")
        for drink in drinks:
            output_dictionary.update({drink["drink_id"]: drink["name"]})
    elif dict_type == "preference":
        people = get_table("person")
        for person in people:
            if person["preference"] is not None:
                output_dictionary.update({person["person_id"]: person["preference"]})
    elif dict_type == "orders":
        orders = get_table("orders")

        current_round = get_round_id()

        orders = [order for order in orders if (order['round_id'] == current_round)]

        for order in orders:
            output_dictionary.update({order["person_id"]: order["drink_id"]})
    else:
        print("Invalid argument. Please enter string 'people', 'drinks', 'preferences' or 'orders' as an argument")

    return output_dictionary


def save_to_db(data_name, data, mode="add"):
    if mode == "add":
        if data_name == "people":
            add_data("person", "name", data.values())
        elif data_name == "drinks":
            add_data("drink", "name", data.values())
        elif data_name == "preferences":
            update_data("person", "person_id", "preference", data)
        elif data_name == "orders":
            pass
        else:
            print("DB table not found. Currently compatible with data_name arguments of: 'people', 'drinks', 'preferences' and 'orders'.")
