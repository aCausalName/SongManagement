import os
import pickle
import m_AddSong
import m_ShowSongList
global dailySongList, AASongList, FASongList


def ShowMenu():
    if user == 0:
        print("身份：游客")
        print("*****************************")
        print("*****  0.退出            ****")
        print("*****  1.添加歌曲        ****")
        print("*****  2.查看歌单        ****")
        print("*****  3.登录管理员      ****")
        print("*****************************")
    else:
        print("身份：管理员")
        print("*****************************")
        print("*****  0.退出            ****")
        print("*****  1.添加歌曲        ****")
        print("*****  2.查看歌单        ****")
        print("*****  3.删除歌曲        ****")
        print("*****  4.添加社团活动    ****")
        print("*****  5.添加自由活动    ****")
        print("*****  6.清空歌单        ****")
        print("*****  7.退出管理员身份  ****")
        print("*****************************")


def ReadSongList():
    # AA = Association Activity  FA = Free Activity
    global dailySongList, AASongList, FASongList

    daily_file = open('dailySong.dat', 'rb')
    AA_file = open('AASong.dat', 'rb')
    FA_file = open('FASong.dat', 'rb')

    dailySongList = pickle.load(daily_file)
    AASongList = pickle.load(AA_file)
    FASongList = pickle.load(FA_file)

    daily_file.close()
    AA_file.close()
    FA_file.close()


def WriteSongList(attached):
    global dailySongList, AASongList, FASongList

    if attached == 'daily':
        daily_file = open('dailySong.dat', 'wb')
        pickle.dump(dailySongList, daily_file)
        daily_file.close()

    elif attached == 'AA':
        AA_file = open('AASong.dat', 'wb')
        pickle.dump(AASongList, AA_file)
        AA_file.close()

    else:
        FA_file = open('FASong.dat', 'wb')
        pickle.dump(FASongList, FA_file)
        FA_file.close()


def AddSong():
    # status: 0-未播放，1-已播放
    global dailySongList, AASongList, FASongList

    newSong = {'id': 0,
               'name': 0,
               'singer': 0,
               'orderer': 0,
               'attached': 0,
               'source': 0,
               'status': 0}
    NewSongInfo = m_AddSong.main()
    if NewSongInfo[0] == '':
        print("您甚至没有输入歌名……")
        os.system('pause')
        return
    newSong['name'] = NewSongInfo[0]
    newSong['singer'] = NewSongInfo[1]
    newSong['orderer'] = NewSongInfo[2]
    newSong['attached'] = NewSongInfo[3]
    newSong['source'] = NewSongInfo[4]

    if newSong['attached'] == '日常放歌':
        dailySongList.append(newSong)
        WriteSongList('daily')
    elif newSong['attached'] == '社团活动':
        AASongList[-1].append(newSong)
        WriteSongList('AA')
    else:
        FASongList[-1].append(newSong)
        WriteSongList('FA')


def DelSong():
    pass


def DelAll():
    global dailySongList, AASongList, FASongList

    dailySongList = []
    AASongList = []
    FASongList = []

    daily_file = open('dailySong.dat', 'wb')
    AA_file = open('AASong.dat', 'wb')
    FA_file = open('FASong.dat', 'wb')

    pickle.dump(dailySongList, daily_file)
    pickle.dump(AASongList, AA_file)
    pickle.dump(FASongList, FA_file)

    daily_file.close()
    AA_file.close()
    FA_file.close()

    print("清除成功！")
    os.system('pause')


def ChoiceGet():
    while 1:
        choice = int(input())
        if choice in [0, 1, 2, 3]:
            return choice
        elif choice in [4, 5, 6, 7] and user == 1:
            return choice
        else:
            print("请按要求输入！")


def ManagerLogin():
    global user
    user = 1


def AddAA():
    pass


def AddFA():
    pass


def main():
    global user
    user = 0

    # 主循环
    while 1:
        os.system('cls')
        ReadSongList()
        ShowMenu()
        choice = ChoiceGet()
        if choice == 1:
            AddSong()
        elif choice == 2:
            m_ShowSongList.main()
        elif choice == 3:
            if user == 0:
                ManagerLogin()
            else:
                DelSong()

        elif choice == 4:
            AddAA()
        elif choice == 5:
            AddFA()
        elif choice == 6:
            DelAll()
        elif choice == 7:
            user = 0
        elif choice == 0:
            break


if __name__ == '__main__':
    global res
    global user
    main()
