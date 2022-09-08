from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulnk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'id': 'Tony Stark',
            'image': '/static/images/iron_man.jpg'
        }
