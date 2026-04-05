# 🏺 UK Pottery Map: Geospatial Analytics Tool

Interested in trying pottery but unsure where coudl we be able to start? Or perhaps you are looking for a local studio for regular practice after your first trial session?

UK Pottery Map is a location-intelligence web application designed to help users discover local pottery studios by simply entering a UK postcode. By leveraging Real-time API integration and Geospatial visualization, this tool automates the process of identifying specialized craft services within a defined 5km urban radius.

## Business Case & Problem Statement

As one of the pottery hobbyist, I identified a significant difficulties in finding a UK loacl pottery craft workshop. Finding a local pottery studio often requires tons of manuals and time-consuming searches across multiple social media platforms and outdated directories.

This project is try to solve this "Search-to-Action" gap by:

* **Centralizing Search**: Aggregating real-time data from OpenStreetMap into a single, intuitive interface.
* **Proximity Intelligence**: indentified a **5km geofence** to ensure search results align with realistic local commuting patterns.
* **Ensure Data Dynamic Accuracy**: Combining the live data via the **Overpass API** instead of relying on static, manual lists that may become obsolete.

## Tech Stack
* **Language**: Python 3.10
* **Data APIs**:
*   Postcodes.io: For high-accuracy UK geocoding (Postcode to Lat/Lon conversion).
*   Overpass API (OpenStreetMap): For real-time querying of geographic map features.
  

## Security & Data Privacy (BA Perspective)

Recognizing that this tool processes location-based data (UK Postcodes), I adopted a **Privacy-by-Design** framework:

* **Zero-Data Retention Policy**: The application is strictly "Stateless." We do not utilize a database to store user postcodes or search history, effectively eliminating the risk of **PII (Personally Identifiable Information)** leaks.
