import random
import time

def main():
    random.seed(time.time())
    numbers = [1,2,3,4,5,6,7,8,9]
    for _ in range(100):
        print(random.sample(numbers, 2))

if __name__ == "__main__":
    main()