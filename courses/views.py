from django.db.models import Sum, Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView,RetrieveDestroyAPIView
from . import serializers
from . import models
from .serializers import Course_videosSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404
class CourseVideosByCourseAPIView(ListAPIView):
    serializer_class = Course_videosSerializer
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return models.Course_videos.objects.filter(course_id=course_id)
class CourseVideoDetailAPIView(DestroyAPIView):
    serializer_class = Course_videosSerializer
    def get_queryset(self):
        return models.Course_videos.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        course_id = self.kwargs['course_id']
        video_id = self.kwargs['id']
        obj = get_object_or_404(queryset, course_id=course_id, id=video_id)
        return obj
def HomePageView(requests):
    users= models.Users.objects.all()
    data=[]
    for i in users:
        i={
            'fullname':i.fullname,
            'email':i.email,
            'phone':i.phone,
            'date':i.date,
            'password':i.password,
            'status_paid':i.status_paid,
            'course':i.course,
            'token_user':i.token_user,
        }
        data.append(i)
    return render(request=requests,template_name='index.html',context={'data':data})
class TeachersSerializer(ListAPIView):
    serializer_class = serializers.TeachersSerializer
    def get_queryset(self):
        return models.Teachers.objects.all()
class TeachersDestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.TeachersSerializer
    def get_queryset(self):
        return models.Teachers.objects.all()

class CoursesSerializer(ListAPIView):
    serializer_class = serializers.CoursesSerializer
    def get_queryset(self):
        return  models.Courses.objects.all()
class CoursesDestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.CoursesSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        count=models.Course_videos.objects.filter(course_id=pk).count()
        return models.Courses.objects.all()
class UsersSerializer(ListAPIView):
    serializer_class = serializers.UsersSerializer

    def get_queryset(self):
        return models.Users.objects.all()
class UsersSerializer(ListAPIView):
    serializer_class = serializers.UsersSerializer
    def get_queryset(self):
        return models.Users.objects.all()
class UsersDestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.UsersSerializer
    def get_queryset(self):
        return models.Users.objects.all()
class Customize_websiteSerializer(ListAPIView):
    serializer_class = serializers.Customize_websiteSerializer
    def get_queryset(self):
        return models.Customize_website.objects.all()
class Customize_websiteDestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.Customize_websiteSerializer
    def get_queryset(self):
        return models.Customize_website.objects.all()
