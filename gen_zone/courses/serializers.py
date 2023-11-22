from rest_framework import serializers
from .models import Course, Module, Lesson, Step, TextContent, ImageContent, VideoContent


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

    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'owner',
            'rating',
            'preview', 
            'price',
            'modules'
        ]

#Usual  
class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = '__all__'


class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ['text']


class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = '__all__'

class StepSerializer(serializers.ModelSerializer):
    text_contents = TextContentSerializer(many=True, read_only=True)
    image_contents = ImageContentSerializer(many=True, read_only=True)
    video_contents = VideoContentSerializer(many=True, read_only=True)

    class Meta:
        model = Step
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'



class FullStepSerializer(serializers.ModelSerializer):
    text_contents = TextContentSerializer(many=True, read_only=True)

    class Meta:
        model = Step
        fields = ['text_contents']