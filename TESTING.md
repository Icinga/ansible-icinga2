# TESTING
This role includes everything necessary to be tested with [Molecule](https://molecule.readthedocs.io/en/latest/). The
[installation documentation](https://molecule.readthedocs.io/en/latest/installation.html) provides
a great walk-through to get started.

## Running tests
Run all tests (all scenarios on all platforms):

``` shell
molecule test --all
```

Run specific scenario (scenario `default` is used by default)

``` shell
molecule test -s default
```

Don't destroy container after running the tests:

``` shell
molecule test --destroy never
```

Run only linter

``` shell
molecule lint
```

Run only syntax checks

``` shell
molecule syntax
```