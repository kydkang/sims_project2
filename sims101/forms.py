from django import forms
from .models import Index101

class IndexForm(forms.ModelForm): 
    class Meta:
        model = Index101
        fields = ['data_one', 'data_two', 'calculated_value']
    #     labels = {
    #     "calculated_value": "Calculated"
    # }
        calculated_value = forms.CharField(disabled=True) 
        
        widgets = {
            'calculated_value': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


    # def __init__(self, *args, **kwargs):
    #     self.created = kwargs.pop('user')  << set in get_form_kwargs in CreateView
    #     super(BookCreateForm, self).__init__(*args, **kwargs)

    # def clean_title(self):    << check the book is unique per user(author) 
    #     title = self.cleaned_data['title']
    #     if Book.objects.filter(user=self.user, title=title).exists():
    #         raise forms.ValidationError("You have already written a book with same title.")
    #     return title

   