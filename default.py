import xbmcplugin
import xbmcgui
import sys

# Ruta del archivo m3u
m3u_file = 'https://github.com/lkf00/ruletekodi/blob/main/links.m3u'

def listar_videos():
    with open(m3u_file, 'r') as f:
        for line in f:
            if line.startswith('http'):
                url = line.strip()
                li = xbmcgui.ListItem(label=url)
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)

listar_videos()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
