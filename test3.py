alphabet_numbers = {
    'a': [1, 2, 3, 4, 5],
    'b': [6, 7, 8, 9, 10],
    'c': [11, 12, 13, 14, 15]
}
x=int(input("Enter a number: "))
for key, value in alphabet_numbers.items():

    if x in value:
        print(f"{key}")

    '''
    items function returns a list of tuples, where each tuple contains a key-value pair from the dictionary.
    In this case, key will be the letter (e.g., 'a', 'b', 'c') 
    and value will be the corresponding list of numbers 
    (e.g., [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]).
              ^                 ^                       ^
              a                 b                       c             
    '''