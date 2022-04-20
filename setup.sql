
-- CREATES A USER DATABASE TABLE:

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
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