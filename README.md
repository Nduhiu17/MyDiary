### MyDiary-API
[![Coverage Status](https://coveralls.io/repos/github/Nduhiu17/MyDiary/badge.svg?branch=master)](https://coveralls.io/github/Nduhiu17/MyDiary?branch=master)


[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)


#### Description
It is an API that enables CRUD methods for creating a Diary entry where users can can pen dwn their feelings
### Development

Clone the repository: 

```https://github.com/Nduhiu17/MyDiary.git```

Check out to the server branch by:
$git checkout develop

Ensure you have the following:

```
1. postgres
2. python3.6
3. Flask
4. Postman
```

Create a virtualenv and activate it by running the following commands.
$python3.6 -m venv virtual
$source virtual/bin/activate

### Dependencies
- Install the project dependencies:
> $ pip install -r requirements.txt

You can run the tests by running:

$```pytest```

After setting up the above. Run:

```python api.py.py```

Test the endpoints registered on `api.py` on Postman:

1.End point to get all entries

  ```https://diary-server.herokuapp.com/api/v1/entries/```

2.End point to get a single entry
 
 ``` https://diary-server.herokuapp.com/api/v1/entries/0```

3.End point to add an entry.

  ```https://diary-server.herokuapp.com/api/v1/entries/```
#### Author

Antony Nduhiu

