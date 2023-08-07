import math

class Teller():

    def __init__(self, speed, teller_id):
        self.available = True
        self.speed = speed
        self.teller_id = teller_id
        self.current_customer = None
        self.service_time_left = None
    
    def start_serving(self, customer):
        self.current_customer = customer
        self.available = False
        self.service_time_left = math.ceil(customer.service_time_need / self.speed)

    def serve(self):
        if self.current_customer:
            self.service_time_left -= 1
            if self.service_time_left <= 0:
                self.finish_serving()

    def finish_serving(self):
        self.current_customer = None
        self.available = True
        self.service_time_left = None
    
    def get_info(self):
        return f'Teller ID: {self.teller_id}, Available: {self.available}, Current Customer: {self.current_customer}, Speed: {self.speed}, Service Time Left: {self.service_time_left}'

