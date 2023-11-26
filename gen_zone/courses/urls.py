from django.urls import path
from .views import CourseRetrieveUpdateView, CourseListCreateView, ModuleCreateView, ModuleDetailView, LessonCreateView, LessonDetailView, StepCreateView, StepDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('course/<int:id>/', CourseRetrieveUpdateView.as_view(), name='course-detail'),
    # path('course/<int:id>/module/<int:module_num>/lesson/<int:lesson_num>/', LessonView.as_view(), name='lesson-detail'),
    path('course/<int:id>/module/', ModuleCreateView.as_view(), name='module-create'),
    path('course/<int:id>/module/<int:module_num>/', ModuleDetailView.as_view(), name='module-detail'),
    path('course/<int:id>/module/<int:module_num>/lesson/', LessonCreateView.as_view(), name='lesson-create'),
    path('course/<int:id>/module/<int:module_num>/lesson/<int:lesson_num>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('course/<int:id>/module/<int:module_num>/lesson/<int:lesson_num>/step/', StepCreateView.as_view(), name='step-create'),
    path('course/<int:id>/module/<int:module_num>/lesson/<int:lesson_num>/step/<int:step_num>/', StepDetailView.as_view(),)
]
