# resource-namer

[![License](https://img.shields.io/badge/license-Apache-blue.svg?style=flat)](https://www.apache.org/licenses/LICENSE-2.0)
[![PyPI Version](https://img.shields.io/pypi/v/resource-namer.svg?style=flat&color=blue)](https://pypi.org/project/resource-namer)
[![Python Versions](https://img.shields.io/pypi/pyversions/resource-namer.svg?logo=python&logoColor=white&style=flat)](https://pypi.org/project/resource-namer)


Name things with better names than GUIDs, use in combination with
GUIDs or datetimes.

## module main

```
python -m resource_namer
```

## local development

```
pip install -e .
```

## run tests:

```
pip install -e .
pytest
```

## Example API usage

```
>>> from resource_namer import generate_name
>>> generate_name()
'handy-human'

# Use a different join character:

>>> generate_name(joiner=".")
'corny.camel'

# seed with a random number

>>> generate_name(seed=42)
'delightful-donkey'

# use plants instead of animals

>>> generate_name(prefer_plants=True)
'irritating-inkberry'

```

https://pypi.org/project/resource-namer
