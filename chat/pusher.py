import os

import pusher

pusher_client = pusher.Pusher(
    app_id=os.getenv('APP_ID'),
    key=os.getenv('KEY'),
    secret=os.getenv('SECRET'),
    cluster=os.getenv('CLUSTER'),
    ssl=bool(int(os.getenv('SSL')))
)
