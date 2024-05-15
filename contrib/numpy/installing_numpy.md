# Installing NumPy

NumPy is the fundamental package for scientific computing in Python.
NumPy is used for working with arrays. 

The only prerequisite for installing NumPy is Python itself.
#
**Step 1: Check if PIP is Installed**

Before installing NumPy, it's essential to ensure that PIP (Python Package Installer) is installed on your system. PIP is a package management system used to install and manage Python packages. You can verify if PIP is installed by running a simple command in your terminal or command prompt. 

```bash
pip --version
```

If PIP is not currently installed on your system, you can install it by visiting the [pypi.org](https://pypi.org/project/pip/) webpage. 

#

**Step 2: Installing PIP**

**get-pip.py**

This is a Python script that uses some bootstrapping logic to install pip.

Open a terminal / command prompt and run:

**Linux**
```bash
python get-pip.py
```

**Windows**
```bash
py get-pip.py
```

**MacOS**
```bash
python get-pip.py
```

#

**Step 3: Installing NumPy**

NumPy can be installed either through conda or pip.

If you use pip, you can install NumPy with:

```bash
pip install numpy
```

If you use conda, you can install NumPy from the defaults or conda-forge channels:

```
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
```

```
# If you want to install from conda-forge
conda config --env --add channels conda-forge
```

```
# The actual install command
conda install numpy
```

You can find more information about how to install [NumPy](https://numpy.org/install/) on numpy.org.

#

**Step 4: Check if NumPy is Installed**

We can utilize the "pip show" command not only to display the version but also to determine whether NumPy is installed on the system.
```bash
pip show numpy
```
