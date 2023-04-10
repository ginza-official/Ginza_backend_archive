from django.db import models
import uuid


class Course_filter(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type



# Create your models here.
class Teachers(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='teachers/images', blank=True, null=True)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    tiktok = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    token_teacher = models.UUIDField( default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Courses(models.Model):

    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    price = models.CharField(default='Bepul',max_length=200)
    image = models.ImageField(upload_to='courses/images', blank=True, null=True)
    video_about = models.FileField(upload_to='courses/videos', blank=True, null=True)
    type = models.CharField(max_length=50,blank=True, null=True,choices=(('Faster','Faster'),('Practice','Practice'),('Special','Special'),('SpecialPractice','SpecialPractice')))
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    filter = models.ForeignKey(Course_filter, on_delete=models.SET_NULL, blank=True, null=True)
    token_course=models.UUIDField( default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
class VideoStatus(models.TextChoices):
    true = 'True', 'True'
    false = 'False', 'False'

class Course_videos(models.Model):

    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    video = models.FileField(upload_to='courses/videos', blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    token_course=models.UUIDField( default=uuid.uuid4, editable=False)
    lock_status=models.CharField(choices=VideoStatus.choices,default=False,max_length=200)
    class Meta:
        unique_together = ('id', 'token_course')
    def __str__(self):
        return self.title
class Users(models.Model):

    fullname = models.CharField(max_length=500)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    status_paid = models.BooleanField(default=False)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    token_user=models.UUIDField( default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.fullname

class user_contact_connection(models.Model):
    username=models.CharField(max_length=80)
    number = models.CharField(max_length=80)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Customize_website(models.Model):
    main_section_picture = models.ImageField(upload_to='customize_website/images', blank=True, null=True)
    count_section_msg = models.CharField(max_length=500, blank=True, null=True)
    count_of_students = models.IntegerField()
    count_of_courses = models.IntegerField()
    count_of_teachers = models.IntegerField()
    faster_course_background = models.ImageField(upload_to='customize_website/images', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    team_purpose = models.CharField(max_length=1000, blank=True, null=True)
    team_background = models.ImageField(upload_to='customize_website/images', blank=True, null=True)
    main_video = models.FileField(upload_to='about_us/videos', blank=True, null=True)
    jobs_title = models.CharField(max_length=500, blank=True, null=True)
    jobs_background = models.ImageField(upload_to='customize_website/images', blank=True, null=True)
    jobs_description = models.CharField(max_length=1000, blank=True, null=True)
    contact_us_title = models.CharField(max_length=500, blank=True, null=True)
    contact_us_background = models.ImageField(upload_to='customize_website/images', blank=True, null=True)
    contact_us_description = models.CharField(max_length=1000, blank=True, null=True)
    footer_background = models.ImageField(upload_to='customize_website/images', blank=True, null=True)
    link_to_instagram = models.CharField(max_length=500, blank=True, null=True)
    link_to_facebook = models.CharField(max_length=500, blank=True, null=True)
    link_to_telegram = models.CharField(max_length=500, blank=True, null=True)
    link_to_youtube = models.CharField(max_length=500, blank=True, null=True)
    link_to_twitter = models.CharField(max_length=500, blank=True, null=True)
    link_to_linkedin = models.CharField(max_length=500, blank=True, null=True)
    link_to_tiktok = models.CharField(max_length=500, blank=True, null=True)
    link_to_whatsapp = models.CharField(max_length=500, blank=True, null=True)
    link_to_email = models.CharField(max_length=500, blank=True, null=True)
    datetime=models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)




    def __str__(self):
        return self.title

