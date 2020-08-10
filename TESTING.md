# TESTING

This role includes everything necessary to be tested with [Molecule](https://molecule.readthedocs.io/en/latest/).

To install all required dependencies in a local development environment you can execute the following:

```bash
# If not existent
python3 -m venv env

source env/bin/activate

pip3 install --upgrade -r requirements.txt
```

## Running tests

To run the default scenario just execute

```bash
molecule test
```

To execute the role and preserve the containers use

```bash
molecule converge
```

After that you can manually execute all tests with

```bash
molecule verify
```

For more details on how to use molecule please refer to the documentation.
