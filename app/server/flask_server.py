from app.source.db_extraction import get_table, add_data, update_data, preference_ids_to_name, table_to_dict, remove_data_by_id
from app.source.input_cleaner import web_name_cleaner
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    if request.method == "GET":
        return render_template("index.html")


@app.route('/example', methods=['GET'])
def example_page():
    if request.method == "GET":
        return render_template("example.html")


@app.route('/people', methods=['GET'])
def people_list():
    if request.method == "GET":
        people = get_table("person")
        drinks = table_to_dict("drink")
        return render_template("people.html", table=people, drinks=drinks)


@app.route('/people/add', methods=['GET', 'POST'])
def add_people():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template("addPerson.html", item_list=drinks)

    elif request.method == "POST":
        drinks = get_table("drink")

        person_name = request.form.get("person-name")
        person_name = web_name_cleaner(person_name)

        drink_id = int(request.form.get("preference-name"))
        drink_name = preference_ids_to_name([drink_id])[0]

        drink_ids = [drink['drink_id'] for drink in drinks]
        all_names = list(table_to_dict("person").values())

        if person_name not in all_names:
            if drink_id in drink_ids:
                add_data("person", "name", [person_name])
                update_data("person", "name", "preference", {person_name: drink_id})

                return render_template('addPerson.html', item_list=drinks, name=person_name, preference=drink_name, success=True)
            else:
                print(f"Your drink chosen was: Drink ID= {drink_id} and Drink Name: {drink_name}")
                return render_template('addPerson.html', item_list=drinks, name=person_name, preference=drink_name, error=True)
        else:
            print(f"Your name has already been entered {person_name}")
            return render_template('addPerson.html', item_list=drinks, name=person_name, preference=drink_name, repeated=True)


@app.route('/people/remove', methods=['GET', 'POST'])
def remove_people():
    if request.method == "GET":
        people = get_table("person")
        return render_template('removePerson.html', item_list=people)

    elif request.method == "POST":
        people = get_table("person")

        person_id = int(request.form.get("people-name"))

        people_ids = list(table_to_dict("person").keys())

        if person_id in people_ids:
            person_name = table_to_dict("person")[person_id]
            remove_data_by_id("person", [person_id])
            people = get_table("person")
            return render_template('removePerson.html', item_list=people, name=person_name, success=True)
        else:
            print(f"You attempted to remove: Person ID= {person_id}")
            return render_template('removePerson.html', item_list=people, error=True)


@app.route('/people/preferences', methods=['GET', 'POST'])
def change_preferences():
    if request.method == "GET":
        pass


@app.route('/drinks', methods=['GET'])
def drinks_list():
    if request.method == "GET":
        drinks = get_table("drink", "name")
        drinks = [drink['name'] for drink in drinks]

        return render_template('drinks.html', item_list=drinks)


@app.route('/drinks/add', methods=['GET', 'POST'])
def add_drinks():
    if request.method == "GET":
        return render_template("addDrink.html")

    elif request.method == "POST":
        drinks = get_table("drink")

        drink = request.form.get("drink-name")
        drink = web_name_cleaner(drink)

        all_drinks = list(table_to_dict("drink").values())

        if drink not in all_drinks:
            add_data("drink", "name", [drink])
            return render_template('addDrink.html', item_list=drinks, name=drink, success=True)
        else:
            print(f"This drink has already been entered {drink}")
            return render_template('addDrink.html', name=drink, repeated=True)


@app.route('/drinks/remove', methods=['GET', 'POST'])
def remove_drinks():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template('removeDrink.html', item_list=drinks)

    elif request.method == "POST":
        drinks = get_table("drink")

        drink_id = int(request.form.get("drink-name"))

        drink_ids = list(table_to_dict("drink").keys())

        if drink_id in drink_ids:
            drink_name = table_to_dict("drink")[drink_id]
            remove_data_by_id("drink", [drink_id])
            drinks = get_table("drink")
            return render_template('removePerson.html', item_list=drinks, name=drink_name, success=True)
        else:
            print(f"You attempted to remove: Person ID= {drink_id}")
            return render_template('removePerson.html', item_list=drinks, error=True)


@app.route('/rounds', methods=['GET', 'POST'])
def rounds_list():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template('rounds.html', item_list=drinks)


@app.route('/rounds/start', methods=['GET', 'POST'])
def create_round():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template('create_round.html', item_list=drinks)


@app.route('/rounds/add_order', methods=['GET', 'POST'])
def add_order():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template('add_order.html', item_list=drinks)


@app.route('/rounds/remove_order', methods=['GET', 'POST'])
def remove_order():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template('remove_order.html', item_list=drinks)


@app.route('/rounds/finish', methods=['GET', 'POST'])
def close_round():
    if request.method == "GET":
        drinks = get_table("drink")
        return render_template('remove_order.html', item_list=drinks)


if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
