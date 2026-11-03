# Create a class Sensor Reading to check machine temperature if machine is critical or not.
# Assign machine ID, recorded time and temperature to the object.
# Using if-else , Check if temperature is 80 or above.
# If yes, return True; otherwise, return False.
# Display if machine is critical or not.

class SensorReading:

    def is_critical(self):
        if self.temperature >= 80:
            return True
        else:
            return False

s1 = SensorReading()

s1.machine_id = "M1"
s1.recorded_at = "10:30"
s1.temperature = 85

print(s1.is_critical())