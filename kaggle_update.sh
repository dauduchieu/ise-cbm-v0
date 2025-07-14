rm -rf venv
kaggle datasets version -p . --dir-mode zip -m "Update with subfolders"
python3 -m venv venv
pip install -r requirements.txt