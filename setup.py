import sys
import os
import shutil


def remove_command():
    os.system('cat ~/.bashrc > %stmp' % base_dir)
    with open(base_dir + 'tmp', 'r') as f:
        content = f.readlines()
    with open(base_dir + 'tmp', 'w') as f:
        for line in content:
            if not line.strip():
                continue
            if line.split()[-1].startswith('exam='):
                continue
            f.write(line + '\n')
    os.system('cat %stmp > ~/.bashrc' % base_dir)
    os.remove('%stmp' % base_dir)


def remove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


system = sys.platform
base_dir = sys.path[0]
if system.startswith('win'):
    dir_char = '\\'
else:
    dir_char = '/'
base_dir += dir_char
flag = False

if len(sys.argv) > 1:
    flag = sys.argv[1] == '--clean' or sys.argv[1] == '--direct'

if system.startswith('win'):
    if sys.argv[1] != '--direct':
        os.system('setx /m PATH %%PATH%%;%s;' % base_dir)
    else:
        remove(base_dir + 'exam.sh')
else:
    os.system('chmod 777 %sexam.sh' % base_dir)
    if sys.argv[1] != '--direct':
        remove_command()
        os.system('echo alias exam="%sexam.sh" >> ~/.bashrc' % base_dir)
        os.system('chmod 777 %sexam.sh' % base_dir)
        os.system('source ~/.bashrc')
    else:
        remove(base_dir + 'exam.bat')
if flag:
    remove('%simg' % base_dir)
    remove('%sREADME.md' % base_dir)
    remove('%s.last_title.txt' % base_dir)
    remove('%s.idea' % base_dir)
remove('%scontent.xls' % base_dir)
remove('%scontent.xlsx' % base_dir)
