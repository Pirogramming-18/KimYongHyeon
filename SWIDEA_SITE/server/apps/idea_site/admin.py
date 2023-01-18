from django.contrib import admin
from .models import Tool, Idea


# class IdeaResource(resources.ModelResource):
# 	class Meta:
# 		model = Idea
# 		fields = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')

class IdeaAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'devtool',)
 
admin.site.register(Tool)
admin.site.register(Idea, IdeaAdmin)