#!/bin/sh
echo "passing env from outer container to inner container"
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)
uvicorn main:app --host 0.0.0.0 --port 8000