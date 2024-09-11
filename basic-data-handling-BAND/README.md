# Basic Data Handling in Python

In this session, we will focus on what to do after obtaining result tables (e.g., `.csv`) from FIJI or any other image analysis software. Many people would typically load these tables into spreadsheet programs, such as Microsoft Excel, to generate figures and perform statistical analysis. Here, we will explore an alternative workflow using Python, combined with Jupyter Notebooks, for these tasks.

## Learning Outcomes

By the end of this session, you will:

- Develop a basic understanding of Python for data exploration.
- Learn how to load `.csv` files into Python.
- Understand how to concatenate (combine) data tables.
- Gain the ability to export data tables into `.csv` files or Excel sheets.
- Be able to create basic plots, such as scatter plots, bar charts, and violin plots.
- Perform basic data analysis and statistical tests.

### Extra information for self-study:
- Learn how to install Data Science packages using conda environments.
- Use VS Code to run and create Jupyter Notebooks.
- Understand how to store and share your environment via `.yml` files.


## Prerequisites

This year we will benefit from BAND the Bioimage ANalysis Desktop - a Desktop-as-a-Service cloub-based platform that generates a desktop environment packed with bioimage analysis tools. This will simplify the installation procedures and let us concentrate on the content of the course. Moreover I provide below a full guide on how to install the required programs on your own computer.

## What is Python?

Rather than reinvent the wheel, it's best to consult established resources for an introduction to Python. You can start by exploring [this essay on the official Python website](https://www.python.org/doc/essays/blurb/) for a broad overview.

For our course, the key question is: [Why is Python so widely used in data science?](https://learnpython.com/blog/why-python-used-for-science/) This resource dives into the reasons Python has become the go-to language for data analysis and scientific computing.

By the end of this session, you'll gain an understanding of why so many people choose Python for data analysis, ranging from basic tasks to more advanced, complex workflows.

## Use Cases

Please note that we will be skipping the installation procedure outlined below, as we will be using BAND for this course. However, interested students are encouraged to try the installation on their own laptops during the week and bring them to the session on Friday. During coffee breaks, we can discuss any issues you might encounter while installing Jupyter Notebooks on your machine.

1. [Book 1:](./Book_01.ipynb) How to read a CSV file into a data table.
2. [Book 2:](./Book_02.ipynb) How to create simple plots with Pandas and Seaborn.
3. [Book 3:](./Book_03.ipynb) How to concatenate data frames.
4. [Book 4:](./Book_04.ipynb) How to create more elaborate plots using Seaborn.
5. [Book 5:](./Book_05.ipynb) Statistical tests using Pandas and SciPy.
6. [Book 6:](./Book_06.ipynb) A quick example of creating a pivot table.
7. [Book 7:](./Book_07.ipynb) A TrackMate example: Plotting Mean Speed Over Time for a Movie.


## Installation guide

We recommend using **Miniforge**, a minimal conda installer that helps avoid the overhead of the full Anaconda distribution. Miniforge allows you to install only the necessary tools and packages, providing a lightweight and efficient setup. You can follow the installation guide here: [Miniforge Installation](https://github.com/conda-forge/miniforge).

Optionally, you might want to install the following programs by following the official guides:
- [VS Code](https://code.visualstudio.com/docs) (for running and editing Jupyter Notebooks)
- [Git](https://github.com/git-guides/install-git) (command line tools for version control - **optional**)

Each of these tools has excellent online tutorials and documentation to guide you through the installation process.


## How to Install Python via Conda

To make things easier, we will be using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to install Python and manage our virtual environments. 

Think of a [virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) as a "box" (or directory) that contains a specific collection of tools (e.g., Python + packages) that you have installed. The great thing about virtual environments is that you can have multiple boxes/environments, each tailored to a specific task or project. If you change or update one environment, your other environments remain unaffected.

To work within a specific environment, we will "activate" the box we want to use.

If you've worked with FIJI before, the concept of virtual environments is similar to having multiple versions of FIJI, where each copy resides in a different folder, allowing you to manage versions independently.

## Step 1: Creating a Conda Environment with Python 3.10

**Prerequisite:** To follow these steps, you need to have Conda installed, and access to the Miniforge prompt on your computer.

### S1.1 Open the Miniforge Prompt:
* On Windows: Click the Windows icon, search for "miniforge", and select **Miniforge Prompt**.

### S1.2 Create a new Conda environment with Python 3.10:

Run the following command in the Miniforge Prompt to create a new Conda environment named `bias-env`:

```bash
conda create -y -n bias-env -c conda-forge python=3.10
```

After ```Conda``` has done its job, you have successfully created a new "box" (environment) containing a copy of Python version 3.10. The name of this environment is `bias-env`, and the Conda channel we used is `conda-forge`.

Think of a Conda channel like choosing a specific shop to buy your products from. In this case, `conda-forge` is the shop we are using to get the packages we need. It’s a popular channel with a large collection of up-to-date and well-maintained packages. While this is a useful concept, going deeper into Conda channels is a bit out of the scope of this session.

S1.3 Now activate your conda environment:

```bash
conda activate bias-env
```

S1.4 Let us check the enviornment, by asking what python is available. Use the command:

```bash
python --version
Python 3.10.14
```

S1.5 Activate Python. Use the command:

```bash
python
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

## OPTIONAL: VS Code

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

## What is a Jupyter Notebook?

Jupyter notebooks are an excellent tool for interactive programming in Data Science. You can explore this [informative article](https://towardsdatascience.com/the-complete-guide-to-jupyter-notebooks-for-data-science-8ff3591f69a4) to dive deeper into its benefits. Think of them as interactive notebooks where you can "attach" a Python environment and execute pieces of code in real-time, making it easy to visualize outputs and explore data. Let's do a small demo to better understand how they work.

## Installing jupyterlab in our virtual environment

This step can be skiped in this demo because we already have jupyterlab installed in our base conda environment. However, if this is not the case you might have to install it separately via:

* Go to the Anaconda Prompt
  * If you closed it, then activate again the bias-env. Follow steps S1.1 and S1.3

```bash
conda install -c conda-forge jupyterlab
```

To test that it is properly installed you can run this in the command line

```bash
where jupyter
```

### Make the virtual environment available to JupyterLab
To make our current environment (kernel) available to JupyterLab we can use:

```bash
ipython kernel install --user --name=bias-env
```
## Using Jupyter Notebooks

You are now ready to use Jupyter notebooks via Jupyter Lab. Simply open your terminal and run the following command:

```bash
jupyter lab
```
A new tab will open in your web browser, and that's it—you’re good to go! 

If you prefer to use VS Code instead of Jupyter Lab, please follow the instructions provided below.
 

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

```bash
ipython kernel install --user --name=bias-env
```

S3.3 Run the Jupyter Notebook in VS Code once again


## Where to go next

Now you are set to a great start. Feel free to play with this notebooks with basic Python if you want to get familiar with the language. There are many cool websites and videos including.

* YouTube series by google team on Python: [day 1 link](https://youtu.be/tKTZoB2Vjuk)
* [RealPython website](https://realpython.com/)
* YouTube series by Neubias Academy on using [Python for image analysis](https://youtu.be/2KF8vBrp3Zw)
* PoL Dresden [course on BioImage analysis using Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)