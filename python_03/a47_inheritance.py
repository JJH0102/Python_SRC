class Parent:
    def __init__(self):
        self.value = "Parent 테스트"
        print("Parent 클래스의 __init__() 메소드가 호출됨")

    def test(self, *args, **kwarg):
        print("Parent 클래스의 test() 메소드입니다.", *args)

class Child(Parent):
    def __init__(self):
        # Parent.__init__(self)
        super().__init__()
        print("Child 클래스의 __init__() 메소드가 호출됨")

    def test(self, *args, **kwarg):
        super().test(*args, **kwarg)
        print("Child 클래스의 test() 메소드입니다.")

def main():
    child = Child()
    child.test("a", "b", "c")

    print(child.value)

if __name__ == "__main__":
    main()