CREATE TABLE POSITION (
    ID SERIAL PRIMARY KEY,
    TITLE VARCHAR(255),
    COMPANY VARCHAR(100),
    SALARY MONEY, --report the lower end of the salary range
    JOB_CITY VARCHAR(50),
    JOB_STATE CHAR(2),
    JOB_TYPE VARCHAR(50) CHECK (JOB_TYPE IN ('In Person', 'Remote', 'Hybrid')), -- In person, Remote, Hybrid
    APPLIED_ON DATE,
    STATUS VARCHAR(50) DEFAULT 'Applied'
);


SELECT * FROM POSITION;