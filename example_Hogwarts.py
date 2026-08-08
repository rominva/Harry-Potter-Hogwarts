from Hogwarts import Wizard, Student, Professor,Ghost, Hogwarts

# __________________________________Wizard_______________________________
sirius = Wizard("Sirius Black", "Gryffindor", 38)

print(sirius)

sirius.age = 40
print(sirius.age)

# sirius.age = 10
# print(sirius.age)

# sirius.house = "Gotham"
# print(sirius.house)

sirius2 = Wizard("Sirius Black", "Slytherin", 38)
print(sirius == sirius2)

dobby = "Dobby The Free House Elf"
print(sirius == dobby)




# _____________________________Student_____________________________________
harry = Student("Harry", "Gryffindor", 17, 7)
ron = Student("Ron", "Gryffindor", 17, 7)
print(harry == ron)
print(harry == 5)

# fred = Student("Fred Weasley", "Gryffindor", 18, 8)

print(harry.introduce())

# harry.earn_points("100")
# harry.lose_points("a hundred")

harry.earn_points(5)
print(harry.points)

harry.earn_points(10)
print(harry.points)

harry.lose_points(50)
print(harry.points)




# ____________________________Professor___________________________________
professor1 = Professor("Remus Lupin", "Gryffindor", 38, "Defence Against the Dark Arts")

print(professor1.introduce())

print(professor1)

# professor1.age = 0




# __________________________________Ghost_______________________________
peeves = Ghost("Peeves", greeting="Oh Potter, You Rotter!")
myrtle = Ghost("Moaning Myrtle", age=14)

print(peeves.introduce())

print(myrtle.introduce())

print(myrtle.house)

print(myrtle.age)




# __________________________________Hogwarts_______________________________
Hogwarts.show_all_wizards()

# Hogwarts.add("Romina Valehi")

Hogwarts.add(Student("George Weasley", "Gryffindor", 13, 3))
Hogwarts.show_all_wizards()

# Hogwarts.add(Student("Ron Weasley", "Gryffindor", 11, 1))

# Hogwarts.remove("Dudley Dursley")

fred = Student("Fred Weasley", "Gryffindor", 13, 3)
# Hogwarts.remove(fred)

quirrell = Professor("Quirinus Quirrell", "Ravenclaw", 30, "Defence Against the Dark Arts")
Hogwarts.add(quirrell)
Hogwarts.show_all_wizards()
Hogwarts.remove(quirrell)
Hogwarts.show_all_wizards()

# Hogwarts.find("Petunia Evans")

print(len(Hogwarts()))

Hogwarts.find(fred)
Hogwarts.add(fred)
Hogwarts.find(fred)

Hogwarts.show_all_wizards()

Hogwarts.show_all_houses()

Hogwarts.show_all_subjects()

print(len(Hogwarts()))

Hogwarts.introduce()

Hogwarts.show_house_members("Gryffindor")

# Hogwarts.show_house_members("privert drive")

# Hogwarts.show_house_members(5)

Hogwarts.show_house_members("Slytherin")