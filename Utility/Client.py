import socket

class KlientRPI:
    def playVideo(self):
        print('run_video')

    def stopVideo(self):
        print('stop_video')

    def sendTheMessage(self):
        print()

    def acceptMessege(self):
        print()

    def stopVideoM1(self):
        # pygame.mixer.music.pause();
        # global set
        # set = 0  # set =0 ,means song is  not playing currently
        print('stop_video')

    def playVideoM1(self):
        # comm =  "/home/aayushshivam7/python\ projects/pygam_vlc.py "
        # call(["python","pygam_vlc.py","abc.mp4"])
        # global player
        # player = vlc.MediaPlayer(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4")
        # player.play()
        # subprocess.call(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4", shell=True)
        print('runVideoM1')

    def stopVideoM2(self):
        # pygame.mixer.music.pause();
        # global set
        # set = 0  # set =0 ,means song is  not playing currently
        print('stopVideoM2')

    def playVideoM2(self):
        # comm =  "/home/aayushshivam7/python\ projects/pygam_vlc.py "
        # call(["python","pygam_vlc.py","abc.mp4"])
        # global player
        # player = vlc.MediaPlayer(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4")
        # player.play()
        # subprocess.call(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4", shell=True)
        print('playVideoM2')

    def stopVideoM3(self):
        # pygame.mixer.music.pause();
        # global set
        # set = 0  # set =0 ,means song is  not playing currently
        print('stopVideoM3')

    def playVideoM3(self):
        # comm =  "/home/aayushshivam7/python\ projects/pygam_vlc.py "
        # call(["python","pygam_vlc.py","abc.mp4"])
        # global player
        # player = vlc.MediaPlayer(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4")
        # player.play()
        # subprocess.call(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4", shell=True)
        print('playVideoM3')

    def playProjector(self):
        print('run_projector')

    def stopProjector(self):
        print('stop_projector')

    # def StVid(self,event):
    #
    #     global file
    #     player.stop()
    #     file = ""
    # print()

    def SdisconnRpi(self):
        print()

    def conn(self):
        print()

    def Sturnofrscreen(self):
        print()

    def Disconnect(self):
        print('disconnect')

    def off_raspberry(self):
        print("off_raspberry")

    def Test(self):
        print("Test")

t = KlientRPI()

def takeMessage(message):
    if message == b"run_video":
        t.playVideo()
    elif message == b"stop_video":
        t.stopVideo()
    elif message == b"off_raspberry":
        t.off_raspberry()
    elif message == b"run_projector":
        t.playProjector()
    elif message == b"stop_projector":
        t.stopProjector()
    elif message == b"run_monitor1":
        t.playVideoM1()
    elif message == b"run_monitor2":
        t.playVideoM2()
    elif message == b"run_monitor3":
        t.playVideoM3()
    elif message == b"stop_monitor1":
        t.stopVideoM1()
    elif message == b"stop_monitor2":
        t.stopVideoM2()
    elif message == b"stop_monitor3":
        t.stopVideoM3()
    elif message == b"disconnect":
        t.Disconnect()
    elif message == b"Test":
        t.Test()
    else:
        print("Error: " + message)

if __name__ == '__main__':

    r = True
    sock = socket.socket()
    while r:
        try:
            try:
                print("Повтор подключения")
                sock.connect(('192.168.1.101', 9090))  # 192.168.1.184
                print('try connect')
            except TimeoutError as e:
                sock = socket.socket()
                print("error " + str(e))
            else:
                while True:
                    data = sock.recv(1024)
                    # data.clean()
                    takeMessage(data)
        except BaseException as be:
            sock = socket.socket()
            print("error BE: " + str(be))
        else:
            pass
