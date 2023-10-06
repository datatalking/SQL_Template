# SQL_Template
My starting point for new projects dealing with data, pandas needs "Highspeed Intuitive Features"
Pandas has many great features but I keep having to re-build most of the same tools for each job.

Pandas needs an upgrade
1. A datatype 'detection' function so it can operate more independently
2. A tool for importing, extraction, transform and loading of now cleaned data to a database
3. A database selection function
4. A long term memory pulling from github


## FEATURES
I took inspiration from Guido Van Rossum's approach to python, Joel Grus approach to jupyter notebooks, the 12 
factor app and Joel Splonsky.

1. Begin with the end in mind so start with a template
2. Establish your .env variables
3. Create .gitignore file
4. Add your name
5. What is your preference for the database
6. Where are we accessing data from
5. Do which statistical tests
6. Enable feature selection for ML training
7. What else?



## ERRATA
There will be bugs we will save those to sqlite db saved on the repo
1. `PG_fetch.py` compare_methods_to_insert_bulk_data gives error 'AttributeError: module 'cursor' has no attribute 'execute''
2. `my_lite_store.db` is duplicated in code and belongs in /data



## CONTRIBUTORS
PR are accepted
1. Complete the GitHub workflows
2. Label 3 bugs and fix one
3. Suggest 3 features and submit on PR



## Future Features
Not in paticular order
1. .env loaded from # TODO https://pypi.org/project/python-dotenv/
2. .gitignore setup for the repo
3. data_dirty/ PATH setup from .env
4. data_dirty/ added somehow to .bash_profile
5. postgresql database setup via #TODO https://medium.com/analytics-vidhya/part-4-pandas-dataframe-to-postgresql-using-python-8ffdb0323c09
6. maybe do pandas logging # TODO https://towardsdatascience.com/introducing-pandas-log-3240a5e57e21
7. 

