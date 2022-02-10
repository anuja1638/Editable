
from django.urls import path, include
from ManualEditing import views

app_name = 'ManualEditing'
urlpatterns = [
    path('', views.homePageView),
    path('manual_editing/', views.manualEditView, name='manualEditUrl' )
]