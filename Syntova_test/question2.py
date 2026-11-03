#  CREATE empty list inactive_machines
inactive_machines = []

# To identify machines that have not sent a reading in the last five minutes 
#  1st need to get the current time and subtract five minutes.
#  Get the current time.
#  Set 
threshold = current time - 5 minutes.
for each machine:

# Give conditin to Check its readings , to ignore missing or invalid timestamps and remove duplicate readings.
# Then , Find the latest reading time.

if no valid reading is found:
          inactive_machines.append(machine_id)

elif latest reading time < threshold:
          inactive_machines.append(machine_id)

else:
        print("Mark machine as active.")

# Display the list of inactive machines.
print(inactive_machines)
