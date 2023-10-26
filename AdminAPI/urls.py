from django.urls import path, re_path as url, include
from AdminAPI import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('local/', views.LocalList.as_view()),
    path('local/<int:pk>/', views.LocalDetail.as_view()),

    path('aluno/', views.AlunoList.as_view()),
    path('aluno/<int:pk>/', views.AlunoDetail.as_view()),

    path('encarregadoDeEducacao/', views.EncarregadoDeEducacaoList.as_view()),
    path('encarregadoDeEducacao/<int:pk>/', views.EncarregadoDeEducacaoDetail.as_view()),

    path('professor/', views.ProfessorList.as_view()),
    path('professor/<int:pk>/', views.ProfessorDetail.as_view()),

    path('disciplina/', views.DisciplinaList.as_view()),
    path('disciplina/<int:pk>/', views.DisciplinaDetail.as_view())
    ]