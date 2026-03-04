from django.shortcuts import render
# from moviesstore.map.models import location

# Create your views here.
def index(request):
    # locations = list(location.objects.values('latitude', 'longitude')[:100])
    # print(locations[:3])
    context = {}
    return render(request, 'map/index.html', context)