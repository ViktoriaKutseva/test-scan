from pathlib import Path

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    files = list(root.rglob("*.py"))
    print(f"python_files={len(files)}")
