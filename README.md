## 💡 Idea
🚨 Rescue Management Web App

ResQForce is a real-time emergency reporting and management platform built using Flask (Python) for the backend and MySQL as the database. The platform is designed to bridge the communication gap between emergency response agencies and civilians during critical situations. It enables seamless coordination by providing a live map interface where all reported emergencies are displayed in real-time, helping first responders make quicker and more informed decisions.

## 🖼️ Screenshots




🔧 Features

- 🧑‍🚒 **Agency Login & Registration**
- 🗺️ **Live Emergency Map with Severity Indicators**
- 🚨 **Report Emergency via Public API**
- 📍 **Track and Update Agency Location**
- 📊 **Dashboard with Pending Emergencies**
- 🔐 **Session-based Authentication**
- 🧼 **Delete All Emergencies (Admin Tool)**
- 🛡 **NDRF Command Dashboard**


🧱 Tech Stack

- Backend: Flask (Python)
- Database: MySQL
- Frontend: HTML, CSS, JavaScript (via Jinja templates)
- Other Tools: Flask-CORS, flask-mysqldb, LEAFLET.JS

## 📁 Project Structure
```plaintext
ResQForce/
│
├── app.py
├── README.md
│
├── sql/
│   ├── sample_data.sql
│   └── schema.sql
│
├── static/
│   ├── css/
│   │   ├── client.css
│   │   ├── dashboard.css
│   │   ├── emergency_map.css
│   │   ├── index.css
│   │   ├── login.css
│   │   └── register.css
│   │
│   ├── js/
│   │   ├── dashboard.js
│   │   └── emergency_map.js
│   │
│   └── img/
│       ├── Screenshot 2025-04-11 at XX.XX.XX.png
│       └── ... (more screenshots)
│
├── templates/
│   ├── client.html
│   ├── dashboard.html
│   ├── emergency_map.html
│   ├── index.html
│   ├── login.html
│   ├── ndrf_dashboard.html
│   └── register.html
```


# API endpoints
- POST /api/report_emergency
- GET  /api/emergencies
- POST /api/update_location
- GET  /api/agencies


