from rest_framework import serializers
from . import models



class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teachers
        fields = [
            'id',
            'name',
            'surname',
            'image',
            'description',
            'date',
            'phone',
            'email',
            'instagram',
            'facebook',
            'telegram',
            'youtube',
            'twitter',
            'linkedin',
            'tiktok',
            'whatsapp',
            'token_teacher'
        ]
class CoursesSerializer(serializers.ModelSerializer):
    teacher_name= serializers.SerializerMethodField()
    def get_teacher_name(self, obj):
        name=models.Teachers.objects.get(id=obj.teacher_id).name
        surname=models.Teachers.objects.get(id=obj.teacher_id).surname
        return f"{name} {surname}"
    class Meta:
        model=models.Courses
        fields=[
            'id',
            'name',
            'description',
            'price',
            'image',
            'video_about',
            'type',
            'teacher_name',
            'date',
            'filter',
            'token_course',
            'video_count'
        ]

    video_count = serializers.SerializerMethodField()
    def get_video_count(self, obj):
        return models.Course_videos.objects.filter(course_id=obj.id).count()


class Course_videosSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course_videos
        fields=[
            'id',
            'course',
            'video',
            'title',
            'description',
            'date',
            'lock_status'
        ]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Users
        fields=[

            'fullname',
            'email',
            'phone',
            'password',
            'date',
            'status_paid',
            'course',
            'token_user'
        ]
class user_contact_connectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.user_contact_connection
        fields=[

            'username',
            'number',
            'date'
        ]

class Customize_websiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customize_website
        fields=[

            'main_section_picture',
            'count_section_msg',
            'count_of_students',
            'count_of_courses',
            'count_of_teachers',
            'faster_course_background',
            'title',
            'team_purpose',
            'team_background',
            'main_video',
            'jobs_title',
            'jobs_background',
            'jobs_description',
            'contact_us_title',
            'contact_us_background',
            'contact_us_description',
            'footer_background',
            'link_to_instagram',
            'link_to_facebook',
            'link_to_telegram',
            'link_to_youtube',
            'link_to_twitter',
            'link_to_linkedin',
            'link_to_tiktok',
            'link_to_whatsapp',
            'link_to_email',
            'datetime',
            'phone_number'

        ]
