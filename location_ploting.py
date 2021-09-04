# -*- coding: utf-8 -*-
"""location_ploting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fJwvMFAJ4FcsfPNaM1lfVNup0n6We39V
"""



import folium

m = folium.Map(location=[10.9221729887682, 76.4520922327631],
               zoom_start=15)

place_lat = [10.9221729887682, 10.9284272242481, 10.9477700542852,10.9591406976083,10.9792900876774,10.9924226778271,10.9519295253494,10.9507299262973,10.9204604372759,10.9221729887682]
place_lng = [76.4520922327631, 76.4896510699134, 76.5201991313599,76.5042399903568,76.4917408874639 ,76.4584491568944,76.4325013353357,76.4353250949947,76.4321421847971,76.4520922327631]

points = []
for i in range(len(place_lat)):
    points.append([place_lat[i], place_lng[i]])

for index,lat in enumerate(place_lat):
    folium.Marker([lat, 
                   place_lng[index]],
                  popup=('city{} \n distance'.format(index)),
                 icon = folium.Icon(color='green',icon='plus')).add_to(m)
folium.PolyLine(points, color='red').add_to(m)

m

















!python -m pip install osmnx