import random


class car:
	def __init__(self, model, color):
		self.fuel = random.randrange(0, 9)
		self.trip_distance = 0
		self.model = model
		self.color = color

	def move(self, distance):
		if self.fuel > distance:
			self.fuel -= distance
			self.trip_distance += distance
		else:
			self.trip_distance += self.fuel
			self.fuel = 0


car1 = car('Subaru', 'Red')
car2 = car('Acura', 'White')
car3 = car('Honda', 'Yellow')

race_dist, desired_dist = 0, 3

while race_dist < desired_dist:
	if car1.fuel == 0 and car2.fuel == 0 and car3.fuel == 0:
		break
	car1.move(random.randrange(0, 9))
	if car1.trip_distance >= desired_dist:
		print(f"Переміг автомобіль {car1.model}, проїхавший {car1.trip_distance} км")
		break
	car2.move(random.randrange(0, 9))
	if car2.trip_distance >= desired_dist:
		print(f"Переміг автомобіль {car2.model}, проїхавший {car2.trip_distance} км")
		break
	car3.move(random.randrange(0, 9))
	if car3.trip_distance >= desired_dist:
		print(f"Переміг автомобіль {car3.model}, проїхавший {car3.trip_distance} км")
		break

print(f"Перший автомобіль: Пройшов {car1.trip_distance} км, залишок палива {car1.fuel}")
print(f"Другий автомобіль: Пройшов {car2.trip_distance} км, залишок палива {car2.fuel}")
print(f"Третій автомобіль: Пройшов {car3.trip_distance} км, залишок палива {car3.fuel}")