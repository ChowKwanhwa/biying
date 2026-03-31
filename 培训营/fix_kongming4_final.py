
import re
import os

path = '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/演讲的艺术4- 孔铭.md'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []

# Speaker 1 -> 孔铭
# Speaker 3 (00:51 - 27:08) -> OK 老师
# Speaker 3 (33:01 - end) -> 主持人/道明
# Speaker 4 (39:30 - 41:12) -> 小米
# Speaker 7 (36:16 - 39:24) -> 苍老师 (贵阳社区)
# Speaker 8 (45:16, 46:45 - 48:07) -> 1组组长 (广东)
# Speaker 5 (48:10 - 49:45) -> 高子涵 (8组组长)
# Speaker 6 (49:49 - 50:25) -> 高显凡 (4组组长)
# Speaker 9 (50:27 - 50:59) -> 7组组长 (遵义)
# Speaker 10 (51:05 - 52:02) -> 3组组长

for i, line in enumerate(lines):
    # Global terminology fixes
    line = line.replace('必赢', '必赢')
    line = line.replace('必营', '必赢')
    line = line.replace('毕营', '必赢')
    line = line.replace('碧云', '必赢')
    line = line.replace('代行杠', '大概讲')
    line = line.replace('由此必营', '由它必赢')
    line = line.replace('TB 钱包', 'TokenPocket 钱包')
    line = line.replace('理范 4.0', 'DeFi 4.0')
    line = line.replace('滑点', '滑点') # Ensure correct spelling if any
    line = line.replace('划点', '滑点')
    line = line.replace('大声老歌', '大象老师')
    line = line.replace('随败游泳', '虽败犹荣')
    line = line.replace('工信兼材', '雄心壮志')
    line = line.replace('洪总', '孔总')
    line = line.replace('六总', '廖总')
    line = line.replace('廖老大', '廖总')
    line = line.replace('廖大', '廖总')
    line = line.replace('并的商业价值', '必赢的商业价值')
    line = line.replace('佣', 'U')
    line = line.replace('uid', '收益/空投')
    line = line.replace('姚清', '摇旗')
    line = line.replace('对撸了洋码', '对撸了')
    line = line.replace('1, 000 佣', '1,000 U')
    line = line.replace('100 佣', '100 U')
    line = line.replace('100 优', '100 U')
    line = line.replace('200 优', '200 U')
    line = line.replace('300 有', '300 U')
    line = line.replace('300 优', '300 U')
    line = line.replace('1, 430 佣', '1,430 U')
    line = line.replace('1, 322 佣', '1,322 U')
    line = line.replace('430 佣', '430 U')
    line = line.replace('by ', 'BYB ')
    line = line.replace('py ', 'BYB ')

    # Basic Speaker Mapping
    line = line.replace('说话人 1', '**孔铭**')
    line = line.replace('说话人 2', '**参与人员/嘉宾**')
    
    # Speaker 3 mapping
    if '说话人 3 00:51' in line or (i > 2 and i < 240 and '说话人 3' in line):
        line = line.replace('说话人 3', '**OK 老师**')
    elif '说话人 3' in line:
        line = line.replace('说话人 3', '**主持人/道明**')

    # Speaker 4 mapping
    if '说话人 4 39:30' in line:
        line = line.replace('说话人 4', '**小米**')
    elif '说话人 4' in line:
        line = line.replace('说话人 4', '**分享人 1**')

    # Speaker 5 mapping
    if '说话人 5 43:23' in line:
        line = line.replace('说话人 5', '**8组组长**')
    elif '说话人 5 43:33' in line:
        line = line.replace('说话人 5', '**4组组长**')
    elif '说话人 5 43:56' in line:
        line = line.replace('说话人 5', '**7组组长**')
    elif '说话人 5 44:14' in line:
        line = line.replace('说话人 5', '**3组组长**')
    elif '说话人 5 44:43' in line:
        line = line.replace('说话人 5', '**1组组长**')
    elif '说话人 5 48:10' in line:
        line = line.replace('说话人 5', '**高子涵 (8组组长)**')
    elif '说话人 5' in line:
        line = line.replace('说话人 5', '**现场互动员**')

    # Other Speakers
    line = line.replace('说话人 7', '**苍老师 (贵阳社区)**')
    line = line.replace('说话人 8', '**1组组长 (广东)**')
    line = line.replace('说话人 6', '**高显凡 (4组组长)**')
    if '说话人 6 36:06' in line:
        line = line.replace('说话人 6', '**分享人 4**')
        
    line = line.replace('说话人 9', '**7组组长 (遵义)**')
    line = line.replace('说话人 10', '**3组组长**')

    new_lines.append(line)

final_content = "".join(new_lines)

# Add H2 Headers
final_content = final_content.replace('**孔铭** 00:02', '## 模块九：商业闭环——必赢的商业价值（主讲：OK 老师）\n\n**孔铭** 00:02')
final_content = final_content.replace('**孔铭** 24:34', '## 模块十：巅峰时刻——讲师训颁奖盛典\n\n**孔铭** 24:34')
final_content = final_content.replace('**孔铭** 52:13', '## 总结：风雨兼程，共创未来\n\n**孔铭** 52:13')

with open(path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Fixes applied successfully to Part 4.")
