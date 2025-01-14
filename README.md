# Bhive Assignment

This assignment as per the provided problem statement, fetches realtime fund schemes, allows user to create portfolio with JWT Authentication. Tech is Python, Django, Sqlite & Celery, redis

Postman collection & api documentation: https://www.postman.com/iambhushan/bhive-assignment-bhushan-lokhande/collection/m3y8fdq/bhive-assignment-bhushan-lokhande?action=share&creator=29746355

Step 1:
Clone the repository

Step 2:
Create a virtual environment and run the following command

```
pip install -r requirements.txt
```

Step 3:
Run following commands

```
python manage.py makemigraions
python manage.py migrate
```

Step 4:
Enter your Rapid api secret key in .env file

```
RAPID_API_SECRET_KEY={SECRET-KEY}
```

Step 5:
Run the following command

```
python manage.py runserver
```

Now Test below apis as per sequence provided with Postman Collection:

```
'bhive/test', 
'bhive/register', 
'bhive/login', 
'bhive/fundhouses', 
'bhive/fundhouse-schemes',
'bhive/portfolio/create'
'bhive/portfolio/list',
```

Use `scheme_name` & `scheme_code` from `bhive/fund-schemes` apis to create portfolio in `bhive/portfolio/create`
A dummy celery task is written to show how hourly update of portfolios value can be done.

Thank You!
