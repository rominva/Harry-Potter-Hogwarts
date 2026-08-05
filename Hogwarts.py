class Wizard:
    def __init__(self, name, house, age):
        self.name = name
        self.house = house
        self.age = age

    def __str__(self):
        return f"{self.name} => house: {self.house}, age: {self.age}"

    def __eq__(self, other):
        # Check the typr of other
        if not isinstance(other, Wizard):
            return False

        return self.name == other.name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age is None:
            self._age = age
            return

        if not isinstance(age, int):
            raise TypeError("Age must be an integer or None")

        if age < 11:
            raise ValueError("Age must be 11 or older")

        self._age = age
        

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house is not None and house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house


class Student(Wizard):
    def __init__(self, name, house, age, year, points=0):
        super().__init__(name, house, age)
        if not 1 <= year <= 7:
            raise ValueError("Invalid year")
        self.year = year
        self.points = points

    def introduce(self):
        return f"Hi! I'm {self.name} from {self.house} house. I'm currently in year {self.year}."

    def earn_points(self, n):
        self.points += n

    def lose_points(self, n):
        # If not enough point
        if n > self.points:
            self.points = 0
            return

        self.points -= n


class Professor(Wizard):
    def __init__(self, name, house, age, subject):
        super().__init__(name, house, age)
        self.subject = subject

    def introduce(self):
        return f"Hello. I'm {self.name}, professor of {self.subject}."


class Ghost(Wizard):
    def __init__(self, name, house, age=None, greeting="Boooo!"):
        super().__init__(name, house, age)
        self.greeting = greeting

    def introduce(self):
        return f"{self.name}: {self.greeting}"


class Hogwarts:
    wizards = [
        Professor("Albus Dumbledore", "Gryffindor", 109, "nothing but a Headmaster"),
        Professor("Minerva McGonagall", "Gryffindor", 70, "Transfiguration"),
        Professor("Severus Snape", "Slytherin", 38, "Potions"),
        Professor("Filius Flitwick", "Ravenclaw", 60, "Charms"),
        Professor("Pomona Sprout", "Hufflepuff", 60, "Herbology"),
        Professor("Rubeus Hagrid", "Gryffindor", 50, "Magical Creatures"),
        Student("Harry Potter", "Gryffindor", 11, 1),
        Student("Ron Weasley", "Gryffindor", 11, 1),
        Student("Hermione Granger", "Gryffindor", 11, 1),
        Student("Neville Longbottom", "Gryffindor", 11, 1),
        Student("Luna Lovegood", "Ravenclaw", 11, 1),
        Student("Draco Malfoy", "Slytherin", 11, 1),
        Student("Cho Chang", "Hufflepuff", 11, 1),
        Student("Cedric Diggory", "Hufflepuff", 12, 2),
        Ghost("Nearly Headless Nick", "Gryffindor", None, "I am neither here nor there."),
        Ghost("The Fat Friar", "Hufflepuff", None, "Hope to see you in Hufflepuff! My old house, you know."),
        Ghost("The Grey Lady", "Ravenclaw", None, "If you have to ask, you'll never know. If you know, you need only ask."),
        Ghost("The Bloody Baron", "Slytherin"),
        Ghost("Moaning Myrtle", "Ravenclaw", None, "If you die, you're welcome to share my toilet!"),
        Ghost("Professor Cuthbert Binns", None, None, "My subject is History of Magic. I deal with facts, not myths and legends."),
        Ghost("Peeves", None, None, "Wondering around at midnight, Ickle Firsties? Tut, tut, tut. Naughty, naughty, you'll get caughty...")
    ]

    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    subjects = ["Astronomy", "Charms", "Defence Against the Dark Arts",
                "Herbology", "History of Magic", "Potions", "Transfiguration"]

    @classmethod
    def add(cls, wizard):
        if not isinstance(wizard, Wizard):
            raise TypeError("You have to enter a Wizard!")

        if wizard in cls.wizards:
            return f"{wizard} already is in Hogwarts."

        cls.wizards.append(wizard)

    @classmethod
    def remove(cls, wizard):
        if not isinstance(wizard, Wizard):
            raise TypeError("You have to enter a Wizard!")

        if wizard not in cls.wizards:
            return f"Sorry, {wizard} is not in Hogwarts."

        cls.wizards.remove(wizard)

    @classmethod
    def find(cls, wizard):
        if not isinstance(wizard, Wizard):
            raise TypeError("You have to enter a Wizard!")

        if wizard in cls.wizards:
            return f"{wizard} is from Hogwarts."
        else:
            return f"{wizard} does not belong to Hogwarts!"

    @classmethod
    def show_all_wizards(cls):
        print("🧙 Wizards Of Hogwarts:")
        for i, wizard in enumerate(cls.wizards):
            print(i+1, wizard)

    @classmethod
    def show_all_houses(cls):
        print("🏠 Houses Of Hogwarts:")
        for j, house in enumerate(cls.houses):
            print(j+1, house)

    @classmethod
    def show_all_subjects(cls):
        print("📚 7 Core Subjects At Hogwarts:")
        for k, subject in enumerate(cls.subjects):
            print(k+1, subject)

    @classmethod
    def __len__(cls):
        return len(cls.wizards)

    @classmethod
    def introduce(cls):
        for wizard in cls.wizards:
            # print(f"{wizard.name}; {wizard.introduce()}")
            print(wizard.introduce())
