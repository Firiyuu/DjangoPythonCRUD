
from crud.models import Student
from crudcreate.forms import NameForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import UpdateView

# ------------------------------------------------------------
# CREATE VIEW
# Description : Create view
# ------------------------------------------------------------
def register(request):
    # Get the request's context.
    context = RequestContext(request)

    # Tthe template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False


    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        name_form = NameForm(data=request.POST)


        # If valid...
        if name_form.is_valid():
            # Save the user's form data to the database.
            name = name_form.save()
            registered = True
            name.save

        else:
            print name_form.errors


    else:
        name_form = NameForm()


    # Render the template depending on the context.
    return render_to_response(
            'crudcreate/registered.html',
            {'name_form':name_form, 'registered':registered},
            context)



class Delete(DeleteView):
    model = Student
    success_url = reverse_lazy('list')
    template_name = 'cruddelete/delete.html'




class Update(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'middle_name', 'course', 'year', 'gender']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update_form'




