# pottery-map-sideprojec
A UK geospatial tool to find pottery studios

## 💼 Business Case & Problem Statement

As a hobbyist, I identified a significant friction point in the UK craft market: **Geospatial Information Fragmentation**. Finding a local pottery studio often requires manual, time-consuming searches across multiple social media platforms and outdated directories.

This project solves this "Search-to-Action" gap by:
* **Data Centralization**: Consolidating real-time studio data from OpenStreetMap into a single interface.
* **Proximity Intelligence**: Implementing a **5km geofence** to ensure search results align with realistic commuting patterns in urban areas.
* **Dynamic Accuracy**: Replacing static, high-maintenance lists with live queries via the **Overpass API**, ensuring users always see active studios.

## 🔒 Security & Data Privacy (BA Perspective)

Recognizing that this tool processes location-based data (UK Postcodes), I adopted a **Privacy-by-Design** framework:

* **Zero-Data Retention Policy**: The application is strictly "Stateless." We do not utilize a database to store user postcodes or search history, effectively eliminating the risk of PII (Personally Identifiable Information) leaks.
