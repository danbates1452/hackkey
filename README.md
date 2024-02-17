# HackKey
Password manager written for HackSussex2024 by the 💣 team.


### Development Environment Setup:
0. Install Python 3.12.2 https://www.python.org/downloads/release/python-3122/
1. Create a virtual environment by running Python from it's installed path. `python -m venv venv` (or Windows users without Python 3.12.2 in path: `c:/Users/<User>/AppData/Local/Programs/Python/Python312/python.exe -m venv venv`). You should see your virtual environment has been created in the subdirectory 'venv'.
3. Activate your virtual environment by running its activate script: `./venv/Scripts/activate` (Mac/Linux: `./venv/bin/activate`) . You can now use 'pip' and 'python' freely as they're in the PATH of your new virtual environment.
4. Run `pip install -r ./requirements.txt` to install our dependencies.

### Commands
You will want to `cd hackkey` to move your working directory to the hackkey/hackkey subdirectory for Django commands.
- Run development server `python manage.py runserver`
- Apply migrations `python manage.py migrate`
- Open the management command line `python manage.py` 