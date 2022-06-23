#!/bin/bash

number=$(( RANDOM % 1000 ))
curl -s --request POST http://localhost:5000/api/timeline_post -d "name=${number}&email=email@example.com&content=Testing Timeline Post API" >> /dev/null
curl -s --request GET http://localhost:5000/api/timeline_post > /tmp/timeline_post_test1.txt
if grep -q "$number" /tmp/timeline_post_test1.txt; then
    curl -s --request DELETE http://localhost:5000/api/timeline_post -d "name=${number}" >> /dev/null
    curl -s --request GET http://localhost:5000/api/timeline_post > /tmp/timeline_post_test2.txt
    if grep -q "$number" /tmp/timeline_post_test2.txt; then
        echo "FAIL"
    else
        echo "PASS"
    fi
else
    echo "FAIL"
fi
