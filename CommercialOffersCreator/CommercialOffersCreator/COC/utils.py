from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *


class ObjectsDetailMixin:

    model = None
    template = None

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        return render(request, self.template, context={self.model.__name__.lower():obj, 'admin_object': obj, 'detail':True})


class ObjectCreateMixin:

    form_model = None
    template  = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj.get_absolut_url())
        else:
            return render (request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj.get_absolut_url())
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        obj.delete()
        return redirect(reverse(self.redirect_url))
