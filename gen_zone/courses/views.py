from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Course, Lesson
from .serializers import CourseSerializer, FullStepSerializer, SBCourseSerializer, LessonSerializer, FullLessonSerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Step
from .serializers import StepSerializer

        
class CourseListView(APIView):
    """
    Описание: данные для сайдбара курса 
    названия, описания:курса, модулей и уроков
    """
    def get_course(self, id):
        try:
            course = Course.objects.get(id=id)
            return course
        except Course.DoesNotExist:
            return None
        
    
    def get(self, request, id):
        course = self.get_course(id)

        if course is not None:
            serializer = SBCourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Курс не найден"}, status=status.HTTP_404_NOT_FOUND)

class LessonView(APIView):
    """
    Описание: данные самого урока с его шагами
    """
    def get_course(self, id):
        try:
            course = self.get_course(id)
            return course
        except Course.DoesNotExist:
            return None
        

    def get(self, request, id, lesson_num, module_num):
        
        course = Course.objects.get(id=id)
        lesson = Lesson.objects.get(module__course=course, module__module_num=module_num,lesson_num=lesson_num)
        serializer = FullLessonSerializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)