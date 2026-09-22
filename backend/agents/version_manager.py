import json
from pathlib import Path


OUTPUT_DIR = Path("outputs")
VERSION_FILE = OUTPUT_DIR / "versions.json"

OUTPUT_DIR.mkdir(exist_ok=True)


def load_versions():
    if not VERSION_FILE.exists():
        return {
            "current_file": None,
            "versions": []
        }

    with open(VERSION_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_version(file_path: str):
    data = load_versions()

    version_number = len(data["versions"]) + 1

    version = {
        "version": version_number,
        "file": file_path
    }

    data["versions"].append(version)
    data["current_file"] = file_path

    with open(VERSION_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    return version


def get_current_file():
    data = load_versions()
    return data["current_file"]


def get_versions():
    return load_versions()["versions"]