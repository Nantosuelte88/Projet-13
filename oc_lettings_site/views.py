from django.shortcuts import render
from django.http import HttpResponseServerError


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.

def index(request):
    return render(request, 'index.html')


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=500)



def trigger_500(request):
    # Lève une exception 500
    raise Exception("This is a test exception for 500 error handler")
