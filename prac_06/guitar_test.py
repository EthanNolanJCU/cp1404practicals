from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson", 1922, 12.50)
guitar2 = Guitar("other", 2013, 3000)

print(f"expected 100, got {guitar1.get_age()}")
print(f"expected 9, got {guitar2.get_age()}")
print(f"expected True, got {guitar1.is_vintage()}")
print(f"expected False, got {guitar2.is_vintage()}")
