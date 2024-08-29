import os


class Tools:
    def __init__(self) -> None:
        pass

    def replace_in_filenames(self, directory, old: str, new: str):
        for filename in os.listdir(directory):
            name, ext = os.path.splitext(filename)

            new_name = name.replace(old, new) + ext

            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)

            if old_file != new_file:
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {new_name}")
