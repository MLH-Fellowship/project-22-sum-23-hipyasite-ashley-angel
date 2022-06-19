tmux new -s my_session
cd project-22-sum-23-hipyasite-ashley-angel
git fetch && git reset origin/main --hard
python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
flask run --host=0.0.0.0
tmux detach
