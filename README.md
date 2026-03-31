# 🚀 AI Agency Dashboard: Automated B2B Lead & Website Generator

**Built by [Arpit Ramesan](https://www.linkedin.com/in/arpitramesan/) | [GitHub](https://github.com/ArkTrek)**

An end-to-end, AI-powered SaaS dashboard designed to automate the digital agency pipeline. This tool locates local businesses that lack a web presence, plots them on an interactive map, and utilizes Google's Gemini AI to instantly generate, preview, and export a modern, customized website code for immediate cold-outreach pitching.

---

## ✨ Core Features

* **🌍 Zero-Cost Lead Generation:** Integrates with the OpenStreetMap (OSM) Overpass API to scan specific cities and niches for businesses missing a `website` tag. Includes fallback mock-data handling to prevent UI breakage during API rate limits.
* **🗺️ Interactive Target Mapping:** Utilizes **Leaflet.js** to dynamically plot leads on a map, featuring an inverted dark-mode tile aesthetic to match the application's theme.
* **⚡ Instant AI Web Design:** Leverages **Gemini 1.5 Flash** to write highly tailored, single-page HTML/Tailwind CSS websites based on the business name, niche, and location.
* **👀 Live iFrame Preview:** Renders the AI-generated code instantly within the dashboard for visual QA before pitching.
* **💾 One-Click Export:** Client-side JavaScript packaging allows you to instantly download the generated `index.html` file to attach to client emails.
* **💎 Premium Glassmorphism UI:** A stunning, modern frontend featuring frosted glass panels, deep-space background orbs, and bespoke CSS animations.

---

## 🛠️ Technology Stack

**Backend (Python)**
* `Flask` - Lightweight web routing and API endpoint creation.
* `Requests` - Handling HTTP calls to the Overpass API.
* `google-generativeai` - Direct integration with the Gemini 1.5 Flash model.

**Frontend (Client-Side)**
* `HTML5` & `Vanilla JS` - For DOM manipulation and client-side downloads.
* `Tailwind CSS (via CDN)` - Utility-first styling for the Glassmorphism aesthetic.
* `Leaflet.js` - Open-source interactive mapping.

---

## 📂 Project Structure

Ensure your directory matches this structure before running the application:

```text
AI_Agency_Dashboard/
│
├── app.py                 # The main Python Flask backend & API router
├── README.md              # Project documentation
│
└── templates/             
    └── index.html         # The Glassmorphism frontend UI
