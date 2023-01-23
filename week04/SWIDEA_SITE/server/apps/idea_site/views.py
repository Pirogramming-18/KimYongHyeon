from django.shortcuts import render, redirect
from .forms import IdeaForm, ToolForm, OrderForm
from .models import Idea, Tool
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from django.contrib import messages
def index(request, *args, **kwargs):
  return redirect('/index')

def idea_list(request, *args, **kwargs ):
    if request.method == 'GET':
      order = request.GET.get('order', 'title')
      form = OrderForm(initial={'order':order})
      page = request.GET.get('page', 1)
      idea_list = Idea.objects.all()      
      paginator = Paginator(idea_list, 4)
      ideas = paginator.get_page(page)
    else: 
      order = request.POST.get('order', 'title')
      form = OrderForm(initial={'order': order})
      page = request.GET.get('page', 1)
      idea_list = Idea.objects.all().order_by(order)      
      paginator = Paginator(idea_list, 4)
      ideas = paginator.get_page(page)
      
    context = {'ideas': ideas,
                 'form': form,
                 'order': order,}  
    return render(request, 'idea_site/idea/list.html', context=context)

def idea_detail(request, pk, *args, **kwargs):
  idea = Idea.objects.get(id=pk)
  context = {'idea': idea,
             }
  return render(request, 'idea_site/idea/detail.html', context=context)

def idea_create(request, *args, **kwargs):
  if request.method == 'POST':
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid() and request.POST.get('devtool') != None:
      saved = form.save(devtool=request.POST.get('devtool'))                             
      return redirect(f'/idea_detail/{saved.id}')
  else:
    form = IdeaForm()
    return render(request, 'idea_site/idea/create.html', {"form" : form})

def idea_update(request, pk, *args, **kwargs):
  idea = Idea.objects.all().get(id=pk)
  if request.method == 'POST':
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
      saved = form.save(devtool=request.POST.get('devtool'))                             
      return redirect(f'/idea_detail/{pk}')
  else: 
    form = IdeaForm(instance=idea)
  return render(request, 'idea_site/idea/update.html', {'form': form, 'pk':pk})

def idea_delete(request, pk, *args, **kwargs):
  try:
   Idea.objects.all().get(id=pk).delete()
  except ProtectedError:
    return redirect('/index')
    
  return redirect('/index')

############################[Tool]###################################

def tool_list(request, *args, **kwargs):
  tools = Tool.objects.all()
  context={
    'tools': tools
  }
  return render(request, 'idea_site/tool/list.html', context=context)

def tool_detail(request, pk, *args, **kwargs):
  tool = Tool.objects.get(id=pk)
  ideas = Idea.objects.filter(devtool=tool)
  context={'tool': tool,
           'ideas': ideas,}
  return render(request, 'idea_site/tool/detail.html', context=context)

def tool_create(request, *args, **kwargs):
  if request.method == 'POST':
    form = ToolForm(request.POST)
    if form.is_valid():
      saved = form.save()
      return redirect(f'/tool_detail/{saved.id}')
  else:
    form = ToolForm()
    
  context = {'form': form}
  return render(request, 'idea_site/tool/create.html', context=context)

def tool_update(request, pk, *args, **kwargs):
  tool = Tool.objects.get(id=pk)
  if request.method == 'POST':
    form = ToolForm(request.POST, instance=tool)
    if form.is_valid():
      form.save()
      return redirect(f'/tool_detail/{tool.id}')
  else:
    form = ToolForm(instance=tool)
    context = {'form': form,
               'pk': pk}
    return render(request, 'idea_site/tool/update.html', context=context)

def tool_delete(request, pk, *args, **kwargs):
  try:
    Tool.objects.all().get(id=pk).delete()
    return redirect('/tool_list')  
  except ProtectedError:
    print('해당 도구를 사용하는 아이디어가 존재합니다.')
  return redirect('/tool_list')  
   



##################[ajax]####################

def toggle_star(request, *args, **kwargs):
  pk = request.POST.get('pk')
  idea = Idea.objects.get(id=pk)
  idea.idea_star = not idea.idea_star
  idea.save()
  
  return JsonResponse({})

def calc_interest(request, *args, **kwargs):
  pk = request.POST.get('pk')
  option = int(request.POST.get('option'))
  idea = Idea.objects.get(id=pk)
  if 0 < idea.interest < 10:
    idea.interest += option
    idea.save()
  elif (idea.interest == 10 and option < 0) or (idea.interest == 0 and option > 0):
    idea.interest += option
    idea.save()
    
  return JsonResponse({'interest': idea.interest})
  

