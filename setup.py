from setuptools import setup

import os, sys, cage

setup(
    name="cage",
    packages = ["cage"],
    version = 0.1
    entry_points = {
        "console_scripts": [
            "run = run",
        ]
    },
    description = "Game Engine Library",
    long_description = "Game Engine Library",
    long_description_content_type = "text/markdown",
    url = "https://github.com/MuhammedAky/Cage",
    author = "Muhammed Can Akyüz",
    author_email = "muhammed.cnaky@gmail.com",
    license = "MIT",
    include_package_data = True,
    install_requires = "requirements.txt"
)