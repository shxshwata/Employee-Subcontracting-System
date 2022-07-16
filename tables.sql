mysql> create table MainTable
-> (UID varchar(10) NOT NULL PRIMARY KEY, -> EmpName varchar(70) NOT NULL,
-> EmpAge integer,
-> EmpPost varchar(70),
-> EmpLocation varchar(70),
-> EmpSalary integer);
mysql> create table Applicants
-> (UID varchar(10) NOT NULL PRIMARY KEY, -> AppName varchar(70) NOT NULL,
-> AppAge integer,
-> AppLocation varchar(70), -> AppExpSalary integer);
mysql> create table Status
-> (UID varchar(10) NOT NULL PRIMARY KEY, -> EmpStatus varchar(70) NOT NULL);
