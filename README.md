# Machine Learning: Theory and Applications — Practical Sessions

**Course:** *Machine Learning: Theory and Applications*  
**Program:** Master in Cognitive Sciences, ENS–PSL  
**Lecturer:** Simona Cocco  
**Teaching Assistant:** [Vito Dichio](https://sites.google.com/view/vito-dichio/home) — vito.dichio@psl.eu

---

## Contents

This repository contains the starting notebooks for the practical sessions (TDs) of the course.

| # | Notebook | Topic |
|---|----------|-------|
| 1 | `1_poisson_retina.ipynb` | Poisson processes, Bayesian inference, and spike trains |
| 2 | `2_entropy_retina.ipynb` | Entropy and information in neural spike trains |
| 3 | `3_PCA_sleep.ipynb` | PCA and replay of neural activity during sleep |
| 4 | `4_Gaussian_sleep.ipynb` | Gaussian model for neural population activity |
| 5 | `5_Perceptron_MNIST.ipynb` | Perceptron |
| 6 | `6_Perceptron_OVO_MNIST.ipynb` | Multi-Class Perceptron |
| 7 | `7_HMM_zebrafish.ipynb` | Hidden Markov Models for Behavioral Analysis |

---

## Getting started

### 1. Download the repository

Click the green **Code** button at the top of this page, then select **Download ZIP**. Extract the archive — make sure to keep the folder structure intact.

Alternatively, if you are familiar with Git:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
```

### 2. Install dependencies

The notebooks require the following Python packages:

```
numpy
matplotlib
seaborn
pandas
h5py
```

You can install them all at once with:
```bash
pip install numpy matplotlib seaborn pandas h5py
```

### 3. Open a notebook

Launch Jupyter from the **root of the repository** (the folder containing this README):
```bash
jupyter notebook
```

> ⚠️ It is important to open Jupyter from the root folder, so that the relative paths to the `data/` folder work correctly.

---

## Reference

Cocco, Monasson, Zamponi — *From Statistical Physics to Data-Driven Modelling: with Applications to Quantitative Biology*, Oxford University Press (2022)
