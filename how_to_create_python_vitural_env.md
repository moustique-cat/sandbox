# Set Up a Virtual Environment (Recommended)

To avoid conflicts between projects, it's a good idea to create isolated environments for each project:

```bash
python3 -m venv my_python_env
```

Replace `my_python_env` with a more meaningful name if you prefer. This will create a directory containing a standalone Python interpreter and libraries.

### Activate the Environment

To activate the environment, run:

```bash
source my_python_env/bin/activate
```

You'll see the environment name in your terminal prompt, indicating it's active. To deactivate it, just run:

```bash
deactivate