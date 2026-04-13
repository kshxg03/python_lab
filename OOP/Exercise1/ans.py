

class Car:
    def __init__(self, brand, model, color="blue"):
        self.brand = brand
        self.model = model
        self.color = color
    
    def display_info(self):
        return f"Brand: {self.brand}, model: {self.model}, color: {self.color}."

    def start_engine(self):
        return f"Engine of {self.brand} {self.model} started."
    
    def stop_engine(self):
        return f"Engine of {self.brand} {self.model} stopped."
    
car_1 = Car("toyota", "corolla", "red")
car_2 = Car("honda", "civic")

print(car_1.display_info())
print(car_2.display_info())
print(car_1.start_engine())
print(car_1.stop_engine())
print(car_2.start_engine())
print(car_2.stop_engine())