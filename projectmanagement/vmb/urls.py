from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("read", views.read, name="read"),
    path("overview", views.overview, name="overview"),
    path("detail_by_project/<int:project_id>/", views.detail_by_project, name="detail_by_project"),
    path("detail_by_project_month/<int:project_id>/<str:month>/", views.detail_by_project_month, name="detail_by_project_month"),
]