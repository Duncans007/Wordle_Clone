from src.Worldle import Worldle

def main():
    max_guesses = 6
    worldle = Worldle(max_guesses=max_guesses, word_length=4)
    while True:
        print(f"Guess {worldle.guesses}: ", end="")
        inp = input()
        ret = worldle.guess(inp)
        print(ret)
        if max_guesses < worldle.guesses:
            worldle.generate_word()
            print("\nNew Game!\n")


if __name__ == "__main__":
    main()