"""
CivicPulse AI - Database Layer (SQLite)
Manages grievances, municipal dispatch states, audit logs, and analytics.
"""

import sqlite3
import os
import json
from datetime import datetime, timedelta

DB_PATH = "civic_pulse.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grievances (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        category TEXT NOT NULL,
        category_name TEXT NOT NULL,
        department TEXT NOT NULL,
        severity_score REAL NOT NULL,
        severity_level TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'TRIAGED',
        sla_hours INTEGER NOT NULL,
        sla_deadline TEXT NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        address TEXT NOT NULL,
        ward TEXT NOT NULL,
        citizen_name TEXT,
        citizen_phone TEXT,
        photo_path TEXT,
        resolution_photo_path TEXT,
        resolution_notes TEXT,
        hazards TEXT,
        upvotes INTEGER DEFAULT 1,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def seed_default_grievances():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM grievances")
    count = cursor.fetchone()[0]
    
    if count == 0:
        now = datetime.now()
        samples = [
            {
                "id": "CIV-2026-1041",
                "title": "Severe crater pothole near Outer Ring Road flyover",
                "description": "Deep asphalt collapse causing two-wheelers to slip during evening traffic. Immediate blacktopping needed.",
                "category": "ROADS",
                "category_name": "Roads & Potholes",
                "department": "Public Works Department (PWD)",
                "severity_score": 8.7,
                "severity_level": "CRITICAL",
                "status": "DISPATCHED",
                "sla_hours": 12,
                "sla_deadline": (now + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M"),
                "latitude": 28.6280,
                "longitude": 77.2180,
                "address": "Ring Road Junction, Pillar 42, Connaught Place Ward",
                "ward": "Ward 4 - Central Delhi",
                "citizen_name": "Rohan Sharma",
                "citizen_phone": "+91 98110 23411",
                "photo_path": "samples/pothole_severe.jpg",
                "resolution_photo_path": None,
                "resolution_notes": "Field unit dispatched with cold-mix asphalt patch truck.",
                "hazards": json.dumps(["Two-wheeler skid risk", "Traffic bottleneck", "Vehicle suspension damage"]),
                "upvotes": 14,
                "created_at": (now - timedelta(hours=4)).strftime("%Y-%m-%d %H:%M"),
                "updated_at": (now - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
            },
            {
                "id": "CIV-2026-1042",
                "title": "Subsurface drinking water pipeline ruptured",
                "description": "Clean potable water spewing onto main road at high pressure. Water pressure drop in adjacent residential blocks.",
                "category": "WATER",
                "category_name": "Water Supply & Drainage",
                "department": "Water Board & Sewage Authority (Jal Sansthan)",
                "severity_score": 9.2,
                "severity_level": "CRITICAL",
                "status": "IN_PROGRESS",
                "sla_hours": 10,
                "sla_deadline": (now + timedelta(hours=4)).strftime("%Y-%m-%d %H:%M"),
                "latitude": 28.5355,
                "longitude": 77.2100,
                "address": "Main Market Road, Block C, Saket",
                "ward": "Ward 12 - South Delhi",
                "citizen_name": "Ananya Sen",
                "citizen_phone": "+91 97230 45890",
                "photo_path": "samples/water_pipeline_burst.jpg",
                "resolution_photo_path": None,
                "resolution_notes": "Main sluice valve isolated; excavation crew on site.",
                "hazards": json.dumps(["Potable water wastage", "Subsurface road erosion", "Localized flooding"]),
                "upvotes": 28,
                "created_at": (now - timedelta(hours=6)).strftime("%Y-%m-%d %H:%M"),
                "updated_at": (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M")
            },
            {
                "id": "CIV-2026-1039",
                "title": "Commercial market garbage container overflowing onto pedestrian walkway",
                "description": "Garbage has not been cleared for 4 days. Strong biohazard odor, stray animals scattering plastic waste.",
                "category": "WASTE",
                "category_name": "Sanitation & Waste Management",
                "department": "Municipal Solid Waste Management (Swachh Cell)",
                "severity_score": 7.4,
                "severity_level": "HIGH",
                "status": "TRIAGED",
                "sla_hours": 24,
                "sla_deadline": (now + timedelta(hours=18)).strftime("%Y-%m-%d %H:%M"),
                "latitude": 28.6506,
                "longitude": 77.1906,
                "address": "Near Metro Gate 2, Karol Bagh Market",
                "ward": "Ward 8 - Karol Bagh",
                "citizen_name": "Mohd. Tariq",
                "citizen_phone": "+91 98450 11200",
                "photo_path": "samples/waste_overflow.jpg",
                "resolution_photo_path": None,
                "resolution_notes": None,
                "hazards": json.dumps(["Biohazard & disease vector", "Severe foul odor", "Drain blockage risk"]),
                "upvotes": 9,
                "created_at": (now - timedelta(hours=6)).strftime("%Y-%m-%d %H:%M"),
                "updated_at": (now - timedelta(hours=6)).strftime("%Y-%m-%d %H:%M")
            },
            {
                "id": "CIV-2026-1035",
                "title": "Overhead 440V distribution cable snapped and dangling",
                "description": "Live electric cable dangling less than 5 feet from sidewalk outside primary school. Sparks visible in drizzle.",
                "category": "ELECTRICITY",
                "category_name": "Power & Street Lighting",
                "department": "Electricity Distribution Corporation (Discom)",
                "severity_score": 9.8,
                "severity_level": "CRITICAL",
                "status": "RESOLVED",
                "sla_hours": 6,
                "sla_deadline": (now - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"),
                "latitude": 28.5921,
                "longitude": 77.0460,
                "address": "Sector 11 Main Road, Near Model School, Dwarka",
                "ward": "Ward 22 - West Delhi",
                "citizen_name": "Vikram Adhikari",
                "citizen_phone": "+91 99100 87342",
                "photo_path": "samples/electrical_hazard.jpg",
                "resolution_photo_path": "samples/repaired_road_success.jpg",
                "resolution_notes": "Feeder de-energized, snapped conductor replaced and elevated to 18ft clearance. Tested live.",
                "hazards": json.dumps(["Electrocution danger", "Short circuit / Fire hazard", "Pedestrian life risk"]),
                "upvotes": 41,
                "created_at": (now - timedelta(hours=8)).strftime("%Y-%m-%d %H:%M"),
                "updated_at": (now - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
            },
            {
                "id": "CIV-2026-1030",
                "title": "Damaged storm drain grating creating wheel trap",
                "description": "Cast iron drain cover broken into halves. Tyres get caught, posing severe risk to cyclists.",
                "category": "ROADS",
                "category_name": "Roads & Potholes",
                "department": "Public Works Department (PWD)",
                "severity_score": 6.8,
                "severity_level": "HIGH",
                "status": "VERIFIED",
                "sla_hours": 36,
                "sla_deadline": (now - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M"),
                "latitude": 28.7041,
                "longitude": 77.1025,
                "address": "Outer Ring Road, Sector 3, Rohini",
                "ward": "Ward 15 - North Delhi",
                "citizen_name": "Pooja Verma",
                "citizen_phone": "+91 98711 55678",
                "photo_path": "samples/pothole_severe.jpg",
                "resolution_photo_path": "samples/repaired_road_success.jpg",
                "resolution_notes": "Heavy-duty ductile iron grating installed and welded to prevent theft.",
                "hazards": json.dumps(["Two-wheeler skid risk", "Pedestrian injury risk"]),
                "upvotes": 19,
                "created_at": (now - timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
                "updated_at": (now - timedelta(hours=5)).strftime("%Y-%m-%d %H:%M")
            }
        ]

        for s in samples:
            cursor.execute("""
            INSERT INTO grievances (
                id, title, description, category, category_name, department,
                severity_score, severity_level, status, sla_hours, sla_deadline,
                latitude, longitude, address, ward, citizen_name, citizen_phone,
                photo_path, resolution_photo_path, resolution_notes, hazards,
                upvotes, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                s["id"], s["title"], s["description"], s["category"], s["category_name"],
                s["department"], s["severity_score"], s["severity_level"], s["status"],
                s["sla_hours"], s["sla_deadline"], s["latitude"], s["longitude"],
                s["address"], s["ward"], s["citizen_name"], s["citizen_phone"],
                s["photo_path"], s["resolution_photo_path"], s["resolution_notes"],
                s["hazards"], s["upvotes"], s["created_at"], s["updated_at"]
            ))
        conn.commit()
    conn.close()

def get_all_grievances(category=None, status=None, ward=None, search=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM grievances WHERE 1=1"
    params = []

    if category and category != "ALL":
        query += " AND category = ?"
        params.append(category)
    if status and status != "ALL":
        query += " AND status = ?"
        params.append(status)
    if ward and ward != "ALL":
        query += " AND ward = ?"
        params.append(ward)
    if search:
        query += " AND (title LIKE ? OR id LIKE ? OR address LIKE ? OR department LIKE ?)"
        s = f"%{search}%"
        params.extend([s, s, s, s])

    query += " ORDER BY severity_score DESC, created_at DESC"
    cursor.execute(query, params)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()

    for r in rows:
        if r.get("hazards"):
            try:
                r["hazards_list"] = json.loads(r["hazards"])
            except:
                r["hazards_list"] = []
        else:
            r["hazards_list"] = []
    return rows

def get_grievance_by_id(grievance_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grievances WHERE id = ?", (grievance_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        d = dict(row)
        try:
            d["hazards_list"] = json.loads(d.get("hazards") or "[]")
        except:
            d["hazards_list"] = []
        return d
    return None

def add_grievance(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO grievances (
        id, title, description, category, category_name, department,
        severity_score, severity_level, status, sla_hours, sla_deadline,
        latitude, longitude, address, ward, citizen_name, citizen_phone,
        photo_path, resolution_photo_path, resolution_notes, hazards,
        upvotes, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["id"], data["title"], data.get("description", ""), data["category"],
        data["category_name"], data["department"], data["severity_score"],
        data["severity_level"], data.get("status", "TRIAGED"), data["sla_hours"],
        data["sla_deadline"], data["latitude"], data["longitude"], data["address"],
        data["ward"], data.get("citizen_name", "Anonymous Citizen"),
        data.get("citizen_phone", "N/A"), data.get("photo_path"),
        data.get("resolution_photo_path"), data.get("resolution_notes"),
        json.dumps(data.get("hazards", [])), data.get("upvotes", 1),
        data["created_at"], data["updated_at"]
    ))
    conn.commit()
    conn.close()

def update_grievance_status(grievance_id, status, notes=None, resolution_photo=None):
    conn = get_connection()
    cursor = conn.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if resolution_photo and notes:
        cursor.execute("""
        UPDATE grievances 
        SET status = ?, resolution_notes = ?, resolution_photo_path = ?, updated_at = ?
        WHERE id = ?
        """, (status, notes, resolution_photo, now_str, grievance_id))
    elif notes:
        cursor.execute("""
        UPDATE grievances 
        SET status = ?, resolution_notes = ?, updated_at = ?
        WHERE id = ?
        """, (status, notes, now_str, grievance_id))
    else:
        cursor.execute("""
        UPDATE grievances 
        SET status = ?, updated_at = ?
        WHERE id = ?
        """, (status, now_str, grievance_id))
    
    conn.commit()
    conn.close()

def upvote_grievance(grievance_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE grievances SET upvotes = upvotes + 1 WHERE id = ?", (grievance_id,))
    conn.commit()
    conn.close()

def get_analytics():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM grievances")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM grievances WHERE status IN ('RESOLVED', 'VERIFIED')")
    resolved = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM grievances WHERE severity_level = 'CRITICAL'")
    critical = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(severity_score) FROM grievances")
    avg_sev = cursor.fetchone()[0] or 0.0

    cursor.execute("SELECT department, COUNT(*) as count FROM grievances GROUP BY department ORDER BY count DESC")
    dept_distribution = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT ward, COUNT(*) as count FROM grievances GROUP BY ward ORDER BY count DESC")
    ward_distribution = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT status, COUNT(*) as count FROM grievances GROUP BY status")
    status_distribution = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return {
        "total_grievances": total,
        "resolved_grievances": resolved,
        "resolution_rate_pct": round((resolved / total * 100) if total > 0 else 0, 1),
        "critical_count": critical,
        "avg_severity": round(avg_sev, 1),
        "dept_distribution": dept_distribution,
        "ward_distribution": ward_distribution,
        "status_distribution": status_distribution
    }

# Run init & seed
init_db()
seed_default_grievances()
