import os


os.system('doskey ga= git add .')
os.system('doskey pmg=python manage.py migrate ')
os.system('doskey pmm=python manage.py makemigrations ')
os.system('doskey pcs=python manage.py createsuperuser ')
os.system('doskey rs=python manage.py runserver ')
os.system('doskey pms=python manage.py shell ')


# In [8]: for i in range(100):
#    ...:      CounselQ.objects.create( author =user, title="hello"+str(i),
#    ...:     content="3434343",
#    ...:     free=True,
#    ...:    path="대여금",)
#    ...:
