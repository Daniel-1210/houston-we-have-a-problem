thonimport json
import logging

logging.basicConfig(level=logging.INFO)

def export_json(data, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Exported {len(data)} records to {file_path}")
    except Exception as e:
        logging.error(f"Failed to export JSON: {e}")