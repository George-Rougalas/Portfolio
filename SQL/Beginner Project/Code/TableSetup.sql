DROP TABLE Positions;
DROP TABLE Vessels;
DROP TABLE VesselTypes;

CREATE TABLE VesselTypes
	(code		NUMERIC(3,0),
	description VARCHAR(60),
	primary key (code)
	);

CREATE TABLE Vessels 
	(id		VARCHAR(100),
	 type	NUMERIC(3,0),
	 flag	VARCHAR(32),
	 primary key (id),
	 foreign key (type) references VesselTypes(code)
	);

CREATE TABLE Positions
	(id		NUMERIC(15,0),
	vessel_id	VARCHAR(100),
	t		TIMESTAMP,
	lon		NUMERIC(10,8) not null,
	lat		NUMERIC(10,8) not null,
	heading	NUMERIC(4,0),
	course	NUMERIC(5,1),
	speed	NUMERIC(5,1),
	primary key (id),
 	foreign key (vessel_id) references Vessels(id)
	);
