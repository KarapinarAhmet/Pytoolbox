import re

VERSION_FILE = "tools/version.py"

def bump_version(part="patch"):
    with open(VERSION_FILE, "r") as f:
        content = f.read()

    version_match = re.search(r'__version__ = "(\d+)\.(\d+)\.(\d+)"', content)
    if not version_match:
        print("Versiyon bilgisi bulunamadı!")
        return

    major, minor, patch = map(int, version_match.groups())

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    else:  # patch
        patch += 1

    new_version = f'__version__ = "{major}.{minor}.{patch}"'

    new_content = re.sub(r'__version__ = "\d+\.\d+\.\d+"', new_version, content)

    with open(VERSION_FILE, "w") as f:
        f.write(new_content)

    print(f"Versiyon güncellendi: {new_version}")

if __name__ == "__main__":
    import sys
    part = sys.argv[1] if len(sys.argv) > 1 else "patch"
    bump_version(part)
