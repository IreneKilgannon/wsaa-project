use sewing_patterns;

create table users (
    userID INTEGER AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(320) NOT NULL,
    password VARCHAR (255),
    PRIMARY KEY (userID)
);


create table patterns (
    patternID VARCHAR(100),
    brand VARCHAR(100) NOT NULL,
    category  ENUM ('Coat', 'Coordinates', 'Dress', 'Jacket', 'Shirt', 'Skirt', 'Sleepwear', 'Trousers', 'Top') NOT NULL,
    fabric_type ENUM ('Woven', 'Stretch', 'All') NOT NULL,
    description VARCHAR(255),
    format ENUM ('Paper', 'PDF')
    ownerID INTEGER NOT NULL,
    PRIMARY KEY (patternID),
    FOREIGN KEY (ownerID) REFERENCES users (userID)
    );


create table borrow_logs (
    loanID INTEGER AUTO_INCREMENT,
    borrow_date DATE NOT NULL,
    borrowerID INTEGER NOT NULL,
    patternID VARCHAR(100) NOT NULL,
    PRIMARY KEY (loanID),
    FOREIGN KEY (borrowerID) REFERENCES users (userID),
    FOREIGN KEY (patternID) REFERENCES patterns (patternID)
);
