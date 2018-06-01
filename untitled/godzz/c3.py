import re
s = '''<a class="bottom_ad_fla" cid="60800473" shuang11="0" href="http://ac.wan.liebao.cn/s/1/1219/4063.html?frm=dbdh-dbfc

" ad_width="80" ad_cord="500,130" style="width: 80px; height: 80px; margin-left: 0px; bottom: 85px; display: block; left: 45px;"> <img src="/static/images/public/20180509/a7c1ce7b085b77532b5dd31ef1800fc6.gif"></a>'''

r = re.findall('http:.+dbfc$',s)
print(r)