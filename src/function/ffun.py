# def greet_user():
#     print("hii there")

# print("me")#it executed first
# greet_user()#then function get executed
# print("you")


# using parameter and arguments

def greet_user(name,last_name):#name is parameter
    print(f"hi {name} {last_name}")

greet_user("shahzad", "good")#shahzad is argument


#key word argument
greet_user("shahzad",last_name="hi")

#NOTE:Positional argument cannot appear after keyword arguments