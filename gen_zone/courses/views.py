from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Course, Lesson
from .serializers import CourseSerializer, FullStepSerializer, SBCourseSerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Step
from .serializers import StepSerializer


class CourseListView(APIView):

    def get_course(self, id):
        try:
            course = Course.objects.get(id=id)
            return course
        except Course.DoesNotExist:
            return None  # Handle the case where the course with the given ID doesn't exist

    def get(self, request, id):
        id = self.kwargs.get('id')
        course = self.get_course(id)

        if course is not None:
            serializer = SBCourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['get'])
    def get_lesson(self, request):
        id = self.kwargs.get('id')
        course = self.get_course(id)
        lesson_num = self.kwargs.get('lesson_num')

        

    
    
    
    
class FullStepView(APIView):
    def get(self, request, id, format=None):
        step = get_object_or_404(Step, id=id)
        serializer = FullStepSerializer(step)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class LessonListView(APIView):
#     def get(self, request, format=None):
#         lessons = Lesson.objects.all()
#         serializer = LessonSerializer(lessons, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class SubLessonListView(APIView):
#     def get(self, request, format=None):
#         sublessons = SubLesson.objects.all()
#         serializer = SubLessonSerializer(sublessons, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

