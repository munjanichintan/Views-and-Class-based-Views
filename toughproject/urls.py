from django.contrib import admin
from django.urls import path
from snippets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
    path('studentapi/<int:id>', views.student_api),
    path('stuapiclass/', views.StudentAPI.as_view()),
    path('stuapiclass/<int:id>', views.StudentAPI.as_view()),
]
