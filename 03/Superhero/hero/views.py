from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, view, **kwargs):
        return {
            view.get_context_data()
        }


class AFOBView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Arm Fall Off Boy',
            'body': "I am Arm Fall Off Boy, and I don't know why",
            'image': '/static/images/armfalloffboy.jpg'
        }


class MatterEaterLadView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Matter Eater Lad',
            'body': 'My name is Matter Eater Lad, watch me eat this fence',
            'image': '/static/images/mattereaterlad.jpg'
        }


class BouncingBoyView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Bouncing Boy',
            'body': 'My name is Bouncing Boy. See image below.',
            'image': '/static/images/bouncingboy.jpg'
        }
