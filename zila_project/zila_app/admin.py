from django.contrib import admin
from zila_app.models import UserProfileInfo
# Register your models here.



def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
    make_published.short_description = "Placed"

def make_shipped(modeladmin, request, queryset):
    queryset.update(status='s')
    make_published.short_description = "Shipped"

def make_Delivered(modeladmin, request, queryset):
    queryset.update(status='d')
    make_published.short_description = "Delivered"


def make_return(modeladmin, request, queryset):
    queryset.update(status='r')
    make_published.short_description = "Return"

class Admin(admin.ModelAdmin):
    list_display = ['user', 'status']

    actions = [make_published,make_return,make_shipped,make_Delivered]


admin.site.register(UserProfileInfo , Admin)
