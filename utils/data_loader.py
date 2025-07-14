import os
import json
import pandas as pd

class DataLoader:
    def __init__(self, path:str):
        self.root = path

    def _get_path(self, *path:str) -> str:
        sep = os.sep
        return self.root + sep + sep.join(path)
    
    def _read_json(self, path:str):
        with open(path, 'r') as f:
            return json.load(f)

    def get_input_data_train(self) -> pd.DataFrame:
        path = self._get_path('_input_data', 'train.csv')
        return pd.read_csv(path)
    
    def get_input_data_test(self) -> pd.DataFrame:
        path = self._get_path('_input_data', 'test.csv')
        return pd.read_csv(path)
    
    def get_data_desc(self):
        path = self._get_path('_data_description', 'data_desc.json')
        return self._read_json(path)
    
    def get_label_desc(self):
        path = self._get_path('_data_description', 'label_desc.json')
        return self._read_json(path)
    
    def get_llm_config(self):
        path = self._get_path('_llm_config', 'api_config.json')
        return self._read_json(path)
    
    def get_data_train(self) -> pd.DataFrame:
        path = self._get_path('data', 'train.csv')
        return pd.read_csv(path)
    
    def get_data_test(self) -> pd.DataFrame:
        path = self._get_path('data', 'test.csv')
        return pd.read_csv(path)
    
    def get_keyword_concepts(self):
        path = self._get_path('concepts', 'keyword_concepts.json')
        return self._read_json(path)
    
    def get_abstract_concepts(self):
        path = self._get_path('concepts', 'abstract_concepts.json')
        return self._read_json(path)
    
    def get_keyword_wl_data(self) -> pd.DataFrame:
        path = self._get_path('weak_label_data', 'keyword_wl.csv')
        return pd.read_csv(path)
    
    def get_abstract_wl_data(self) -> pd.DataFrame:
        path = self._get_path('weak_label_data', 'abstract_wl.csv')
        return pd.read_csv(path)
    
