# HackKey
Password manager written for HackSussex2024 by the 💣 team.

Devpost - https://devpost.com/software/hackkey-a-gamified-password-manager?ref_content=my-projects-tab&ref_feature=my_projects

### Development Environment Setup:
0. Install Python 3.12.2 https://www.python.org/downloads/release/python-3122/
1. Create a virtual environment in the same directory as this readme. `python -m venv venv` (or Windows users without Python 3.12.2 in path: `c:/Users/{User}/AppData/Local/Programs/Python/Python312/python.exe -m venv venv`, replacing '{User}' with your username). You should see your virtual environment has been created in the subdirectory 'venv'.
3. Activate your virtual environment by running its activate script: `./venv/Scripts/activate` (Mac/Linux: `./venv/bin/activate`) . You can now use 'pip' and 'python' freely as they're in the PATH of your new virtual environment.
4. Run `pip install -r ./requirements.txt` to install our dependencies.
5. Apply model migrations: `python hackkey/manage.py migrate hackkey`.

### Commands
- Run development server `python hackkey/manage.py runserver`
- Apply migrations `python hackkey/manage.py migrate`
- Open the management command line `python hackkey/manage.py`
- Update your dependencies `pip install -r ./requirements.txt`
