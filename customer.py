import random

class Customer():
    def __init__(self, customer_id, service_time_need):
        self.customer_id = customer_id
        self.service_time_need = service_time_need
        self.arrival_time = self.set_arrival_time()
        self.waiting_time = 0

    def set_arrival_time(self):
        opening_time = 9 * 60
        closing_time = 17 * 60
        return random.randint(opening_time, closing_time)

    def set_waiting_time(self, current_time):
        self.waiting_time = max(current_time - self.arrival_time, 0)

print(Customer)