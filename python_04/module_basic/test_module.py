PI = 3.14159226535

def number_input():
    output = input("숫자 입력 : ")

    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_cir_circle_area(radius):
    return PI * radius ** 2

class Rectangle:
    """ this os Rectangle class, initial args is two """

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

def main():
    print("test_module.py 의 __name__")
    print(__name__)

if __name__ == "__main__":
    main()