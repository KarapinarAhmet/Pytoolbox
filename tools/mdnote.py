import os
from datetime import datetime

def create_note(content):
    folder = "notes"
    if not os.path.exists(folder):
        os.makedirs(folder)
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".md"
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Not - {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(content + "\n")
    print(f"Not oluşturuldu: {filepath}")
