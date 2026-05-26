# RUN THE CODE CUZ U UNDERSTAND... DONT UNDERSTAND IT CUZ IT RAN
# OOPS Examples

Small, readable Python examples demonstrating core Object-Oriented Programming (OOP) concepts.

## Project summary

This folder contains focused example scripts that teach one idea at a time (classes, encapsulation, inheritance, polymorphism, abstract base classes) plus small utility/test scripts to practice concepts.

## Files and purpose

- `ex1.py`: Simple `Character` class showing attributes, methods, and interactions.
- `ex2.py`: `BankAccount` demonstrating encapsulation and private attributes.
- `ex3.py`: Inheritance examples (`Knight`, `Wizard`, `Witch`) and method overriding.
- `ex4.py`: Polymorphism and duck typing; multiple character types used interchangeably.
- `ex5.py`: Abstract base class (`PaymentMethod`) with concrete implementations.
- `bucket.py`: Simple shape classes (`circle`, `square`, `triangle`) and a `bucket` container class that stores counts of shapes by type. Includes example usage at the bottom showing how to add shapes and print the bucket contents.
- `test.py`, `test2.py`, `test3.py`: Minimal scripts that demonstrate or test individual ideas.
- `property.py`: Examples demonstrating Python @property decorator for controlled attribute access using the example of a videogame charecter's health
- `magic.py`: Examples demonstrating Python magic methods or dunder methods for how custom classes should behave with built-in functions and operators using an example of a videogame inventory
- `static-and-class.py`: Examples demonstrating class methods and static methods showcasing how and why we use them
## How to run

Use your Python interpreter (3.8+ recommended). Examples:

```bash
python ex1.py
python ex3.py
python test.py
```

Each file is meant to be easy to read and to show a single idea in OOP or a small Python concept.

# Reusable Prompt For Creating Similar Exercises

Use this prompt to continue learning OOP or any programming topic in the same practical style.

```text
I want to learn [TOPIC] practically step-by-step using Python.

Teach me like a beginner who learns best by building systems instead of memorizing theory.

Structure the learning like this:

1. Introduce ONE concept at a time
2. Explain the real-world problem the concept solves
3. Give a small practical example/project
4. Explain the code line-by-line
5. Explain WHY things work
6. Show internal thinking/flow of the program
7. Give upgrade tasks after each exercise
8. Gradually increase difficulty
9. Use practical examples like:
   - games
   - APIs
   - banking systems
   - notification systems
   - backend systems
   - simulations
10. Avoid overcomplicated academic explanations
11. Focus heavily on intuition and practical understanding
12. Make me write code myself after showing examples
13. Ask me to intentionally break and improve the code
14. Explain common beginner confusions
15. Teach in a conversational and highly practical way

I want the exercises to feel like mini real-world systems instead of textbook problems.
```