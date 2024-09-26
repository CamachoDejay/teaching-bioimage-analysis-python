[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Python for bioimage analysis 2h lecture + demo

## Presentation
About 20m minutes:
* Image based quantitative biology
* Automated microscopy - HCS
* Smart microscopy - Feedback Microscopy
* BioImage Analysis - BIAS
* Why python
* Demo

## Python & JupyterLab Installation using virtual environments

The Jupyter Notebook is available as a part of JupyterLab, so my recommendation is to install JupyterLab as it is the latest generation of the Jupyter project. While JupyterLab is itself a useful development environment, other Integrated Development Environments have great support for Jupyter Notebooks and allow for customization and ease of use, such as [PyCharm](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html) and [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). To keep the demo simple we will use Jupyter's web interface.

### Python virtual environments
There are many ways to install Python [e.g.1](https://wiki.python.org/moin/BeginnersGuide/Download) & [e.g.2](https://realpython.com/installing-python/), but in a nutshell, there is something to keep in mind: different projects might need different flavours of Python with different sets of libraries. This is why it is strongly recommended that you manage your Python installations via “virtual environments”. You can think of virtual environments as an isolated set-up of Python that you wish to use including libraries and their versions. They can easily be created, modified and shared. It is for this reason that we suggest an installation workflow that includes the installation of [miniconda](https://docs.conda.io/en/latest/miniconda.html), a tool that can manage multiple virtual environments. Anohter good recomedation is the use of [mamba](https://mamba.readthedocs.io/en/latest/index.html) a fast and corss-platform package manager.

### Examples
1) [Book 1](./book-01-rice-example.ipynb) Rice Example From the article: ["Jupyter Notebooks for Generating and Distributing Bioimage Analysis Workflows"](https://analyticalscience.wiley.com/do/10.1002/was.0004000374)

2) [Book 2](./book-02-quick-example-BIAS.ipynb) based on data from one of the studets, data [available here](https://gunet-my.sharepoint.com/:f:/g/personal/rafael_camacho_gu_se/Er04f61cMRlJlxTPy5liik0BhMOvadVSxtrXcPRQP4ecGw?e=fMtDOY)

### Instalation
### 1.1) Installing miniconda: 
Miniconda is a free minimal installer for conda. The latest installation instructions can be found at:
https://docs.conda.io/en/latest/miniconda.html  

Once installed you should have access to the “Anaconda Prompt”. To test your installation, simply open the Anaconda Prompt, and then write the command:
```
> Python
```
This should open Python in your terminal. Notice the “>>>” in the prompt. To exit Python you can run the command:
```
>>> quit()
```
### 1.2) Create a virtual environment that will be used to install Jupyter Lab. 
**Note** that we will use python 3.9 to be compatible with Napari. Go to the Anaconda Prompt and run the command:
```
> conda create -y -n pybias-env -c conda-forge python=3.9
```
### 1.3) Activate environment
Once the virtual environment with the name pybias-env is created, then you can activate it to install the desired packages.
```
> conda activate pybias-env
```
**Note** how the terminal now starts with (pybias-env)
### 1.4) Install JupyterLab 
Now we install JupyterLab in the environment using
```
> conda install -c conda-forge jupyterlab
```
### 1.5) Make virtual environment available to JupyterLab
To make our current environment (kernel) available to JupyterLab we use:
```
> ipython kernel install --user --name=pybias-env
```
## JupyterLab’s web interface
When we launch a Jupyter Notebook, we use the “IPython Kernel” in the background, a library that offers an interactive command line interface. You can think of IPython Kernel as the computer engine that runs the code contained in a Notebook document. ipykernel is installed alongside JupyterLab, and that is why we can use it directly. 

### 2) Starting JupyterLab’s web interface
Starting JupyterLab is very simple. 
### 2.1) Open the anaconda prompt
Open the anaconda prompt and navigate to the desired folder. Below is an example using an empty folder named “jlab” in my “Documents” folder. 
```
> cd Documents/jlab
```
### 2.2) Activate appropiate environment
Make sure you have activated the ```pybias-env``` environment (see above installation procedure). Then run the command:
```
> jupyter lab
```
A web browser should open with the address: http://localhost:8888/lab

## 3) Creating a new Jupyter Notebook
You can find great documentation on [how to create Notebooks using JupyterLab](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html). Bellow is a minimal example:

3.1) Go to the JupyterLab web interface. 

3.2) Go to File > New > Notebook

3.3) Select the Kernel we have created: ```pybias-env```

3.4) Go to File > Save Notebook to rename your file as desired: e.g., ```Example.ipynb```

## 4) Notebook Cells
A Notebook’s cell can contain either live code, or documentation information in the form of formatted text via [Markdown](https://daringfireball.net/projects/markdown/), see for example Figure 02 of the manuscript. To start exploring Notebook Cells write the following on the first cell of your example notebook:
```
[ ] print(‘Hi bioimage analyst’)
```
Then you can use “ctr + enter” to run the current cell. 

## 5) Simple BIAS Python setup
A bare Jupyter Notebook is not going to take us very far if we try to solve a BIAS problem. To follow the examples depicted in Figures 1-3 of the article we must install ```scikit-image```, which is a collection of algorithms for image processing written in Python, ```matplotlib``` for creating figures, and ```pandas``` to handle tabular data.

5.1) Go to the Anaconda Prompt

5.2) Activate the pybias-env
```
> conda activate pybias-env
```

5.3) Install scikit-image, matplotlib, and pandas by

```
> conda install -c conda-forge scikit-image matplotlib pandas
```
5.4) Go to the desired path, and start JupyterLab
```
> jupyter lab
```

## 6 Sharing your virtual environment with others

6.1) Activate the environment to export, e.g. our Jupyter.env
```
> conda activate pybias-env
```
6.2) Export the active environment to a file
```
> conda env export > environment.yml
```
6.3) Email a copy of this file together with the Notebook file.

6.4) Instruct your collaborator to create the environment locally from the environment.yml file via:
```
> conda env create -f environment.yml
```

The managing of environments is an interesting topic in its own right and good documentation can be found at the [anaconda site](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## 7) Importing microscopy images and metadata into python
One critical aspect when handling microscopy images is the import of data from proprietary file formats and the correct handling of image metadata. Here, we can recommend to look at [AICSImageIO](https://github.com/AllenCellModeling/aicsimageio) a library to handle image reading, metadata conversion, and image writing for microscopy images in python. A minimal example can be found in their [quickstart](https://github.com/AllenCellModeling/aicsimageio#quickstart)

## 8) Python resources for bioimage analysis

### The Image.sc Forum
A scientific community forum for discussing image analysis software: [link to the Forum](https://forum.image.sc/). Many bioimage analysts and developers are available at the forum and it is a great place to ask Python BIAS-related questions.
### scikit-image 
A collection of algorithms for image processing written in Python [project site](https://scikit-image.org/). It has great documentation, implementation examples, and an active community that can be reached via its website, or the Image.sc forum.




