# Basic data handling in python

Throughout this session we will concentrate on what to do after we get results tables (e.g. ".csv") form FIJI or any other image analysis software. Most people would take the tables, load them in a spreadsheet program, such as Microsfots Excel, and then continue from there with figure generation and statistical testing. Here I showcase the option of using Python, in combination with Jupyter Notebooks for these tasks.

## Learning outcome

* Basic understanding of Python for data exploration

* How to install Data Science packages using conda environments

* How to use VS Code to run and create Jupyter Notebooks

* How to store and share your environment via ```.yml``` files

* How to load ```.csv``` files

* How to concatenate (combine) data tables

* How to export data tables into ```.csv``` files or Excel sheets

* How to do basic plots, e.g. scatter, bars and violin plots

## Prerequisites

To save time during the session, students will hace access to a work station with already installed [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (Anaconda Prompt), [VS Code](https://code.visualstudio.com/docs), and [git](https://github.com/git-guides/install-git) command line tools. However, we write some instructions for those following off site.

## What is python?

This is better answered by looking at online resources such as: https://www.python.org/doc/essays/blurb/

In the context of our course the most important question is [why is python used in data science?](https://learnpython.com/blog/why-python-used-for-science/)

I hope that by the end of the session you will understand why so many people are moving to Python to do data analysis tasks, from the most basic to the most advanced.

## How to install Python via conda

To make things easier we will be using [conda to install python and manage our virtual environments.](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) Think of a [virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) as a box (directory) that contains a specific collection tools (e.g. Python + packages) that you have installed. The good thing is that you can have different boxes/environments, and if you change one environment, your other environments are not affected. To work with them we will then "activate" the box we want to use.

After working with FIJI during the course, the concept of virtual environments is very similar as having multiple versions of FIJI by keeping different copies in different folders.

## Step 1: Creating a conda env with python 3.9

**Prerequisite** to go over these steps you need to have installed ```conda```, and the anaconda prompt on your computer.

S1.1 Open an Anaconda Promt:

* Go to Windows icon -> search for "anaconda" -> open Anaconda Prompt (Anaconda 3)

S1.2 Create a new conda environment for Python using this command in the promt:

```
> conda create -y -n bias-env -c conda-forge python=3.9
```

After ```conda``` has done its job you have created a new "box" containing a copy of Python version 3.9. The name of this environment is ```bias-env``` and as ```conda```channel we have used ```conda-forge```. Think of a conda channel as buying your products from a specific shop. ```conda-forge``` is my favorite store, but this discussion is a bit out of the scope of the session.

S1.3 Now activate your conda environment:

```
> conda activate bias-env
```

S1.4 Let us check the enviornment, by asking what python is available. Use the command:

```
> which python

Python 3.9.xx | packaged by conda-forge |...

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