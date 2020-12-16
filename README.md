# python-repo-example
A minimal example of a Python project


## Installation

1. (optional) create a virtual environement
   ```bash
   conda env create -n example-env python=3.8
   conda activate example-env
   ```

2. Install requirements and the package
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Usage

Import and use the package. For instance,
```py
from repo_example.base import add_int

add_int(1, 2)   # returns 3
```

### Running tests

Tests can be run with [pytest](https://docs.pytest.org/en/latest/)
```
pytest
```

### Code style

Use [black](https://pypi.org/project/black/) Python extension and
[nb-black](https://github.com/dnanhkhoa/nb_black) to auto-format jupyter
notebooks.
 



