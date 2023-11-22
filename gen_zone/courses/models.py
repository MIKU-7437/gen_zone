from django.db import models
from users.models import User

def course_preview_upload_path(instance, filename):
    return f'courses/{instance.title}_{instance.id}/preview/{filename}'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    preview = models.ImageField(upload_to=course_preview_upload_path, null=False, blank=False)
    price = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    module_num = models.IntegerField()
    module_title = models.CharField(max_length=255)
    module_description = models.TextField()

    def __str__(self):
        return self.module_title
    
    class Meta:
        unique_together = ['course', 'module_num']

class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    lesson_num = models.IntegerField()
    lesson_title = models.CharField(max_length=255)
    lesson_description = models.TextField()

    def __str__(self):
        return self.lesson_title
    
    class Meta:
        unique_together = ['module', 'lesson_num']
    
class Step(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='steps', on_delete=models.CASCADE)
    step_num = models.IntegerField()

    def __str__(self):
        return f'{self.lesson.lesson_title}.{self.step_num}'

    class Meta:
        unique_together = ['lesson', 'step_num']



def content_upload_path(instance, filename):
    return f'courses/{instance.step.lesson.module.course.title}_{instance.step.lesson.module.course.id}/{instance.step.lesson.module.module_title}/{instance.step.lesson.lesson_title}/{filename}'

class TextContent(models.Model):
    step = models.ForeignKey(Step, related_name='text_contents', on_delete=models.CASCADE)
    text = models.TextField()
    

class ImageContent(models.Model):
    step = models.ForeignKey(Step, related_name='image_contents', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=content_upload_path)
    

class VideoContent(models.Model):
    step = models.ForeignKey(Step, related_name='video_contents', on_delete=models.CASCADE)
    video_url = models.URLField()