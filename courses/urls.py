from django.urls import path
from . import views
from .views import CourseVideosByCourseAPIView, CourseVideoDetailAPIView
urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('teachers/', views.TeachersSerializer.as_view()),
    path('teachers/<int:pk>', views.TeachersDestroyApiView.as_view()),
    path('profiles/<int:pk>', views.TeachersDestroyApiView.as_view()),
    path('courses/', views.CoursesSerializer.as_view()),
    path('courses/<int:pk>', views.CoursesDestroyApiView.as_view()),
    # path('course_videos/', views.Course_videosSerializer.as_view()),
    # path('course_videos/<int:pk>', views.Course_videosDestroyApiView.as_view()),
    path('users/', views.UsersSerializer.as_view()),
    path('users/<int:pk>', views.UsersDestroyApiView.as_view()),
    path('customize_website/', views.Customize_websiteSerializer.as_view()),
    path('customize_website/<int:pk>', views.Customize_websiteDestroyApiView.as_view()),
    path('courses/<int:course_id>/videos/', CourseVideosByCourseAPIView.as_view(), name='course_videos_by_course'),
    path('courses/<int:course_id>/videos/<int:id>/', CourseVideoDetailAPIView.as_view(), name='course_video_detail'),
]
