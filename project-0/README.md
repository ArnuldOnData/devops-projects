# README

An extremely minimal project to learn GitHub Actions

## What is Project-0
Wanted to learn what kind of GitHub Action template I need to write to:
- build a docker image
- run the image 
- save the output to a plain text file

## How To Use Project-0
1. Fork this repo
2. remove "output.txt" (if you let it be there then GitHub Actions will fail)
3. Last step changes the repo contents, and this a trigger for the GitHub Actions workflow I have written. You can also edit the sample.py file to do something else if you want
4. git add and commit
5. git push
6. You will see the GitHub building the image and running the python program in "Actions" tab 
7. You will see a new file called "output.txt" with the output from GitHub Action workflow
8. You will receive an email from GitHub too on whether the Actions failed/succeeded
9. Workflow is in the usual place: `devops-projects/.github/workflows/project-0.yaml`



