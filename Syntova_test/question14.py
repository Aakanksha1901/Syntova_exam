# first Created a FastAPI application.
# Take inputs for machine ID, recorded time and temperature in JSON forma.
# Check whether the given details are correct.
# If details are wrong, show an error message.
# Display a success message.

from fastapi import FastAPI

app = FastAPI()

@app.post("/reading")
def reading():

    machine_id = input("Enter machine ID: ")
    recorded_at = input("Enter recorded time: ")
    temperature = float(input("Enter temperature: "))

    if not machine_id or not recorded_at:
        return {"error": "Invalid input"}

    return {
        "message": "Reading received"
        }