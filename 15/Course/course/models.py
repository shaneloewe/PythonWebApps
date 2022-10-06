from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse_lazy


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    # title = models.CharField(max_length=100)
    # notes = models.TextField()
    github = models.URLField(default="https://github.com")
    server = models.URLField(default="https://digitalocean.com")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('student_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @staticmethod
    def get_me(user):
        return Student.objects.get_or_create(user=user)[0]
