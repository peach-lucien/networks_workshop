# Workshop on Network Science

##### Authors: Mauricio Barahona and Robert Peach

##### Motiviation

We are surrounded by systems that are hopelessly complicated - complex systems - and behind each complex system there is an intricate network that encodes the interactions between the individual components.
Knowing the systems components, such as the neurons in the brain, is insufficient to derive the collective behaviour of millions interacting. Given the important role complex systems play in our daily life, in science and in economy, their understanding, mathematical description, prediction, and eventually control is one of the major intellectual and scientific challenges of the 21st century. We will never understand complex systems unless we develop a deep understanding of the networks behind them.

![title](images/network.gif)


Network science is a relatively new discipline when compared to traditional subjects: Its exact beginning is up for debate, but has only really emerged as a separate discipline during the 21st century. The development of tools to interrogate networks, and the areas that have benefitted from network analyses, have grown exponentially over recent years. 

Note: There is no real difference between a **graph** and  **network**. However, when we model a real, existing system as a graph, we tend to call it a network.



##### What to expect from this workshop?

We want to give a first introduction to networks, show you a diverse set of applications, and introduce standard methods for working with networks in Python. We will certainly not be comprehensive, but instead zone in on a few interesting use-cases, with a slight tendency towards neuroscience. We will lightly touch on the following:
1. Introduction to the NetworkX package in Python.
2. The structure of the Caenorhabditis elegans connectome.
3. Dynamics on networks (e.g., synchronisation, epidemics).
4. Network Neuroscience.

##### What might we learn?

We don't necessarily want you to learn every detail about the examples we give, instead we want to give you a flavour for networks such that you might see links with your own research now or in the future.

1. Familiarity with NetworkX Python package.
2. Understanding the importance of approaches to visualisation of networks.
3. How to apply algorithmic tools to examine network structure, including:
    - Community detection
    - Centrality
    - Clustering
4. Perform dynamics on networks:
    - Synchronisation models
    - Epidemic simulations
5. Aspects of network construction with neuroscientific data:
    - Functional connectivity data
    - Pose estimation data


### Getting started

You will need to have a running version of Python and Jupyter notebooks. This is easily installed using Anaconda https://docs.anaconda.com/anaconda/install/index.html.

Before you run these notebooks, there are a few dependencies (packages that you need to also have installed). These should all be defined in the requirements.txt file. 

Just access the main folder for this code via the terminal and run:
> pip install -r requirements.txt

If there are any further problems, please let us know and we will do our best to fix it.
