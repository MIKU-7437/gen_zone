from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsOwnerOrReadOnly


class CourseListCreateView(generics.ListCreateAPIView):
    """
    список все курсов и создание своего

    только зареганые пользователя могуть создавать курсы
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        if request.user.is_authenticated:
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Только зарегистрированные пользователи могут создавать курсы"}, status=status.HTTP_401_UNAUTHORIZED)



class CourseRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Описание: редактирование курса владельцеми просмотр всем остальным
    названия, описания: курса, модулей и уроков
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_url_kwarg = 'id'

    def get_course(self, id):
        try:
            course = Course.objects.get(id=id)
            return course
        except Course.DoesNotExist:
            return None

    def get(self, request, id):
        course = self.get_course(id)

        if course is not None:
            serializer = self.get_serializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Курс не найден"}, status=status.HTTP_404_NOT_FOUND)
class LessonView(APIView):
    """
    Описание: данные самого урока с его шагами
    """

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    def get_course(self, id):
        try:
            course = Course.objects.get(id=id)
            return course
        except Course.DoesNotExist:
            return None
        

    def get_lesson(self, course, lesson_num, module_num):
        try:
            lesson = Lesson.objects.get(module__course=course, module__module_num=module_num, lesson_num=lesson_num)
            return lesson
        except Lesson.DoesNotExist:
            return None

    def get(self, request, id, lesson_num, module_num):
        
        course = self.get_course(id)
        
        if course is not None:
            lesson = self.get_lesson(course, lesson_num, module_num)

            if lesson is not None:
                serializer = LessonSerializer(lesson)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Урок не найден"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Курс не найден"}, status=status.HTTP_404_NOT_FOUND)
