# Generating training data, to train the db-schema-bot README

## Approach

Create a small test dataset in CSV format, via Chat-GPT3.5 Turbo (why: power + speed + low effort)

- Description, Table (name), JSON

Ideally, about 20 million rows?
Initially less - say 10,000 rows.

## Example Output

```
./test.sh
```

```
>> Create training data with 10 tables
{
  "tables": [
    {
      "table-name": "Customers",
      "fields": [
        {
          "id": "Id",
          "type": "int"
        },
        {
          "id": "Name",
          "type": "string"
        },
        {
          "id": "Email",
          "type": "string"
        },
        {
          "id": "Phone",
          "type": "string"
        }
      ],
      "sql": "CREATE TABLE Customers (\n  Id INT PRIMARY KEY,\n  Name VARCHAR(50),\n  Email VARCHAR(100),\n  Phone VARCHAR(20)\n);",
      "test-data-csv": "Customers.csv:\nId,Name,Email,Phone\n1,John Doe,johndoe@example.com,1234567890\n2,Jane Smith,janesmith@example.com,9876543210\n"
    },
```

## Reference

[gpt-dm via Chat-GPT](../../../README.md)
