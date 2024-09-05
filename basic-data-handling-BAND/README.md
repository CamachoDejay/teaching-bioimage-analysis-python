# Basic Data Handling in Python

In this session, we will focus on what to do after obtaining result tables (e.g., `.csv`) from FIJI or any other image analysis software. Many people would typically load these tables into spreadsheet programs, such as Microsoft Excel, to generate figures and perform statistical analysis. Here, we will explore an alternative workflow using Python, combined with Jupyter Notebooks, for these tasks.

## Learning Outcomes

By the end of this session, you will:

- Have a basic understanding of Python for data exploration.
- Know how to install Data Science packages using conda environments.
- Be able to use VS Code to run and create Jupyter Notebooks.
- Learn how to store and share your environment via `.yml` files.
- Know how to load `.csv` files into Python.
- Understand how to concatenate (combine) data tables.
- Be able to export data tables into `.csv` files or Excel sheets.
- Know how to create basic plots, such as scatter plots, bar charts, and violin plots.

## Prerequisites

This year we will benefit from BAND the Bioimage ANalysis Desktop - a Desktop-as-a-Service cloub-based platform that generates a desktop environment packed with bioimage analysis tools. This will simplify the installation procedures and let us concentrate on the content of the course. Moreover I provide below a full guide on how to install the required programs on your own computer.

## What is Python?

Rather than reinvent the wheel, it's best to consult established resources for an introduction to Python. You can start by exploring [this essay on the official Python website](https://www.python.org/doc/essays/blurb/) for a broad overview.

For our course, the key question is: [Why is Python so widely used in data science?](https://learnpython.com/blog/why-python-used-for-science/) This resource dives into the reasons Python has become the go-to language for data analysis and scientific computing.

By the end of this session, you'll gain an understanding of why so many people choose Python for data analysis, ranging from basic tasks to more advanced, complex workflows.


## Installation guide

For this course, we recommend using **Miniforge**, a minimal conda installer that helps avoid the overhead of the full Anaconda distribution. Miniforge allows you to install only the necessary tools and packages, providing a lightweight and efficient setup. You can follow the installation guide here: [Miniforge Installation](https://github.com/conda-forge/miniforge).

Additionally, you will need the following programs, which you can install by following the official guides:
- [VS Code](https://code.visualstudio.com/docs) (for running and editing Jupyter Notebooks)
- [Git](https://github.com/git-guides/install-git) (command line tools for version control - **optional**)

Each of these tools has excellent online tutorials and documentation to guide you through the installation process.



## How to install Python via conda

To make things easier we will be using [conda to install python and manage our virtual environments.](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) Think of a [virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) as a box (directory) that contains a specific collection tools (e.g. Python + packages) that you have installed. The good thing is that you can have different boxes/environments, and if you change one environment, your other environments are not affected. To work with them we will then "activate" the box we want to use.

After working with FIJI during the course, the concept of virtual environments is very similar as having multiple versions of FIJI by keeping different copies in different folders.

## Step 1: Creating a conda env with python 3.10

**Prerequisite** to go over these steps you need to have installed ```conda```, and the anaconda prompt on your computer.

S1.1 Open an Anaconda Promt:

* Go to Windows icon -> search for "anaconda" -> open Anaconda Prompt (Anaconda 3)

S1.2 Create a new conda environment for Python using this command in the promt:

```
> conda create -y -n bias-env -c conda-forge python=3.10
```

After ```conda``` has done its job you have created a new "box" containing a copy of Python version 3.9. The name of this environment is ```bias-env``` and as ```conda```channel we have used ```conda-forge```. Think of a conda channel as buying your products from a specific shop. ```conda-forge``` is my favorite store, but this discussion is a bit out of the scope of the session.

S1.3 Now activate your conda environment:

```
> conda activate bias-env
```

S1.4 Let us check the enviornment, by asking what python is available. Use the command:

```
> which python

Python 3.10.xx | packaged by conda-forge |...

> python --version

```

S1.5 Activate Python. Use the command:

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

S1.7 lets do some basic print statements
```python
>>> print("Hello")
Hello
>>> name = "Rafa"
>>> print("Hello " + name)
Hello Rafa

```
This should remind you of the way we worked with strings in IJ Macro language

S1.8 lets get out of python

```python
>>> quit()
```

## VS Code

VS Code is a lightweight source code editor which runs on your desktop and is available for Windows, macOS and Linux. Using its extensions it is a great tool for Python and Jupyter books.

How to install it (not live): please follow the [instructions here to install VS Code](https://code.visualstudio.com/docs/setup/setup-overview), and the [nice documentation here to have it ready for python.](https://code.visualstudio.com/docs/languages/python).

## Step 2 Open VS Code and create a Python file

**Prerequisite** I assume you already have VS Code installed.

S2.1 Open VS Code:

* Go to Windows icon -> search for ```Code``` -> open Visual Studio Code

S2.2 Cereate a new folder so we can work on it:

* you can use cmd, or windows file explorer for this.

S2.3 Open the folder in VS Code using

* File -> open folder -> Yes, It trust

S2.4 Create a new python file by:

* create **New File** -> name it ```hello.py```
* Install the [recommended extensions](https://code.visualstudio.com/docs/languages/python)
* in the file write: ```print("hello students")```
* run the file via the arrow on the top right
* look at the terminal

S2.5 Select an interpreter (aka virtual environment)

* use Ctr + Shift + P to open the command pallete
* look for ```interpreter```
* choose ```Python: Select Interpreter```
* look for the ```bias-env```

S2.6 Run again the file

## What is a Jupyter Notebook

Jupyter notebooks are a great tool for interactive programming in Data Science. [Look at this great article.](https://towardsdatascience.com/the-complete-guide-to-jupyter-notebooks-for-data-science-8ff3591f69a4) You can think of them as interactive books where we can "attach" a Python environment and interactively run pieces of code. Lets do a small demo so it is easier to understand.

## Installing jupyterlab in our virtual environment

This step can be skiped in this demo because we already have jupyterlab installed in our base conda environment. However, if this is not the case you might have to install it separately via:

* Go to the Anaconda Prompt
  * If you closed it, then activate again the bias-env. Follow steps S1.1 and S1.3

```conda install -c conda-forge jupyterlab```

To test that it is properly installed you can run this in the command line

```where jupyter```

### Make the virtual environment available to JupyterLab
To make our current environment (kernel) available to JupyterLab we can use:

```ipython kernel install --user --name=bias-env```

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

* Try to run the cell.

**Note** If you forgot the ipython kernel step you will notice a complaint from VS Code. In this case make sure you have ```ipykernel``` installed.


S3.2 Optional Installing ```ipykernel```

* Go to the Anaconda Prompt
  * If you closed it, then activate again the bias-env. Follow steps S1.1 and S1.3
* run the command: ```conda install ipykernel```
* say yes via ```y```

Then we make the current environment available as a jupyter kernel

```ipython kernel install --user --name=bias-env```

S3.3 Run the Jupyter Notebook in VS Code once again

## To continue working on our use case

Now lets move to the example books in this repo.

## Where to go next

Now you are set to a great start. Feel free to play with this notebooks with basic Python if you want to get familiar with the language. There are many cool websites and videos including.

* YouTube series by google team on Python: [day 1 link](https://youtu.be/tKTZoB2Vjuk)
* [RealPython website](https://realpython.com/)
* YouTube series by Neubias Academy on using [Python for image analysis](https://youtu.be/2KF8vBrp3Zw)
* PoL Dresden [course on BioImage analysis using Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)