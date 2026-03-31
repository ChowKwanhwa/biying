
import os

files = [
    '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/演讲的艺术 - 孔铭.md',
    '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/演讲的艺术2- 孔铭.md',
    '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/演讲的艺术3- 孔铭.md',
    '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/演讲的艺术4- 孔铭.md'
]

for p in files:
    if not os.path.exists(p): continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Consistency Fixes
    content = content.replace('郭继涵', '郭洁涵')
    content = content.replace('腾飞', '鹏飞')
    content = content.replace('毕莹', '必赢')
    content = content.replace('必营', '必赢')
    content = content.replace('必赢', '必赢') # Just to be sure
    content = content.replace(' uid', ' 收益')
    content = content.replace('UID', '收益')
    content = content.replace('TP 钱包', 'TokenPocket 钱包')
    content = content.replace('BIB', 'BYB') # Standardizing token name to BYB based on context in part 3/4
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final consistency pass completed.")
