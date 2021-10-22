import pyglet
import sys, os
os.chdir(sys._MEIPASS)
filename = 'rick.mp4' 
window=pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(filename)

player.queue(MediaLoad)
player.play()

@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)


pyglet.app.run()