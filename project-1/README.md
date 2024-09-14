# README

An extremely minimal project to learn GitHub Actions. Wanted to learn what kind of GitHub Action template I need to write to:
- run a python program 
- save the output to a plain text file
- 

## What Does It Do
A sample python program that converts a list of random temperatures from Celsius to Fahrenheit


## Workflow
As soon as a file is modifed and saved insside `project-` folder, github triggers its Actions: project-1.yaml workflow. The workflow runs the python program and saves the output in a text file


## How To Use Project-1
1. Fork this repo
2. Do a git clone
3. Edit some file (e.g. add/remove a word, or even replace the sample.py with a new sample.py)
4. Add, commit and then push the changes
5. You can see the GitHub Actions running the python program in the "Actions" tab
6. CI Workflow will create a file called "output.txt" which contains the output from running sample.py
7. CI/GitHub Actions file is in the usual place: `devops-projects/.github/workflows/project-1.yaml`


