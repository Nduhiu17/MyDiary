coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser

FLASK_APP=app FLASK_DEBUG=1 flask run

sudo kill $(sudo lsof -t -i:5000)

var2 = 'mice'

var = 2.5
a = f'INSERT INTO "public"."entries" (entryid, title, description, datecreated)VALUES(0, {var2}, {var}, {0});'

print(a)
