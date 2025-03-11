
# budget

a tool to track the budget in my projects

In a first step every project is defined with a budget.

In a second step all the "Expenditure Items" are being imported from Oracle and imported to a local database.

Then a consolidated view can be generated, that shows all expenditures that occurred by project. and in addition how much is left from the budget.

## backlog

- [ ] create a burndown, based on the project runtime, the occured cost and the budget

## set up the development environment

```python

# create an environment
python3 -m venv budget-env
source budget-env/bin/activate


mkdir projectmanagement
django-admin startproject budget projectmanagement
python3 manage.py runserver
cd projectmanagement 
python3 manage.py runserver

python3 manage.py migrate

python3 manage.py startapp vmb

python3 manage.py makemigrations vmb
````

```python
# setting up env
python3 -m venv budget-env
source ../../../virtualenv/budget-env/bin/activate
pip3 install -r ../requirements.txt
````

