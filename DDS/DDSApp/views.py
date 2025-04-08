from .models import DDSRecord, Subcategory, Category, Type, Status
from .forms import DDSRecordForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from django.forms import modelform_factory
from django.contrib import messages

MODEL_MAP = {
    'status': Status,
    'type': Type,
    'category': Category,
    'subcategory': Subcategory,
}

def handbook_view(request):
    if request.method == 'POST':
        if 'save_status' in request.POST:
            form = StatusForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('handbook')
        elif 'save_type' in request.POST:
            form = TypeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('handbook')
        elif 'save_category' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('handbook')
        elif 'save_subcategory' in request.POST:
            form = SubcategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('handbook')

    context = {
        'status_form': StatusForm(),
        'type_form': TypeForm(),
        'category_form': CategoryForm(),
        'subcategory_form': SubcategoryForm(),
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.select_related('type'),
        'subcategories': Subcategory.objects.select_related('category'),
    }
    return render(request, 'handbook.html', context)

def delete_handbook_item(request, model_name, pk):
    model = MODEL_MAP.get(model_name)
    if model:
        obj = get_object_or_404(model, pk=pk)
        obj.delete()
        messages.success(request, f"{model_name.capitalize()} удалён.")
    return redirect('handbook')

FORM_MAP = {
    'status': StatusForm,
    'type': TypeForm,
    'category': CategoryForm,
    'subcategory': SubcategoryForm,
}

def edit_handbook_item(request, model_name, pk):
    model = MODEL_MAP.get(model_name)
    form_class = FORM_MAP.get(model_name)

    if not model or not form_class:
        return redirect('handbook')

    obj = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('handbook')
    else:
        form = form_class(instance=obj)

    return render(request, 'edit_handbook_item.html', {
        'form': form,
        'model_name': model_name,
        'object': obj,
    })

def load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)


def record_delete(request, pk):
    record = get_object_or_404(DDSRecord, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect('record_list')
    return render(request, 'delete_confirm.html', {'record': record})


def load_categories(request):
    type_value = request.GET.get('type')
    categories = Category.objects.filter(type=type_value).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)


def record_list(request):
    records = DDSRecord.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    types = Type.objects.all()
    statuses = Status.objects.all()

    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    status_id = request.GET.get('status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    sort_order = request.GET.get('sort', 'desc')

    if type_id:
        records = records.filter(type_id=type_id)
    if category_id:
        records = records.filter(category_id=category_id)
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)
    if status_id:
        records = records.filter(status_id=status_id)
    if start_date:
        records = records.filter(created_at__gte=parse_date(start_date))
    if end_date:
        records = records.filter(created_at__lte=parse_date(end_date))
    if sort_order == 'asc':
        records = records.order_by('created_at')
    else:
        records = records.order_by('-created_at')

    context = {
        'records': records,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'statuses': statuses,
        'selected_type': type_id,
        'selected_category': category_id,
        'selected_subcategory': subcategory_id,
        'selected_status': status_id,
        'start_date': start_date,
        'end_date': end_date,
        'sort_order': sort_order,
    }
    return render(request, 'record_list.html', context)



def record_create(request):
    if request.method == 'POST':
        form = DDSRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = DDSRecordForm()
    return render(request, 'record_form.html', {'form': form})


def record_edit(request, pk):
    record = get_object_or_404(DDSRecord, pk=pk)
    if request.method == 'POST':
        form = DDSRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = DDSRecordForm(instance=record)
    return render(request, 'record_form.html', {'form': form})