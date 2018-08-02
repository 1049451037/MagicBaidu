# MagicBaidu

Baidu search API. This is a brother repository of [MagicGoogle](https://github.com/howie6879/MagicGoogle).

# Requirement

* Python 3

# Installation

```shell
pip install MagicBaidu
```

# Tutorial

## Get dict data

```python
from MagicBaidu import MagicBaidu
import pprint

mb = MagicBaidu()

# Get {'title','url','text'}
for i in mb.search(query='python'):
	try:
		pprint.pprint(i)
	except:
		pass
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
```

## Get URL

```python
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
```

## Get Real URL

Do not do this too frequently.

```python
>>> from MagicBaidu import MagicBaidu
>>> mg = MagicBaidu()
>>> import time
>>> for url in mg.search_url(query='python'):
...     print(mg.get_real_url(url))
...     time.sleep(1)
...
'''
Output:
https://www.python.org/
https://www.python.org/getit
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
http://www.runoob.com/python/python-tutorial.html
http://baike.baidu.com/link?url=udBsVTeYGOMZAYpKmncYucFy55A0AaX5CryqRhSUwqsdzENOI72JaO9MbrmdrwY38c9zJARbYSadyBKImtgh6q
http://www.runoob.com/python/python-intro.html
http://python.jobbole.com/
https://www.python.org/downloads/windows/
http://www.runoob.com/python3/python3-tutorial.html
http://www.okpython.com/
'''
```
