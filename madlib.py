# Madlib project
# aminly dealing with concatenation of the strings

# Basically a madlib is a paragraph with blanks in the middle which is left to fill by the users

# Illustrating an example

Adj = input("Adjective :")
noun = input("Noun :")
colour = input("Colour :")
verb = input("Verb :")
preposition = input("Preposition :")
cuss = input("Enter a cuss word :")
adverb = input("Adverb :")

madlib = f"The night is {Adj} and heavy with {noun} when I paint the front of The House {colour}.\
\nI paint quickly and quietly. I don’t want to {verb} my neighbor up. \
\nThe brush goes shhh shhh {preposition} the wall and even that is loud.  \
\nMy feet crunch on gravel as I finish up and slip into my home.  \
\nMy neighbor’s cursing wakes me up in the morning.\nI hear {cuss}! and shit! I split the blinds with two fingers. \
\nThe sun shines {adverb} bright and I squint to see my other neighbors file outside. \nThey see the {colour} paint and shake the..."

print(madlib)