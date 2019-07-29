import compmusic
from compmusic import dunya
from tqdm import tqdm_notebook
dunya.set_token("deb6f838c438293fdf765833e0619bdf8c76d577")


compmusic.dunya.carnatic.get_raagas()
raagas = compmusic.dunya.carnatic.get_raagas()

raga_dict = {}
for i in raagas:
    raga_dict[i['name']] = i['uuid']

songs_todi = compmusic.dunya.carnatic.get_raaga(raga_dict["Tōḍi"])
songs_kamas = compmusic.dunya.carnatic.get_raaga(raga_dict["Kamās"])
songs_saurastram = compmusic.dunya.carnatic.get_raaga(raga_dict["Saurāṣtraṁ"])


for i in tqdm_notebook(songs_todi["recordings"]):
    compmusic.dunya.carnatic.download_mp3(i["mbid"], "data/todi/")


for i in tqdm_notebook(songs_kamas["recordings"]):
    compmusic.dunya.carnatic.download_mp3(i["mbid"], "data/kamas/")

for i in tqdm_notebook(songs_saurastram["recordings"]):
    compmusic.dunya.carnatic.download_mp3(i["mbid"], "data/saurastram/")
