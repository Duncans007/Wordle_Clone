from flask import Flask, render_template, url_for

app = Flask(__name__)

##### Initialize Data
guess_dict = {}
guesses = 6
word_length = 6

for i in range(1, guesses+1):
    guess_dict[i] = {
        "letters": ["\xa0"]*word_length,  # letters or \xa0 for blank
        "colors": ["gray"]*word_length  # Options gray, yellow, green
    }


@app.route("/")
@app.route("/worldle")
def home():
    return render_template("./worldle_page.html", guesses=guesses, word_length=word_length, data=guess_dict, title="Worldle")


if __name__ == '__main__':
    app.run(debug=True)