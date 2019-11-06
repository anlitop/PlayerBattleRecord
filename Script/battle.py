import pandas as pd
import config
import draw


#global value
current_id=0
key=''
count=0


def init_dict():
	kdict={
		"人数":0,
		"战斗场次分布":[],
		"战斗胜场分布":[],
		"战斗胜率分布":[],
		"段位分布":[],
		"付费玩家分布":[]
	}
	return kdict
def built_kdict(keys):
	kdict={}
	for kkey in keys:
		kdict[kkey]=init_dict()
	return kdict
def init_player(kdict,key):
        
    idx=kdict[key]["人数"]
    if idx>=2:
	    #处理上一位玩家
        kdict[key]["战斗胜率分布"][idx-1]=kdict[key]["战斗胜场分布"][idx-1]/kdict[key]["战斗场次分布"][idx-1]
	
	#初始化新一位玩家
    kdict[key]["人数"]+=1
    kdict[key]["战斗场次分布"].append(0)
    kdict[key]["战斗胜场分布"].append(0)
    kdict[key]["战斗胜率分布"].append(0)
    kdict[key]["段位分布"].append(0)
    kdict[key]["付费玩家分布"].append(0)

    

def update_player(kdict,key,data_content):
	#处理叠加
	idx=kdict[key]["人数"]
	kdict[key]["战斗场次分布"][idx-1]+=data_content["games"]
	if data_content["is_win"]==1 and data_content["race_type"] in (1011,1010):
		kdict[key]["战斗胜场分布"][idx-1]+=data_content["games"]
def is_sr_player(id,ids):
    
    if id in ids["#account_id"].tolist():
        return True
    return False
def ana(data,kdict):
    global current_id
    global sr_account
    global count
    count+=1
    if is_sr_player(data["#account_id"],sr_account):
        key='次留玩家'
    else:
        key='非次留玩家'
    if data["#account_id"]==current_id:
		#同一个玩家
        update_player(kdict,key,data)
    else:
        current_id=data["#account_id"]
        init_player(kdict,key)
        update_player(kdict,key,data)
    print(count)
def run():
    global sr_account
    config_json=config.get_config()
    sr_account=pd.read_csv(config_json["次留玩家id"])
    battle=pd.read_csv(config_json["战斗记录"])
    kdict=built_kdict(["次留玩家","非次留玩家"])
    battle.apply(ana,axis=1,kdict=kdict)
    config.save_dict(kdict)
if __name__ == "__main__":
    run()
    data=config.get_dict("kdict.json")
    draw.draw(range(0,data["次留玩家"]["人数"]),data["次留玩家"]["战斗场次分布"])
    
    