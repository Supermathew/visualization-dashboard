from django.urls import path
from .views import FilterBySectorView,FilterByEndYearView,FilterByTopicView,FilterByRegionView,FilterByPestView,FilterBysourceView,FilterByCountryView,FilterByrelevanceView,FilterByintensityView,bar_chart_data,IntensityLikelihooddata,RelevanceByTopicsPieView,Yearandintensity,Countrywisecount

urlpatterns = [
    path('filter/sector/<str:sector>/', FilterBySectorView.as_view(), name='filter-by-sector'),
    path('filter/endyear/<str:EndYear>/', FilterByEndYearView.as_view(), name='filter-by-endyear'),
    path('filter/topic/<str:topic>/', FilterByTopicView.as_view(), name='filter-by-topic'),
    path('filter/region/<str:region>/', FilterByRegionView.as_view(), name='filter-by-region'),
    path('filter/pestle/<str:pestle>/', FilterByPestView.as_view(), name='filter-by-pestle'),
    path('filter/source/<str:source>/', FilterBysourceView.as_view(), name='filter-by-source'),
    path('filter/country/<str:Country>/', FilterByCountryView.as_view(), name='filter-by-Country'),
    path('filter/relevance/<int:relevance>/', FilterByrelevanceView.as_view(), name='filter-by-relevance'),
    path('filter/intensity/<int:intensity>/', FilterByintensityView.as_view(), name='filter-by-intensity'),
    path('visual/inten-sect/', bar_chart_data, name='visual-by-intensity-sector'),
    path('visual/Intensity-Likelihood/', IntensityLikelihooddata, name='visual-by-intensity-likelihood'),
    path('visual/relevance-topic/', RelevanceByTopicsPieView, name='visual-by-relevance-topic'),
    path('visual/year-intensity/', Yearandintensity, name='visual-by-year-intensity'),
    path('visual/countrywisecount/', Countrywisecount, name='visual-by-country-count'),





]
