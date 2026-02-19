CREATE TABLE assets(id SERIAL PRIMARY KEY,target TEXT);
CREATE TABLE vulnerabilities(id SERIAL PRIMARY KEY,asset INT,severity TEXT);
CREATE TABLE credentials(id SERIAL PRIMARY KEY,username TEXT,password TEXT);
