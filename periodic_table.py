import periodictable

atomic_no = int(input("Enter an atomic no: "))
element = periodictable.elements[atomic_no]
print("Atomic number: ", element.number)
print("Symbol: ", element.symbol)
print("Name: ", element.name)
print("Atomic mass: ", element.mass)
print("Density: ", element.density)