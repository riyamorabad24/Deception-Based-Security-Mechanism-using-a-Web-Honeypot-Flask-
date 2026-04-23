"""
Deception-Based Security System — Bank Login Honeypot
======================================================
A fake bank login page that looks real but is actually a trap.
Any login attempt is treated as suspicious and logged with full details.

Author: [Your Name]
"""

from flask import Flask, request, render_template, redirect, url_for
import json
import os
from datetime import datetime, timezone

app = Flask(__name__)

LOG_FILE = "honeypot_log.json"


# ─────────────────────────────────────────────
# LOAD / SAVE LOG
# ─────────────────────────────────────────────

def load_log() -> list:
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)


def save_log(data: list):
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ─────────────────────────────────────────────
# LOG AN ALERT
# ─────────────────────────────────────────────

def log_alert(event: str, details: dict):
    """Save a suspicious activity alert to the log file."""
    log = load_log()
    entry = {
        "id":        len(log) + 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event":     event,
        "details":   details,
        "status":    "SUSPICIOUS ACTIVITY DETECTED"
    }
    log.append(entry)
    save_log(log)

    # Print alert to terminal
    print("\n" + "!" * 60)
    print("  🚨 HONEYPOT ALERT!")
    print(f"  Event     : {event}")
    print(f"  Time      : {entry['timestamp']}")
    for key, value in details.items():
        print(f"  {key:<10}: {value}")
    print("!" * 60 + "\n")


# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.route("/", methods=["GET"])
def home():
    """Redirect root to the fake login page."""
    return redirect(url_for("login"))


@app.route("/login", methods=["GET"])
def login():
    """Show the fake bank login page."""
    # Log the fact that someone even visited the page
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent", "Unknown")

    log_alert("PAGE_VISITED", {
        "IP Address": ip,
        "User-Agent": user_agent,
        "Page":       "/login"
    })

    return render_template("login.html", error=None)


@app.route("/login", methods=["POST"])
def login_post():
    """Capture and log any login attempt."""
    username   = request.form.get("username", "")
    password   = request.form.get("password", "")
    ip         = request.remote_addr
    user_agent = request.headers.get("User-Agent", "Unknown")

    # Log the full attempt
    log_alert("LOGIN_ATTEMPT", {
        "IP Address": ip,
        "Username":   username,
        "Password":   password,
        "User-Agent": user_agent
    })

    # Always reject — redirect to alert page
    return redirect(url_for("alert"))


@app.route("/alert")
def alert():
    """Show suspicious activity warning page."""
    return render_template("alert.html")


@app.route("/logs")
def view_logs():
    """Show all captured honeypot alerts (admin view)."""
    log = load_log()
    return render_template("logs.html", logs=log)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  HONEYPOT SYSTEM STARTED")
    print("=" * 60)
    print("  Fake bank login running at: http://127.0.0.1:5000")
    print("  View captured alerts at  : http://127.0.0.1:5000/logs")
    print("  Press CTRL+C to stop")
    print("=" * 60 + "\n")
    app.run(debug=False)