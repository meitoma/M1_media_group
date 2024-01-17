import numpy as np
import os
from os.path import join, dirname
from dotenv import load_dotenv

parts={
    1:'1_INTRODUCTION,RELATED WORK',
    2:'2_APPROACH First half',
    3:'3_APPROACH Second half',
    4:'4_EXPERIMENTAL RESULTS,CONCLUSION',
}

class member:
    def __init__(self,name,first_choice_num,second_choice_num):
        self.name=name
        self.first_choice_num=first_choice_num
        self.second_choice_num=second_choice_num
        self.part_num=0

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path) #.envファイルの読み込み

member1=member(name=os.environ.get("NAME1"),first_choice_num=4,second_choice_num=1)
member2=member(name=os.environ.get("NAME2"),first_choice_num=4,second_choice_num=None)
member3=member(name=os.environ.get("NAME3"),first_choice_num=1,second_choice_num=2)
member4=member(name=os.environ.get("NAME4"),first_choice_num=1,second_choice_num=None)

members=[member1,member2,member3,member4]
choices=np.array([m.first_choice_num for m in members])

Undecided_part={1,2,3,4}
while Undecided_part:
    unsuccessful_mem=set()
    #? partの担当者決定 
    for part_num in range(1,5):
        select_mem=set(np.where(choices==part_num)[0])
        if len(select_mem)==0 or part_num not in Undecided_part:continue
        if len(select_mem)==1:
            members[select_mem.pop()].part_num = part_num
        else:
            decide_mem=select_mem.pop()
            members[decide_mem].part_num = part_num
            unsuccessful_mem = unsuccessful_mem.union(select_mem)
        Undecided_part.remove(part_num)
    
    #? 未決定のmemberの希望を更新
    choices=np.array([0]*4)
    cp_Undecided_part=set(Undecided_part)
    for m in range(4):
        if m in unsuccessful_mem:
            choices[m] = members[m].second_choice_num if members[m].second_choice_num is not None else cp_Undecided_part.pop()

for m in members:
    print(f"{m.name}\t:{parts[m.part_num]}")