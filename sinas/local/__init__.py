import subprocess


def build_jekyll(jekyll_exe, source_dir, dest_dir):
    """Builds the project in `source_dir` with the provided jekyll executable and places the result in `dest_dir`"""
    process = subprocess.run([jekyll_exe, "build", "--source", source_dir, "--destination", dest_dir])
    return process.returncode
