from bank_main import Bank
from bank_teller import Teller
from customer import Customer
import random

bank = Bank()
teller1 = Teller(speed=1, teller_id=1)
teller2 = Teller(speed=3, teller_id=2)
bank.add_tellers(teller1)
bank.add_tellers(teller2)

# Example of adding customers
for _ in range(5):  # let's say 5 customers
    customer = Customer(service_time_need=random.randint(1, 3))
    bank.add_customer(customer)

bank.run_simulation(days=1)
