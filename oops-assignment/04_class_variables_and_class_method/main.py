class Bank:
    # Class variable
    bank_name = "Ahad Bank"

    # Class method
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

if __name__ == "__main__":
   user1 = Bank()
   user2 = Bank()

   print("Before changing the bank name:")
   print(f"User 1 Bank Name: {user1.bank_name}")
   print(f"User 2 Bank Name: {user2.bank_name}")

   Bank.change_bank_name("Aiza Bank")
   print("\nAfter changing the bank name:")
   print(f"User 1 Bank Name: {user1.bank_name}")
   print(f"User 2 Bank Name: {user2.bank_name}")
   