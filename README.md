# Smart Field-Photo Inspector
> **Georeferenced Photo Inspector & Automated Technical Reporting for Site Inspections (*Plaatsbeschrijving*) in Flanders.**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://patopitaya.github.io/Proyect-Surveyor/)
[![CRS](https://img.shields.io/badge/CRS-EPSG%3A31370%20(Lambert%2072)-blue)](https://epsg.io/31370)
[![Tech](https://img.shields.io/badge/Stack-Leaflet%20|%20Vanilla%20JS%20|%20jsPDF-orange)](https://github.com/PatoPitaya/Proyect-Surveyor)

---

## 📌 Context & Problem Statement
In Belgian construction and civil engineering, establishing a formal pre-work or post-work site condition report (**plaatsbeschrijving aanvang/beëindiging der werken**) is mandatory to mitigate liability disputes between contractors, municipal authorities (*e.g., Stad Antwerpen*), and neighboring property owners.

Typically, field surveyors take dozens or hundreds of high-resolution site photos, followed by hours of manual documentation: manually extracting GPS tags, formatting Word tables, and locating markers on blueprints. 

**Smart Field-Photo Inspector** automates this workflow directly inside the browser, transforming raw field captures into a standardized, legally structured PDF report in seconds.

---

## ⚙️ Core Technical Features

- **Automated EXIF Metadata Extraction:** Reads raw GPS coordinates (latitude, longitude, altitude), timestamps, and camera equipment directly from JPG and HEIC/HEIF images via client-side parsing.
- **Belgian Lambert 72 Projection (EPSG:31370):** Automatically reprojects WGS84 global coordinates into the official Belgian Lambert 72 coordinate reference system for surveying accuracy.
- **Interactive WebGIS Interface:** Visualizes inspection markers on top of high-detail street and satellite layers (Esri, Carto, OpenStreetMap). Includes a manual placement fallback for indoor/basement captures without GPS lock.
- **Automated PDF Report Generation:**
  - Standardized administrative metadata dossier (*Project, Werf, Gerechtsdeskundige, Dossier referentie*).
  - Summary table of observations cross-referenced with photo indices.
  - **Dynamic Fotoplan:** Captures the contextual basemap at street level with numbered marker overlays, North arrow, and scale.
  - Full-page photographic evidence report with technical pathology notes (*e.g., haarscheuren, vochtplekken, verzakkingen*).
  - Formal signature block for contradictory perusal (*Ondertekening Deskundige / Bouwheer*).
- **Client-Side Processing & Privacy:** 100% in-browser processing. Zero server-side uploads or external database dependencies, ensuring total confidentiality of field data.
- **Field-Ready Optimization:** Automatic EXIF orientation correction and adaptive memory downscaling (1600px canvas compression) to support batches of 30+ smartphone captures without performance bottlenecks.

---

## 🛠️ Tech Stack

* **Front-End / Core:** Vanilla JavaScript (ES6+), HTML5 Canvas, Modern CSS.
* **Mapping & GIS:** [Leaflet.js](https://leafletjs.com/), Esri World Street/Imagery, Carto Basemaps.
* **PDF Engine:** [jsPDF](https://github.com/parallax/jsPDF) + [jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable).
* **Image Processing:** `exif-js`, `heic2any` (Apple HEIC to JPEG conversion in memory).

---

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/PatoPitaya/Proyect-Surveyor.git](https://github.com/PatoPitaya/Proyect-Surveyor.git)
   cd Proyect-Surveyor
