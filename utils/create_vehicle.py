from types import coroutine
import requests

URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
}

def create_user(color, license_plate, v_type, owner_id):
    vehicle_data = SAMPLE_VEHICLE
    vehicle_data["color"] = color
    vehicle_data["license_plate"] = license_plate
    vehicle_data["v_type"] = v_type
    vehicle_data["owner_id"] = owner_id
    response = requests.post(URL, json=vehicle_data)
    if response.status_code == 204:
        print("Successfully created a new vehicle.")
    else:
        print("Something went wrong while trying to create a new vehicle.")

if __name__ == "__main__":
    color = input("Enter the vehicle color: ")
    license_plate = input("Enter the license plate: ")
    v_type = input("Enter the vehicle type: ")
    owner_id = input("Enter the owner's id: ")
    create_user(color, license_plate, v_type, owner_id)