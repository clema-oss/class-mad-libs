def chupzi_mad_lib():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Create the story using an f-string to embed the variables
    madlib_story = (f"Today I went to a {adjective} zoo. I saw a {noun} {verb} across the entire {place}.")

    # Print the final story
    print("Your Mad Lib Story:")

    print(madlib_story)