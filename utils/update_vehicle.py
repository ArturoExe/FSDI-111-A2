import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/vehicles/"

def update_user(vehicle_data, vehicle_id):
    url = "%s/%s/" % (URL, vehicle_id)
    response = requests.put(url, json=vehicle_data)
    if response.status.code == 204:
        print("Successfully updated user.")
    else:
        print("Something went wrong while trying to update user.")

def get_user(vehicle_id):
    url = "%s/%s/" % (URL, vehicle_id)
    response = requests.get(url)
    if response.status_code == 200:
        print("Vehicle: ")
        pprint(response.json())
        return response.json().get("vehicle")[0]
    else:
        print("Something went wrong while trying to retrieve the vehicle.")
        return ""

if __name__ == "__main__":
    vehicle_id = input("Type in the vehicle's id: ")
    target_vehicle = get_user(int(vehicle_id))
    color = input("Type in a new color (or leave blank): ")
    license_plate = input("Type in a new license plate (or leave blank): ")

    if first_name:
        target_user["first_name"] = first_name
    if last_name:
        target_user["last_name"] = last_name
    if hobbies:
        target_user["hobbies"] = hobbies
    update_user(target_user)
    option = input("Would you like to see the updated user? (y/n): ")
    if option == "y" or option =="Y":
        get_user(user_id)