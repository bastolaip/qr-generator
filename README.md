# qr-generator

This is small python project to generate a qr code along with logo at the center of the qr code and some text(optional) at the center bottom of the qr image.

# How to?

## 1. Install Python 3.10

### 1. macOS

You can install Python 3.10 using Homebrew, a package manager for macOS.

Install Homebrew (if not already installed): Open your terminal and run:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Python 3.10:

```
brew install python@3.10
```

Verify installation: Once installed, verify by checking the version:

```
python3.10 --version
```

Set Python 3.10 as default (optional): If you want to set Python 3.10 as your default python3, run:

```
brew link --overwrite python@3.10
```

## 2. Create Virtual Environment

### Using venv (built-in)

#### Step-by-Step Instructions:

1. Navigate to your project directory (or any directory where you want to create the virtual environment):

```
cd /path/to/your/project
```

2. Create the virtual environment: Run the following command to create a virtual environment named venv (or any name you prefer):

```
python3.10 -m venv venv
```

This will create a folder called venv containing the necessary files to run the virtual environment.

3. Activate the virtual environment:

On macOS/Linux:

```
source venv/bin/activate
```

On Windows:

```
venv\Scripts\activate
```

4. Verify the virtual environment is active: Once the environment is active, you should see the environment name (e.g., (venv)) in your terminal prompt. You can also verify by running:

```
python --version
```

It should point to the Python version in your virtual environment.

5. Deactivate the virtual environment: When you're done and want to deactivate the environment, simply run:

```
deactivate
```

## 3. Install Dependency

```
pip install -r requirements.txt
```

## 4. Update `qr.py` to your desired data/information

-   Rreplace `assets/logo.png` by your logo
-   Update your data in line 68 of `qr.py`

```
# Usage example
generate_qr_with_logo_in_rounded_rectangle(
    data="http://example.com",
    logo_path="assets/logo.png",  # Path to your logo image
    output_path="output/qr.png",  # Output file
    text="Hello world!"  # Text to add
)
```

In above function call, update `data` value to your data value and `text` to your text. If you do not want it, keep it blank.

## 5. Run to Generate qr Code

```
$ python3.10 qr.py
```

The qr image will be saved in `output/qr.png`.
