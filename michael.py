def michael_mad_lib():
    date = input("Enter a date (MM/DD/YYYY): ")
    name = input("Enter a name: ")
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    sig = input("Enter another name: ")

    print(f"\n\n- YOUR STORY -")
    print(f"Date: {date}")
    print(f"\nPlease excuse {name} who is far too {adj} to attend {noun} class.")
    print("Signed:")
    print(sig)

if __name__ == "__main__":
    michael_mad_lib()