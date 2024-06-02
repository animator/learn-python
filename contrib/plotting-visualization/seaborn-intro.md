Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

## Seaborn Installation
Before installing Matplotlib, ensure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/).

Below are the steps to install and setup Seaborn:

1. Open your terminal or command prompt and run the following command to install Seaborn using `pip`:

```bash
pip install seaborn
```

2. The basic invocation of `pip` will install seaborn and, if necessary, its mandatory dependencies. It is possible to include optional dependencies that give access to a few advanced features:
```bash
pip install seaborn[stats]
```

3. The library is also included as part of the Anaconda distribution, and it can be installed with `conda`:
```bash
conda install seaborn
```

4. As the main Anaconda repository can be slow to add new releases, you may prefer using the conda-forge channel:
```bash
conda install seaborn -c conda-forge
```

## Dependencies
### Supported Python versions
- Python 3.8+

### Mandatory Dependencies
 - [numpy](https://numpy.org/)
 - [pandas](https://pandas.pydata.org/)
 - [matplotlib](https://matplotlib.org/)

### Optional Dependencies
 - [statsmodels](https://www.statsmodels.org/stable/index.html) for advanced regression plots
 - [scipy](https://scipy.org/) for clustering matrices and some advanced options
 - [fastcluster](https://pypi.org/project/fastcluster/) for faster clustering of large matrices
