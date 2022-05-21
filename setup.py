from setuptools import setup, find_packages
from pathlib import Path
from osu2mp3.__init__ import VERSION

setup(
    name='osu2mp3',
    version=VERSION,
    description="Convert your osu! beatmaps (.osz) to properly-tagged .mp3 files",
    long_description=Path.joinpath(Path(__file__).parent.resolve(), "README.md").open().read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hewlett-packard-lovecraft/osu2mp3",
    author="hewlett-packard-lovecraft",
    author_email="hxia05@protonmail.com",
    license="MIT",
    packages=find_packages(
        where='.',
        include=['osu2mp3*'],  # ["*"] by default
        exclude=['tests'],  # empty by default
    ),
    include_package_data=True,
    install_requires=["eyed3"],
    keywords=["mp3", "osu"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "osu2mp3=osu2mp3.__main__:main",
        ]
    },
)
