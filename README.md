# Weather Home Station (rasp client)

Personal project to check temperature using a raspberry pi and a DHT22 sensor

## setup  
### Installing requirements

``pip3 install -r requirements.txt``

### Environment variables

Define the Service account credentials path. (See [Create GCP Keys](https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console))

``export GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json``

### run  
#### Development 

Just execute the command and the result will be print on console

``python3 check.py``

#### Production

To production mode will be necessary informa another options:

* **--runner** : Runners available (local|gcp). The `local` prints on console, `gcp` send a message to a GCP PubSub Topic, in this case the following options are `required`
* **--project_id** : The GCP project id where the topic was created
* **--topic_id** : The GCP topic id where the message will be published

``python3 check.py --runner gcp --project_id *your_gcp_project_id* --topic_id *your_gcp_topic_id*``