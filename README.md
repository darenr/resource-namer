![academic avocado](https://github.com/darenr/academic-avocado-namer/blob/main/academic-avocado.png?raw=true)

*DallE generated project mascot*


# academic-avocado-namer

[![License](https://img.shields.io/badge/license-Apache-blue.svg?style=flat)](https://www.apache.org/licenses/LICENSE-2.0)
[![PyPI Version](https://img.shields.io/pypi/v/academic-avocado-namer.svg?style=flat&color=blue)](https://pypi.org/project/academic-avocado-namer)
[![Python Versions](https://img.shields.io/pypi/pyversions/academic-avocado-namer.svg?logo=python&logoColor=white&style=flat)](https://pypi.org/project/academic-avocado-namer)


Name things with better names than GUIDs, use in combination with
GUIDs or datetimes.

## module main

```
python -m academic_avocado_namer
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
>>> from academic_avocado_namer import generate_name
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

https://pypi.org/project/academic-avocado-namer