from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.all_notes, name='all_notes'),
    path('note_detail/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/create/', views.note_create_update, name='new_note'),
    path('note/<int:note_id>/edit/',
         views.note_create_update,
         name='update_note'
         ),
    path('note/<int:note_id>/delete/', views.note_delete, name='delete_note'),
]
