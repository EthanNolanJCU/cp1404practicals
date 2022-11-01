from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

print("\nThe dynamically typed languages are:")

if python.is_dynamic():
    print(python.name)
if ruby.is_dynamic():
    print(ruby.name)
if visual_basic.is_dynamic():
    print(visual_basic.name)
