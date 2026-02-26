def eli_mad_lib():
    date = input("Date: ")
    name = input("Name: ")
    noun = input("Noun: ")
    pronoun = input("Pronoun: ")
    event = input("Event: ")
    signature = input("Sign: ")
    print("Date:", date)
    print(name, "is too cool for", noun, "class. Instead", pronoun, "will be attending the", event + ".")
    print("Signed:", signature)

if __name__ == "__main__":
    eli_mad_lib()
