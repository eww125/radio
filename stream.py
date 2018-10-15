# 1. Install mplayer command line (via Brew, Macports, or APT)
# 2. Add the following aliases to ~/.profile
# 3. Type `source ~/.profile`
# 3. Type `news` or `current` to listen in your terminal

alias jazz = 'mplayer http://ice7.securenetsystems.net/KCSM2'
alias news = "mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/news.pls" # MPR News 
alias current = "mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/the_current.pls" # The Current 
alias classical = "mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/classical.pls" # Classical MPR 
alias localcurrent = "mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/local.pls" # Local Current 
alias heartland = "mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/radio_heartland.pls" # MPR Radio Heartland 
alias wonderground = "mplayer http://wondergroundstream2.publicradio.org/wonderground" # MPR Wonderground Windows Media 
alias choral = "mplayer -playlist http://choralstream1.publicradio.org/choral.m3u" # Clasical MPR Choral
alias wefunk = "mplayer -playlist http://www.wefunkradio.com/play/shoutcast.pls" # WEFUNK Radio MP3 64K
alias sleepbot = "mplayer -playlist http://sleepbot.com/ambience/cgi/listen.cgi/listen.pls" # Sleepbot Environmental Broadcast 56K MP3
alias groovesalad = "mplayer -playlist http://somafm.com/groovesalad130.pls" # Soma FM Groove Salad iTunes AAC 128K
alias dronezone = "mplayer -playlist http://somafm.com/dronezone130.pls" # Soma FM Drone Zone iTunes AAC 128K
alias lush = "mplayer -playlist http://somafm.com/lush130.pls" # Soma FM Lush iTunes AAC 128K
alias sonicuniverse = "mplayer -playlist http://somafm.com/sonicuniverse.pls" # Soma FM Sonic Universe iTunes AAC 128K
