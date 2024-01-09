# WebDriverIO Project

This is a python, pytest project for execute a tests over Carnnival.com

## Installation

1. **Clone (copy) the repository:**

    ```bash
    git clone repo_URL
    cd your-repo
    ```

2. **Install packages:**

    ```bash
    pip install -r requirements.txt
    brew install allure
    ```

2. **Driver:**
Download and copy the chrome driver into the folder **drivers**

## Running Tests

Execute the following command to run Pytest tests:

```bash
pytest --alluredir=report --capture=no --localhost --browser "chrome" -v
```

## Generate report

After have test execution done execute the following command to generate the Allure report:

```bash
 allure serve report  
```

## Project Structure
The primary files and directories are organized as follows:

```
├── pages/
│   └── base.py
│   └── home_page.py
│   └── result_page.py
├── test_data/
│   └── locators
│       └── common.py
│       └── home_page.py
│       └── result_page.py
├── tests/
│   └── test_userStory01.py
│   └── test_userStory02.py
├── utils/
│   └── webdriver_factory.py
├── conftest.py
├── requirements.txt
├── settings.py
└── README.md
```

## Result record example

https://drive.google.com/file/d/1o_Ag6iJcrzKHHqbJTPbYHLG_7mvDriWE/view?usp=sharing