import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users/"

def deactivate_user(user_id):
    url = "%s/%s/" % (URL, user_id)
    response = requests.delete(url)
    if response.status_code == 204:
        print("Successfully deactivated user.")
    else:
        print("Something went wrong while trying to deactivate the user.")

def get_user(user_id):
    url = "%s/%s/" % (URL, user_id)
    response = requests.get(url)
    if response.status_code == 200:
        print("User: ")
        pprint(response.json())
        return response.json().get("user")[0]
    else:
        print("Something went wrong while trying to retrieve the user.")
        return ""

if __name__ == "__main__":
    user_id = input("Type in the user's id: ")
    deactivate = input("Would you like to deactivate the user? (y/n): ")
    if deactivate == "y" or deactivate == "Y":
        deactivate_user(user_id)
    else:
        print("User was not deactivated.")
    option = input("Would you like to see the updated user? (y/n): ")
    if option == "y" or option =="Y":
        get_user(user_id)