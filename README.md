# Soostone-WebServer
 


Run server.py (Python3)

## POST
Use post request for adding new item.
localhost:9000/input
Add item to Body as raw data.

#### Python Code:
```
import requests

url = "localhost:9000/input"

payload="test"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

#### Javascript/JQuery Code:
```
var settings = {
  "url": "localhost:9000/input",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "text/plain"
  },
  "data": "test",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

## GET
Use Get request for querying key.
localhost:9000/query
Add key to body as raw data.

#### Python Code:
```
import requests

url = "localhost:9000/query"

payload="test"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```
#### Javascript/JQuery Code:
```
var settings = {
  "url": "localhost:9000/query",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Content-Type": "text/plain"
  },
  "data": "test",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
