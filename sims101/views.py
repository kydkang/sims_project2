from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import PermissionRequiredMixin 
from .models import Index101
from .forms import IndexForm 
from commons.models import Description


class IndexListView(PermissionRequiredMixin, ListView):
    permission_required = ('sims101.index-contributor') 
    model = Index101                      ###  Or,   queryset = Post.objects.all()
    template_name = 'sims101/index_list.html'   ### default context name is 'object_list'. To change it, enter context_object_name = 'posts'
    # paginate_by = 3       ## 3 objects per page 

    def get_context_data(self, **kwargs):   ### get the first object to be used in the index_list.html 
        context = super(IndexListView, self).get_context_data(**kwargs) 
        context['first'] = Index101.objects.first()  
        context['description'] = Description.objects.get(sequence=Index101.SEQUENCE)
        return context

class IndexDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('sims101.index-contributor') 
    model = Index101
    template_name = 'sims101/index_detail.html' 

class IndexCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('sims101.index-contributor') 
    model = Index101
    form_class = IndexForm 
    template_name = 'sims101/index_create.html'
    login_url = 'login'
    success_url = reverse_lazy('sims101:index_list')  
    ### CreateView, UpdateView에 success_url을 제공하지 않는 경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크한다 by Django ]]

    def setup(self, request, *args, **kwargs): 
        super().setup(request, *args, **kwargs)
        request.session['created'] = "true"
        request.session.modified = True
# 
#  You can populate with some  initialization data for the form. 
    # def get_initial(self, *args, **kwargs):
    #         initial = super(IndexCreateView, self).get_initial(**kwargs)
    #         initial['title'] = 'My Title'
    #         return initial
    

from django.shortcuts import render
def ajax_change_session(request):  
    request.session['created'] = ""
    request.session.modified = True
    return render(request, 'sims101/index_delete.html') 

class IndexUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('sims101.index-validator') 
    model = Index101
    form_class = IndexForm
    template_name = 'sims101/index_update.html'
    success_url = reverse_lazy('sims101:index_list')  

class IndexDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('sims101.index-validator')    
    model = Index101
    template_name = 'sims101/index_delete.html'
    success_url = reverse_lazy('sims101:index_list')  
 





