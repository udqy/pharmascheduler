# pharmascheduler
An ML based Django application for scheduling the production of pharmaceutical products in a factory

Setup:
```bash
python -m venv venv
source venv/bin/activate    # for windows: use venv\Scripts\activate
pip install -r requirements.txt
```

Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:
```bash
python manage.py createsuperuser
```


Start the development server:
```bash
python manage.py runserver
```
