from django.urls import path
from .views import CourseListView, FullStepView

urlpatterns = [
    #TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST
    # path('courses/', CourseListView.as_view(), name='course-list'),
    # path('step/<int:id>/', FullStepView.as_view(), name='full-step'),
    path('course/<int:id>/', CourseListView.as_view(), name='course-detail'),
    path('course/<int:id>/lesson_num/<int:lesson_num>/', CourseListView.as_view(), name='course-detail'),
    # path('lessons/', LessonListView.as_view(), name='lesson-list'),
    # path('sublessons/', SubLessonListView.as_view(), name='sublesson-list'),
]
