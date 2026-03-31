from flask import Flask, render_template, request, jsonify
import requests
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your API key here (or export it to your environment variables)
genai.configure(api_key="AIzaSyDBSc3FOfH0YplkGhVjLGWqP00caNqAuJg")

@app.route('/')
def home():
    """Serves the main frontend dashboard."""
    return render_template('index.html')

@app.route('/api/find_leads', methods=['POST'])
def find_leads():
    data = request.json
    city = data.get('city', 'Kozhikode')
    niche = data.get('niche', 'cafe')

    overpass_query = f"""
    [out:json][timeout:15];
    area[name="{city}"]->.searchArea;
    node["amenity"="{niche}"](area.searchArea);
    out center 20; 
    """
    
    overpass_servers = [
        "http://overpass-api.de/api/interpreter",
        "https://overpass.kumi.systems/api/interpreter"
    ]
    
    headers = {'User-Agent': 'AIAgencyBuilder/1.0 (Testing Local App)'}
    
    print(f"\n[SYSTEM] Fetching {niche}s in {city}...")
    
    for url in overpass_servers:
        try:
            response = requests.post(url, data={'data': overpass_query}, headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                leads = []
                
                for element in data.get('elements', []):
                    tags = element.get('tags', {})
                    if 'name' in tags and 'website' not in tags:
                        
                        # Extract Coordinates (handles both raw nodes and centered ways)
                        lat = element.get('lat') or element.get('center', {}).get('lat')
                        lon = element.get('lon') or element.get('center', {}).get('lon')
                        
                        if lat and lon: # Only add if we have a valid location
                            leads.append({
                                'name': tags['name'],
                                'address': tags.get('addr:street', 'Address not listed'),
                                'lat': lat,
                                'lon': lon
                            })
                        
                if leads:
                    print(f"[SYSTEM] API Success! Found {len(leads)} live leads.")
                    return jsonify({"status": "success", "leads": leads})
                
        except Exception:
            continue

    print("[WARNING] Live APIs blocked. Injecting Mock Data to keep the UI working.")
    mock_leads = [
        {"name": f"The Local {niche.capitalize()}", "address": f"Beach Road, {city}", "lat": 11.2626, "lon": 75.7673},
        {"name": f"Sunset {niche.capitalize()}", "address": f"Mavoor Road, {city}", "lat": 11.2550, "lon": 75.7850},
        {"name": f"Urban {niche.capitalize()} Hub", "address": f"SM Street, {city}", "lat": 11.2500, "lon": 75.7800}
    ]
    
    return jsonify({"status": "success", "leads": mock_leads, "note": "Using mock data due to API timeout."})
    
@app.route('/api/generate_demo', methods=['POST'])
def generate_demo():
    """Generates a premium website UI using the Gemini API."""
    data = request.json
    business_name = data.get('businessName')
    niche = data.get('niche')
    city = data.get('city')

    print(f"\n[SYSTEM] Gemini API is designing a premium UI for {business_name}...")

    # Initialize Gemini 3.1 Pro
    model = genai.GenerativeModel('gemini-2.5-flash')

    # The "Premium Agency" Prompt
    prompt = f"""
    You are a world-class frontend designer building a high-end website demo.
    Target Business: {business_name}
    Niche: {niche}
    Location: {city}

    Write a stunning, single-page HTML website using Tailwind CSS via CDN (<script src="https://cdn.tailwindcss.com"></script>).
    
    Design Requirements:
    - Use a modern, dark-mode or highly saturated aesthetic.
    - Include a Hero section with a dramatic gradient background and a clear Call-To-Action.
    - Include an 'About Us' section mentioning their location in {city}.
    - Include a 'Services/Menu' grid with hover effects (e.g., hover:scale-105 transition-all).
    - Use high-quality placeholder images via Unsplash Source (e.g., https://source.unsplash.com/800x600/?{niche}).
    
    CRITICAL: Output ONLY the raw HTML code. Do not wrap it in ```html markdown block. Do not say "Here is the code". Just output the raw <!DOCTYPE html> string.
    """

    try:
        response = model.generate_content(prompt)
        html_code = response.text
        
        # Strip markdown formatting just in case
        html_code = html_code.replace("```html", "").replace("```", "").strip()
        
        print("[SYSTEM] Gemini generation complete!")
        return jsonify({"status": "success", "html": html_code})

    except Exception as e:
        print(f"[ERROR] Gemini API failed: {str(e)}")
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Running on port 5000 by default
    app.run(debug=True, port=5000)