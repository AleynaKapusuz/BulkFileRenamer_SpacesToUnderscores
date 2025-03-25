import os

base_dir = r"your_path"

for i in range(0, 31):
    folder_path = os.path.join(base_dir, str(i))

    for filename in os.listdir(folder_path):
        if ' ' in filename:
            new_filename = filename.replace(' ', '_')

            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            os.rename(old_path, new_path)

            print(f"Renamed: {old_path} -> {new_path}")
