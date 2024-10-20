# SusiAPI
SusiAPI is a Python web scraper designed to retrieve student grades from [susi.uni-sofia.bg](susi.uni-sofia.bg). It is a simple tool that automates the process of accessing and extracting grades, saving time for students who need to frequently check their academic performance online. It also displays the accumulated ECTS credits both from the mandatory and extracurricular courses, as well the grade formed for a scholarship.

This is a personal project, created for educational purposes. It is not affiliated with Sofia University.

__This is only a proof of concept.__

## Installation

### Windows
Run `install.bat`

### Linux/MacOS
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

If you ran the installer, you can simply run `run.bat` to start the program.

Otherwise:\
Run `venv/Scripts/activate.bat` (Windows) or `source venv/bin/activate` (MacOS/Linux)\
then `python susi_api.py` in the project directory.

## Examples

![Session](misc/image.png)

![Overall performance](misc/image-1.png)
