cp -f ./kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json

rm -rf venv
kaggle datasets create -p . --dir-mode zip
python3 -m venv venv
pip install -r requirements.txt
