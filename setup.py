from typing import List

import setuptools


def read_multiline_as_list(file_path: str) -> List[str]:
    with open(file_path) as fh:
        contents = fh.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = read_multiline_as_list("requirements.txt")

classifiers = read_multiline_as_list("classifiers.txt")

setuptools.setup(
    name="multibase_dataclass",
    version="0.1.0.2020.10.23",
    author="Nei Cardoso de Oliveira Neto",
    author_email="nei.neto@hotmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cardoso-neto/multibase_dataclass",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=classifiers,
    keywords='multibase encodings wrapper dataclass object-oriented',
    # entry_points = {
    #     'console_scripts': [
    #         '',
    #     ],
    # },
    python_requires=">=3.8",
    install_requires=requirements,
)
