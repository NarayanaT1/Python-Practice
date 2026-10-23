# Class
class MotorBike:
    def __init__(self, speed):
        self.speed = speed  # State

    # Behavior
    def increase_speed(self, how_much):
        self.speed += how_much

    # Behavior
    def decrease_speed(self, how_much):
        if self.speed - how_much > 0:
            self.speed -= how_much
        else:
            print("Get a life")


# Instance 1 or Object 1
honda = MotorBike(50)

# Instance 2 or Object 2
ducati = MotorBike(250)

# State changes through object behavior
honda.increase_speed(150)
ducati.increase_speed(25)

honda.decrease_speed(50)
ducati.decrease_speed(25)

honda.decrease_speed(350)

print(honda.speed)
print(ducati.speed)