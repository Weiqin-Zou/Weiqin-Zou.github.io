import pypinyin

import argparse, mimetypes, sys, os, fileinput


parser = argparse.ArgumentParser(description='Import a new member to the page.\n e.g. python updater.py 2025 张三 /your/photo/path/pic.jpg -n myphotoname -w your.website.com\n The information of the member called San Zhang whose personal website is your.website.com will be added to the pages, and his photo will be renamed to myphotoname.jpg and copied to images/members.', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', type=str, help="year of the class")
parser.add_argument('name', type=str, help="Chinese name of the member")
parser.add_argument('photo_path', type=str, help="file path of the member's photo")
parser.add_argument('-n', '--filename', type=str, help="copied photo's filename, extension name(e.g. .jpg/.png) not included")
parser.add_argument('-w', '--website', type=str, help="personal homepage address")
args = parser.parse_args()
script_path = sys.path[0]


def get_eng_name(name: str) -> str:
    """
    生成英文姓名
    """
    fuxing_list = ['欧阳', '太史', '端木', '上官', '司马', '东方', '独孤', '南宫', '万俟', '闻人', '夏侯', '诸葛', '尉迟', '公羊', '赫连', '澹台', '皇甫', '宗政', '濮阳', '公冶', '太叔', '申屠', '公孙', '慕容', '仲孙', '钟离', '长孙', '宇文', '司徒', '鲜于', '司空', '闾丘', '子车', '亓官', '司寇', '巫马', '公西', '颛孙', '壤驷', '公良', '漆雕', '乐正', '宰父', '谷梁', '拓跋', '夹谷', '轩辕', '令狐', '段干', '百里', '呼延', '东郭', '南门', '羊舌', '微生', '公户', '公玉', '公仪', '梁丘', '公仲', '公上', '公门', '公山', '公坚', '左丘', '公伯', '西门', '公祖', '第五', '公乘', '贯丘', '公皙', '南荣', '东里', '东宫', '仲长', '子书', '子桑', '即墨', '达奚', '褚师', '吴铭']

    trans = pypinyin.pinyin(name, style=pypinyin.NORMAL)
    trans = [i[0] for i in trans]
    name_start_index = 1
    if name[0:2] in fuxing_list:  # 判断是否为复姓
        name_start_index = 2  # 名起始的index后移一位
    eng_name = f'{"".join(trans[name_start_index:]).capitalize()} {"".join(trans[0:name_start_index]).capitalize()}'  # '名 姓'

    return eng_name


def if_photo_supported(photo_path: str) -> bool:
    """
    判断输入的文件是否为浏览器支持的图片格式
    """
    supported_format = ['image/jpeg', 'image/png', 'image/apng', 'image/gif', 'image/bmp', 'image/webp']
    return mimetypes.guess_type(photo_path)[0] in supported_format


def if_script_moved() -> bool:
    """
    判断该脚本有没有被移动位置(操作文件依赖于原项目的相对路径)
    """
    return not(os.path.exists(script_path + "/../_pages/about.md") and os.path.exists(script_path + "/../_pages_cn/about_cn.md"))


def insert_member(year: str, name: str, website: str):
    """
    插入新成员信息(写入两个页面的对应内容中，复制照片)
    """
    # 复制照片文件
    file_ext = os.path.splitext(args.photo_path)[1]
    if args.filename is not None:
        file_base_name = args.filename
    else:
        file_base_name = os.path.splitext(args.photo_path.split('\\')[-1].split('/')[-1])[0]
    file_full_name = file_base_name + file_ext
    with open(args.photo_path, "rb") as src, open(script_path + "/../images/members/" + file_full_name, "wb") as dst:
        data = src.read()
        dst.write(data)

    # 构造新插入的行
    eng_name = get_eng_name(name)
    line1 = '    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">'
    line2 = f'      <div class="image_box" style="background-image: url(/images/members/{args.target_photo_filename});"></div>'
    line3 = '      <div style="text-align: left;">'
    line4 = f'{eng_name}/{name}'
    line4_cn = f'{name}/{eng_name}'
    if website is not None:
        line4 = f'        <a href="{website}" target="_blank">' + line4 + '</a>'
        line4_cn = f'        <a href="{website}" target="_blank">' + line4_cn + '</a>'
    else:
        line4 = '        ' + line4
        line4_cn = '        ' + line4_cn
    line5 = '      </div>'
    line6 = '    </div>'
    lines = [line1 + '\n', line2 + '\n', line3 + '\n', line4 + '\n', line5 + '\n', line6 + '\n']
    lines_cn = [line1 + '\n', line2 + '\n', line3 + '\n', line4_cn + '\n', line5 + '\n', line6 + '\n']

    # 从两个about.md文件读取全文，找到需要插入的位置
    insert_line_num = 0
    insert_line_num_cn = 0
    year_not_exist = True
    output = []
    output_cn = []
    with fileinput.input(script_path + "/../_pages/about.md", encoding="utf-8") as f:
        for line in f:
            if line.replace('\n', '') == f'## Class of {year}':
                year_not_exist = False
                insert_line_num = fileinput.lineno()
            if line.replace('\n', '') == "<span class='anchor' id='more-about-me'></span>" and year_not_exist:
                insert_line_num = fileinput.lineno()
            output.append(line)

    with fileinput.input(script_path + "/../_pages_cn/about_cn.md", encoding="utf-8") as f:
        for line in f:
            if line.replace('\n', '') == f'## {year}级' or (line.replace('\n', '') == "<span class='anchor' id='more-about-me'></span>" and year_not_exist):
                insert_line_num_cn = fileinput.lineno()
            output_cn.append(line)

    # 想要插入的年份不存在的情况
    if year_not_exist:
        # 构造新的年份信息的行
        line1_new = f'## Class of {year}'
        line1_new_cn = f'## {year}级'
        line2_new = '<div class="bootstrap">'
        line3_new = '  <div class="row">'
        line4_new = '  </div>'
        line5_new = '</div>'
        lines_new = [line1_new + '\n', line2_new + '\n', line3_new + '\n', line4_new + '\n', line5_new + '\n', '\n']
        lines_new_cn = [line1_new_cn + '\n', line2_new + '\n', line3_new + '\n', line4_new + '\n', line5_new + '\n', '\n']

        # 插入新的年份信息
        insert_line_num -= 3
        for line in lines_new:
            output.insert(insert_line_num, line)
            insert_line_num += 1
        insert_line_num -= 5

        insert_line_num_cn -= 3
        for line in lines_new_cn:
            output_cn.insert(insert_line_num_cn, line)
            insert_line_num_cn += 1
        insert_line_num_cn -= 5

    # 插入member信息
    insert_line_num += 2
    for line in lines:
        output.insert(insert_line_num, line)
        insert_line_num += 1

    insert_line_num_cn += 2
    for line in lines_cn:
        output_cn.insert(insert_line_num_cn, line)
        insert_line_num_cn += 1

    # 写回插入后的页面文件
    with open(script_path + "/../_pages/about.md", "w+", encoding="utf-8") as file:
        file.write(''.join([str(s) for s in output]))
    with open(script_path + "/../_pages_cn/about_cn.md", "w+", encoding="utf-8") as file:
        file.write(''.join([str(s) for s in output_cn]))


if __name__ == '__main__':
    if if_photo_supported(args.photo_path) is False:
        print("error: File not found! / File format not supported!")
        sys.exit(1)

    if if_script_moved():
        print("error: Script should not be moved! Please move it back!")
        sys.exit(1)

    insert_member(args.year, args.name, args.website)
