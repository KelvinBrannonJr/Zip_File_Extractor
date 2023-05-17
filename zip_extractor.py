import zipfile
from pathlib import Path

# Use 'r' in absolute paths for windows escape character error
# r - gets the raw string form for the absolute path string
compress_file_path = Path(r"D:\python Zip File Extractor\compressed.zip")
destination_file_path = Path(r"D:\python Zip File Extractor\files")


def extract_archive(archive_path, destination_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_dir)


if __name__ == "__main__":
    extract_archive(compress_file_path, destination_file_path)
