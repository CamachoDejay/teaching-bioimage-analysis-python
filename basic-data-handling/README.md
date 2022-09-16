# Basic data handling in python

What to do after I get tables (e.g. ".csv") form FIJI or any other image analysis software

## Learning outcome

Basic understanding of Python for data exploration

How to install Data Science packages using conda environments

How to use VS Code to run and create jupyter notebooks

How to store and share your environment via .yml files

How to load ".csv" files

How to concatenate (combine) data tables

How to do basic plots, e.g. scatter, bars and violin plots

## Prerequisites

To save time, students in this demo will not have to install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (Anaconda Prompt) or [VS Code](https://code.visualstudio.com/docs). However, we write down some instructions on how to do this below.

## What is python

This is better answered by looking at online resources such as: https://www.python.org/doc/essays/blurb/

In the context of our course the most important question is [why is python used in data science.](https://learnpython.com/blog/why-python-used-for-science/)

## How to install python via conda

To make things easier we will be using [conda to install python and manage our virtual environments.](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) Think of a [virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) as a box (directory) that contains a specific collection tools (e.g. python + packages) that you have installed. The good thing is that you can have different boxes/environments, and if you change one environment, your other environments are not affected. To work with them we will then "activate" the box we want to use.

## Step 1: Creating a conda env with python 3.9

S1.1 Open an Anaconda Promt:

* Go to Windows icon -> search for "anaconda" -> open Anaconda Prompt (Anaconda 3)

S1.2 Create a new conda environment for python using this command in the promt:

```
> conda create -y -n bias-env -c conda-forge python=3.9
```

S1.3 Now activate your conda environment:

```
> conda activate bias-env
```

S1.4 Let us check the enviornment, use the command:

```
> which python
Python 3.9.xx | packaged by conda-forge |...
```

S1.5 Activate Python, use the command:

```
> python
```

S1.6 lets do some basic math

```python
>>> a = 3
>>> b = 6
>>> a+b
9
```

S1.7 lets get out of python

```python
>>> quit()
```

## VS Code

VS Code is a lightweight source code editor which runs on your desktop and is available for Windows, macOS and Linux. Using its extensions it can support Python and Jupyter books.

How to install it (not live): please follow the [instructions here to install VS Code](https://code.visualstudio.com/docs/setup/setup-overview), and the [nice documentation here to have it ready for python.](https://code.visualstudio.com/docs/languages/python).

## Step 2 Open VS Code and create a Python file

S2.1 Open VS Code:

* Go to Windows icon -> search for ```Code``` -> open Visual Studio Code

S2.2 Cereate a new folder so we can work on it:

* you can use cmd, or windows file explorer for this.

S2.3 Open the folder in VS Code using

* File -> open folder -> Yes, It trust

S2.4 Create a new python file by:

* create **New File** -> name it ```hellow.py```
* Install the [recommended extensions](https://code.visualstudio.com/docs/languages/python)
* in the file write: ```print("hello students")```
* run the file via the arrow on the top right
* look at the terminal

S2.5 Select an interpreter (aka virtual environment)

* use Ctr + Shift + P to open the command palleteinter
* look for ```interpreter```
* choose ```Python: Select Interpreter```
* look for the ```bias-env```

S2.6 Run again the file

## What is a Jupyter Notebook

Jupyter notebooks are a great tool for interactive programming in Data Science. [Look at this great article.](https://towardsdatascience.com/the-complete-guide-to-jupyter-notebooks-for-data-science-8ff3591f69a4) You can think of them as interactive books where we can "attach" a Python environment and interactively run pieces of code. Lets do a small demo so it is easier to understand.

## Step 3 Using VS Code to create and run Jupyter Notebooks

You can go over [this guide to get many details on how to use Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). Below a practical example.

S3.1 Crete new jupyter book in VS Code

* Create a new notebook by creating a new ```.ipynb``` file in your workspace. The extension resembles Ipython NoteBook

* Alternatively
  * use Ctr + Shift + P to open the command palleteinter
  * look for ```jupyter```
  * choose ```Python: Create: New Jupyter Notebook```
  * use:  File -> Save to save the file with ```.ipynb``` extension
* Select your kernel AKA virtual environment
* Create a cell with simple math:

```python
a = 3
b = 6
a+b
```

* Try to run the cell and you will notice a complaint from VS Code. We better install ```ipykernel```.
* Click on Cancel

S3.2 Installing ```ipykernel```, our first package

* Go to the Anaconda Prompt
  * If you closed it, then activate again the bias-env. Follow steps S1.1 and S1.3
* run the command: ```conda install ipykernel```
* say yes via ```y```

S3.3 Run the Jupyter Notebook in VS Code once again


## Where to go next

Add here link to different resources
