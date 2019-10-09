
CREATE TABLE Business (
	busID VARCHAR(500),
	name VARCHAR(500),
	address VARCHAR(500),
	city VARCHAR(500),
	state VARCHAR(500),
	latitude VARCHAR(500),
	longitude VARCHAR(500),
	zipcode INT,
	numCheckins INT,
	stars INT,
	numReviews INT,
	avgRating FLOAT, 
	isOpen INT,
	PRIMARY KEY (busID)
);

CREATE TABLE YelpUser (
	userID VARCHAR(50) NOT NULL,
	name VARCHAR(50),
	avgStar INT,
	userSince VARCHAR(50),
	fans INT,
	cool INT, 
	funny INT, 
	useful INT,
	review_count INT,
	latitude VARCHAR(50),
	longitude VARCHAR(50),
	PRIMARY KEY (userID)
);

CREATE TABLE Review (
	reviewID VARCHAR(500) NOT NULL,
    userID VARCHAR(500) NOT NULL,
    busID VARCHAR(500) NOT NULL,
	date VARCHAR(500),
	stars INT,
	text VARCHAR(10000),
	useful INT,
	funny INT,
	cool INT, 
	PRIMARY KEY (reviewID)
);

CREATE TABLE Hours (
	busID VARCHAR(50),
	day VARCHAR(10),
	openclose VARCHAR(50),
	PRIMARY KEY (busID, day, openclose),
	FOREIGN KEY (busID) REFERENCES Business(busID)
);

CREATE TABLE Category (
	busID VARCHAR(50),
	category_name VARCHAR(50) NOT NULL,
	PRIMARY KEY (busID, category_name),
	FOREIGN KEY (busID) REFERENCES Business(busID)
);

CREATE TABLE Attribute (
	busID VARCHAR(50),
	attribute_name VARCHAR(50) NOT NULL,
	value VARCHAR(50),
	PRIMARY KEY (busID, attribute_name),
	FOREIGN KEY (busID) REFERENCES Business(busID)
);

CREATE TABLE CheckIn (
	busID VARCHAR(50),
	day VARCHAR(10),
	hour VARCHAR(5),
	numCheck INT,
	PRIMARY KEY (day, hour, busID),
	FOREIGN KEY (busID) REFERENCES Business(busID)
);

