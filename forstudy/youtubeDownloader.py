import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=ixkoVwKQaJg')
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :
    print(i, ',', videos[i])

down_dir = "soo/PycharmProjects/crawling"

videos[0].download(down_dir)