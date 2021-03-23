## task3
counter of appearances for three lists of timestamp intervals with one endpoint api

## To launch
```
pip install -r requirements.txt
uvicorn main:app --reload -p 8000
```
or with docker
```
docker build -t task3_image .
docker run -d --name task3_container -p 8000:80 task3
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
