### MyDiary-API

[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)




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
>$python3.6 -m venv virtual

>$source virtual/bin/activate

### Dependencies
- Install the project dependencies:
> $ pip install -r requirements.txt

You can run the tests by running:

>$```pytest```

After setting up the above. Run the application by:

>$```FLASK_APP=app flask run``

Test the endpoints registered  on Postman:

1.End point to get all entries

  ```https://diary-server.herokuapp.com/api/v1/entries/```

2.End point to get a single entry
 
 ``` https://diary-server.herokuapp.com/api/v1/entries/0```

3.End point to add an entry.

  ```https://diary-server.herokuapp.com/api/v1/entries/```

4.End point to update an entry.

  ```https://diary-server.herokuapp.com/api/v1/entries/2```

4.End point to delete an entry.

  ```https://diary-server.herokuapp.com/api/v1/entries/1```

### User interface

Please click on the link below to view the user interface design

  >```https://nduhiu17.github.io/MyDiary/```


### Licence

>```This application is licenced under GNU licence```


#### Author

Antony Nduhiu

