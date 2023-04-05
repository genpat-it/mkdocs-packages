# MkDocscs packages

Collection of MkDocs packages we use to build our documentation.

## Introduction

We use [MkDocs](https://www.mkdocs.org) to make documentation of our projects and in this repo we are collecting all packages internally developed to fit some particular needs.

The packages are divided in two folders `mkdocs-plugins` and `mkdocs-themes`, respectively for MkDocs plugins and MkDocs themes (actually we have just one theme :D).

You will find below some useful information on how to build and publish your own plugin or your own theme.

## PyPi links to pakcages

**Plugins**

* [mkdocs-izsam-search](https://pypi.org/project/mkdocs-izsam-search/)
* [mkdocs-izsam-video](https://pypi.org/project/mkdocs-izsam-video/)

**Theme**

* [mkdocs-bionformatic-izsam-theme](https://pypi.org/project/mkdocs-bionformatic-izsam-theme/)

## Create pip packages

Source: [How to write your own Python Package and publish it on PyPi](https://thucnc.medium.com/how-to-publish-your-own-python-package-to-pypi-4318868210f9)

### Create a PyPi account

If you already have a PyPi account (and still remember your username/password, of course), you can skip this step. Otherwise, please go to PyPi homepage and register new account instantly.

### Generate distribution archives and upload to PyPi

#### Generating distribution archives

These are archives that are uploaded to the Package Index and can be installed by pip.
Make sure you have the latest versions of `setuptools` and `wheel` installed:

```bash
pip install --user --upgrade setuptools wheel
```
Now run this command from the same directory where setup.py is located:

```bash
python3 setup.py sdist bdist_wheel
```

#### Uploading the distribution archives

To do this, you can use twine. First, install it using pip:

```bash
pip install --user --upgrade twine
```

Then upload all the archives to PyPi:

```bash
python3 -m twine upload dist/*
... enter your PyPi username and password
```

Now everyone can install your package with familiar pip install command:

```bash
pip install {your_package_name}
```
