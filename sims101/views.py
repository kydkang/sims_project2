from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import PermissionRequiredMixin 
from .models import Index101

class IndexListView(PermissionRequiredMixin, ListView):
    permission_required = ('sims101.index_manager') 
    model = Index101                      ###  Or,   queryset = Post.objects.all()
    template_name = 'sims101/index_list.html'   ### default context name is 'object_list'. To change it, enter context_object_name = 'posts'
    ### paginate_by = 3       ## 3 objects per page 

class IndexDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('sims101.index_manager') 
    model = Index101
    template_name = 'sims101/index_detail.html' ### default context name is 'object'. 

class IndexCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('sims101.index_manager') 
    model = Index101
    template_name = 'sims101/index_create.html'
    fields = ['data_one', 'data_two']
    login_url = 'login'
    ### CreateView, UpdateView에 success_url을 제공하지 않는 경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크한다 by Django ]]

class IndexUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('sims101.index_manager') 
    model = Index101
    template_name = 'sims101/index_update.html'
    fields = ['data_one', 'data_two']

class IndexDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('sims101.index_manager')    
    model = Index101
    template_name = 'sims101/index_delete.html'
    success_url = reverse_lazy('sims101:index_list')  
 

    # You can populate with some  initialization data, if needed: 
    # def get_initial(self, *args, **kwargs):
    #         initial = super(IndexCreateView, self).get_initial(**kwargs)
    #         initial['title'] = 'My Title'
    #         return initial
    # 

#     for CreateView and UpdateView, you can use form_valid for additional settings.
#     def form_valid(self, form):
#         form.instance.author = self.request.user 
#         return super().form_valid(form) 


    # # Initialize attributes shared by all view methods.
    # def setup(self, request, *args, **kwargs): 
    #     super().setup(request, *args, **kwargs)
    #     # get the Area objects using object ids passed by session 
    #     # this list will be sent to the template by the get_context_data() below
    #     if request.session._session:
    #         self.areas = [Area.objects.get(id=id) for id in request.session['affected_areas']] 

    # # Insert the area list  into the context dict.
    # def get_context_data(self, **kwargs):
    #     context = super(InformeDetailView, self).get_context_data(**kwargs)
    #     for example  self.kwargs['pk']   # pk is from the url 

    #     if request.session._session:
    #         context['areaset'] = self.areas
    #     return context