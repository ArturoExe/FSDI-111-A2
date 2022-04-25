from flask  import Flask,request
from app.database import user,vehicle

from datetime import datetime

app=Flask(__name__)
VERSION = "1.0.0"


@app.get("/version")
def get_version():
    out = {
        "server-time":datetime.now().strftime("%F %H:%M:%S"),
        "version":VERSION
    }

    return out

@app.get("/users")
def get_all_users():
    user_list=user.scan()
    resp={
        "status":"ok",
        "message":"success",
        "user":user_list
    }
    return resp


@app.get("/users/<int:pk>/")
def get_user_by_id(pk):
    target_user=user.select_by_id(pk)
    resp={
        "status":"ok",
        "message":"success",
    }

    if target_user: #if target user is not empty
        resp["user"]=target_user
        return resp
    else:
        resp["status"]="error"
        resp["message"]="user not found"
        return resp,404


@app.post("/users/")
def create_user():

    user_data=request.json #request is Flask context object
    user.insert(user_data) #stores it into a dictionary
    return "",204 #no content status code but operation succesful

@app.put("/users/<int:pk>/") 
def update_user(pk):
    user_data=request.json 
    user.update(pk,user_data)
    return "",204

@app.delete("/users/<int:pk>/")
def deactivate_user(pk):
    user.deactivate(pk)
    return "",204


@app.post("/vehicles/")
def create_vehicle():
    vehicle_data = request.json
    vehicle.insert(vehicle_data)
    return "", 204

@app.get("/vehicles/")
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "users": vehicle_list
    }
    return resp

@app.get("/vehicles/<int:pk>")
def get_vehicle_by_id(pk):
    target_vehicle = vehicle.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
    }
    if target_vehicle:
        resp["user"] = target_vehicle
        return resp
    else:
        resp["status"] = "error"
        resp["message"] = "User not found"
        return resp, 404

@app.put("/vehicles/<int:pk>/")
def update_vehicle(pk):
    vehicle_data = request.json
    vehicle.update(pk, vehicle_data)
    return "", 204

@app.delete("/users/<int:pk>/")
def deactivate_vehicle(pk):
    vehicle.deactivate(pk)
    return "", 204