from src.Worldle import Worldle

def main():
    worldle = Worldle(max_guesses=6, word_length=4)
    while True:
        print(f"Guess {worldle.guesses}: ", end="")
        inp = input()
        ret = worldle.guess(inp)
        print(ret)


if __name__ == "__main__":
    main()