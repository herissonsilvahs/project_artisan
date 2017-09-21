import os
os.system("python manage.py makemigrations addresses accounts artisans categories artifacts comments")
os.system("python manage.py migrate")
# os.system("python3 manage.py runserver")