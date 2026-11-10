
# Student CI Project

## Overview
A simple Python calculator application developed to demonstrate Continuous Integration using Jenkins and GitHub.

## Features
- Addition
- Subtraction
- Multiplication
- Automated unit testing

## Requirements
- Python 3
- Jenkins
- Git

## Run the Application
```bash
python app.py
```

## Run Automated Tests
```bash
python -m unittest discover -s tests -v
```

## CI Pipeline
Jenkins retrieves the source code from GitHub, executes the application tests, and reports the build result.
This project uses Jenkins Poll SCM to automatically detect GitHub changes and run the CI pipeline.