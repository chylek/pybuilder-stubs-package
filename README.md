# PyBuilder plugin that creates "*-stubs" package for your project using MyPy's stubgen

This plugin adds `stubs_publish` and `stubs_upload` tasks.

Using MyPy's stubgen it creates type hinting stubs (*.pyi files) 
as a separate package. This stubs-only package is identified in 
accordance to PEP 561 with the `-stubs` suffix in its name.

The package name comes from the `name` and `version` of your pybuilder project.

## `stubs_publish`

Calls `stubgen` with `--include-private --include-docstrings` arguments,
adds appropriate setup.py file, and creates a wheel.

## `stubs_upload`

Uses twine to upload the -stubs package.