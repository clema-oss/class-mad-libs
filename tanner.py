l = [
    "Adjective", "Adjective", "Noun", "Noun", "Plural Noun", "Game",
    "Plural Noun", "Verb-ing", "Verb-ing", "Plural Noun", "Plant",
    "Part of the body", "A place", "Verb-ing", "Adjective", "Number",
    "Plural noun"
]

def mad_lib(): # genuinly the worst implementation of a function i have ever written but wtv
    answers = []
    for word in l:
        answers.append(input(f"Enter a {word}: "))
    madlib = f"""A vacation is when you take a trip to some {answers[0]} place
with your {answers[1]} family. Usually you go to some place
that is near a/an {answers[2]} or up on a/an {answers[3]}.
A good vacation place is one where you can ride {answers[4]}
or play {answers[5]} or go hunting for {answers[6]}. I like
to spend my time {answers[7]} or {answers[8]}.
When parents go on a vacation, they spend their time eating
three {answers[9]} a day, and fathers play golf, and mothers
sit around {answers[10]}. Last summer, my little brother
fell in a/an {answers[11]} and got poison {answers[12]} all
over {answers[13]}. My family is going to go to (the)
{answers[14]}, and I will practice {answers[15]}. Parents
need vacations more than kids because parents are always very
{answers[16]} and because they have to work
hours every day all year making enough money to pay
for the vacation."""
    return madlib


if __name__ == "__main__":
    print("\n" + mad_lib())
