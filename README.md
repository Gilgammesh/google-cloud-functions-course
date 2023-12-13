# Google Cloud Functions Course

## Starting a project

To start a new project in Google Cloud, we can go to the 
[Firebase Console](https://console.firebase.google.com) or create it from [Google Cloud Platform Console](https://console.cloud.google.com)

## Creating a virtual environment

First we have to install `python-dotenv` with the following command:

```sh
pip install python-dotenv
```

Install new package to our environment we creat a file called `requirements.txt` and execute the following command:

```sh
pin install -r requirements.txt
```

## Creating first google function

Create folder `helloworld` in root project

Create file `main.py`, this contain logic for api

```py
def hello_world(request):
    request_args = request.args
    if request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return f'Hello {name}!'
```

Move inside folder `helloworld` and run function with command:

```sh
functions-framework --target hello_world --debug
```

We call by the function name `hello_world`

## Deploy our functions

First login with google cloud account

```
gcloud init
```

List projects

```
gcloud projects list
```

Set our project ID with the following command:

```
gcloud config set project [YOUT_PROJECT_ID]
```

Then we deploy our funcitons with this command:

```
gcloud functions deploy [FUNCTION_NAME] --runtime python310 --trigger-http
```