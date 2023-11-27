from django.shortcuts import render
# Create your views here.
#request -> response
# request handler
def hello_world(request):
    # Pull data from database
    # Transform data
    # Send email
    # etc
    return render(request, 'myapp/hello.html')
