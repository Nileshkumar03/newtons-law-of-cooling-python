# Newton's Law of Cooling – Python Simulation

## Overview
This project investigates Newton's Law of Cooling through mathematical modelling, numerical methods and Python-based computational analysis. It compares analytical and numerical solutions to study the cooling behaviour of an object approaching ambient temperature.

## Objectives
- Study the mathematical formulation of Newton's Law of Cooling.
- Estimate the cooling constant using experimental temperature data.
- Implement numerical solutions using Euler and fourth-order Runge-Kutta methods.
- Compare analytical and numerical results.
- Visualize temperature variations with time.

## Mathematical Model

Newton's Law of Cooling is expressed as:

\[
\frac{dT}{dt}=-k(T-T_s)
\]

The analytical solution is:

\[
T(t)=T_s+(T_0-T_s)e^{-kt}
\]

Where:
- T = Object temperature
- Ts = Surrounding temperature
- T0 = Initial temperature
- k = Cooling constant
- t = Time

## Technologies Used
- Python
- NumPy
- SciPy
- Pandas
- Matplotlib

## Numerical Methods
- Analytical Solution
- Euler Method
- Fourth-Order Runge-Kutta (RK4)
- Nonlinear Curve Fitting

## Project Structure

```text
Newtons_Law_of_Cooling/
│
├── data/
│   └── experimental_data.csv
│
├── src/
│   ├── cooling_model.py
│   ├── data_analysis.py
│   └── numerical_methods.py
│
├── plots/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Nileshkumar03/newtons-law-of-cooling-python.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation from the project directory:

```bash
python src/data_analysis.py
```

## Results
The project generates graphical comparisons of experimental observations, analytical predictions and numerical solutions using Euler and Runge-Kutta methods.

Generated plots are saved in the `plots/` directory.

## Future Improvements
- Perform actual laboratory experiments and collect temperature measurements.
- Investigate the effects of ambient temperature and cooling conditions.
- Conduct numerical error and convergence analysis.
- Extend the model to investigate more complex heat-transfer behaviour.

## Note on Data
The currently included temperature observations are illustrative sample data and are intended for demonstrating the computational model. They are not actual experimental measurements.

## Author
**Nilesh Kumar**

Independent Computational Physics Project
