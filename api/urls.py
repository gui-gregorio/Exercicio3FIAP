from django.contrib import admin
from django.urls import path, include
from usuarios import views as views
from rest_framework import routers


route = routers.DefaultRouter()





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('pacientes/',views.PacienteViewSet.as_view()),
    path('pacientes/<int:pk>',views.PacienteViewSetRetrieve.as_view()),
    path('funcionarios/',views.FuncionarioViewSet.as_view()),
    path('funcionarios/<int:pk>',views.FuncionarioViewSetRetrieve.as_view()),
    path('consultas/',views.ConsultaAgendadaViewSet.as_view()),
    path('consultas/<int:pk>',views.ConsultaAgendadaViewSet.as_view()),
]