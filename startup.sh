#!/bin/sh
echo "passing env from outer container to inner container"
# Get environment variables to show up in SSH session
eval $(printenv | awk -F= '{print "export " "\""$1"\"""=""\""$2"\"" }' >> /etc/profile)
uvicorn main:app --host 0.0.0.0 --port 8000