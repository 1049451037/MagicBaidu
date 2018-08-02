import os
import sys
import time
import random
import pprint

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MagicBaidu import MagicBaidu

################################################
# """
# cd MagicBaidu
# python Examples/baidu_search.py
# """
#################################################

mb = MagicBaidu()

# Get {'title','url','text'}
for i in mb.search(query='python'):
	try:
		pprint.pprint(i)
	except:
		pass

time.sleep(random.randint(1, 5))

# Output
'''
{'text': 'The official home of the Python Programming Language...  # Python 3: '
         "List comprehensions >>> fruits = ['Banana', 'Apple', 'Lime'] >>> "
         'loud_fruits ...',
 'title': 'Welcome to Python.org官网',
 'url': 'http://www.baidu.com/link?url=q1XOORMUTtdQ4ZETaeGR8dUB2fVwmPJitpC9yXyaZgr7hblAu9KdTTVtNTVbA4YG'}
{'text': 'The official home of the Python Programming Language...  Python '
         'releases by version number: Release version Release date Click for '
         'more  Python 3.7.0 2018...',
 'title': 'Download Python | Python.org',
 'url': 'http://www.baidu.com/link?url=LqB_67xjqPO6t3-qvk8S3Z8Hgkxx_BLg3Q5fK7Dqv0ORDf1jxC97ytXxSbTpv0MA'}
{'text': '这是小白的Python新手教程,具有如下特点:中文,免费,零起点,完整示例,基于最新的Python 3版本。...',
 'title': 'Python教程 - 廖雪峰的官方网站',
 'url': 'http://www.baidu.com/link?url=td8reUWHJ3ubay4HVxybEMDe-ilddmWsGV9YELCkqS65JP_6PcBPripF997V8clFMRfG-PLQmQAM3aNb8NZPTvwgbTYUtfX4B7gfLvmmI27la_C53jW1YrMfHW6kFpzY'}
......
'''
# Get first page
for url in mb.search_url(query='python'):
	pprint.pprint(url)

time.sleep(random.randint(1, 5))

# Output
'''
'http://www.baidu.com/link?url=90eYpfUta8MyOjZAtOSawwpUYp10pHaUgxxrpCxr43y-XIUeZ8ZLxL8Kqon4q7Ug'
'http://www.baidu.com/link?url=3zE-dzr1l3uxYndpVcD4Qz7sluHZneX7NrLb5mVQ1xvMSeKartvrUwHCCMuGce9c'
'http://www.baidu.com/link?url=vzhkuZt0T2NPr8G6ZSgCuljx-yCgkM-ELDVPqAUE-iH_G7IgFJ23nPqW8VPNNxOlri-fbgcrn9b1hxn7eUXwh-tZxyBqx281oBv10ZKqGwlI55QS-9Wz_a-vb-3Vprq7'
'http://www.baidu.com/link?url=F1cwT3dPMiab0yzElV3jT4pKJDAnoBduyEsOtBsj92Nv8jsqcaM-YSZIOm4u56uvHf-b-uYww_JazKqo46jX5K'
'http://www.baidu.com/link?url=TtrR8v1nKV1ewe4fE6oTnAb3MmaMiEtszjk_5x5HaFzOwe14VKBTM46gQP5ix3FRxZjbKYI80sByWc2nlXkc_q'
'http://www.baidu.com/link?url=oUNlVuYFsEgYMbgVa7Egb8KmPYR2ZHIqgcDysY0I2tnFG0CFxIwWTR0FjAxbM_V4MgU-g6GjgprSbucC4K23e_'
'http://www.baidu.com/link?url=XoEPODbTz5OGtkMucTZ0-pdeZFq-uFDI7UEgXKgrXG40RnRIXVsgur7Qy0MrFtr5'
'http://www.baidu.com/link?url=O0wCEpKOzOLZpV8Kl_mGJTXUTyP5WRWdnET77DuHGhB-wTUEj5-AZ3Qjc2776BtoLM-6eiZ_4UDK4NcC64XC8q'
'http://www.baidu.com/link?url=wnTflVB4BdECgRUtTotX1_HDub5wxphJkGquuvq_wgTrEfltrTJfmUWGrZXB5ctOXivbK4pvsK-_sOwE-PCOyK'
'http://www.baidu.com/link?url=usBFR86TeJZz0UtrQDoJJtq7f9VN39h9l47MC4AKkyg7GTcVo3asXrJEwIf_pOHl'
'''

# Get second page
for url in mb.search_url(query='python', start=10):
	pprint.pprint(url)

# Output
'''
'http://www.baidu.com/link?url=9kUngEn19EkoocSXk62EildRYzZRrju6FbE3MrZRfiqzQovS8qCgyBiHGZShlFZ1'
'http://www.baidu.com/link?url=pbjTQ_VCm3BbC59-zXKPfUTU4ozBFKi1iCysGv_2Hd_agR2QI4ks7QnLGGF4ASyi'
'http://www.baidu.com/link?url=8q98tGuTFE65j_rze8HwrFTRXIFUiJqing1PSXzPk_qOxL4XnDTEkd0dTMHBgLgzzy_0bPrXCDtIq-oMYPzS2q'
'http://www.baidu.com/link?url=EOmr_kEpISaHax2kyI0F9hPhMaRUKceFtz8Hk-1F3K0vhqrt0qH7N-w5GmFAjO8d'
'http://www.baidu.com/link?url=rkTbJXv4wTBQdqI5f0HMulRgBxEUKlunmx6_UNEb8gGcoriXFmic4J2TSamshlN4-NiLcwoAiqbzMaPpl7R37bya7TT0NHHGLlC_7phEBWMpb5KLTUwu5ZCiBCWU7K9T'
'http://www.baidu.com/link?url=xt4WNqzcSijFT3lUC93yxLDx1NSMiSxXgw96lpLM_iiC3EJ_z0HFiShdAI0AGd5Xqv8dsWimZMBRR4f_Aj1bRa'
'http://www.baidu.com/link?url=dyGGWGi_VZBUvTcDTuB4QPHfaTswUMRAbY8GwYDG0qTXwqd6ECj5AUMiMO3sRbMn'
'http://www.baidu.com/link?url=XJM0tfKyqsAdhw6rdJqFyifz6_k-b8hCvqSSUpaa8oE9WdIM1CkkT649PNYTFcyu'
'http://www.baidu.com/link?url=gznZzx3XQZ013sQ_i8hq52ejnz8QKzPrfaDZpAJhF1tHMoo4Jhbg5Czm2qIr0ZbD'
'http://www.baidu.com/link?url=AP5MHEkcs1mKWnYGsMkJBZtJKXWvnxGbMgYESnIWZLVarW04lMM_eUut8TAHEvuekQN2GrN_XWoPi6ybLUArkq'
'''