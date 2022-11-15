from django.views.generic.base import TemplateView

from keithvaluation.models import CondemnationCase, JudicialHearing

class TestimonyView(TemplateView):
    page_title = 'Expert Testimony'
    template_name = 'list-pages/expert-testimony.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['condemnations'] = CondemnationCase.objects.all()
        context['hearings'] = JudicialHearing.objects.all()
        return context
