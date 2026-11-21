# 🏆 IDEA//FORGE Online Hackathon — Submission Kit

## 1. Project Overview & Meta Details
- **Project Title:** **CivicPulse AI (जन-समाधान)** — Autonomous Civic Grievance Triage, Multimodal Severity Assessment & Public Accountability Platform
- **Track Selected:** **Track 1: Civic Pulse, Digital Governance & Public Information**
- **Problem Statement Chosen:** **Problem 2: Transparent Civic Grievance & Infrastructure Triage System**
  > *"A platform where citizens report problems like damaged roads, pollution or water leaks using photos, videos or audio. It rates how serious each problem is, sends it to the right authority, and shows a public dashboard of complaints and fixes."*
- **Platform Registration:** Registered on Challazo (`challazo.in`) & filled submission form (`https://bit.ly/onlinehackathon-ideaforge`)

---

## 2. The Core Problem Statement
Urban infrastructure governance currently suffers from three critical failure points:
1. **Unstructured & Subjective Backlogs**: Municipal portals treat a minor crack in a residential lane identically to a 4-foot deep lethal crater on an arterial road. Without automated severity rating, critical hazards wait days while low-priority cosmetic complaints get worked on first.
2. **Duplicate Administrative Floods**: When a major water main bursts or a road collapses, 50-100 citizens file separate tickets. Field engineers waste hours deduplicating tickets manually.
3. **No Closed-Loop Public Verification**: Grievances are frequently marked "Resolved" by contractors on paper without physical verification, causing deep public cynicism.

---

## 3. The CivicPulse AI Solution
CivicPulse AI reimagines municipal grievance management as an autonomous, multimodal, and transparent pipeline:
1. **Multimodal Computer Vision Analysis**: Analyzes photos to identify surface defects (cracks, craters, burst pipelines, exposed live cables, overflowing bins) and computes a mathematical severity rating from 1.0 to 10.0.
2. **Audio & Regional Dialect Engine**: Listens to voice complaints in English, Hindi/Hinglish, and regional languages, extracting safety hazard keywords (e.g. *accident risk, sparking, hospital road*).
3. **Spatial Deduplication & Community Upvoting**: Uses Haversine geospatial proximity math (75-meter threshold) to group neighborhood reports. When a duplicate report comes in, it automatically upvotes the existing ticket and notifies the citizen instead of cluttering municipal dispatch.
4. **Intelligent Department Routing & SLA**: Directly classifies and routes tickets to PWD, Jal Sansthan, Municipal Waste Management, or DISCOM with dynamically calculated SLA targets (from 6 hours for critical electrical hazards to 36 hours for general repairs).
5. **3D GIS Transparency Heatmap**: Visualizes real-time civic health across municipal wards with interactive 3D pin overlays.
6. **"Before & After" Resolution Audit**: Enforces visual proof of repair before municipal officers can close a ticket.
7. **RTI & Open Data Compliance**: One-click public CSV audit export for civic researchers, media, and citizens.

---

## 4. 2-Minute Video Pitch Script (For Judges)

### [0:00 - 0:25] Hook & Problem
*"Judges, imagine riding your two-wheeler home at dusk, only to hit a 4-foot pothole that was reported three weeks ago, but sat buried at the bottom of an unstructured municipal portal. Every year, thousands of road accidents and billions of liters of potable water are wasted simply because cities lack an intelligent triage system. Today, we are proud to introduce **CivicPulse AI**."*

### [0:25 - 0:55] Live Citizen Demo & Multimodal AI
*(Screen share: Report Issue Tab)*  
*"With CivicPulse, a citizen simply snaps a photo or records a quick voice complaint in Hindi or English. Instantly, our Multimodal AI engine scans the image: it detects structural damage, computes a severity score of 8.7 out of 10, identifies hazard risks like two-wheeler skid danger, calculates an estimated repair budget, and assigns a strict 12-hour SLA. Even better, our geospatial engine checks if a neighbor already reported this within 75 meters, automatically upvoting the ticket instead of creating duplicates."*

### [0:55 - 1:25] Municipal Command Center & Transparency
*(Screen share: Live 3D Map & Municipal Portal)*  
*"On the governance side, municipal officers receive a pre-triaged work order routed automatically to the Public Works Department. Citizens and civil society track every step on our public 3D GIS heatmap. And the best part? A contractor cannot just click 'Resolved'—they must upload an after-repair photo, creating a verifiable before-and-after audit trail."*

### [1:25 - 1:45] Impact & Scalability
*"CivicPulse turns complaints into measurable civic data. It works out-of-the-box, integrates seamlessly with municipal WhatsApp channels or city helplines, and provides 1-click open data reports for RTI transparency."*

### [1:45 - 2:00] Conclusion
*"CivicPulse AI empowers citizens, accelerates municipal response, and restores trust in digital governance. Thank you!"*

---

## 5. Technology Stack
- **Frontend & Web Framework:** Streamlit (v1.50) with Custom Responsive CSS & Glassmorphism Theme
- **Data Visualization & GIS:** Pydeck 3D GIS layers & Pandas
- **AI & Multimodal Triage Engine:** Pillow Computer Vision, Edge/Texture Density Algorithms, Audio Urgency Classifier
- **Geospatial Math:** Haversine Proximity Deduplication (Latitude/Longitude clustering)
- **Database & Storage:** SQLite3 with pre-seeded metropolitan civic dataset and audit logging
- **Export Formats:** Open Data CSV / RTI Audit tables
