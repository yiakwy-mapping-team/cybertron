TOP_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd)"

cd $TOP_DIR

# publish data
nohup python -m examples.python.talker &

# process data
python -m examples.python.listener
