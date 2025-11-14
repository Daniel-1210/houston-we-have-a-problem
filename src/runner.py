thonimport json
import logging
from pathlib import Path
from extractors.issue_parser import parse_issue_text
from outputs.exporters import export_json
from config.settings import Settings

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def main():
    settings = Settings.load()
    input_path = Path(settings["inputFile"])

    if not input_path.exists():
        logging.error(f"Input file not found: {input_path}")
        return

    issues = []

    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            issue_data = parse_issue_text(line, source_url=settings["defaultSourceUrl"])
            issues.append(issue_data)

    output_path = Path(settings["outputFile"])
    export_json(issues, output_path)

    logging.info(f"Extraction complete → {output_path.absolute()}")

if __name__ == "__main__":
    main()