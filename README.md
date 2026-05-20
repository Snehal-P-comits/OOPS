# OOPS Examples

This folder contains simple Python examples for object-oriented programming (OOP) and a couple of small practice scripts.

## What is happening here

These files show basic OOP ideas in Python:

- `ex1.py`: A `Character` class with `name`, `health`, and `attack_power`. It shows how to make an object, call methods like `attack`, and print the character stats.
- `ex2.py`: A `BankAccount` class that uses a private balance (`__balance`). It shows encapsulation by using methods like `get_balance`, `deposit`, `withdraw`, and `transfer` instead of touching internal data directly.
- `ex3.py`: Inheritance and subclass behavior. A `Character` parent class is extended by `Knight`, `Wizard`, and `Witch`. It shows how child classes reuse parent code, add new features, and override methods.
- `ex4.py`: Polymorphism and duck typing. `Knight`, `Wizard`, and `Archer` all inherit from `Character`, but each has its own `attack` and `speak` behavior. The code runs them in a loop to demonstrate that they can be treated the same way while acting differently.
- `ex5.py`: Abstract classes using `ABC` and `@abstractmethod`. It defines a `PaymentMethod` interface and two concrete implementations: `CreditCardPayment` and `UPIPayment`.

## Other example scripts

- `test.py`: A simple test that finds a unique number in a list using XOR. The comments compare a slow O(n²) approach with the faster O(n) solution.
- `test2.py`: A tiny class inheritance example showing how `B` extends `A` and how the constructor works with `super()`.
- `test3.py`: A small dictionary lookup example that maps a number input to a letter key in `alphabet_numbers`.

## How to use

Run any file with Python, for example:

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