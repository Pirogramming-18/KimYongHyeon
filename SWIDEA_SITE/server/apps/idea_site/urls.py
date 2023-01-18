from django.urls import path
from . import views

app_name = 'idea_site'

urlpatterns = [
    path('', views.index),
    
    #idea
    path('index', views.idea_list),
    path('idea_detail/<int:pk>', views.idea_detail, name = 'idea_detail'),
    path('idea_create', views.idea_create, name = 'idea_create'),
    path('idea_update/<int:pk>', views.idea_update, name = 'idea_update'),
    path('idea_delete/<int:pk>', views.idea_delete, name = 'idea_delete'),
    #tool
    path('tool_list', views.tool_list, name = 'tool_list'),
    path('tool_detail/<int:pk>', views.tool_detail, name = 'tool_detail'),
    path('tool_create', views.tool_create, name = 'tool_create'),
    path('tool_update/<int:pk>', views.tool_update, name = 'tool_update'),
    path('tool_delete/<int:pk>', views.tool_delete, name = 'tool_delete'),
    
    #ajax
    path('toggle-star', views.toggle_star),
    path('calc-interest', views.calc_interest),
]
