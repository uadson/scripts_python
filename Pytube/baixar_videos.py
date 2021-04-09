import pytube


url = input('Cole o link do video aqui: ')

print('Baixando vídeo...')

yt = pytube.YouTube(url)

video = yt.streams.get_highest_resolution()

video.download()

print('Vídeo baixado com sucesso!')