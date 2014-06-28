from django.shortcuts import render_to_response
from django.http import HttpResponse
from page.models import UserProfile

def user_profile(request, user_id=1):
    return render_to_response('prof.html', {'prof': UserProfile.objects.get(id=user_id)})   

