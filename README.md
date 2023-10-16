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
```

Make sure to replace `"YOUR_API_KEY"` with your actual Curated API key in order to gain access to your account via the API. Please see the documentation provided by Curated for [getting started with the Curated API](https://support.curated.co/help/getting-started-with-the-api)

### Setting publication id

_You must perform this step or you cannot communicate with the Curated API_

To target any individual publication within the API you'll need to get its id from within Curated. You can also achieve this by reviewing the results from the following API call:

```python
print(curated_api.request_all_publications())
```

This will return a JSON response containing all publications within your account. Choose the ID from the one you want to target and assign that to the `curated_api` instance you have created.

```python
publication_id = "YOUR_PUBLICATION_ID"
curated_api.set_publication_id(publication_id)
```

###

## Tests

The package comes with a set of tests. To run the tests:

1. Navigate to the package directory.
2. Run the test files using Python:

```
python -m unittest tests/test_curated_api.py
python -m unittest tests/test_curated_category.py
python -m unittest tests/test_curated_link.py
```

## License

This package is licensed under the MIT license. See the LICENSE file for more details.
