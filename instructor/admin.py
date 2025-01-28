from django.contrib import admin

# Register your models here.
from instructor.models import User,Category,Course


admin.site.register(User)

admin.site.register(Category)

admin.site.register(Course)