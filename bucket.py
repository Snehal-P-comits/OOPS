class circle:
    def __init__(self, radius: float) -> None: 
        '''
            Annotations are used to indicate the expected types of the parameters and the return type of the function,
            they are not enforced by the Python interpreter but they can be used by developers and tools to understand the code better and catch potential errors. 
            In this case, we are indicating that the radius parameter is expected to be a float and that this function does not return anything, it's just meant to initialize the object.
            Note that we are not enforcing the type of the radius parameter,
            so if someone passes a different type (e.g., a string), it will not raise an error, 
            but it may cause issues later on when we try to use the radius as a float.
        '''
        #what does the -> None mean here?
        # it means that this function does not return anything, 
        # it's just a constructor that initializes the object, 
        # so it doesn't need to return anything, it's just creating the object and setting its properties, 
        # so it doesn't need to return anything, it's just a convention to indicate that this function is not meant to return anything, 
        # it's just meant to initialize the object.
        self.radius = radius
    
    def increase_size(self, amount: float) -> None:
        # Then why -> None is used here if the func is ment to modify something
        # eaxctly, it MODIFIES the object but dosen't RETURN anything
        self.radius += amount

    def decrease_size(self, amount: float) -> None:
        # same as above, it modifies the object but doesn't return anything
        self.radius -= amount

class square:
    def __init__(self, side_length: float) -> None:
        # same as the circle's __init__ class , it initializes the object but doesn't return anything
        self.side_length = side_length

class triangle:
    def __init__(self, base: float, height: float) -> None:
        # same as the circle's __init__ class , it initializes the object but doesn't return anything
        self.base = base
        self.height = height



class bucket:
    def __init__(self, capacity: int) -> None:
        # similar to the __init__ functions in the circle and square classes, it initializes the bucket object but doesn't return anything
        # default maximum capacity is 10 if not provided
        try:
            cap = int(capacity)
            if cap < 0:
                raise ValueError("Capacity cannot be negative")
        except (ValueError, TypeError):
            cap = 10
        self.capacity = cap
        self.contents: dict[str, int] = dict()  # Using a dictionary to store items and their counts so shapes can be the key and the value can be the count of that shape in the bucket

    def add(self, item: object) -> None:
        # we are using -> None here because this function is meant to modify the bucket's contents but not return anything, it's just meant to add an item to the bucket and update the contents accordingly, so it doesn't need to return anything, it's just a convention to indicate that this function is not meant to return anything, it's just meant to modify the bucket's contents.
        if len(self.contents) < self.capacity:
            '''
            if you do it in the following way your op will be somewahat like this:
            {<__main__.circle object at 0x0000017D8AAD1010>: 1, <__main__.circle object at 0x0000017D8AAD8F50>: 1}
            self.contents[item] = self.contents.get(item, 0) + 1
            what is happening here is that we added 2 circles to the bucket and the bucket is storing the circles but there are 2 issues:
            1. The circles are stored as objects and not as their properties, so we cannot easily access their properties like radius.
            2. the circles aren't being stored as the same item, they are being stored as 2 different items because they are different objects in memory, so we cannot easily count how many circles we have in the bucket.
            we cant make this function so specific to one shape because later on we'll be introducing more buckets with different properties by inheriting from this class
            so we need a general way to store the shapes in the bucket, we can do this by storing the shapes as their properties instead of their objects, for example we can store the circles as their radius and the squares as their side length, this way we can easily access their properties and count how many of each shape we have in the bucket.
            we cant even make it using a lot of if statements to check the type of the shape and store it accordingly because later on we'll be introducing more shapes with different properties, so we need a general way to store the shapes in the bucket, we can do this by storing the shapes as their properties instead of their objects, for example we can store the circles as their radius and the squares as their side length, this way we can easily access their properties and count how many of each shape we have in the bucket.
            so it should be written like this:

NICE
            '''
            self.contents[type(item).__name__] = self.contents.get(type(item).__name__, 0) + 1
        else:
            print("Bucket is full!")

    def remove(self, item: str) -> None:
        # we are using -> None here because this function is meant to modify the bucket's contents but not return anything, it's just meant to remove an item from the bucket and update the contents accordingly, so it doesn't need to return anything, it's just a convention to indicate that this function is not meant to return anything, it's just meant to modify the bucket's contents.
        if item in self.contents:
            self.contents[item] -= 1
            if self.contents[item] == 0:
                del self.contents[item]
        else:
            print("Item not found in bucket!")

    def show_contents(self) -> None:
        # we are using -> None here because this function is meant to print the contents of the bucket but not return anything, it's just meant to show the contents of the bucket, so it doesn't need to return anything, it's just a convention to indicate that this function is not meant to return anything, it's just meant to print the contents of the bucket.
        print(f"the bucket contains the following items: {self.contents}")


bucket1=bucket(100)
bucket1.add(circle(3))
bucket1.add(circle(4))

print(bucket1.capacity)
bucket1.show_contents()
