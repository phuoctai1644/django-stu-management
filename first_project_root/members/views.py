from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member

# Create your views here.
def members(request):
  myMembers = Member.objects.all(). values()
  template = loader.get_template('all-member.html')
  context = {
    'myMembers': myMembers
  }
  return HttpResponse(template.render(context, request))
