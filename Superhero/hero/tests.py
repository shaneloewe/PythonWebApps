from django.test import SimpleTestCase, TestCase
from hero.models import Superhero, Photo
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from json import dump


print(Superhero.objects.all())
heroes = Superhero.objects.all()
print(len(heroes))
data = [s for s in Superhero.objects.all().values()]
print(data)
# Write to JSON File
with open("C:/Users/shane/OneDrive/Desktop/myData.json", "w") as f:
    dump(data, f, indent=4)

print(Photo.objects.all())


class BlogAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)


class SuperheroViewsTest(TestCase):
    # def test_hero_list_view(self):
    #    self.assertEqual(len(heroes), 2)

    def test_hero_add_view(self):
        a = dict(title='T 1', body='None')

        b = dict(title='T 2', body='None')
        response = self.client.post(reverse("hero_add"), a)
        response = self.client.post(reverse("hero_add"), b)
        #self.assertEqual(len(heroes), 2)


users = User.objects.all()
print(len(users))


class UserTest(TestCase):
    def getUser(self, userList):
        for user in userList:
            print(user.username)

    def test_user_list(self):
        self.getUser(users)
