
import re
import os

path = '/Users/ericc/Desktop/土豆/必赢/培训营/niubige2/私域流量成交技巧 - 牛逼哥.md'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Global Typo/Terminology Fixes
replacements = {
    '链接传球': '链接全球',
    '投标': '图标',
    '草传': '草船',
    '曹传': '草船',
    '草船借鉴': '草船借箭',
    '曹军': '草船',
    '必赢': '必赢',
    '碧莹': '必赢',
    '晚推': '网推',
    '纽约哥': '牛逼哥',
    '刘斌哥': '牛逼哥',
    '纽约': '牛逼哥',
    '牛刀哥': '牛逼哥',
    '欧克老师': 'OK老师',
    'b 圈': 'B圈',
    '币圈': 'B圈',
    '毕生社区': '必胜社区',
    '麦当': '卖灯',
    '回联': '互联',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# 2. Speaker Label Mapping
content = re.sub(r'说话人 1 (\d{2}:\d{2})', r'**牛逼哥** \1', content)
content = re.sub(r'说话人 2 (\d{2}:\d{2})', r'**牛逼哥** \1', content)

# 昌老师
content = content.replace('说话人 3 06:00', '**分享人 1** 06:00')
content = content.replace('说话人 3 09:57', '**分享人 1** 09:57')
content = content.replace('说话人 3 10:59', '**分享人 1** 10:59')
content = content.replace('说话人 3 12:11', '**分享人 1** 12:11')

# Student question
content = content.replace('说话人 4 09:28', '**分享人 2** 09:28')

# 张夕颜
content = content.replace('说话人 5 12:58', '**分享人 3** 12:58')
content = content.replace('说话人 5 13:05', '**分享人 3** 13:05')
content = content.replace('说话人 5 14:38', '**分享人 3** 14:38')
content = content.replace('说话人 5 14:43', '**分享人 3** 14:43')
content = content.replace('说话人 5 15:02', '**分享人 3** 15:02')
content = content.replace('说话人 5 27:31', '**分享人 3** 27:31')

# 说话人 6
content = content.replace('说话人 6 16:22', '**分享人 4** 16:22')
content = content.replace('说话人 6 16:52', '**分享人 4** 16:52')

# 说话人 7
content = content.replace('说话人 7 17:02', '**分享人 5** 17:02')
content = content.replace('说话人 7 17:24', '**分享人 5** 17:24')

# 老田
content = content.replace('说话人 4 18:01', '**分享人 6** 18:01')
content = content.replace('说话人 4 18:15', '**分享人 6** 18:15')
content = content.replace('说话人 4 18:19', '**分享人 6** 18:19')
content = content.replace('说话人 4 18:59', '**分享人 6** 18:59')
content = content.replace('说话人 4 19:32', '**分享人 6** 19:32')
content = content.replace('说话人 4 19:59', '**分享人 6** 19:59')
content = content.replace('说话人 4 21:04', '**分享人 6** 21:04')
content = content.replace('说话人 4 21:49', '**分享人 6** 21:49')
content = content.replace('说话人 4 21:59', '**分享人 6** 21:59')
content = content.replace('说话人 4 22:04', '**分享人 6** 22:04')
content = content.replace('说话人 4 24:02', '**分享人 6** 24:02')
content = content.replace('说话人 4 33:57', '**分享人 6** 33:57')

# 赵思姐
content = content.replace('说话人 8 23:13', '**分享人 7** 23:13')
content = content.replace('说话人 8 23:29', '**分享人 7** 23:29')
content = content.replace('说话人 8 23:44', '**分享人 7** 23:44')
content = content.replace('说话人 8 23:52', '**分享人 7** 23:52')
content = content.replace('说话人 8 23:57', '**分享人 7** 23:57')
content = content.replace('说话人 8 29:10', '**分享人 7** 29:10')

# 温雨慧
content = content.replace('说话人 9 24:23', '**分享人 8** 24:23')
content = content.replace('说话人 9 25:05', '**分享人 8** 25:05')
content = content.replace('说话人 9 25:46', '**分享人 8** 25:46')

# 郑主席
content = content.replace('说话人 10 26:42', '**分享人 9** 26:42')

# 菲儿
content = content.replace('说话人 9 27:32', '**分享人 10** 27:32')
content = content.replace('说话人 9 27:45', '**分享人 10** 27:45')
content = content.replace('说话人 9 28:00', '**分享人 10** 28:00')
content = content.replace('说话人 9 28:37', '**分享人 10** 28:37')
content = content.replace('说话人 9 29:12', '**分享人 10** 29:12')
content = content.replace('说话人 9 29:32', '**分享人 10** 29:32')
content = content.replace('说话人 9 29:40', '**分享人 10** 29:40')
content = content.replace('说话人 9 32:32', '**分享人 10** 32:32')

# 说话人 11
content = content.replace('说话人 11 29:50', '**分享人 11** 29:50')
content = content.replace('说话人 11 29:57', '**分享人 11** 29:57')
content = content.replace('说话人 11 30:02', '**分享人 11** 30:02')
content = content.replace('说话人 11 30:15', '**分享人 11** 30:15')
content = content.replace('说话人 11 30:41', '**分享人 11** 30:41')
content = content.replace('说话人 11 31:30', '**分享人 11** 31:30')
content = content.replace('说话人 11 31:38', '**分享人 11** 31:38')
content = content.replace('说话人 11 32:21', '**分享人 11** 32:21')
content = content.replace('说话人 11 32:41', '**分享人 11** 32:41')
content = content.replace('说话人 11 33:17', '**分享人 11** 33:17')

# Title
if not content.strip().startswith('#'):
    content = '# 私域流量成交技巧专题培训实录\n\n' + content.strip()

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
