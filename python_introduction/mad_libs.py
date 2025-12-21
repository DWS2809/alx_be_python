# mad libs program with conditionals statements
print("Welcome to the Mad libs game!")
print("Please provide the following words:")

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

# conditional variation
if adjective.lower() == "scary":
    mood = "Everyone ran away ni fear!"
else: 
    mood = "Everyone joined in the fun!"

# mad libs story
story = (f"""One day, a {adjective} {noun} decided to {verb}. 
It traveled to {place} and met wild {animal}.
The moment was unforgettable.
{mood}""")
print("\n--- Your Mad Libs Story ---")
print(story)