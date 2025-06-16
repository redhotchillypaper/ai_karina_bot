import ai_integration
import os


def main():
    karinaBot = ai_integration.Karina("gpt4all-falcon-newbpe-q4_0")
    karinaBot.start()

if __name__ == "__main__":
    main()


