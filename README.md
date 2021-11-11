# yodatranslator

## Overview

yodatranslator is a simple translator English to Yoda-language.

Project is created for educational purposes. It is intended to test a project structure and distribution package
structure.

## Configuration instructions

If you would like to use yodatranslator from CLI I don't recommend to use virtual environment.

Before installation It may be neccessary to upgrade your building tools:

```shell
python -m pip install -U pip setuptools wheel
```

## Installation instructions

Choose your installation method:

### I. Directly from github:
1. Type in your console:
```shell
pip install git+https://github.com/donpolaco/yodatranslator.git
```
2. That's all!



###II. Indirect method:

1. Download the repository from: https://github.com/donpolaco/yodatranslator (button: Code/download ZIP) and unzip it
   
or clone the repository by typing:
```shell
git clone https://github.com/donpolaco/yodatranslator.git
``` 

2. Go to the project directory:
```shell
cd yodatranslator
```
3. Install from direcory:
```shell
pip install .
```

## Operating instructions

Yodatranslator may be use as a python package or as a command line tool.

1. In order to use it as a command line tool just type:

```shell
yodatranslator words [words ...] 
```

Type:

```shell
yodatranslator --help 
```

for help.

2. In order to use it as a python package simply import it:

```python
import yodatranslator
```

## A file manifest
```
yodatranslator
│   .gitignore
│   LICENSE
│   MANIFEST.in
│   pyproject.toml
│   README.md
│   requirements.txt
│   setup.cfg
│   
└───src
    └───yodatranslator
            translator.py
            __init__.py
            __main__.py
```
## Copyright and licensing information

MIT License

Copyright (c) 2021 donpolaco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Contact information

**donpolaco**

**email:** paszczap [ at ] poczta [ dot ] fm

## Known bugs[0]

None.

## Troubleshooting[0]

None.

## Credits and acknowledgments

- The project is inspired by [this video](https://www.youtube.com/watch?v=zF2oVp8ZUdM)
- The README.md structure is inspired by Filip Cornell's template
  form [this project](https://github.com/Filco306/python-project-template) originally retreived
  from [Wikipedia](https://en.wikipedia.org/wiki/README)
- The .gitignore created using [gitignore.io](https://www.toptal.com/developers/gitignore)
- Used [funtranlations.com API description](https://funtranslations.com/api)
- MIT license is fetched from [github.com](https://github.com/).

## Changelog

### 0.0.5 - [2021.11.11]

#### Changed

- the first version using new distribution format
- the first version on github

## News

### 0.0.5 - [2021.11.11]

#### Changed

- Now you can easily install package using pip

