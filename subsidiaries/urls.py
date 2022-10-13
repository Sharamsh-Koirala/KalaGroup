from django.urls import path
from . import views

urlpatterns = [
    path('', views.subsidiaries, name='subsidiaries'),
    path('subsidiary/<str:pk>/', views.subsidiary, name="subsidiary"),
    path('kala-incorporated/', views.subsidiaryKalaInc, name="subsidiary_kala_incorporated"),
    path('kala-marketing/', views.subsidiaryKalaMarketing, name="subsidiary_kala_marketing"),
    path('kala-international/', views.subsidiaryKalaInternational, name="subsidiary_kala_international"),
    path('kala-agency/', views.subsidiaryKalaAgency, name="subsidiary_kala_agency"),
    path('kala-evgo/', views.subsidiaryEVGO, name="subsidiary_evgo"),
    path('kala-agro/', views.subsidiaryKalaAgro, name="subsidiary_kala_agro"),
]
