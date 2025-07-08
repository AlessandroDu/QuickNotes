from django.contrib import admin
from django.urls import path
from QuickNotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('notes/', views.QuickNotes, name='quicknotes'),
    path('note/<int:note_id>/', views.QuickNote, name='quicknote'),
    path('notes/edit/<int:note_id>/', views.edit, name='edit'),
    path('notes/delete/<int:note_id>/', views.delete, name='delete'),
    path('notes/add/', views.add, name='add'),
]
