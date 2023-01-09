Usage
=====

.. _installation:

Installation
------------

To use ``resource-namer``, first install it using pip:

.. code-block:: console

   $ pip install resource-namer

Example Usage
-------------

.. code-block:: python3

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
