# Installation
This requires python 3.5 or greater to run, and we assume python setup tools.
Run the following commands to run
```
cd {path to this git project}/server/
pip install virtualenv
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
# Run
To execute, run the following command:
```
PARTICLE_ACCESS_TOKEN={put particle access token here} FLASK_APP=server FLASK_ENV=development flask run --host 0.0.0.0 --port 80
```

# Test
Open up your browser to http://localhost:80/. And you should see "Hello, World!".
