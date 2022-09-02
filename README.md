![academic avocado](https://github.com/darenr/academic-avocado-namer/blob/main/academic-avocado.png?raw=true)


# academic-avocado-namer

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

# Use a different join character:

>>> generate_name(joiner=".")

# seed with a random number

>>> generate_name(seed=42)

# use plants instead of animals

>>> generate_name(prefer_plants=True)

```


## Example output (with prefer_plants=False)

```
vain-viper
nocturnal-nightingale
annual-alligator
ultimate-unicorn
careless-chicken
aggressive-armadillo
deafening-dolphin
worrisome-wasp
whopping-woodcock
bright-butterfly
truthful-toad
masculine-mermaid
experienced-eagle
worse-worm
precious-penguin
precious-partridge
```
