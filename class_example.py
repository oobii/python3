class Duck3:

    # using keyword arguments
    # storing object data in the dictionary, a lot of flexibility
    def __init__(self, **kwargs):
        self.variables = kwargs

        print('contructor')

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)

    def quack(self):
        print('Quack!')

    def walk(self):
        print('Walks like a duck!')

# old , seed Duck3
class Duck2:

    # using key word arguments
    def __init__(self, **kwargs):
        # setting default color
        self._color = kwargs.get('color', 'white')
        print('contructor')

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def quack(self):
        print('Quack!')

    def walk(self):
        print('Walks like a duck!')

# old, see Duck3
class Duck:

    def __init__(self, color='white'):
        print('contructor')
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def quack(self):
        print('Quack!')

    def walk(self):
        print('Walks like a duck!')

# Code is here
def main():
    tim = Duck3(feet=2, color='blue')
    print('Tim', tim.get_variable('feet'))
    print('Tim', tim.get_variable('color'))

    tim.set_variable('color', 'orange')
    print('new Tim', tim.get_variable('feet'))
    print('new Tim', tim.get_variable('color'))



# old code
    fred = Duck2(color='blue')
    print("Fred the Duck with color", fred.get_color())

    # object donald is created and we call methonds on object donald
    # donald is the first argument to the methods
    donald = Duck()
    donald.quack()
    donald.walk()

    print(donald.get_color())
    donald.set_color('blue')
    print(donald.get_color())


if __name__ == '__main__':
    main()
