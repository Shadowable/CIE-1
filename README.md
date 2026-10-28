# Simple Flask App

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000/ in your browser.

## Try the API in Postman

Start the app, then create these requests in Postman:

- **GET** `http://127.0.0.1:5000/api/greeting?name=Kate`
	- Expected response: `{"message":"Hello, Kate!"}`
- **POST** `http://127.0.0.1:5000/api/greeting`
	- Select **Body > raw > JSON** and send:

		```json
		{
			"name": "Kate"
		}
		```

	- Expected response: `{"message":"Hello, Kate!"}`

The POST request returns HTTP 400 if the JSON body is missing a non-empty `name` string.