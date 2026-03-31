
import re
import os

path = '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/演讲的艺术3- 孔铭.md'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
current_speaker4 = None # Will switch between 邱教授, 鹏飞, 郭继涵

# Speaker mapping based on line indices (approximate based on view_file)
# Line 232 (说话人 4 14:05) -> 邱教授
# Line 415 (说话人 4 34:40) -> 鹏飞
# Line 436 (说话人 4 37:54) -> 郭继涵

for i, line in enumerate(lines):
    # Update current_speaker4 context
    if '说话人 4 14:05' in line:
        current_speaker4 = '**邱教授**'
    elif '说话人 4 34:40' in line:
        current_speaker4 = '**鹏飞**'
    elif '说话人 4 37:54' in line:
        current_speaker4 = '**郭继涵**'

    # Global terminology fixes
    line = line.replace('必赢', '必赢')
    line = line.replace('毕赢', '必赢')
    line = line.replace('碧云', '必赢')
    line = line.replace('碧莹', '必赢')
    line = line.replace('自营家辅歌人', '必赢家族的人')
    line = line.replace('全闭眼睛', '必赢')
    line = line.replace('隆中帝', '隆中对')
    line = line.replace('龙中队', '隆中对')
    line = line.replace('迪拜4.0', 'DeFi 4.0')
    line = line.replace('UHD 7', 'USDT')
    line = line.replace('佣', 'U') # Handle 1430 佣 -> 1430 U
    line = line.replace('精子', '精准')
    line = line.replace('平均奖', '平级奖')
    line = line.replace('通收', '通缩')
    line = line.replace('分居地', '根据地')
    line = line.replace('佛浩特', '呼和浩特')
    line = line.replace('步四海容忍', '步入深蓝') # Or similar context "平稳步入"
    line = line.replace('四海如任', '四海纵横')
    line = line.replace('大行杠什么是规则制定', '大概讲什么是规则制定')
    line = line.replace('牛逼格', '牛逼哥')
    line = line.replace('机会激活', '激发激活')
    line = line.replace('底池... 130 滴万枚', '底池... 131 万枚')
    line = line.replace('by ', 'BYB ')
    line = line.replace('BYB B', 'BYB')
    line = line.replace('1, 000(1, 000)+', '1,000')
    line = line.replace('碧莹', '必赢')
    line = line.replace('1, 430 佣', '1,430 U')
    line = line.replace('1, 322 佣', '1,322 U')
    line = line.replace('1430 佣', '1430 U')
    line = line.replace('UHD 7', 'USDT')
    line = line.replace('迪拜4.0', 'DeFi 4.0')
    line = line.replace('顺之者长', '顺之者昌')
    line = line.replace('理财平台... Web center', 'Web3 理财平台')

    # Basic Speaker Labels
    line = line.replace('说话人 1', '**孔铭**')
    line = line.replace('说话人 2', '**分享人 1**')
    line = line.replace('说话人 3', '**主持人**') # Often handling logistics or 道明/其他
    line = line.replace('说话人 5', '**吴子敬**')
    line = line.replace('说话人 6', '**谢大姐**')

    # Conditional Speaker 4 Labels
    if '说话人 4' in line:
        if current_speaker4:
            line = line.replace('说话人 4', current_speaker4)
        else:
            line = line.replace('说话人 4', '**分享人 2**') # Fallback

    new_lines.append(line)

final_content = "".join(new_lines)
final_content = re.sub(r'1, 000(1, 000)+', '1,000', final_content)

# Add H2 Headers
final_content = final_content.replace('**孔铭** 00:01', '## 模块六：规则与秩序——必赢家族的行为准则\n\n**孔铭** 00:01')
final_content = final_content.replace('**吴子敬** 09:11', '## 模块七：学员分享——五组：吴子敬、邱教授与谢大姐\n\n**吴子敬** 09:11')
final_content = final_content.replace('**鹏飞** 34:40', '## 模块八：学员分享——六组：鹏飞与郭继涵\n\n**鹏飞** 34:40')
final_content = final_content.replace('**主持人** 33:31', '## 结束：晚餐与后续安排\n\n**主持人** 33:31')

with open(path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Fixes applied successfully to Part 3.")
