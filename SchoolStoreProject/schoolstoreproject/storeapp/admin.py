from django.contrib import admin
from .models import Department,Course,Person,logins,register
# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Person)
admin.site.register(logins)
admin.site.register(register)

