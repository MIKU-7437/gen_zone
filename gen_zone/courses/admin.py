from django.contrib import admin
from .models import Course, Module, Lesson, Step, TextContent, ImageContent, VideoContent
from django.utils.html import format_html
# Register your models here.

class TextContentInline(admin.StackedInline):
    model = TextContent
    extra = 1

class ImageContentInline(admin.StackedInline):
    model = ImageContent
    extra = 1

class VideoContentInline(admin.StackedInline):
    model = VideoContent
    extra = 1

class StepInline(admin.StackedInline):
    model = Step
    inlines = [TextContentInline, ImageContentInline, VideoContentInline]
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    inlines = [StepInline]
    extra = 1

class ModuleInline(admin.StackedInline):
    model = Module
    inlines = [LessonInline]
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]

    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        # Метод для отображения изображения пользователя в виде тега HTML
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.preview.url)
    
    image_tag.short_description = 'Image'

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [StepInline]

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    inlines = [TextContentInline, ImageContentInline, VideoContentInline]

@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    pass

@admin.register(ImageContent)
class ImageContentAdmin(admin.ModelAdmin):
    pass

@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    pass
