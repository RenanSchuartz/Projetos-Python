
import folium

mapa = folium.Map(
    location=[-25.542422365993435, -50.491306491645766],
    title = 'Mapa Municipio',
    zoom_start=15
    
)

folium.Marker(
    [-25.542422365993435, -50.491306491645766],
    popup='<i>Mercado Triunfo</i>',
    tooltip= 'Aperte aqui'
).add_to(mapa)

mapa.save('./São João do triunfo.html')