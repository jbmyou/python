from os import listdir, chdir, rename
from os.path import splitext, join
from sys import exit
from datetime import datetime
import traceback

try :

    path = ""
    src = ""

    old = input("'I:/music/01 Old'경로가 맞으면 Enter, 아니라면 새 경로를 입력하세요 : ").strip()
    if old == "" : 
        path = r'I:\music\01 Old'
    else :
        path = old

    
    files_c = listdir(path)
    music = {}

    for f in files_c :
        stem = splitext(f)[0]
        title = stem.split('_')
        
        if len(title) == 4 :
            music[title[3]] = title[0] + "_" + title[1] +"_"
        else :
            pass
    
    daum = input("'I:/Download/DaumMail'경로가 맞으면 Enter, 아니라면 새 경로를 입력하세요 : ").strip()
    if daum == "" :
        src = r'I:\Download\DaumMail'
    else :
        src = daum.strip()

    dst = path

    chdir(src)
    files = listdir(src)

    count = 0
    fail_list = []
    sucess_list = []
    fail_count = 0
    new_f = ""
    for f in files :
        stem = splitext(f)[0]
        key = stem.split('_')[1]
        singer_song = music.get(key)

        if singer_song is not None :
            new_f = singer_song + f
            rename(f, join(dst,new_f))
            count += 1
            sucess_list.append([str(count), f, new_f])
        else :
            fail_count += 1
            fail_list.append([str(fail_count), f])

    chdir("c:")
    r = open(r"C:\Users\jbmyo\Desktop\move_music_result"+\
            datetime.today().strftime("%Y%m%d")+".txt", 'w')
    r.write("=====파일 이동 성공 목록=====\n")
    digit = len(sucess_list)
    for i, f, nf in sucess_list :
        r.write(i.rjust(digit) +"   "+f+"\t"+nf+"\n")
    r.write("\n")
    r.write("=====파일 이동 실패 목록=====\n")
    for i, f in fail_list :
        r.write(i.rjust(digit)+"   "+f+"\n")
    r.close()
    print()
    print("바탕화면에 로그파일이 생성되었습니다.")
    print(count, "개의 파일 이동 성공")
    print(fail_count, "개의 파일 이동 실패")

except :
    print("오류 발생")
    print(traceback.format_exc())

finally :
    print()
    print("끝내려면 아무키나 누르고 Enter를 누르세요")
    x = input()
    if x != None :
        exit(0)