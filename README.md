# Eunoia Cloud

we can start my declaring our variable in google cloud

```
PROJECT_ID=$(gcloud config get-value core/project)
REGION=us-central1
```

before we deploy our cloud run we need to make a sql instances to hold django database
```
gcloud run deploy django-cloudrun --platform managed --region $REGION \
  --image gcr.io/$PROJECT_ID/django-cloudrun \
  --add-cloudsql-instances ${PROJECT_ID}:${REGION}:mydb \
  --allow-unauthenticated
```


redeploy command with revision:

```
gcloud builds submit --tag gcr.io/$PROJECT_ID/django-cloudrun

gcloud builds submit --config cloudmigrate.yaml \
    --substitutions _REGION=$REGION

gcloud run deploy django-cloudrun --platform managed --region $REGION \
  --image gcr.io/$PROJECT_ID/django-cloudrun
```
