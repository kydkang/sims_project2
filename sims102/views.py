from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Index102

class IndexListView(ListView):
    model = Index102                       ###  Or,   queryset = Post.objects.all()
    template_name = 'sims102/index_list.html'   ### default context name is 'object_list'. To change it, enter context_object_name = 'posts'

class IndexDetailView(DetailView):
    model = Index102
    template_name = 'sims102/index_detail.html' ### default context name is 'object'. 

class IndexCreateView(CreateView):
    model = Index102
    template_name = 'sims102/index_create.html'
    fields = '__all__'
    ### CreateView, UpdateView에 success_url을 제공하지 않는 경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크한다 by Django ]]

 

    # You can populate with some  initialization data, if needed: 
    # def get_initial(self, *args, **kwargs):
    #         initial = super(IndexCreateView, self).get_initial(**kwargs)
    #         initial['title'] = 'My Title'
    #         return initial
    # 
