# Flask_api

## Introduction
A simple Flask application that provides an API endpoint to retrieve specific information in JSON format.

## Installation
1. Clone the repository
``` 
git clone https://github.com/CyrusNchege/Flask_api

cd Flask_api
```
2. Create a virtual environment
```
python3 -m venv venv
```
3. Activate the virtual environment

windows:
```
venv\Scripts\activate
```
macOS/Linux:
```
source venv/bin/activate
```
4. Install the dependencies
```
pip install -r requirements.txt
```
5. Run the application
```
python3 app.py
```

## endpoint

```
/api
```

The API endpoint accepts GET requests with two query parameters:

**slack_name:** Your Slack name.(e.g., "Cyrus-Nchege")

**track:** The track you are interested in (e.g., "Devops").

### Example

```
http://localhost:5000/api?slack_name=Cyrus-Nchege&track=baDevops

```
### Response

``` json
{
  "slack_name": "Cyrus-Nchege",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "Devops",
  "github_file_url": "https://github.com/CyrusNchege/Flask_api/blob/main/app.py",
  "github_repo_url": "https://github.com/CyrusNchege/Flask_api",
  "status_code": 200
}
```

