class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public
        self._salary = salary  # protected
        self.__ssn = ssn  # private

if __name__ == "__main__":
    emp = Employee("Asad", 50000, "123-45-6789")
    print("Public Variable:", emp.name)  # Accessing public variable
    print("Protected Variable:", emp._salary)  # Accessing protected variable
    try:
        print("Private Variable:", emp.__ssn)  # This will raise an AttributeError
    except AttributeError:
        print("Cannot access private variable __ssn.")
