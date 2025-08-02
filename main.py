import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstproject.settings")
django.setup()

from accounts.models import Role, User
#Role.objects.create(title = 'user')
#Role.objects.get(id = '3').delete()
#admin_role = Role.objects.get(title='admin')
#User.objects.create(name='test_user', email='test_user@gmail.com', role=admin_role)