export NOW=`date +"%Y-%m-%d-%H%M%S"`
echo $NOW
python3 test.py --runner local --project_id $GCP_WEATHER_PROJECT_ID --topic_id $GCP_WEATHER_LOCAL_TOPIC_ID > logs/$NOW.log