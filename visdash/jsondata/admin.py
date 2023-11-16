from django.contrib import admin

# Register your models here.
from .models import EnergyInsight,JSONData
from django.contrib import admin, messages 

admin.site.register(EnergyInsight)
# admin.site.register(JSONData)
from datetime import datetime


import json
from django.contrib import admin, messages
from django.contrib.auth.hashers import make_password
from .models import JSONData  # Import your model here
from django.contrib.auth.models import User  # Import the User model if not already imported
import json
from django.contrib import admin, messages
from .models import EnergyInsight

@admin.register(JSONData)
class JSONDataAdmin(admin.ModelAdmin):
    list_display = ('id',)
    actions = ['create_objects_from_json']

    def create_objects_from_json(self, request, queryset):
        for json_data in queryset:
            try:
                with open(json_data.json_file.path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                for item in data:
                    added_str = item.get('added', '')
                    published_str = item.get('published', '')

                    if added_str and published_str:
                        added = datetime.strptime(added_str, '%B, %d %Y %H:%M:%S')
                        published = datetime.strptime(published_str, '%B, %d %Y %H:%M:%S')
                    else:
                        added = None
                        published = None

                    intensity_str = item.get('intensity', None)
                    likelihood = item.get('likelihood',None)
                    relevance = item.get('relevance',None)
                    if intensity_str is not None:
                        try:
                            intensity = int(intensity_str)
                        except ValueError:
                            intensity = None
                    else:
                        intensity = None
                    if likelihood is not None:
                        try:
                            likelihood = int(likelihood)
                        except ValueError:
                            likelihood = None
                    else:
                        likelihood = None
                    if relevance is not None:
                        try:
                            relevance = int(relevance)
                        except ValueError:
                            relevance = None
                    else:
                        relevance = None
                    end_year = item.get('end_year')
                    sector = item.get('sector')
                    topic = item.get('topic')
                    insight = item.get('insight')
                    url = item.get('url')
                    region = item.get('region')
                    start_year = item.get('start_year')
                    impact = item.get('impact')
                    country = item.get('country')
                    pestle = item.get('pestle')
                    source = item.get('source')
                    title = item.get('title')

                    EnergyInsight.objects.create(
                        end_year=end_year,
                        intensity=intensity,
                        sector=sector,
                        topic=topic,
                        insight=insight,
                        url=url,
                        region=region,
                        start_year=start_year,
                        impact=impact,
                        added=added,
                        published=published,
                        country=country,
                        relevance=relevance,
                        pestle=pestle,
                        source=source,
                        title=title,
                        likelihood=likelihood
                    )

                self.message_user(request, f"EnergyInsight objects created from {json_data.json_file.name}")
            except Exception as e:
                self.message_user(request, f"Error processing {json_data.json_file.name}: {str(e)}", level=messages.ERROR)

    create_objects_from_json.short_description = "Create EnergyInsight Objects from JSON Data"
