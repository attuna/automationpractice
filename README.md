# Automation Practice Testing


## Features

- **Login Tests**: Verify login functionality with both valid and invalid credentials.
- **Registration Tests**: Test user registration processes, including handling valid and invalid inputs.
- **Shopping Flow**: Validate product selection, cart addition, and the checkout process.
- **Sorting/Filtering**: Ensure correct functionality for product sorting and filtering.

## Setup
### 1.Clone the Repository

```bash
git clone https://github.com/attuna/automation-practice.git
cd automation-practice
```

### 2.Install Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

To run tests with specific markers, use the following command:

```bash
pytest -m "marker_name"
```

For example, to run tests related to login and that are successful:
```bash
pytest -m "login and successful"
```

## Generating Reports

To generate a test report in JSON format, use the following command:
```bash
pytest --cucumberjson=<path_to_json_report>
```
