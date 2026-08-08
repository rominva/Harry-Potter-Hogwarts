# 🧙 Hogwarts Wizard Management System

A small **Object-Oriented Programming (OOP)** project inspired by the Harry Potter universe.

This project was created to practice and demonstrate core Python OOP concepts such as:

* Classes and objects
* Inheritance
* Encapsulation with `@property`
* Getters and setters
* Input validation
* Magic methods (`__str__`, `__eq__`, `__len__`)
* Class methods
* Polymorphism
* `isinstance()`
* Lambda functions
* Sorting objects
* Class-level data management

---

## 🏰 Project Overview

The project models members of Hogwarts School of Witchcraft and Wizardry.

There are three types of Hogwarts members:

* 👨‍🏫 `Professor`
* 🎓 `Student`
* 👻 `Ghost`

All three inherit from the base `Wizard` class.

The `Hogwarts` class acts as a central manager for all members and provides methods for adding, removing, finding, displaying, and organizing wizards.

---

## 🧩 Class Structure

```text
                    Wizard
                   /      \
                  /        \
            Student      Professor
               
                    Ghost
                      ↑
                   Wizard
```

More precisely:

```text
Wizard
├── Student
├── Professor
└── Ghost

Hogwarts
└── manages all Wizard objects
```

### `Wizard`

The base class for all Hogwarts members.

Attributes:

* `name`
* `house`
* `age`

It also provides validation for `age` and `house`.

### `Student`

Inherits from `Wizard`.

Additional attributes:

* `year`
* `points`

Additional methods:

* `introduce()`
* `earn_points()`
* `lose_points()`

Students can earn and lose house points, but their points cannot become negative.

### `Professor`

Inherits from `Wizard`.

Additional attribute:

* `subject`

Provides its own `introduce()` method.

### `Ghost`

Inherits from `Wizard`.

Additional attributes:

* `greeting`

Ghosts can have `None` as their house or age because not every ghost belongs to a house or has a meaningful age.

### `Hogwarts`

A class that manages the members of Hogwarts.

It contains:

* A list of all wizards
* The four Hogwarts houses
* The seven core subjects

It also provides class methods for managing and displaying Hogwarts members.

---

## ✨ Main Features

### 👤 Wizard Validation

The `Wizard` class validates its attributes using properties.

#### Age

Age must either be:

* An integer
* `None`

If an integer is provided, it must be at least `11`.

```python
wizard.age = 15
```

Invalid values raise an exception:

```python
wizard.age = "fifteen"
# TypeError

wizard.age = 8
# ValueError
```

#### House

A wizard can belong to one of the four Hogwarts houses:

```text
Gryffindor
Slytherin
Ravenclaw
Hufflepuff
```

A house can also be `None`, which is useful for characters such as some ghosts.

---

## 🪄 Inheritance

`Student`, `Professor`, and `Ghost` inherit common functionality from `Wizard`.

For example:

```python
class Student(Wizard):
    ...
```

This allows a `Student` to automatically have attributes such as `name`, `house`, and `age` while also having its own student-specific attributes and methods.

The subclasses use `super().__init__()` to initialize the inherited attributes.

---

## 🔐 Encapsulation with Properties

The `age` and `house` attributes use Python properties.

For example:

```python
@property
def age(self):
    return self._age

@age.setter
def age(self, age):
    ...
```

This allows validation to happen whenever a value is assigned.

Instead of directly modifying the internal attribute:

```python
wizard._age
```

the public interface is:

```python
wizard.age
```

This keeps validation logic inside the class.

---

## ⚖️ Magic Methods

The project implements several Python magic methods.

### `__str__`

Provides a readable representation of a wizard:

```python
print(harry)
```

Example output:

```text
Harry Potter => house: Gryffindor, age: 11
```

### `__eq__`

Allows two wizard objects to be compared based on their:

* name
* house
* age

For example:

```python
harry1 == harry2
```

The method also checks that the other object is a `Wizard`.

### `__len__`

The `Hogwarts` class implements:

```python
len(Hogwarts)
```

to return the number of wizards currently registered at Hogwarts.

---

## 🏫 Hogwarts Management

The `Hogwarts` class provides several class methods.

### Add a wizard

```python
Hogwarts.add(wizard)
```

The method:

1. Checks that the object is a `Wizard`
2. Checks that the wizard is not already in Hogwarts
3. Adds the wizard to the Hogwarts member list

