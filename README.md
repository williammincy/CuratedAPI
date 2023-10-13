# Example Package: Curated API

This package provides a Python interface for the Curated API. With it, you can easily manage issues, links, and subscribers within publications using the `CuratedApi` class.

## Installation

To install the package, you can use pip:

```
pip install curatedapi_wm
```

## Usage

To use the `CuratedApi` class within your Python project:

```python
from curatedapi import CuratedApi

api_key = "YOUR_API_KEY"
curated_api = CuratedApi(api_key)
# ... (use the methods of the curated_api instance as needed)
```

Make sure to replace `"YOUR_API_KEY"` with your actual Curated API key in order to gain access to your account via the API. Please see the documentation provided by Curated for [getting started with the Curated API](https://support.curated.co/help/getting-started-with-the-api)

## Tests

The package comes with a set of tests. To run the tests:

1. Navigate to the package directory.
2. Run the test files using Python:

```
python -m unittest tests/test_section_1.py
python -m unittest tests/test_section_2.py
python -m unittest tests/test_section_3.py
```

## License

This package is licensed under the MIT license. See the LICENSE file for more details.
