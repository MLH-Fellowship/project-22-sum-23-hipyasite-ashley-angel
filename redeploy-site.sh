#!/bin/bash

tmux kill-server
cd ~/project-22-sum-23-hipyasite-ashley-angel
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new "python -m venv python3-virtualenv;source python3-virtusud