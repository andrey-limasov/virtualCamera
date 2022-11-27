import mimetypes
import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects

    return render(request, 'index.html')

def archive(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects

    return render(request, 'archive.html')

def download_video_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filepath = BASE_DIR + '/cameraadmin/static/video/video.mp4'
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=video.mp4"
    # Return the response value
    return response