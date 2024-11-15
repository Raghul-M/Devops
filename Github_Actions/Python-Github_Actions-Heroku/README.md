
# Python Webapp Deployment on Heroku Using GitHub Actions

![1_HY_qNXxMeD3LyUaXZHlcug](https://github.com/Raghul-M/Python-Github_Actions-Heroku/assets/71755586/5fdcf2d8-2c08-46a0-822b-31ac8ae0640d)

This project demonstrates how to deploy a simple Python web application using Flask to Heroku deployment, with automated testing using pytest and deployment using GitHub Actions.

## Project Description

This project includes:
- A basic Flask web application.
- Tests written in pytest.
- Automated deployment to Heroku using GitHub Actions.

## Prerequisites

- Python 3.10+
- Git
- GitHub account
- Heroku account
- Heroku CLI


### Local Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Raghul-M/Python-Github_Actions-Heroku.git
   cd Python-Github_Actions-Heroku
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application locally:**
   ```sh
   python3 app.py
   ```

### Running Tests

 **Run tests with pytest:**
   ```sh
   pytest
   ```
![Screenshot from 2024-06-28 15-29-45](https://github.com/Raghul-M/Python-Github_Actions-Heroku/assets/71755586/f824b763-f8db-44fa-902b-0aead8c918df)

## Deployment

**Heroku Setup**

![Screenshot from 2024-06-28 15-40-58](https://github.com/Raghul-M/Python-Github_Actions-Heroku/assets/71755586/2d0e3693-8991-40d7-b487-06050c70ad7a)


1. **Login to Heroku:**
   ```sh
   heroku login
   ```

2. **Create a new Heroku app:**
   ```sh
   heroku create your-app-name
   ```

3. **Set up GitHub Actions for Heroku deployment:**

   - Go to your GitHub repository.
   - Navigate to `Settings` > `Secrets` > `New repository secret`.
   - Add the following secrets:
     - `HEROKU_API_KEY`: Your Heroku API key.
     - `HEROKU_APP_NAME`: Your Heroku app name.


4. **Add the GitHub Actions workflow file (`.github/workflows/deploy.yml`):**
   ```yaml
   name: Python application
   on:
    push:
      branches: [ "main" ]
    pull_request:
      branches: [ "main" ]
    permissions:
      contents: read
    jobs:
      build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest

    deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.12.12
      with:
          heroku_api_key: ${{secrets.HEROKU_API_TOKEN}}
          heroku_app_name: ${{secrets.HEROKU_APP_NAME}} #Must be unique in Heroku
          heroku_email: "eyaiinov1234@gmail.com"
    
   ```

## Screenshots


### Localhost App
![Screenshot from 2024-06-28 15-36-18](https://github.com/Raghul-M/Python-Github_Actions-Heroku/assets/71755586/1a8a00c3-deba-4e39-bfd0-6b5f72601337)

### Deployed App on Heroku
![Screenshot from 2024-06-28 15-37-23](https://github.com/Raghul-M/Python-Github_Actions-Heroku/assets/71755586/9b08a9fa-63cb-4a0e-bb79-7ba8144880c0)




