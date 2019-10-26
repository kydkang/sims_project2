from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage,  PageNotAnInteger
from .models import Index101
from .forms import IndexForm 
from commons.models import Description

# class IndexListView(PermissionRequiredMixin, ListView):
#     permission_required = ('sims101.index-contributor') 
#     model = Index101                      ###  Or,   queryset = Post.objects.all()
#     template_name = 'sims101/index_list.html'   ### default context name is 'object_list'. To change it, enter context_object_name = 'posts'
#     # paginate_by = 3       ## 3 objects per page 

#     def get_context_data(self, **kwargs):   ### get the first object to be used in the index_list.html 
#         context = super(IndexListView, self).get_context_data(**kwargs) 
#         context['first'] = Index101.objects.first()  
#         context['description'] = Description.objects.get(sequence=Index101.SEQUENCE)
#         if not ('form' in context):
#             context['form'] = IndexForm()
#         return context

@permission_required('sims101.index_contributor')
def IndexListView(request):
    object_list = Index101.objects.all() 
    first = Index101.objects.first()  
    description= Description.objects.get(sequence=Index101.SEQUENCE)

    paginator = Paginator(object_list, 333)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage: 
        object_list = paginator.page(paginator.num_pages) 

    if request.method == 'POST':
        form = IndexForm(request.POST)
        context = {'form':form, 'object_list':object_list, 'first':first, 'description':description}
        if form.is_valid():              
            book = form.save()
            book.save()
            request.session['created'] = "true"
            # request.session.modified = True
            return render(request, 'sims101/index_list.html', context)
    else:
        form = IndexForm()
        context = {'form':form, 'object_list':object_list, 'first':first, 'description':description}
    return render(request, 'sims101/index_list.html', context)

# class IndexDetailView(PermissionRequiredMixin, DetailView):
#     permission_required = ('sims101.index-contributor') 
#     model = Index101
#     template_name = 'sims101/index_detail.html' 

from django.shortcuts import render
def ajax_change_session(request):  
    request.session['created'] = ""
    return render(request, 'sims101/index_delete.html') 

from decimal import Decimal
def ajax_calculate(request):     ###  same as 'calculate' function  in model.py 
    first_data = request.GET.get('first_data')
    second_data = request.GET.get('second_data')
    final_value = int(first_data) * Decimal(second_data)   
    return render(request, 'sims101/final_value.html', {'final_value':final_value})

class IndexUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('sims101.index_validator') 
    model = Index101
    form_class = IndexForm
    template_name = 'sims101/index_update.html'
    success_url = reverse_lazy('sims101:index_list')  

class IndexDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('sims101.index_validator')    
    model = Index101
    template_name = 'sims101/index_delete.html'
    success_url = reverse_lazy('sims101:index_list')  
 
 # class IndexCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = ('sims101.index-contributor') 
#     model = Index101
#     form_class = IndexForm 
#     template_name = 'sims101/index_create.html'
#     login_url = 'login'
#     success_url = reverse_lazy('sims101:index_list')  
#     ### CreateView, UpdateView에 success_url을 제공하지 않는 경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크한다 by Django ]]

#     def form_invalid(self, form):  
#         first = Index101.objects.first()  
#         description = Description.objects.get(sequence=Index101.SEQUENCE)  
#         object_list = Index101.objects.all()  
#         context = {'first':first, 'description':description, 'form':form, 'object_list':object_list} 
#         return render(self.request, 'sims101/index_list.html', context)

#         # return HttpResponseRedirect('/101/')

#     def setup(self, request, *args, **kwargs): 
#         super().setup(request, *args, **kwargs)
#         request.session['created'] = "true"
#         request.session.modified = True
# 
#  You can populate with some  initialization data for the form. 
    # def get_initial(self, *args, **kwargs):
    #         initial = super(IndexCreateView, self).get_initial(**kwargs)
    #         initial['title'] = 'My Title'
    #         return initial





