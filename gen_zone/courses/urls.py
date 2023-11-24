from django.urls import path
from .views import CourseRetrieveUpdateView, LessonView, CourseListCreateView


urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('course/<int:id>/', CourseRetrieveUpdateView.as_view(), name='course-detail'),
    path('course/<int:id>/module/<int:module_num>/lesson/<int:lesson_num>/', LessonView.as_view(), name='lesson-detail'),
]