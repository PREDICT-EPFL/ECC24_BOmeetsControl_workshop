# Introduction
This is the tutorial repository used for the workshop "When Bayesian optimization meets real-time control" held at European Control Conference 2024, Stockholm,
Sweden. 

Throughout this tutorial, we will use the programming language python. If you are not familiar with python, you may refer to this
[python tutorial](https://www.w3schools.com/python/default.asp). We will also use jupyter notebook. If you are not familiar with this, please be referred to this
[jupyter notebook tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/). 

# Requirements
- gym==0.24.1
- numpy==1.24.4
- matplotlib==3.7.1
- IPython==7.22.0
- moviepy==1.0.3
- GPy==1.9.9
- ax-platform==0.3.3

# Installation of requirements

To install the required dependencies, you can use the `requirements.txt` file. Make sure you have [pip](https://pip.pypa.io/en/stable/) installed.

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

# Structure

This tutorial includes the following parts,  

## Implement BO algorithm using the Gaussian process package GPy:
- 'demo1.ipynb': Demonstrate the implementation of a Bayesian optimization algorithm.
- 'exercise1.ipynb': Exercise for you to implement a Bayesian optimization algorithm by yourself.

## Use Ax to solve problems. 
- 'acrobot.ipynb': Demonstrate the application of Ax to solving a PID controller tuning problem for acrobot. 
- 'cart_pole_play_exercise.ipynb': Exercise for you to apply the Bayesian optimization algorithm to a PD controller tuning problem by yourself.
