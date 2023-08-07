from collections import deque
from bank_teller import Teller
from customer import Customer
import random

class Bank():
    def __init__(self):
        self.tellers = []
        self.customers = deque()
        self.opening_time = 9
        self.closing_time = 17
        self.current_time = self.opening_time
        self.total_customers_served = 0

    def add_tellers(self, teller):
        self.tellers.append(teller)

    def add_customer(self, customer):
        if self.opening_time <= self.current_time < self.closing_time:
            self.customers.appendleft(customer)
            for teller in self.tellers:
                if teller.available:
                    teller.start_serving(customer)
                    break
            print(f"Customer {customer.customer_id} has entered the bank.")
        else:
            print("Bank is currently closed.")

    def serve_customer(self):
        for teller in self.tellers:
            if not teller.available:
                teller.serve()
                if teller.available and self.customers:
                    new_customer = self.customers.popleft()
                    self.total_customers_served += 1
                    teller.start_serving(new_customer)

    def end_of_day_operations(self):
        self.current_time = self.opening_time
        for teller in self.tellers:
            teller.current_customer = None
            teller.service_time_left = None
            teller.available = True
        self.customers.clear()
        print(self.total_customers_served)

    def advance_time(self, minutes=1): 
        self.current_time += minutes/60
        if self.current_time >= self.closing_time:
            self.end_of_day_operations()

    def maybe_add_customer(self):
        if random.random() < 0.1: 
            service_time_need = random.randint(5, 60)  
            customer = Customer(id(self.customers), service_time_need)
            self.add_customer(customer)

    def generate_report(self):
        print("End of Day Report")
        print(f"Total Customers Served: {self.total_customers_served}")

    def run_simulation(self, days=1):
        for _ in range(days):
            while self.opening_time <= self.current_time < self.closing_time:
                self.maybe_add_customer()
                self.serve_customer()
                self.advance_time(5)
            self.generate_report()
            self.end_of_day_operations()
