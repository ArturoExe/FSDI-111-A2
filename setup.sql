
-- CREATES A USER DATABASE TABLE:

--table user
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

-- table type
CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64) 
   
);

--table vehicle
CREATE TABLE vehicle(
id INTEGER PRIMARY KEY AUTOINCREMENT,
color VARCHAR(45) NOT NULL,
license_plate VARCHAR(45) NOT NULL,
v_type INTEGER NOT NULL,
owner_id INTEGER NOT NULL,
active BOOLEAN DEFAULT 1,
FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
FOREIGN KEY (owner_id) REFERENCES user(id)

);

-- INSERT SOME DUMMY DATA:

INSERT INTO user(
    first_name,
    last_name,
    hobbies
)VALUES(
    "Arturo",
    "Martinez",
    "Video Games"
);

INSERT INTO user(
    first_name,
    last_name,
    hobbies
)VALUES(
    "Miguel",
    "Nunez",
    "Skate"
);

INSERT INTO user(
    first_name,
    last_name,
    hobbies
)VALUES(
    "Memo",
    "Pinkuski",
    "Listen to music"
);


--Dummy data vehicle

INSERT INTO vehicle_type (description) VALUES ("Truck");
INSERT INTO vehicle_type (description) VALUES ("Car");
INSERT INTO vehicle_type (description) VALUES ("SUV");
INSERT INTO vehicle_type (description) VALUES ("Motorcycle");



INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
)VALUES(
    "red",
    "HEll01",
    1,
    1
);


INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
)VALUES(
    "blue",
    "HEll02",
    2,
    2
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
)VALUES(
    "orange",
    "Hi03",
    3,
    3
);
