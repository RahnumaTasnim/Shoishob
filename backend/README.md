# Shoishob Flask backend

ML model is saved locally with Pickle in `model` folder.

Then, model is loaded in flask app.

Flask is used to create a REST api on `/` endpoint. The api expects a JSON with `value_array` property. On request, flask feeds the ML model(that is loaded with pickle) with `value_array`. The result is then returned to frontend as the api's response.

## How to run

- Open `cmd` in `shoisho_backend`

Run following commands,

```bash
.venv\scripts\activate
python app.py
```

- Make a POST request to `127.0.0.1:5000` with following JSON body

```json
{
  "value_array": "1,0,0,0,0,1,1,1"
}
```
