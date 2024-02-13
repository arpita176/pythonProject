import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        dest_path = pathlib.Path(dest_dir, 'compressed.zip')
        for filepath in filepaths:
            archive.write(filepath)
