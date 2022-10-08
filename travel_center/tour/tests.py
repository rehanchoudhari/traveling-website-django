from django.test import TestCase

# Create your tests here.
def list(request):
  username = request.POST('username')
  retrun redirect("/")
