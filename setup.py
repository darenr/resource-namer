# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

"""Build and installation script for names_generator."""


# standard libs
import re
from setuptools import setup, find_packages


# get long description from README.rst
with open("README.md", mode="r") as readme:
    long_description = readme.read()


# get package metadata by parsing __meta__ module
with open("academic_avocado_namer/__meta__.py", mode="r") as source:
    content = source.read().strip()
    metadata = {
        key: re.search(key + r'\s*=\s*[\'"]([^\'"]*)[\'"]', content).group(1)
        for key in [
            "__version__",
            "__authors__",
            "__contact__",
            "__description__",
            "__license__",
        ]
    }


setup(
    name="academic-avocado-namer",
    version=metadata["__version__"],
    author=metadata["__authors__"],
    author_email=metadata["__contact__"],
    description=metadata["__description__"],
    license=metadata["__license__"],
    keywords="random name generator",
    url="https://github.com/darenr/academic-avocado-namer",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
