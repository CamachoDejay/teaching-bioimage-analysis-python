# Quick demo on image processing using python

I will show case how to do a basic image analysis pipeline using Python packages such as skimage and napari.

## Learning outcome

* Basic understanding of Napari as an image viewer

* How to install image processing packages

* How to do a basic image analysis pipeline including
  * Image loading
  * Image exploration
  * Thresholding
  * Filtering - background substraction
  * Basic quantification based on image mask/labels

## Prerequisites

To save time during the session, I assume that students have access to a computer with already installed [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (Anaconda Prompt), and [git](https://github.com/git-guides/install-git) command line tools. Further, I will be using [VS Code](https://code.visualstudio.com/docs) to go over the material.

## How to install required packages

To make things easier we will be using [conda to install python and manage our virtual environments.](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) Think of a [virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) as a box (directory) that contains a specific collection tools (e.g. Python + packages) that you have installed. The good thing is that you can have different boxes/environments, and if you change one environment, your other environments are not affected. To work with them we will then "activate" the box we want to use.

## Creating a conda env via a yml file

**Prerequisite** to go over these steps you need to have installed ```conda```, and the anaconda prompt on your computer.

S1.1 Open an Anaconda Promt:

* Open Anaconda Prompt (Anaconda 3)

S1.2 Create a new conda environment for Python using this command in the promt. First navigate to the folder **quick_demo_220928**, then:

```
> conda env create -f environment.yml
```

After ```conda``` has done its job you have created a new "box" containing a copy of Python version 3.9. The name of this environment is ```demo-env``` and as ```conda```channel we have used ```conda-forge```. Think of a conda channel as buying your products from a specific shop. ```conda-forge``` is my favorite store, but this discussion is a bit out of the scope of the session.

S1.3 Now activate your conda environment:

```
> conda activate demo-env
```

S1.4 Test python
```
> python --version
```

## VS Code

VS Code is a lightweight source code editor which runs on your desktop and is available for Windows, macOS and Linux. Using its extensions it is a great tool for Python and Jupyter books.

How to install it (not live): please follow the [instructions here to install VS Code](https://code.visualstudio.com/docs/setup/setup-overview), and the [nice documentation here to have it ready for python.](https://code.visualstudio.com/docs/languages/python).

## What is a Jupyter Notebook

Jupyter notebooks are a great tool for interactive programming in Data Science. [Look at this great article.](https://towardsdatascience.com/the-complete-guide-to-jupyter-notebooks-for-data-science-8ff3591f69a4) You can think of them as interactive books where we can "attach" a Python environment and interactively run pieces of code. Lets do a small demo so it is easier to understand.

## Installing jupyterlab

This step can be skiped in this demo because we already have jupyterlab installed in our ```demo-env```. However, if this is not the case you might have to install it separately via:

* Go to the Anaconda Prompt
  
```
> conda install -c conda-forge jupyterlab
```

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

* Try to run the cell and you might notice a complaint from VS Code. Make sure you installed ```ipykernel```. This is already done in the demo-env

## To continue working on our use case

Now lets move to the example books in this repo.

## Where to go next

Now you are set to a great start. Feel free to play with this notebooks with basic Python if you want to get familiar with the language. There are many cool websites and videos including.

* YouTube series by google team on Python: [day 1 link](https://youtu.be/tKTZoB2Vjuk)
* [RealPython website](https://realpython.com/)
* YouTube series by Neubias Academy on using [Python for image analysis](https://youtu.be/2KF8vBrp3Zw)
* PoL Dresden [course on BioImage analysis using Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)