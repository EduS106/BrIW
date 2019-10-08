from source.db_extraction import get_table, add_data, update_data
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def name_choice():
    if request.method == "GET":
        people = get_table("person", "name")
        people = [person['name'] for person in people]

        return render_template("yourname.html", item_list=people)



@app.route('/choosedrink', methods=['GET', 'POST'])
def drink_choice():
    if request.method == "GET":
        drinks = get_table("drink", "name")
        drinks = [drink['name'] for drink in drinks]

        return render_template('yourdrink.html', item_list=drinks)

    elif request.method == "POST":

        person_name = request.form.get("person-name")

        drink_name = request.form.get("drink-name")

        for drink in get_table("drink"):

            if str(drink_name) == str(drink[1]):
                add_data("person", "name", [person_name])

                update_data("person", "name", "preference", {person_name: drink[0]})

                return render_template("return_form.html", title="Posted", person=person_name, drink=drink_name)

        people = get_table("person", "name")

        drinks = get_table("drink", "name")

        the_list = [people, drinks]

        return render_template('people.html', title="Create Form", list_list=the_list)




    '''elif request.method == "POST":

        person_name = request.form.get("person-name")
        drink_name = request.form.get("drink-name")

        for drink in get_table("drink"):
            if str(drink_name) == str(drink[1]):
                add_data("person", "name", [person_name])
                update_data("person", "name", "preference", {person_name: drink[0]})
                return render_template("return_form.html", title="Posted", person=person_name, drink=drink_name)

        people = get_table("person", "name")
        drinks = get_table("drink", "name")
        the_list = [people, drinks]

        return render_template('people.html', title="Create Form", list_list=the_list)'''


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
