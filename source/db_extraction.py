import pymysql
from source.file_handler import start_dict
from os import environ


def connect_db():
    connection = pymysql.connect(
        environ.get("academyDBhost"),  # host
        environ.get("academyDBuser"),  # username
        environ.get("academyDBpass"),  # password
        environ.get("academyDB")  # database
    )
    return connection


def add_data(db, table_name, field, data):
    # data is a list of names or drinks, for example
    cursor = db.cursor()

    try:
        for value in data:
            sql_query = f"INSERT INTO {table_name} ({field}) VALUES (%s);"
            print(sql_query)
            cursor.execute(sql_query, (value,))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()


def update_data(db, table_name, where_field, field_to_set, new_data):
    # data is a dictionary of the value of the field where you want to set a field value {where_value:added_value}
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


def get_preferences():
    pass


'''def initialise_db(db, sql_initialisation_script_path):
    cursor = db.cursor()
    tables = []
    try:

        query_file = open(sql_initialisation_script_path, "r")
        query = query_file.read()

        print("All queries:", query)

        print("Query:", query)

        cursor.execute(query)

        db.commit()

        sql_query = "SHOW TABLES"

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        for row in rows:
            tables.append(row)

        print("DB initialised. The following tables have been created:", tables)

    except Exception as e:
        print(f"The following exception occurred:{e}")

    finally:
        cursor.close()'''


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
            print("Person:", person_id, "\tDrink:", drink_id)
            cursor.execute(sql_query, (drink_id, person_id))

        db.commit()

    except Exception as e:
        print(f"The following exception occurred: {e}")

    finally:
        cursor.close()


def get_table(db, table_name):

    table = []

    cursor = db.cursor()

    try:

        sql_query = f"select * from {table_name};"

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        for row in rows:
            table.append(row)

    except Exception as e:
        print(f"The following exception occurred:{e}")

    finally:
        cursor.close()

    return table

db = connect_db()
update_data(db, "person", "name", "preference", {"Kieran":131, "Christos":2})
db.close()

