# gpt-dm
Data modelling via natural language using an LLM. Outputs JSON or ANSI SQL. Also generates Test data, in ANSI SQL or CSV format.

## Design

Loosely based on [gpt-command](https://github.com/mrseanryan/gpt-command), using a sequence of 'expert' prompts.

Prompt Engineering is used to direct the LLM to select the best role for the user input, and then take a step by step approach to generating an answer.

Each prompt is an expert on one task, for example, creating JSON of a database schema, or generating test data in CSV format.

Within each prompt, instructions are given to avoid hallucinations or invalid formats or other unwanted output.

## Dependencies

Requires a LLM - by default, uses OpenAI's ChatGPT.

## Usage

To use as a CLI (Command Line Interface) REPL (Read-Eval-Print Loop) prompt:
```go.sh```

or to use as a web server:

```go_web.sh```

For the web server, you need to pass the user prompt as GET query parameter 'p'.

Example:

- http://localhost:8083/?p=I%20need%20a%20make%20a%20Car%20Parts%20application

So, another application can use the web server to send in natural language prompts from the user, and receive response in appropriate format (JSON or CSV or SQL).

The other application can then act on the given output.

## Commands

Commands with prompts are configured to suit your application.

Example - see [config__application_commander.py](config__application_commander.py).

### Example Output

```
Hello, I am an AI assistant. Here are my capabilities:
 -  creating a database schema for an application
 -  taking a database schema for an application and generating the SQL creation script
 -  taking a database SQL creation script and generating a test-data SQL insertion script
 -  taking a database SQL creation script and generating test-data in CSV format

What is the name of your application? >>My Car Parts
=== === === ===
>> My Car Parts
=== RESPONSE ===
What are the entities related to the "My Car Parts" application?
(To exit, just press ENTER) >Car, Wheel, Tyre        
=== === === ===
>> Car, Wheel, Tyre
=== RESPONSE ===
How are the entities Car, Wheel, and Tyre related to each other in the "My Car Parts" application?
(To exit, just press ENTER) >A car has four wheels. Each wheel has a tyre
=== === === ===
>> A car has four wheels. Each wheel has a tyre
=== RESPONSE ===
Based on the information provided, the entities Car, Wheel, and Tyre are related as follows:

- A Car has four Wheels.
- Each Wheel has one Tyre.

Here is the database schema for the "My Car Parts" application:

```json
{
  "application": "My Car Parts",
  "entity-names": ["Car", "Wheel", "Tyre"],
  "entity-attributes": {
    "Car": [],
    "Wheel": [],
    "Tyre": []
  },
  "entity-relationships": {
    "Car": {
      "Wheel": "one-to-many"
    },
    "Wheel": {
      "Tyre": "one-to-one"
    }
  }
}
```

Please note that the entity attributes are not specified in the provided information.
(To exit, just press ENTER) >Create some test data in SQL
=== === === ===
>> Create some test data in SQL
=== RESPONSE ===
Sure! Here's an example of how you can create test data in SQL for the "My Car Parts" application:

```sql
-- Create the Car table
CREATE TABLE Car (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);

-- Create the Wheel table
CREATE TABLE Wheel (
  id INT PRIMARY KEY,
  car_id INT,
  name VARCHAR(50),
  FOREIGN KEY (car_id) REFERENCES Car(id)
);

-- Create the Tyre table
CREATE TABLE Tyre (
  id INT PRIMARY KEY,
  wheel_id INT,
  name VARCHAR(50),
  FOREIGN KEY (wheel_id) REFERENCES Wheel(id)
);

-- Insert test data into the Car table
INSERT INTO Car (id, name) VALUES
  (1, 'Car 1'),
  (2, 'Car 2'),
  (3, 'Car 3');

-- Insert test data into the Wheel table
INSERT INTO Wheel (id, car_id, name) VALUES
  (1, 1, 'Wheel 1'),
  (2, 1, 'Wheel 2'),
  (3, 2, 'Wheel 3'),
  (4, 2, 'Wheel 4'),
  (5, 3, 'Wheel 5'),
  (6, 3, 'Wheel 6');

-- Insert test data into the Tyre table
INSERT INTO Tyre (id, wheel_id, name) VALUES
  (1, 1, 'Tyre 1'),
  (2, 2, 'Tyre 2'),
  (3, 3, 'Tyre 3'),
  (4, 4, 'Tyre 4'),
  (5, 5, 'Tyre 5'),
  (6, 6, 'Tyre 6');
```

This script creates the necessary tables (Car, Wheel, Tyre) and inserts test data into them. You can modify the test data as needed.
(To exit, just press ENTER) >Add suitable attributes to the entities
=== === === ===
>> Add suitable attributes to the entities
=== RESPONSE ===
Certainly! Here's an updated version of the SQL script with suitable attributes added to the entities:

```sql
-- Create the Car table
CREATE TABLE Car (
  id INT PRIMARY KEY,
  brand VARCHAR(50),
  model VARCHAR(50),
  year INT
);

-- Create the Wheel table
CREATE TABLE Wheel (
  id INT PRIMARY KEY,
  car_id INT,
  position VARCHAR(10),
  FOREIGN KEY (car_id) REFERENCES Car(id)
);

-- Create the Tyre table
CREATE TABLE Tyre (
  id INT PRIMARY KEY,
  wheel_id INT,
  brand VARCHAR(50),
  size VARCHAR(10),
  FOREIGN KEY (wheel_id) REFERENCES Wheel(id)
);

-- Insert test data into the Car table
INSERT INTO Car (id, brand, model, year) VALUES
  (1, 'Toyota', 'Corolla', 2020),
  (2, 'Honda', 'Civic', 2019),
  (3, 'Ford', 'Mustang', 2021);

-- Insert test data into the Wheel table
INSERT INTO Wheel (id, car_id, position) VALUES
  (1, 1, 'Front Left'),
  (2, 1, 'Front Right'),
  (3, 1, 'Rear Left'),
  (4, 1, 'Rear Right'),
  (5, 2, 'Front Left'),
  (6, 2, 'Front Right'),
  (7, 2, 'Rear Left'),
  (8, 2, 'Rear Right'),
  (9, 3, 'Front Left'),
  (10, 3, 'Front Right'),
  (11, 3, 'Rear Left'),
  (12, 3, 'Rear Right');

-- Insert test data into the Tyre table
INSERT INTO Tyre (id, wheel_id, brand, size) VALUES
  (1, 1, 'Michelin', '205/55R16'),
  (2, 2, 'Michelin', '205/55R16'),
  (3, 3, 'Michelin', '205/55R16'),
  (4, 4, 'Michelin', '205/55R16'),
  (5, 5, 'Bridgestone', '215/45R17'),
  (6, 6, 'Bridgestone', '215/45R17'),
  (7, 7, 'Bridgestone', '215/45R17'),
  (8, 8, 'Bridgestone', '215/45R17'),
  (9, 9, 'Goodyear', '235/50R18'),
  (10, 10, 'Goodyear', '235/50R18'),
  (11, 11, 'Goodyear', '235/50R18'),
  (12, 12, 'Goodyear', '235/50R18');
```

In this updated script, I added suitable attributes to each entity (Car, Wheel, Tyre) such as brand, model, year for Car, position for Wheel, and brand, size for Tyre. You can modify the attributes and test data as needed.
(To exit, just press ENTER) >Create the test data in CSV
=== === === ===
>> Create the test data in CSV
=== RESPONSE ===
Certainly! Here's an example of how you can create test data in CSV format for the "My Car Parts" application:

Car.csv:
```
id,brand,model,year
1,Toyota,Corolla,2020
2,Honda,Civic,2019
3,Ford,Mustang,2021
```

Wheel.csv:
```
id,car_id,position
1,1,Front Left
2,1,Front Right
3,1,Rear Left
4,1,Rear Right
5,2,Front Left
6,2,Front Right
7,2,Rear Left
8,2,Rear Right
9,3,Front Left
10,3,Front Right
11,3,Rear Left
12,3,Rear Right
```

Tyre.csv:
```
id,wheel_id,brand,size
1,1,Michelin,205/55R16
2,2,Michelin,205/55R16
3,3,Michelin,205/55R16
4,4,Michelin,205/55R16
5,5,Bridgestone,215/45R17
6,6,Bridgestone,215/45R17
7,7,Bridgestone,215/45R17
8,8,Bridgestone,215/45R17
9,9,Goodyear,235/50R18
10,10,Goodyear,235/50R18
11,11,Goodyear,235/50R18
12,12,Goodyear,235/50R18
```

You can save each of these CSV files with their respective names and use them to populate the tables in your database.
(To exit, just press ENTER) >Create the schema in JSON
=== === === ===
>> Create the schema in JSON
=== RESPONSE ===
Here is the database schema in JSON format for the "My Car Parts" application:

```json
{
  "application": "My Car Parts",
  "entity-names": ["Car", "Wheel", "Tyre"],
  "entity-attributes": {
    "Car": ["id", "brand", "model", "year"],
    "Wheel": ["id", "car_id", "position"],
    "Tyre": ["id", "wheel_id", "brand", "size"]
  },
  "entity-relationships": {
    "Car": {
      "Wheel": "one-to-many"
    },
    "Wheel": {
      "Tyre": "one-to-one"
    }
  }
}
```

In this schema, each entity (Car, Wheel, Tyre) is defined with its corresponding attributes. The entity relationships are also specified, indicating that a Car has a one-to-many relationship with Wheel, and Wheel has a one-to-one relationship with Tyre.
```

# Unrecognised user prompts

User prompts that are not related to any of the known Commands, are sent directly to the LLM.

Examples:

```
>> Who won the battle of Agincourt, and why was it fought?
{"general_response": " The battle of Agincourt was fought in 1415 during the Hundred Years' War between the English and French. The English army, led by King Henry V, was victorious in the battle. The French army was significantly larger, but the English were able to win thanks to their superior tactics. "}
```

```
>> What is my favourite color?
{"general_response": " I'm sorry, I don't know. "}
```

## Set up

```
pip3 install --upgrade openai
```

Set environment variable with your OpenAI key:

```
export OPENAI_API_KEY="xxx"
```

Add that to your shell initializing script (`~/.zprofile` or similar)

Load in current terminal:

```
source ~/.zprofile
```

## Test

`test.sh`

or

`python3 test.py`
