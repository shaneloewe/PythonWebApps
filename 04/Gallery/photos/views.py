from pathlib import Path
from django.views.generic import TemplateView


class PhotoView(TemplateView):
    template_name = 'photo.html'


def photo_list():
    def photo_details(i, f):
        captions = ['This is Arm Fall Off Boy. He can remove his left arm on command!',
                    'This is Bouncing Boy. Self-Explanitory...',
                    'This is Matter Eater Lad. He can eat this fence and also anything!'
                    ]
        caption = captions[i]
        return dict(id=i, file=f, caption=caption)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)
