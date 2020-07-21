from django.shortcuts import render
from .models import Excursion, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    excursions = Excursion.objects.all()
    data = {
        "type": "FeatureCollection",
        "features": []
    }

    for excursion in excursions:
        lat = excursion.lat
        lon = excursion.lon
        inner_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": {
                "title": excursion.title,
                "placeId": excursion.id,
                "detailsUrl": reverse('place_in_detail', args=[excursion.id])
            }
        }
        data["features"].append(inner_data)

    context = {'values': data}

    return render(request, 'index.html', context=context)


def place_in_detail(request, place_id):
    place = get_object_or_404(Excursion, pk=place_id)
    imgs = Image.objects.filter(excursion_title=place)
    image_urls = []
    for img in imgs:
        image_urls.append(img.image.url)

    data = {
        "title": place.title,
        "imgs": image_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }

    response = JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 2})

    return response
