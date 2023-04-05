#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Godfrey", "Otieno")
say_my_name("Joseph", "kroos")
say_my_name("Raila")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
