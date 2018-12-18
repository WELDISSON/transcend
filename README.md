# transcend
> Repository with example for UI test automation using behave and splinter for python.
> Repository used in the talk **["Organizing your test suite with Page Objects pattern"](https://goo.gl/dtdrfH)**

---
## Table of Contents
> Índice `README`.
- [Clone](#clone)
- [Prerequisite](#prerequisite)
- [Installation](#installation)
- [Support](#support)
- [License](#license)

---
### Clone
- Clone this repo to your local machine using `https://github.com/WELDISSON/transcend.git`
```shell
$ git clone https://github.com/WELDISSON/transcend.git
````

---
## Prerequisite
- [python install](https://www.python.org/downloads/release/python-2715/)
- [pip install](https://pip.pypa.io/en/stable/installing/)

---
## Installation
- Install all dependencies (test/requirement.txt)

```shell
$ (sudo) pip install -r requirement.txt
```

---
### Run application
- run the command to lift the application
```shell
$ python -m SimpleHTTPServer 8000
```
- check in browser url: http://localhost:8000

--- 
### Run test
- Execute your tests no page objects:

```shell

$ behave test/
```
- Execute your tests with page objects:

```shell

$ behave test_po/
```
---
## Support
- E-mail: `weldisson.araujo@gmail.com`

---
## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2018 © <a target="_blank">Weldisson Araujo</a>

---
