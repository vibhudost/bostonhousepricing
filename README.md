# Bostonhousepricing
### Software and Tools requirements
1. [Git Hub](https://github.com/)
2. [Heroku Account](https://heroku.com)  (Or any other Cloud Service)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLi](https://cli.github.com/)

### Create a new environment on VS code
DATA Spell


conda will show command not found error
Once completed, add Conda to path as shown in the command below:
export PATH=/home/debian/anaconda3/bin:$PATH
### depends where anaconda is installed
or export PATH=/home/admin/anaconda3/bin:$PATH 
### chekc for conda version
conda --version

restart VS code
Ctrl+Shift+P search Python:create environment
search for conda
It will show creating environment

We can deactivate an environment using deactivate

Create a new environment for the project

through terminal

```
conda create -p venv python==3.7 -y
```
venv is environment name
or directly through GUI

```
pip install -r requirement.txt
```

Add files in .gitignore which you dont want to commit
like herethe environment .conda