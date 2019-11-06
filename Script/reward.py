from json import dumps,load
import pandas as pd



def init_config():
    with open("Config.json",'r',encoding = 'utf-8') as f:
        return load(f)

if __name__ == "__main__":
    config=init_config()
    townitem=pd.read
    print(config["物品表格"])
