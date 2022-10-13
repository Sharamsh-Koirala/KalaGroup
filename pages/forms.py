from re import L
from django.forms import ModelForm
from .models import IndexPage, ServicePage, AboutPage


class IndexPageForm(ModelForm):
    class Meta:
        model = IndexPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IndexPageForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

class ServicePageForm(ModelForm):
    class Meta:
        model = ServicePage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServicePageForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

class AboutPageForm(ModelForm):
    class Meta:
        model = AboutPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AboutPageForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})