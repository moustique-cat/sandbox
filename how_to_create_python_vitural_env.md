## How a Virtual Environment Works

When you create a virtual environment, Python essentially makes a copy of its interpreter and standard library into the project directory. It then modifies the environment variables to prioritize this local version when you run your code.

1. Creating a Virtual Environment

To create a virtual environment, use the venv module, which is included in the standard library:

```bash
python -m venv venv
```

This creates a venv directory in your project folder with the following structure:

```
venv/
├── bin/ (or Scripts/ on Windows)
│   ├── activate
│   └── python
├── include/
├── lib/
│   └── python3.x/
└── pyvenv.cfg
```

Key parts:
- bin/ (or Scripts/ on Windows): Contains the Python interpreter and scripts like activate.
- lib/: Includes the standard library and installed packages.
- pyvenv.cfg: Configuration file with basic environment settings.

2. Activating the Virtual Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

Windows (Command Prompt):
```
.\venv\Scripts\activate.bat
```

After activating, you should see (venv) in your terminal prompt, indicating the environment is active.
3. Installing Packages Locally

Now that your virtual environment is active, you can install packages:

```bash
pip install rich
```

This will only install the package in your venv directory, not system-wide.

4. Freezing and Sharing Dependencies

You can create a list of all the installed packages to share with others:

```bash
pip freeze > requirements.txt
```

This file will contain something like:

```text
rich==13.3.1
```

Later, you (or someone else) can recreate the exact same environment with:

```bash
pip install -r requirements.txt
```

5. Deactivating the Environment

To deactivate the virtual environment, simply run:

```bash
deactivate
```

This resets your terminal to use the global Python interpreter again.
6. Cleaning Up (Deleting the Environment)

If you ever want to completely remove the virtual environment, you can just delete the venv directory:

```bash
rm -rf venv  # macOS/Linux
```
```shell
rd /s /q venv  # Windows
```

## Why Use a Virtual Environment?
Here’s why it’s a good idea:
- Isolation: Keeps your project’s dependencies isolated from the global Python environment.
- Reproducibility: Makes it easy to share your project with others, including exact dependency versions.
- Security: Prevents unintentional interference with system-level packages.