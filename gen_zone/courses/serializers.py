from rest_framework import serializers
from .models import Course, Module, Lesson, Step, Content
from users.serializers import UserSerializer


# for sidebar
class SBLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson_num', 'lesson_title', 'lesson_description']

class SBModuleSerializer(serializers.ModelSerializer):
    lessons = SBLessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['module_num','module_title' ,'module_description', 'lessons']

class SBCourseSerializer(serializers.ModelSerializer):
    modules = SBModuleSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'owner',
            'rating',
            'preview', 
            'price',
            'modules'
        ]
    def get_preview_url(self, obj):
        # Здесь создайте URL для изображения, используя его относительный путь
        if obj.preview:
            return self.context['request'].build_absolute_uri(obj.preview.url)
        return None
#usual
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['content_num', 'content_type', 'text', 'image', 'width', 'height']

class StepSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Step
        fields = ['step_num', 'contents']

class LessonSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['lesson_num', 'lesson_title', 'lesson_description', 'steps']

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['module_num', 'module_title' ,'module_description', 'lessons']

class CourseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    modules = SBModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'owner', 'rating', 'preview', 'price', 'modules']
        read_only_fields = ['rating', 'id', 'modules']
        extra_kwargs = {'preview': {'required': False}}
    
