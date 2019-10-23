from django import forms
from .models import Index101

class IndexForm(forms.ModelForm): 
    class Meta:
        model = Index101
        fields = ['data_one', 'data_two', 'calculated_value']
        calculated_value = forms.CharField(disabled=True) 
        
        widgets = {
            'calculated_value': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


    # def __init__(self, *args, **kwargs):
    #     self.created = kwargs.pop('created')
    #     super(BookCreateForm, self).__init__(*args, **kwargs)

    # def clean_title(self):
        # if self.created == "true"
        #     self.create = "false"

    #     title = self.cleaned_data['title']
    #     if Book.objects.filter(user=self.user, title=title).exists():
    #         raise forms.ValidationError("You have already written a book with same title.")
    #     return title

# clean function에서 rerouting to last page ... if created 이면.... 