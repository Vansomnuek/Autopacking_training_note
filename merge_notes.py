import os

base_dir = "training-notes"

def merge_notes(folder_path):
    """
    รวมไฟล์ Markdown จาก subfolder ของ folder_path
    โดยตรวจสอบไฟล์ทั้งหมดที่มีใน subfolder แรก
    แล้วรวมไฟล์ตามชื่อเดียวกันจากทุกคน
    """
    # หา list ของไฟล์ทั้งหมดใน subfolder แรก
    subfolders = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    if not subfolders:
        return

    first_sub = os.path.join(folder_path, subfolders[0])
    md_files = [f for f in os.listdir(first_sub) if f.endswith(".md")]

    for filename in md_files:
        merged_content = []
        output_file = os.path.join(folder_path, filename)

        for sub in sorted(subfolders):
            sub_path = os.path.join(folder_path, sub)
            file_path = os.path.join(sub_path, filename)

            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                merged_content.append(f"## {sub}\n\n{content}\n")

        if merged_content:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("\n\n---\n\n".join(merged_content))
            print(f"✅ Created {output_file}")

# loop ทุก main folder เช่น CTU, RDS, WCS
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        merge_notes(folder_path)
