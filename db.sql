use sewing_patterns;

create table users (
    userID INTEGER AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(320),
    password VARCHAR (255),
    PRIMARY KEY (personID)
);


create table patterns (
    patternID VARCHAR(100),
    brand VARCHAR(100),
    category  ENUM ('Coat', 'Coordinates', 'Dress', 'Jacket', 'Shirt', 'Skirt', 'Sleepwear', 'Trousers', 'Top'),
    fabric_type ENUM ('Woven', 'Stretch', 'All'),
    description VARCHAR(255),
    ownerID INTEGER,
    PRIMARY KEY patternID,
    FOREIGN KEY ownerID REFERENCES users (userID)
    );


create table borrow_logs (
    loanID INTEGER AUTO_INCREMENT,
    borrow_date DATE,
    borrowerID INTEGER,
    patternID VARCHAR(100),
    PRIMARY KEY loanID,
    FOREIGN KEY borrowerID REFERENCES users (userID),
    FOREIGN KEY patternID REFERENCES patterns (patternID)
);
