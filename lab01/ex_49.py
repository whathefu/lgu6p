class BankAccount :
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{owner}님의 계좌가 잔액 {balance}원으로 개설되었습니다.")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else :
            print("0보다 큰 금액을 입금해주세요.")

    def get_balance(self):
        print(f"계좌의 현재 잔액은 {self.balance}원입니다.")

    def withdraw(self,amount):
        if self.balance>= self.balance > 0 :
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else:
            print("출금 금액이 잔액을 초과하거나 잘못되었습니다.")
        
    def get_balance(self):
        print(f"계좌의 현재 잔액은 {self.balance}원 입니다.")

    def password(self,passwd):
        passwd = input("비밀번호를 입력하세요 :")
        if passwd == '1234' :
            print(f"비밀번호가 맞습니다 \n 계좌의 현재 잔액은 {self.balance}원 입니다.")
        else: 
            print("비밀번호가 틀렸습니다.")

    def remittance(self, amount, account):
        self.withdraw(amount)
        account.desposit(amount)



account1 = BankAccount("홍길동", 10000)
account1.deposit(5000)
account1.get_balance()

account1.withdraw(3000)
account1.get_balance()
account1.password(passwd=1234)

account2 = BankAccount("김길동", '0000', 1000000)
account2.get_balance()

account2.remittance(500000, account1)
account1.get_balance