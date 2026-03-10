import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
try:
    django.setup()
    print("✅ Django Setup: OK")
except Exception as e:
    print(f"❌ Django Setup Failed: {e}")
    sys.exit(1)

from django.urls import resolve, reverse
from django.db import connection
from main.models import BlogPost

print("\n--- Database Check ---")
try:
    db_name = connection.settings_dict['NAME']
    print(f"Database Path: {db_name}")
    if os.path.exists(db_name):
        print(f"✅ Database File Found. Permissions: {oct(os.stat(db_name).st_mode)[-3:]}")
    else:
        print("❌ Database File NOT FOUND!")
    
    post_count = BlogPost.objects.count()
    print(f"✅ BlogPost Table: OK (Found {post_count} posts)")
except Exception as e:
    print(f"❌ Database Error: {e}")

print("\n--- URL Resolution Check ---")
urls_to_check = [
    ('/', 'main:index'),
    ('/blog/', 'main:blog_list'),
    ('/admin/', None),
]

for path, name in urls_to_check:
    try:
        if name:
            url = reverse(name)
            print(f"✅ Reverse '{name}': {url}")
        match = resolve(path)
        print(f"✅ Resolve '{path}': {match.view_name}")
    except Exception as e:
        print(f"❌ URL Error for {path}: {e}")

print("\n--- Template Check ---")
template_path = os.path.join(os.path.dirname(__file__), 'main', 'templates', 'blog_list.html')
if os.path.exists(template_path):
    print(f"✅ Blog template found at: {template_path}")
else:
    print(f"❌ Blog template MISSING at: {template_path}")
