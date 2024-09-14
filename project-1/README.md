# README

An extremely minimal project to learn GitHub Actions. Wanted to learn to write a Continuous Integration (CI) pipeline which runs whenever a new code change is pushed. CI should:
- run a python program 
- save the output of the python program to a plain text file


## Python Program
Converts a list of random temperatures from Celsius to Fahrenheit


## Workflow
As soon as a file is modifed and saved inside `project-1` folder, github triggers its Actions. 


## How To Use Project-1
1. Fork this repo
2. Do a git clone
3. Edit some file (e.g. add/remove a word, or even replace the sample.py with a new sample.py)
4. Add, commit and then push the changes
5. You can see the GitHub Actions running the python program in the "Actions" tab
6. CI Workflow will create a file called `output.txt` which contains the output from running `sample.py`
7. CI/GitHub Actions file is in the usual place: `devops-projects/.github/workflows/project-1.yaml`


