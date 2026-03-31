
import os

folder = '/Users/ericc/Desktop/土豆/必赢/培训营/kongming/'
files = [
    '演讲的艺术1- 孔铭.md',
    '演讲的艺术2- 孔铭.md',
    '演讲的艺术3- 孔铭.md',
    '演讲的艺术4- 孔铭.md'
]
output_file = '演讲的艺术专题培训全集 - 孔铭.md'

full_path_out = os.path.join(folder, output_file)

merged_content = "# 《演讲的艺术》专题培训实录全集\n\n**主讲人**：孔铭、OK 老师等\n**培训主题**：必赢商业逻辑与演讲沟通艺术\n\n---\n\n"

for i, f_name in enumerate(files):
    f_path = os.path.join(folder, f_name)
    if os.path.exists(f_path):
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Clean up specific headers if they are duplicated or irrelevant in a combined doc
            # But here I'll just keep the module headers as they are already hierarchical (H2)
            merged_content += f"### 第三期：演讲的艺术（第 {i+1} 部分）\n\n"
            merged_content += content
            merged_content += "\n\n---\n\n"

with open(full_path_out, 'w', encoding='utf-8') as f:
    f.write(merged_content)

print(f"Successfully merged into {output_file}")
