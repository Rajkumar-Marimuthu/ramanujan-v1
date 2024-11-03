import os

def say_hello(name):
    print(f"hello {name}")
    print(os.environ['OPENAI_API_KEY_FIRST'])

name = input("Enter your name : ")
say_hello(name)

print(3//5)
print(3/5)