from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import os
import folium

def home(request):
    shp_dir = os.path.join(os.getcwd(),'media','shp')
    # folium
    m = folium.Map(location=[41.29246, 12.5736108],zoom_start=6)
    ## style
    style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
    style_rivers = { 'color': 'blue'}
    ## adding to view
    folium.GeoJson(os.path.join(shp_dir,'cities.geojson'),name='basin',style_function=lambda x:style_basin).add_to(m)
    folium.GeoJson(os.path.join(shp_dir,'roads.geojson'),name='rivers',style_function=lambda x:style_rivers).add_to(m)
    folium.LayerControl().add_to(m)
    ## exporting
    m=m._repr_html_()
    context = {'my_map': m}
    ## rendering
    return render(request,'index.html',context)