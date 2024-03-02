#!/usr/bin/env python3

import pickle
import jsonpickle
from pathlib import Path

if __name__=='__main__':
  for p in Path('./pretrained_models').glob('**/config.pickle'):
    with open(p, 'rb') as f:
      config_obj = pickle.load(f)
    with open(p.parent/'config.json', 'w') as f:
      config_json = jsonpickle.encode(config_obj)
      config_json_edit = config_json.replace('config.GlobalConfig', 'team_code.config.GlobalConfig')
      f.write(config_json_edit)