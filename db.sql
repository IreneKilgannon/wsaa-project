use sewing_patterns;

create table users (
    userID INTEGER AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
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
    userID INTEGER NOT NULL,
    PRIMARY KEY (patternID),
    FOREIGN KEY (userID) REFERENCES users (userID)
    ON DELETE cascade
    ON UPDATE
    );


create table fabrics (
    fabricID INTEGER AUTO_INCREMENT,
    image VARCHAR(250) NOT NULL,
    pattern VARCHAR(100) NOT NULL,
    category ENUM ('Woven', 'Knit', 'All') NOT NULL,
    type VARCHAR(100) NOT NULL,
    colour VARCHAR(50) NOT NULL,
    use ENUM('Dress', 'Quilting', 'Furnishing') NOT NULL,
    amount DECIMAL(5,2) NOT NULL,
    other_details VARCHAR(255),
    PRIMARY KEY (fabricID),
);

create table borrow_requests (
    loanID INTEGER AUTO_INCREMENT,
    userID INTEGER NOT NULL,
    patternID VARCHAR(100) NOT NULL,
    PRIMARY KEY (loanID),
    FOREIGN KEY (userID) REFERENCES users (userID),
    FOREIGN KEY (patternID) REFERENCES patterns (patternID)
);
