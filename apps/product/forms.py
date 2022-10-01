from django.forms import ModelForm
from .models import Product, Category

def addFormControl(elements):
    for field in elements:
        field.field.widget.attrs['class'] = 'form-control'

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        addFormControl(self.visible_fields())  
    class Meta:
        model = Product
        fields = ['name','description','base_price','offer_price','image','category']

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm,self).__init__(*args, **kwargs)
        addFormControl(self.visible_fields())
    class Meta:
        model = Category
        fields = ['category']