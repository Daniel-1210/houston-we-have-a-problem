thonimport logging
from datetime import datetime
from .utils_time import utc_now_iso

logging.basicConfig(level=logging.INFO)

def parse_issue_text(text: str, source_url: str):
    """
    Parses a raw problem line.
    """
    title = "Houston, we have a problem!" if "problem" in text.lower() else "Detected Issue"
    summary = text[:120] if len(text) > 0 else "No description provided."
    severity = "high" if "error" in text.lower() or "critical" in text.lower() else "unknown"

    return {
        "problemTitle": title,
        "problemSummary": summary,
        "severityLevel": severity,
        "detectedAt": utc_now_iso(),
        "sourceUrl": source_url,
        "rawContent": text,
    }