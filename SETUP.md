# 🚀 Quick Start Guide: Python 3.11 + pip + Jupyter Notebook

> 📝 **Note**: Use this guide if you don't have Python, pip, and git installed. If you have Python, pip, and git installed, you can skip this guide.

This guide helps you set up **Python 3.11**, **pip**, and **Jupyter Notebook** on **Mac**, **Windows**, and **Linux** machines.

---

## 🖥️ macOS

### 1. Install Homebrew (if not already installed)
Visit [https://brew.sh/](https://brew.sh/) and follow the instructions to install Homebrew.

Or run in Terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python 3.11
```bash
brew install python@3.11
```

### 3. Ensure pip is available
```bash
python3.11 -m ensurepip --upgrade
```

### 4. Add Python 3.11 to PATH (if needed)
```bash
echo 'export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
```

### 5. Install Jupyter
```bash
python3.11 -m pip install --upgrade pip
python3.11 -m pip install notebook
```

### 6. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 🪟 Windows

### 1. Install Python 3.11

- Download installer from the [official Python site](https://www.python.org/downloads/release/python-3110/)
- ✅ **Ensure “Add Python to PATH” is checked during installation**

### 2. Verify installation
```powershell
python --version
pip --version
```

### 3. Install Git

- Download Git from [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Run the installer with default options
- Verify installation:


### 4. Install Jupyter
```powershell
pip install notebook
```

### 5. Launch Jupyter Notebook
```powershell
jupyter notebook
```

---

## 🐧 Linux (Debian/Ubuntu)

### 1. Install Python 3.11
```bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev -y
```

### 2. Ensure pip is available
```bash
sudo apt install python3-pip -y
python3.11 -m ensurepip --upgrade
```

### 3. Install Jupyter
```bash
python3.11 -m pip install --upgrade pip
python3.11 -m pip install notebook
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## ✅ You’re Ready!

Jupyter will open in your browser. Create a new Python 3 notebook and start coding with ease.

---

---

## 📦 Create an Isolated Environment (Recommended)

We recommend using [**Mamba**](https://mamba.readthedocs.io/en/latest/) — a fast drop-in replacement for conda — to manage your Python environments.

### 1. Install Mamba

#### macOS & Linux (with Miniconda/Conda already installed):
```bash
conda install mamba -n base -c conda-forge
```

#### Windows:
Open Anaconda Prompt (as Administrator), then run:
```bash
conda install mamba -n base -c conda-forge
```

### 2. Create a new environment for your project
```bash
mamba create -n sdg_demo python=3.11 -y
```

### 3. Activate the environment
```bash
conda activate sdg_demo
```

### 4. Install the SDG package
```bash
pip install git+https://github.com/instructlab/sdg
```

Now you're ready to use the `instructlab/sdg` package in your `sdg_demo` environment!

---
