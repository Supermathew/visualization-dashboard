from rest_framework import generics
from jsondata.models import EnergyInsight
from .serializers import DataItemSerializer
from django.http import JsonResponse
from django.db.models import Avg

# Add sector filter in the dashboard
class FilterBySectorView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        sector = self.kwargs['sector']
        return EnergyInsight.objects.filter(sector=sector)



# Add end year filter in the dashboard
class FilterByEndYearView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        end_year = self.kwargs['end_year']
        return EnergyInsight.objects.filter(end_year=end_year)

# Add topics filters in the dashboard
class FilterByTopicView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        topic = self.kwargs['topic']
        return EnergyInsight.objects.filter(topic=topic)

# Add region filter in the dashboard
class FilterByRegionView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        region = self.kwargs['region']
        return EnergyInsight.objects.filter(region=region)

class FilterByPestView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        pestle = self.kwargs['pestle']
        return EnergyInsight.objects.filter(pestle=pestle)

class FilterBysourceView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        source = self.kwargs['source']
        return EnergyInsight.objects.filter(source=source)

class FilterByCountryView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        country = self.kwargs['Country']
        return EnergyInsight.objects.filter(country=country)

# City

class FilterByrelevanceView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        relevance = self.kwargs['relevance']
        return EnergyInsight.objects.filter(relevance=relevance)


class FilterByintensityView(generics.ListAPIView):
    serializer_class = DataItemSerializer

    def get_queryset(self):
        intensity = self.kwargs['intensity']
        return EnergyInsight.objects.filter(intensity=intensity)




def bar_chart_data(request):
    data = EnergyInsight.objects.values('sector').annotate(avg_intensity=Avg('intensity'))
    formatted_data = [{'sector': entry['sector'], 'avg_intensity': entry['avg_intensity']} for entry in data]
    return JsonResponse(formatted_data, safe=False)



def IntensityLikelihooddata(request):
    scatter_data = EnergyInsight.objects.values('intensity', 'likelihood')
    formatted_data = list(scatter_data)
    return JsonResponse(formatted_data, safe=False)


def RelevanceByTopicsPieView(request):
    relevance_data = EnergyInsight.objects.values('topic').annotate(avg_relevance=Avg('relevance'))
    formatted_data = [{'topic': entry['topic'], 'avg_relevance': entry['avg_relevance']} for entry in relevance_data]
    return JsonResponse(formatted_data, safe=False)


def Yearandintensity(request):
    trends_data = EnergyInsight.objects.values('start_year').annotate(avg_intensity=Avg('intensity'))

    formatted_data = [{'year': entry['start_year'], 'avg_intensity': entry['avg_intensity']} for entry in trends_data]

    return JsonResponse(formatted_data, safe=False)

from django.db.models import Count


def Countrywisecount(request):
    country_data = EnergyInsight.objects.values('country').annotate(entry_count=Count('country'))

    formatted_data = [{'country': entry['country'], 'entry_count': entry['entry_count']} for entry in country_data]

    return JsonResponse(formatted_data, safe=False)
