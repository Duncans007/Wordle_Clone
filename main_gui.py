from flask import Flask, render_template, request
from src.Worldle import Worldle


##### Create function to set and reset the guess dictionary
def reset_dict():
    dictionary = {}
    for i in range(1, max_guesses + 1):
        dictionary[i] = {
            "letters": ["\xa0"]*word_length,  # letters or \xa0 for blank
            "colors": ["gray"]*word_length  # Options gray, yellow, green
        }
    return dictionary



##### Initialize Data
max_guesses = 6
word_length = 5

page_title = "Worldle"
game_object = Worldle(word_length=word_length, max_guesses=max_guesses)
guess_dict = reset_dict()



##### Run Flask
app = Flask(__name__)


##### Flask ome game page
@app.route("/")
def worldle_game():
    return render_template("./worldle_page.html", guesses=max_guesses, word_length=word_length, data=guess_dict, guesses_left=True, title=page_title, error_msg="")


##### Flask home page POST request
@app.route("/", methods=['POST'])
def button_press():

    global guess_dict, game_object
    error_msg = ""

    # Handles guess making
    if request.form['submit_button'] == "Make Guess":

        guesses_left = True
        # get form input
        text_guess = request.form['worldle_guess'].lower()
        # pass guess to game object
        game_return = game_object.guess(text_guess)


        # error value 0, 1, 4: successfully made guess
        if game_return[0] in [0, 1, 4]:
            # update output dictionary
            guess_dict[game_object.guesses - 1] = {
                'letters': [*text_guess],
                'colors': game_object.output_to_colors(game_return[1])
            }
            if game_return[0] == 0:
                error_msg = ""
            elif game_return[0] == 1:
                error_msg = f"That's the last guess! Your word was \'{game_return[2]}\'."
                guesses_left = False
            elif game_return[0] == 4:
                error_msg = "You guessed right!"
                guesses_left = False


        # error value 2: guess not proper length
        # error value 3: not an actual word
        # error value 5: is not alpha
        elif game_return[0] in [2,3,5]:
            error_msg = game_return[1]


    # Handle reset button
    elif request.form['submit_button'] == "Reset":
        guess_dict = reset_dict()
        game_object = Worldle(word_length=word_length, max_guesses=max_guesses)
        guesses_left = True


    # return template
    return render_template("./worldle_page.html", guesses=max_guesses, word_length=word_length, data=guess_dict, guesses_left=guesses_left, title=page_title, error_msg=error_msg)



if __name__ == '__main__':
    app.run(debug=True)