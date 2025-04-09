from django import forms
from .models import DDSRecord, Category, Subcategory, Type, Status

class DDSRecordForm(forms.ModelForm):
    class Meta:
        model = DDSRecord
        fields = '__all__'
        labels = {
            'status': 'Статус',
            'type': 'Тип',
            'category': 'Категория',
            'subcategory': 'Подкатегория',
            'amount': 'Сумма в рублях',
            'comment': 'Комментарий',
            'created_at': 'Дата создания',
        }
        widgets = {
            'created_at': forms.DateInput(attrs={
                'type': 'date'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                record_type = self.data.get('type')
                self.fields['category'].queryset = Category.objects.filter(type=record_type)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.type:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.category:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {
            'name': 'Название',
        }

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        labels = {
            'name': 'Название',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        labels = {
            'name': 'Название',
            'type': 'Тип',
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        labels = {
            'name': 'Название',
            'category': 'Категория',
        }