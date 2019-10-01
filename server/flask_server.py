from source.db_extraction import get_table, add_data, update_data
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == "GET":
        people = get_table("person", "name")
        drinks = get_table("drink", "name")
        the_list = [people, drinks]
        return render_template('index.html', item_list=people)

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

        return render_template('index.html', title="Create Form", list_list=the_list, fail=drink_name)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)


'''import random
from source.db_extraction import get_table
from flask import Flask, jsonify, render_template, render_template_string, request


app = Flask(__name__)

@app.route("/")
def render_index():
    if request.method == "GET":
        people = get_table("person")
        drinks = get_table("drink")
        the_list = [people, drinks]
        return render_template("index.html", list_list=the_list)
    elif request.method ==


@app.route("/mainMenu")
def render_main_menu():
    return render_template("mainMenu.html")


if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=True)'''