class Counter:
    count = 0

    def __init__(self):
        Counter.count +=1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

if __name__ == "__main__":
    # Creating instances of Counter
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()

    # Show the count of objects created
    Counter.show_count()  # Output: Total objects created: 3