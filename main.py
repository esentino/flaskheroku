from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def calc():
    html = """
    <h2> Kalkulator: </h2>
    <form action="/calc" method="POST">
        <input type="text" name="liczba"/>
        <input type="text" name="liczba2"/>
        <select name="dzialanie">
    <option>+</option>
    <option>-</option>
    <option>*</option>
    <option>/</option>
        </select>
        <button type="submit"> Wyslij </button>
    </form>
    """
    if request.method == "POST":
        liczba = int(request.form['liczba'])
        liczba2 = int(request.form['liczba2'])
        dzialanie = request.form['dzialanie']
        if dzialanie == "*":
            wynik = liczba * liczba2
        elif dzialanie == "/":
            wynik = liczba / liczba2
        elif dzialanie == "+":
            wynik = liczba + liczba2
        elif dzialanie == "-":
            wynik = liczba - liczba2
        return f"{wynik}"
    return html

if __name__ == "__main__":
    app.run(debug=True)
