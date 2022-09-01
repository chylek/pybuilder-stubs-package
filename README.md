# PyBuilder plugin that creates *-stubs package for your project

This plugin adds `stubs_publish` and `stubs_upload` tasks that you can use in
your build script.

Using MyPy's `stubgen` it creates type hinting stubs (*.pyi files) as a separate
package. This stubs-only package is named with the `-stubs` suffix following
[PEP 561](https://peps.python.org/pep-0561/). For a pybuilder project `foo` this
would create stubs-only package `foo-stubs`.

The stubs-only package's version will be the same as version of your pybuilder
project and the stubs-only package will have install dependency on that specific
version of the project.

## Tasks

### `stubs_publish`

Generates *.pyi files using `stubgen` on your project's source files, adds
appropriate setup.py file, and creates a wheel.

### `stubs_upload`

Uses twine to upload the -stubs package.

## Properties

The plugin understands additional properties in your project that 
control flags for the stubgen.

### `stubs_include_private` 

boolean, adds the `--include-private` flag to `stubgen` if set to `True`.

### `stubs_include_docstrings`

boolean, adds the `--include-docstrings` flag to `stubgen` if set to `True`.
Stubgen then includes docstrings for classes and methods in the stubs.

*Note that this flag is not merged yet ([PR #13284](https://github.com/python/mypy/pull/13284))*