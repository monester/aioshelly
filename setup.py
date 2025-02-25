"""Setup module for aioshelly."""
from pathlib import Path

from setuptools import find_packages, setup

PROJECT_DIR = Path(__file__).parent.resolve()
README_FILE = PROJECT_DIR / "README.md"
VERSION = "6.0.0"


setup(
    name="aioshelly",
    version=VERSION,
    license="Apache License 2.0",
    url="https://github.com/home-assistant-libs/aioshelly",
    author="Paulus Schoutsen",
    author_email="paulus@home-assistant.io",
    description="Asynchronous library to control Shelly devices.",
    long_description=README_FILE.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
    package_data={"aioshelly": ["py.typed"]},
    zip_safe=True,
    platforms="any",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
