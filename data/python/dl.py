import os
import subprocess
import time
import shutil

# 删除目录下所有的文件
directory = "./data/rules/"

# 确保目录存在并遍历删除其中的文件
if os.path.exists(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"无法删除文件: {file_path}, 错误: {e}")
else:
    print(f"目录 {directory} 不存在")

# 删除目录本身
try:
    shutil.rmtree(directory)
    print(f"成功删除目录 {directory} 及其中的所有文件")
except Exception as e:
    print(f"无法删除目录 {directory}, 错误: {e}")

# 创建临时文件夹
os.makedirs("./tmp/", exist_ok=True)

# 复制补充规则到tmp文件夹
subprocess.run("cp ./data/mod/adblock.txt ./tmp/adblock01.txt", shell=True)
subprocess.run("cp ./data/mod/whitelist.txt ./tmp/allow01.txt", shell=True)


# 拦截规则
adblock = [
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt", # AdGuard 中文过滤器 2w+规则
    "https://easylist-downloads.adblockplus.org/easylistchina.txt",                                 # EasyList China 2w+规则
    "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",                            # 用于移除网站屏蔽拦截 2000+规则
    "https://raw.githubusercontent.com/chuan0712/Anti-advertising/master/data/mod/OwnerFilter.txt", # 自定义规则
    "https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt",                          # 轻量广告规则，5000+规则
    "https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt",          # app下载屏蔽 1000-规则
    "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt", # 秋风 2000+规则
    "https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt",                # 乘风 1000+规则
]

# 白名单规则
allow = [
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/allowlist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/allowlist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/allowlist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/allowlist.txt"
]

# 下载
for i, adblock_url in enumerate(adblock):
    subprocess.Popen(f"curl -m 60 --retry-delay 2 --retry 5 -k -L -C - -o tmp/adblock{i}.txt --connect-timeout 60 -s {adblock_url} | iconv -t utf-8", shell=True).wait()
    time.sleep(1)

for j, allow_url in enumerate(allow):
    subprocess.Popen(f"curl -m 60 --retry-delay 2 --retry 5 -k -L -C - -o tmp/allow{j}.txt --connect-timeout 60 -s {allow_url} | iconv -t utf-8", shell=True).wait()
    time.sleep(1)
    
print('规则下载完成')