---

### Remove a wizard

```python
Hogwarts.remove(wizard)
```

The method verifies that the wizard exists before removing them.

---

### Find a wizard

```python
Hogwarts.find(wizard)
```

Checks whether a wizard belongs to Hogwarts.

---

### Show all wizards

```python
Hogwarts.show_all_wizards()
```

Members are grouped into:

* 👨‍🏫 Professors
* 🎓 Students
* 👻 Ghosts

Each group is sorted alphabetically by name using a `lambda` function:

```python
sorted(professors, key=lambda professor: professor.name)
```

---

### Show all houses

```python
Hogwarts.show_all_houses()
```

Displays the four Hogwarts houses.

---

### Show all subjects

```python
Hogwarts.show_all_subjects()
```

Displays the seven core subjects.

---

### Introduce all members

```python
Hogwarts.introduce()
```

Each wizard uses its own `introduce()` method.

For example:

```text
Hi! I'm Harry Potter from Gryffindor house. I'm currently in year 1.

Hello. I'm Minerva McGonagall, professor of Transfiguration.

Nearly Headless Nick: I am neither here nor there.
```

This demonstrates **polymorphism**: the same method call can produce different behavior depending on the object's class.

---

### Show members of a house

```python
Hogwarts.show_house_members("Gryffindor")
```

Displays all Hogwarts members belonging to the selected house.

---

## 🎓 Student Points

Students have a `points` attribute.

They can earn points:

```python
harry.earn_points(10)
```

and lose points:

```python
harry.lose_points(5)
```

The project prevents points from becoming negative.

For example, if a student has 3 points:

```python
harry.lose_points(10)
```

their points become:

```text
0
```

instead of:

```text
-7
```

---

## 🧪 Example

```python
harry = Student("Harry Potter", "Gryffindor", 11, 1)

print(harry)
```

Output:

```text
Harry Potter => house: Gryffindor, age: 11
```

Earn points:

```python
harry.earn_points(20)

print(harry.points)
```

Output:

```text
20
```

Lose points:

```python
harry.lose_points(5)

print(harry.points)
```

Output:

```text
15
```

Add Harry to Hogwarts:

```python
Hogwarts.add(harry)
```

Check membership:

```python
Hogwarts.find(harry)
```

---

## 🧠 Concepts Practiced

This project was designed as an OOP practice project and covers the following Python concepts:

| Concept        | Where it is used                                      |
| -------------- | ----------------------------------------------------- |
| Classes        | `Wizard`, `Student`, `Professor`, `Ghost`, `Hogwarts` |
| Objects        | Hogwarts characters                                   |
| Inheritance    | `Student`, `Professor`, `Ghost` inherit from `Wizard` |
| `super()`      | Subclass constructors                                 |
| Encapsulation  | `age` and `house` properties                          |
| Getters        | `@property`                                           |
| Setters        | `@age.setter`, `@house.setter`                        |
| Validation     | Age, house, year, points                              |
| `__str__`      | Readable wizard representation                        |
| `__eq__`       | Comparing wizard objects                              |
| `__len__`      | Counting Hogwarts members                             |
| Class methods  | Hogwarts management methods                           |
| Polymorphism   | Different `introduce()` implementations               |
| `isinstance()` | Type checking                                         |
| Lambda         | Sorting wizards by name                               |
| `sorted()`     | Alphabetical member lists                             |
| Lists          | Storing Hogwarts members                              |

---

## 📁 Project Structure

A simple project structure could be:

```text
hogwarts-oop/
│
├── hogwarts.py
└── README.md
```

---

## 🚀 Possible Future Improvements

Some possible extensions for the project:

* Add a `House` class instead of storing houses as strings.
* Give each house its own point total.
* Add a `Subject` class.
* Add teachers and students to specific subjects.
* Implement house rankings based on points.
* Add a method for transferring a student between houses.
* Add more validation for student points and professor subjects.
* Add unit tests using `pytest`.
* Separate the classes into multiple Python modules.
* Create a command-line interface for interacting with Hogwarts.

---

## 📚 Purpose

This project is a hands-on exercise in **Python Object-Oriented Programming**.

The main goal was not to build a production-ready Hogwarts simulator, but to practice designing classes, defining relationships between objects, validating data, and using Python's object-oriented features in a meaningful project.

