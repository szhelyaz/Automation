# Automation

## 1. What are the benefits of using Python language as a language, what are it's drawbacks?

- Pros: Python is a popular programming language that offers many benefits: ease of use, readability, and a large community of developers.
- Cons: It also has some limitations, such as slower performance compared to compiled languages, memory management issues, dynamic typing, and version compatibility.

## 2. What is the difference between a Tuple and List in Python?

The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified.
- Tuples are more memory efficient than the lists.
- When it comes to the time efficiency, tuples have a slight advantage over the lists especially when we consider lookup value.
- If you have data that shouldn’t change, you should choose tuple data type over lists.

## 3. Is Indentation Required in Python?

Yes, Python relies on indentation to define the structure of code blocks, making it unique among programming languages. 

   ### Rules of Indentation in Python: 

- Python’s default indentation spaces are four spaces. The number of spaces, however, is entirely up to the user. A minimum of one space is required to indent         a statement.
- Indentation is not permitted on the first line of Python code.
- Python requires indentation to define statement blocks.
- A block of code must have a consistent number of spaces.
To indent in Python, whitespaces are preferred over tabs. Also, use either whitespace or tabs to indent; mixing tabs and whitespaces in indentation can result in incorrect indentation errors.

## 4. Difference between for loop and while loop in Python.

| | For loop  |  While loop  |   
|---|---|---|
|1|For loop is used to iterate over a sequence of items.   | While loop is used to repeatedly execute a block of statements while a condition is true.  |  
| 2| For loops are designed for iterating over a sequence of items. Eg. list, tuple, etc. | While loop is used when the number of iterations is not known in advance or when we want to repeat a block of code until a certain condition is met.  |   
|3|For loop require a sequence to iterate over.|While the loop requires an initial condition that is tested at the beginning of the loop.|
|4|For loop is typically used for iterating over a fixed sequence of items |While loop is used for more complex control flow situations.|

## 5. What is List Comprehension, why do we need it and is it faster than a loop for list creation? Give an Example. 

List comprehension is an easy to read, compact, and elegant way of creating a list from any existing iterable object. 
Basically, it's a simpler way to create a new list from the values in a list you already have.

It is generally a single line of code enclosed in square brackets. You can use it to filter, format, modify, or do other small tasks on existing iterables such as strings, tuples, sets, dataframes, array lists, and so on.

But you should avoid using list comprehension if you have too many conditions to add for filtering or modifying as it will make your code more complex and harder to read.


  ```
# Filter a list with a "for loop"
MILLION_NUMBERS = list(range(1_000_000))
def for_loop():
    output = []
    for element in MILLION_NUMBERS:
        if not element % 2:
            output.append(element)
    return output'
    ```

  ```
   ```
# Filter a list a list with list comprehension

MILLION_NUMBERS = list(range(1_000_000))

def list_comprehension():
    return [number for number in MILLION_NUMBERS if not number % 2]

   ```
## 6. What are unit tests in Python?
Unit testing is a crucial aspect of software development that involves testing individual units or components of code to ensure their proper functioning. It aims to validate that each unit, such as a function or method, works as intended and produces the expected output.
Python, being a popular programming language, offers several frameworks and tools to facilitate unit testing. The Python unit testing process typically follows a set of steps. 
- First, developers write test cases to  validate the behavior of a unit. Test cases often cover both routine and edge cases to ensure robustness. 
- Next, developers utilize a unit testing framework, such as PyTest, unittest, or doctest, to organize and execute these test cases.
- The framework provides essential features like assertion methods to check the expected output against the actual output.
## 7. What is the difference between a shallow copy and a deep copy?
Assignment statements in Python do not copy objects, they create bindings between a target and an object. For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. This module provides generic shallow and deep copy operations (explained below).
Interface summary:
*copy.**copy**(x)*
<br>Return a shallow copy of x.
*copy.**deepcopy**(x[, memo])*
<br>Return a deep copy of x.
*exception copy.**Error***
<br>Raised for module specific errors.
The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
- A **shallow copy** constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A **deep copy** constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
## 8. What are Decorators?
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 
## 9. When a parameter is passed to a function, is it by value (copy) or reference (pointer) ?
If a pointer is passed to a function as a parameter and tried to be modified then the changes made to the pointer does not reflects back outside that function. This is because only a copy of the pointer is passed to the function. 
<br>It can be said that “pass by pointer” is passing a pointer by value. In most cases, this does not present a problem. 
<br>The problem comes when you modify the pointer inside the function. Instead of modifying the variable, you are only modifying a copy of the pointer and the original pointer remains unmodified.
## 10. Does Python support multiple Inheritance (OOP)?
**YES** 
<br>Inheritance is a required feature of every object-oriented programming language.
<br>This means that Python supports inheritance. 
<br>It’s one of the few languages that supports multiple inheritance.
