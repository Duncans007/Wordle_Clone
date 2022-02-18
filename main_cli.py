from src.Worldle import Worldle

def main():
    worldle = Worldle()
    while True:
        print(f"Guess {worldle.guesses}: ", end="")
        inp = input()
        ret = worldle.guess(inp)
        print(ret)


if __name__ == "__main__":
    main()