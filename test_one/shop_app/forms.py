from django import forms

from .models import Shop_Item


class Shop_Add(forms.ModelForm):
    class Meta:
        model = Shop_Item
        fields = ('name_product', 'unit','provider','price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
