# flask-ngrok

A simple way to demo Flask apps from your machine.
Makes your [Flask](http://flask.pocoo.org/) apps running on localhost available
 over the internet via the excellent [ngrok](https://ngrok.com/) tool.

## Compatability
Python 3.11+ is required.

## Installation

```bash
pip install flask-ngrok
```

## Quickstart
Import and add a call to patch_to_run_with_ngrok to patch your Flask app so that it can be accessed with public url
```python 
from flask_ngrok import patch_to_run_with_ngrok

app = ...

patch_to_run_with_ngrok(app=app)
```

### Quick example:
```python
from flask import Flask
from flask_ngrok import patch_to_run_with_ngrok

app = Flask(__name__)

# Patch Flask app.run function to also run ngrok when called
patch_to_run_with_ngrok(app)  

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```
---
## Other use-cases:
You can use an app object however you like
```python
from flask import Flask
from flask_ngrok import patch_to_run_with_ngrok

app = Flask(__name__)


def hello():
    return 'Hello, World!'


def set_up_app(app_to_set_up: Flask):
    patch_to_run_with_ngrok(app_to_set_up)
    app_to_set_up.add_url_rule('/', 'hello', hello, methods=['GET'])


def main():
    set_up_app(app)
    app.run('0.0.0.0', 3000)  
    # Note that you can specify port positionally
    # (you don't need to use keyword args syntax like port=...)
 
    
if __name__ == '__main__':
    main()
```


### Credits:
https://github.com/gstaff/flask-ngrok

