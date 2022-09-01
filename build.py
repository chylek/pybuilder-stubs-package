# -*- coding: utf-8 -*-
import os

from pybuilder.core import use_plugin, init, Author

use_plugin("python.distutils")


def read_from(filename):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)) as f:
        result = f.read()
    return result


default_task = ["publish", "clean"]

name = "pybuilder-stubs-package"
summary = "PyBuilder plugin that creates \"*-stubs\" package for your project using MyPy's stubgen"
authors = [Author('Adam Chýlek', 'adam.chylek@amitia-ai.com')]
version = read_from('VERSION')
license = 'MIT'
url = 'https://github.com/chylek/pybuilder-stubs-package'

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
]

description = """
TODO
"""

@init
def set_properties(project):
    project.set_property("name", name)
    project.set_property("version", version)

    build_dir = os.path.join("releases", "$name-$version")
    project.set_property("dir_dist", build_dir)
    project.set_property("distutils_classifiers", classifiers)
    project.set_property("distutils_commands", ["sdist", "bdist_egg", "bdist_wheel"])

    project.set_property("copy_resources_glob", ["MANIFEST.in", "VERSION", "README.md", "LICENSE"])
    project.set_property("copy_resources_target", "${dir_dist}")
