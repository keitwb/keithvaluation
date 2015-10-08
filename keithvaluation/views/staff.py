from django.views.generic.list import ListView

from keithvaluation.models import Staff

class StaffView(ListView):
    page_title = 'Staff'
    template_name = 'staff.html'
    context_object_name = 'staff_members'
    model = Staff
