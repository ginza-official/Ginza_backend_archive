from django import forms
# Register your models here.
from django.contrib import admin
from courses.models import *
# Register your models here.






@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display =('id','name','surname','phone','date','token_teacher')
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display =('id','name','price','teacher','type','date','filter','token_course')
    list_editable = ['price']


@admin.register(Course_videos)
class Course_videosAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'course',
                    'title',
                    'date',
                    'lock_status',

                    ]
    list_editable = ['lock_status']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','fullname','email','phone','date','course','token_user','status_paid','password']
    list_editable = ['status_paid','password']

@admin.register(user_contact_connection)
class user_contact_connection(admin.ModelAdmin):
    list_display = ['id','username','number','date']

@admin.register(Customize_website)
class Customize_websiteAdmin(admin.ModelAdmin):
    list_display = ['id','datetime']
