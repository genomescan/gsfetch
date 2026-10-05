# GSFetch

GSFetch is a command-line tool for downloading your project data from the GenomeScan Customer Portal. It downloads files in parallel, which makes transfers of large projects considerably faster than downloading through the browser.

Works on Linux, Windows and macOS.

## Contents

- [Installation](#installation)
  - [Option 1: Executable](#option-1-executable)
  - [Option 2: pip](#option-2-pip)
  - [Option 3: From source](#option-3-from-source)
- [Quick start](#quick-start)
  - [Logging in](#logging-in)
  - [`list`: browse your projects and files](#list-browse-your-projects-and-files)
  - [`download`: download files](#download-download-files)
  - [General options](#general-options)
- [Getting help](#getting-help)

## Installation

There are three ways to install GSFetch:

| Option | Best for | Requirements |
| --- | --- | --- |
| 1. Executable | Quick use without Python | Windows or Linux |
| 2. pip | Most users | Python 3.10+ |
| 3. From source | Development | Python 3.10+, git |

### Option 1: Executable

Download the executable for your platform from the [latest release](https://github.com/genomescan/gsfetch/releases/latest). It is currently available for Windows and Linux only. The executable can take a few seconds to start up.

### Option 2: pip

We recommend installing GSFetch in a virtual environment.

**Linux / macOS**

```bash
python3 -m venv env
source env/bin/activate
pip install gsfetch
```

**Windows**

```bash
python -m venv env
env\Scripts\activate
pip install gsfetch
```

After installation the `gsfetch` command is available while the virtual environment is active.

### Option 3: From source

**Linux / macOS**

```bash
git clone https://github.com/genomescan/gsfetch.git
cd gsfetch
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

**Windows**

```bash
git clone https://github.com/genomescan/gsfetch.git
cd gsfetch
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

When running from source, use `python main.py` wherever this README says `gsfetch`, for example:

```bash
python main.py list 100000
```

## Quick start

The examples below use project `100000`. Replace it with your own project code.

GSFetch has two subcommands:

| Subcommand | What it does |
| --- | --- |
| `list` | Show your projects, or the files inside a project |
| `download` | Download a whole project, a directory, or specific files |

Every subcommand has its own help page, for example `gsfetch list -h`.

### Logging in

The first time you run a command, GSFetch asks you to log in:

1. Enter the **email** and **password** of your Customer Portal account.
2. You receive a **token** by email. Enter it when GSFetch asks for it.

Your session is saved in `.gs_cookies.txt` in your home directory, so you don't have to log in again every time. To log out, see [General options](#general-options).

### `list`: browse your projects and files

Show all projects you have access to:

```bash
gsfetch list
```

Show all files in project `100000`, including everything in subdirectories:

```bash
gsfetch list 100000
```

Show only the files in the top level of the project (not recursive):

```bash
gsfetch list 100000 -n
```

Show the contents of a specific directory inside the project:

```bash
gsfetch list 100000 Raw_data          # everything in Raw_data, including subdirectories
gsfetch list 100000 Raw_data -n       # only the files directly in Raw_data
```

Print a flat list of file paths with their MD5 checksums, so you can verify your downloads afterwards:

```bash
gsfetch list 100000 -md5
```

| Option | Description |
| --- | --- |
| `PROJECT` | Project code, e.g. `100000`. Leave it out to list all your projects. |
| `PATH` | Directory inside the project to list. Defaults to the whole project. |
| `-n`, `--non-recursive` | Don't descend into subdirectories. |
| `-md5`, `--md5sums` | Print file paths with their MD5 checksums. |

### `download`: download files

Download the complete project `100000` to the current directory:

```bash
gsfetch download 100000
```

Download to a different folder (it is created if it doesn't exist):

```bash
gsfetch download 100000 -o C:\data\project100000
```

Download only the files in the top level of the project:

```bash
gsfetch download 100000 -n
```

Download a specific directory, a specific file, or a combination (separate them with spaces):

```bash
gsfetch download 100000 Raw_data
gsfetch download 100000 Raw_data/sample1_R1.fastq.gz
gsfetch download 100000 Raw_data Reports/summary.pdf
```

When you name specific files or directories, GSFetch first shows what it is about to download and asks you to confirm with `y`.

Tip: run `gsfetch list 100000` first to see the exact paths you can pass to `download`.

| Option | Description |
| --- | --- |
| `PROJECT` | Project code, e.g. `100000`. Required. |
| `TARGET` | One or more files or directories to download, separated by spaces. Leave it out to download the whole project. |
| `-o`, `--output` | Folder to save the files in. Defaults to the current directory. |
| `-n`, `--non-recursive` | Don't descend into subdirectories. |
| `-t`, `--threads` | Number of parallel downloads. Defaults to the number of CPU cores. |

### General options

These options go **before** the subcommand, or are used on their own:

| Option | Description |
| --- | --- |
| `-h`, `--help` | Show the help page. |
| `-v`, `--version` | Show the GSFetch version. |
| `-c`, `--clear-cookies` | Log out and remove your saved session. |
| `-H`, `--host` | Use a different portal URL (normally not needed). |

```bash
gsfetch --version
gsfetch -c
```

## Getting help

- Run `gsfetch --help`, `gsfetch list -h` or `gsfetch download -h` for all options.
