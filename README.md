# Elective 4 Midterm 


##  Introduction

Elec4Midterm is a Python-based image processing project that applies multiple visual enhancement and transformation techniques to digital images. The project demonstrates modular image processing, automated testing, and continuous integration (CI) using GitHub Actions. Users can apply effects such as beautification, cartoonization, nostalgic filters, brightness enhancement, slow-shutter effects, and image classification in a reproducible and automated way.

This project is designed for academic and practical DevOps learning by combining image processing with automation, testing, and collaborative development workflows.



##  Project Functionality

The system processes digital images using multiple automated techniques:

* Beautification Enhancement  
* Brightness Adjustment  
* Cartoon Effect Transformation  
* Nostalgic/Vintage Filtering  
* Slow Shutter Motion Blur  
* Image Classification (Candid or Posed)

All processes are automated and produce output images after execution.



##  Architecture Overview

The project follows a modular DevOps-oriented structure:

* **Input images** are stored in the `input/` directory  
* **Processing modules** located in `src/` apply image transformations  
* **Outputs** are saved inside `output/`  
* **Unit tests** validate each processing module  
* **GitHub Actions CI pipeline** automatically validates code changes  

###  Pipeline Flow

User → Input Folder → Processing Scripts → Output Folder<br/>
↓<br/>
Unit Testing<br/>
↓<br/>
GitHub Actions CI<br/>



##  DevOps Pipeline (GitHub Actions)

This project implements Continuous Integration (CI) using GitHub Actions.

###  CI Pipeline Workflow

The pipeline automatically runs whenever code is pushed or a pull request is created.

###  Automated Steps

1. Clone repository  
2. Setup Python environment  
3. Install dependencies using: <br/>
 pip install -r requirements.txt
4. Execute automated tests using: <br/>
pytest
5. Pipeline reports PASS or FAIL status  



###  CI Benefits

* Early bug detection  
* Automated validation  
* Improved collaboration  
* Reliable build environment  



##  Installation and Usage (End Users)

###  Prerequisites

* Python 3.8 or higher  
* pip package manager  



###  Installation

git clone https://github.com/your-username/Elec4Midterm.git <br/>
cd Elec4Midterm <br/>
pip install -r requirements.txt <br/>

###  Usage

1. Place image inside `input/` folder  
2. Run desired processing script: <br/>
python src/cartoon.py

3. Processed image will appear in `output/`

---

##  Installation and Usage (Contributors)

### 🛠 Development Setup

1. Fork the repository  
2. Clone your fork: <br/>
git clone https://github.com/your-username/Elec4Midterm.git <br/>
cd Elec4Midterm
3. Create virtual environment: <br/>
python -m venv venv <br/>
source venv/bin/activate <br/>
Windows: <br/>
venv\Scripts\activate
4. Install dependencies: <br/>
pip install -r requirements.txt

---

###  Running Tests <br/>
pytest

##  Code Quality & Structure

The project follows:

* Modular script design  
* Clear folder organization  
* Unit testing for validation  
* Version control best practices  
* Continuous integration automation  

##  Collaboration & Git Usage

This project uses structured Git workflows including:

* Feature branching  
* Pull request reviews  
* Clear commit messages  
* CI validation before merging  

##  Contributor Expectations

Contributors should:

* Create issues before starting major features  
* Use feature branches  
* Write unit tests for new functionality  
* Ensure CI tests pass before pull requests  
* Follow clean commit message standards


##  Collaborators

* Member 1 – Roshan Alfonso Garcia
* Member 2 – Mervin Valerio
* Member 3 – Maquee Visitacion
* Member 4 – Xavier Hans Visda
