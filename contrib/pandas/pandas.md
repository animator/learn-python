## Installation of Pandas:
__Pandas can be installed on your PC using PIP (Python Package manager)__

If you have PIP already installed on a system, then installation of Pandas is very easy.

If you do not have PIP installed, you can download and install it from this page:  https://pypi.org/project/pip/

After Installing PIP in your PC, follow the below given steps:

__Step 1: Launch Command Prompt__

To open the Start menu, press the Windows key or click the Start button. To access the Command Prompt, type “cmd” in the search bar, click the displayed app, or use Windows key + r, enter “cmd,” and press Enter.

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20231206151658/pppp.png)

__Step 2:Run the command__

Pandas can be installed using PIP by use of the following command in Command Prompt.
    pip install pandas

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20231206152811/pandas.png)

__How to verify whether Pandas is Installed or not:__

To check whether the pandas package is installed or not in python we can simply verify the version. To get the version details of pandas. we use __version()__ attribute.

    import pandas as pd
    print(pd.__version__)

The above code will give the version of pandas installed in your PC.