## task3
counter of appearances for three lists of timestamp intervals with one endpoint api

## To launch
```
pip install -r requirements.txt
uvicorn app:app --reload
```

## Endpoint

at http://127.0.0.1:8000/appearance

method: POST

structure of request body:
```
{
  "lesson": [ int ],
  "pupil": [ int ],
  "tutor": [int ]
}
```
more info at '/docs' or '/redoc'
