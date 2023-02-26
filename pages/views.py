from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from listings.choices import price_choices,bedroom_choices,state_choices
from listings.models import Listing
from agent.models import Agent
from listings.serializers import ListingSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    serializer = ListingSerializer(listings, many=True)
    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }

    return Response(serializer.data)

@api_view(['GET'])
def about(request):
    # Get all Agent
    agents = Agent.objects.order_by('-hire_date')
    
    # Get the best of all seller 
    mvp_agent = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agents' : agents,
        'mvp_agent': mvp_agent
    }

    return Response(request, 'pages/about.html', context)