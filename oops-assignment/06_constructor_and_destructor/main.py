class Logger:
    def __init__(self):
        print("Logger initialized") #Constructor
    
    def __del__(self):
        print("Logger destroyed") #Destructor

if __name__ == "__main__":
    log = Logger()
    del log