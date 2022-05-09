#Bank Account

class Bank_account:
  def __init__(self, new_account_number, starting_balance):
    self.account_number = new_account_number
    self.balance =starting_balance

  def deposit(self, deposit_amount):
    self.balance += deposit_amount

  def withdraw(self, withdraw_amount):
    if self.balance >= withdraw_amount:
      self.balance -= withdraw_amount

  def transfer_funds(self, other_account, amount):
    if self.balance >= amount :
      other_account.deposit(amount)
      self.withdraw(amount)



bobs_bank_account = Bank_account(1234, 0)
bobs_bank_account.deposit(500)
print(f"Bob now has: {bobs_bank_account.balance}")
bobs_bank_account.withdraw(500)
print(f"Bob now has: {bobs_bank_account.balance}")
bobs_bank_account.deposit(500)
print(f"Bob now has: {bobs_bank_account.balance}")

sams_bank_account = Bank_account(3234, 0)
sams_bank_account.deposit(300)
print(f"Sam now has: {sams_bank_account.balance}")

bobs_bank_account.transfer_funds(sams_bank_account, 100)
print(f"Bob now has: {bobs_bank_account.balance}")
print(f"Sam now has: {sams_bank_account.balance}")