from django.contrib import admin
#Base User Admin
from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
#importamos el modelo User
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass