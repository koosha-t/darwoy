import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


with open("requirements.txt", "r") as req:
    external_packages = req.read()

setuptools.setup(
    name = "mine-digger",
    version = "0.0.1",
    author = "Koosha Tahmasebipour",
    author_email = "kooshi.ml@gmail.com",
    description = "crawling the web, mining the social web.",
    long_description = long_description,
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=external_packages,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)