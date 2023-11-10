from pathlib import Path
import os
import subprocess
import re

file_dir_path = Path(__file__).parent.resolve()

xml_bz2_files = list(filter(lambda x: str(x).find("20231001-pages-articles-multistream.xml.bz2") !=-1,os.listdir(file_dir_path)))

for file in xml_bz2_files:
    tag = re.search("^.+?(?=-)",file).group(0)
    subprocess.run(['python', "WikiExtractor.py", "--infn", 
                str (file)],
                    cwd=Path.joinpath(file_dir_path))

    old_name = Path(Path.joinpath(file_dir_path,"wiki.txt"))
    new_name =  Path.joinpath(file_dir_path,f"{tag}{old_name.suffix}")
    old_name.rename(new_name)
