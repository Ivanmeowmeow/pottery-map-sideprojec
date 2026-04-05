from flask import Flask, render_template, request
import requests
import folium
import time

app = Flask(__name__)

def get_map_data(postcode):
    # 1. Postcode to Coordinates
    geo_url = f"https://api.postcodes.io/postcodes/{postcode}"
    try:
        res = requests.get(geo_url).json()
        if res['status'] != 200: return None, "Postcode not found."
        lat, lon = res['result']['latitude'], res['result']['longitude']
    except: return None, "Connection error."

    # 2. Search Pottery (Overpass API)
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json][timeout:25];
    (node["craft"~"pottery"](around:5000,{lat},{lon});
     node["shop"~"pottery"](around:5000,{lat},{lon});
     way["craft"~"pottery"](around:5000,{lat},{lon});
     way["shop"~"pottery"](around:5000,{lat},{lon}););
    out center;
    """
    elements = []
    try:
        resp = requests.get(overpass_url, params={'data': query})
        if resp.status_code == 200:
            elements = resp.json().get('elements', [])
    except: pass

    # 3. Build Folium Map
    m = folium.Map(location=[lat, lon], zoom_start=13)
    folium.Circle([lat, lon], radius=5000, color='#795548', fill=True, fill_opacity=0.1, popup='5km Radius').add_to(m)
    folium.Marker([lat, lon], popup="Search Center", icon=folium.Icon(color='red', icon='home')).add_to(m)

    for item in elements:
        tags = item.get('tags', {})
        name = tags.get('name', 'Pottery Studio')
        phone = tags.get('phone') or tags.get('contact:phone') or "Not available"
        addr = f"{tags.get('addr:housenumber','')} {tags.get('addr:street','')}, {tags.get('addr:postcode','')}".strip(", ")
        
        popup_html = f"<b>{name}</b><br><hr>📍 {addr}<br>📞 {phone}"
        it_lat = item.get('lat') or item.get('center', {}).get('lat')
        it_lon = item.get('lon') or item.get('center', {}).get('lon')
        folium.Marker([it_lat, it_lon], popup=folium.Popup(popup_html, max_width=250), icon=folium.Icon(color='blue')).add_to(m)

    return m._repr_html_(), None

@app.route('/', methods=['GET', 'POST'])
def index():
    map_html, error = None, None
    if request.method == 'POST':
        postcode = request.form.get('postcode', '').strip().upper()
        if postcode: map_html, error = get_map_data(postcode)
    return render_template('index.html', map_html=map_html, error_msg=error)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
