
# budget

a tool to track the budget in my project

## set up

```python
python3 -m venv budget-env
source budget-env/bin/activate
python3 -m pip install Django
mkdir projectmanagement
django-admin startproject budget projectmanagement
python3 manage.py runserver
cd projectmanagement 
python3 manage.py runserver

python3 manage.py migrate

python3 manage.py startapp vmb
````

