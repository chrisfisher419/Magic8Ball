import random

question = input("I am a magic 8 ball! If you have a yes/no type question you are unsure of, ask me!")
message = ['It is certain',
           'Yes, Absolutely',
           'Indubitably',
           'You should know that is a yes already!'
           'I am unsure, try again in a few minutes',
           'Not a good time...',
           'What kind of silly question is that?',
           'Yeah, definitely not',
           'Are you insane? No',
           'Not in a million years',
           'Doubtful',
           ]
if question == "What is the meaning of life?":
    print("42")
else:
    print(message[random.randint(0, len(message) - 1)])
