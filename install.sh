#!/usr/bin/env sh


mkdir -p /opt/project_s
cp s.py /opt/project_s/s.py
chmod +x /opt/project_s/s.py
ln -s -f /opt/project_s/s.py /usr/local/bin/s
echo "success"
