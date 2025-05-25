class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine() #composition

    def start(self):
        self.engine.start() #here we are using the engine class

if __name__ == "__main__":
    my_car = Car()
    my_car.start() # Output: Engine started