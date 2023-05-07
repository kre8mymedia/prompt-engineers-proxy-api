# Prompt Engineers - API Proxy Server

### JWT Authenication Docs From Here
https://testdriven.io/blog/fastapi-jwt-auth/

### Run Development environment by running the following...
```bash
## Setup virutal env
python3 -m venv .venv
source env/bin/activate
pip3 install -r requirements.txt

## Run dev environment
bash scripts/dev.sh

## Run tests
bash scripts/test.sh

## Build docker image
bash scripts/build.sh

## Deploy using kubernetes and helm
bash scripts/upgrade.sh $APP_ENV $NAMESPACE $IMAGE_REPO
```