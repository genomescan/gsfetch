# GSFetch

GSFetch is a command-line tool designed to accelerate file downloads from the GenomeScan Customer Portal. It leverages multiprocessing to significantly improve download speeds and efficiency. Works on linux, windows and macOS. 


## Installation

There are 3 options for installing GSport.
1. Executable (can be a little slow to startup)
2. Pip install
3. Manual installation


## 1: Executable
This is only available for Windows and linux at the moment. Simply download the executable from the latest release


## 2: Pip install

### Prerequisites

Ensure you have the following installed:
- Python 3.8.X
- Pip (Python package manager)
- python-venv (Linux/ macOS) or virtualenv(windows)

```bash
pip install gsfetch
```

## 3: Manual install

### Prerequisites

Ensure you have the following installed:
- Python 3.10.X
- Pip (Python package manager)
- python-venv (Linux/ macOS) or virtualenv(windows)


### Linux/macOS

```bash
git clone https://github.com/genomescan/gsfetch.git
cd gsfetch
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Windows

```bash
git clone https://github.com/genomescan/gsfetch.git
cd gsfetch
virtualenv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

## Usage

To see all available options, run:

```bash
python gsfetch.py --help
```
