import random
import subprocess
import vlc


def main():
    stagione = random.randint(1, 10)
    if (stagione == 1):
        episodio = random.randint(1, 13)
        # vlc_open = subprocess.Popen(["/home/matteo/Scaricati/Stagione 1/The Simpsons s1e0" + episodio + ".avi"])
    elif (stagione == 2 or stagione == 4 or stagione == 5):
        # stagioni 2 - 4 - 5
        episodio = random.randint(1, 22)
    elif (stagione == 3):
        episodio = random.randint(1, 24)
    elif (stagione == 6 or stagione == 7 or stagione == 8 or stagione == 9):
        episodio = random.randint(1, 25)
    elif (stagione == 10):
        episodio = random.randint(1, 23)
    print("Stagione: ", stagione, " episodio: ", episodio)
    # vlc_open = subprocess.Popen(["/home/matteo/Scaricati/"]) # Apri la cartella e il file

    if (episodio >= 1 and episodio <= 9):
        print("/home/matteo/Scaricati/SIMPSON/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e0" + str(episodio) + ".avi")
        #vp = subprocess.call(["/home/matteo/Scaricati/SIMPSON/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e0" + str(episodio) + ".avi"])

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new("/home/matteo/Scaricati/SIMPSON/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e0" + str(episodio) + ".avi")
        #media.get_mrl()
        player.set_media(Media)
        player.play()
        # p = subprocess.Popen(['vlc', '-vvv', "/home/matteo/Scaricati/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e0" + str(episodio) + ".avi"])
        # vlc_open = subprocess.Popen(["/home/matteo/Scaricati/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e0" + str(episodio) + ".avi"])

    else:
        print("/home/matteo/Scaricati/SIMPSON/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e" + str(episodio) + ".avi")
        #vp1 = vp = subprocess.call(["/home/matteo/Scaricati/SIMPSON/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e" + str(episodio) + ".avi"])

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new("/home/matteo/Scaricati/SIMPSON/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e" + str(episodio) + ".avi")
        # media.get_mrl()
        player.set_media(Media)
        player.play()
        # p = subprocess.Popen(['vlc', '-vvv', "/home/matteo/Scaricati/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e" + str(episodio) + ".avi"])
        # vlc_open = subprocess.Popen(["/home/matteo/Scaricati/Stagione " + str(stagione) + "/The Simpsons s" + str(stagione) + "e" + str(episodio) + ".avi"])


if __name__ == '__main__':
    main()
