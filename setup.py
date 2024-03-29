import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pngdeband",
    version="0.1.0",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="24bit PNG to 15bit PNG with de-banding filter for X68k",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/pngdeband",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pngdeband=pngdeband.pngdeband:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    setup_requires=["setuptools"],
    install_requires=["ffmpeg-python"],
)
