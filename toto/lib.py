from termcolor import colored

def whats_my_name():
    return "Hello my name is Martin"

def who_am_i():
    name = whats_my_name()
    print(colored(name, "red"))