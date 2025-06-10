from gpt4all import GPT4All
import subprocess

class Karina:
    
    def __init__(self, model_name):
        self.model = GPT4All(model_name)
    
    def increase_volume(self):
        subprocess.run(['osascript', '-e', 'set volume output volume 100'])


    def decrease_volume(self):
        subprocess.run(['osascript', '-e', 'set volume output volume 10'])

    def start(self):
        with self.model.chat_session() as session:
            print(session.generate("Your name is Karina, you are female. You are a really helpful bot, so please be acting accordingly!"))
            while True:
                prompt = input("🧠 Ти: ")
                if prompt.lower() in ["вихід", "exit", "quit"]:
                    break
                if prompt.lower() in ['зменши гучність']:
                    self.decrease_volume()
                if prompt.lower() in ['підвищи гучність', 'збільши гучність']:
                    self.increase_volume()
                response = session.generate(prompt)
                print("🤖 AI:", response)
