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
    
    def output_ocr_results(self, results: list) -> None:
        with open("./src/output/ocr_results.txt", "w", encoding="utf-8") as f:
            for idx, result in enumerate(results):
                f.write(f"Image {idx + 1}:\n")
                f.write("Boxes:\n")
                for box in result["boxes"]:
                    f.write(f"  {box}\n")
                f.write("Texts:\n")
                for text in result["texts"]:
                    f.write(f"  {text}\n")
                f.write("\n")  # Add a newline for separation between images
