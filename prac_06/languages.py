from prac_06.programming_language import ProgrammingLanguage

languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
             ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
             ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print(languages[0])

print("\nThe dynamically typed languages are:")

for language in languages:
    if language.is_dynamic():
        print(language.name)
