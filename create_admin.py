import os
import django

# Set the environment to your project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# CHOOSE YOUR DETAILS HERE
username = 'tanvir14ahmed'
email = 'tanvir14ahmed@gmail.com'
password = 'Lifeis1*exam'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created successfully!")
else:
    print(f"User '{username}' already exists.")