# TheLanguage1

[![CI](https://github.com/davidbrownell/TheLanguage1/actions/workflows/standard.yaml/badge.svg?event=push)](https://github.com/davidbrownell/TheLanguage1/actions/workflows/standard.yaml)
[![Code Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/davidbrownell/4065d22fd6323840e81951a3bd271e1c/raw/TheLanguage1_coverage.json)](https://github.com/davidbrownell/TheLanguage1/actions)
[![License](https://img.shields.io/github/license/davidbrownell/TheLanguage1?color=dark-green)](https://github.com/davidbrownell/TheLanguage1/blob/master/LICENSE.txt)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/davidbrownell/TheLanguage1?color=dark-green)](https://github.com/davidbrownell/TheLanguage1/commits/main/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/TheLanguage1?color=dark-green)](https://pypi.org/project/thelanguage1/)
[![PyPI - Version](https://img.shields.io/pypi/v/TheLanguage1?color=dark-green)](https://pypi.org/project/thelanguage1/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/TheLanguage1)](https://pypistats.org/packages/thelanguage1)

# TheLanguage1
Initial implementation of \"TheLanguage\".

### Overview

TODO: Complete this section

### How to use TheLanguage1

TODO: Complete this section

## Installation via Executable

Download an executable for Linux, MacOS, or Windows to use the functionality provided by this repository without a dependency on [Python](https://www.python.org).

1. Download the archive for the latest release [here](https://github.com/davidbrownell/TheLanguage1/releases/latest); the files will begin with `exe.` and contain the name of your operating system.
2. Decompress the archive

## Installation via pip

Install the TheLanguage1 package via [pip](https://pip.pypa.io/en/stable/) (Package Installer for Python) to use it with your python code.

`pip install TheLanguage1`

## Local Development

Follow these steps to prepare the repository for local development activities.

1) Clone this repository
2) Bootstrap the local repository by running...
    | Operating System | Command |
    | --- | --- |
    | Linux / MacOS | <p>Standard:<br/>`Bootstrap.sh`</p><p>Standard + packaging:<br/>`Bootstrap.sh --package`</p> |
    | Windows | <p>Standard:<br/>`Bootstrap.cmd`</p><p>Standard + packaging:<br/>`Bootstrap.cmd --package`</p> |
3) Activate the development environment by running...
    | Operating System | Command |
    | --- | --- |
    | Linux / MacOS | `. ./Activate.sh` |
    | Windows | `Activate.cmd` |
4) Invoke `Build.py`
    | Command | Description | Example | Notes |
    | --- | --- | --- | --- |
    | `black` | Validates that the source code is formatted by [black](https://github.com/psf/black). | <p>Validation:<br/>`python Build.py black`</p><p>Perform formatting:<br/>`python Build.py black --format`</p> | |
    | `pylint` | Validates the source code using [pylint](https://github.com/pylint-dev/pylint). | `python Build.py pylint` | |
    | `pytest` | Runs automated tests using [pytest](https://docs.pytest.org/). | <p>Without Code Coverage:<br/>`python Build.py pytest`</p><p>With Code Coverage:<br/>`python Build.py pytest --code-coverage`</p> | |
    | `update_version` | Updates the [semantic version](https://semver.org/) of the package based on git commits using [AutoGitSemVer](https://github.com/davidbrownell/AutoGitSemVer). | `python Build.py update_version` | |
    | `package` | Creates a Python wheel package for distribution; outputs to the `/dist` directory. | `python Build.py package` | Requires `--package` when bootstrapping in step #2. |
    | `publish` | Publishes a Python wheel package to [PyPi](https://pypi.org/). | <p>https://test.pypi.org:<br/>`python Build.py publish`</p><p>https://pypi.org:<br/>`python Build.py publish --production`</p> | Requires `--package` when bootstrapping in step #2. |
    | `build_binary` | Builds an executable for your package that can be run on machines without a python installation; outputs to the `/build` directory. | `python Build.py build_binary` | Requires `--package` when bootstrapping in step #2. |

5) [Optional] Deactivate the development environment by running...
    | Operating System | Command |
    | --- | --- |
    | Linux / MacOS | `. ./Deactivate.sh` |
    | Windows | `Deactivate.cmd` |

## License

TheLanguage1 is licensed under the <a href="https://choosealicense.com/licenses/mit/" target="_blank">MIT</a> license.
