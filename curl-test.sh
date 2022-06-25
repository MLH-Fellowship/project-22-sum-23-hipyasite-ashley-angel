#!/bin/sh

curl -f -s -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=angel&email=angel.angel@mlh.io&content=coolio'
status="$?"
b=0

if [ $status == 0 ]
then
   echo "this was a success"
   curl -s --request GET http://localhost:5000/api/timeline_post
else
   echo "this was a failure"
fi
