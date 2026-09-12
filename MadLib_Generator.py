Adjective = input("Enter your choice of an adjective: ").strip().title()
Word = input("Enter your choice of a word: ").strip().title()
article = "An" if Adjective[0].lower() in "aeiou" else "A"
print(f"I have {article.lower()} {Adjective} {Word}")
