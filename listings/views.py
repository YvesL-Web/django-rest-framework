from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ListingSerializer
from .choices import state_choices, price_choices, bedroom_choices
from .models import Listing
from agent.models import Agent
# Create your views here.

@api_view(['GET'])
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer = ListingSerializer(listings, many=True)
    paginator = Paginator(listings,6)
    page_number = request.GET.get('page')
    page_listings = paginator.get_page(page_number)

    context = {
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'pages':page_listings,
    }

    return Response(serializer.data)



@api_view(['GET'])
def listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    serializer = ListingSerializer(listing, many=False)
    context = {
        'listing':listing
    }
    return Response(serializer.data)

@api_view(['GET'])
def search_param(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # typing keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices' : state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'listings' : queryset_list,
        'values' :request.GET,
    }

    return Response(request, 'listings/search.html',context)

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