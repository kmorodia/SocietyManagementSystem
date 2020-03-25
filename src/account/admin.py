from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import Useradmin

# Register your models here.
admin.site.register(Account)