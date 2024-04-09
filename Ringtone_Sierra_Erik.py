# python code
#
# script_name: Final Ringtone
#
# author: Erik Sierra
#
# description: Ringtone
#
#
#

#Setup
from earsketch import *
init()
setTempo(120)

#Music
synthRise = YG_EDM_SYNTH_RISE_1
airRise = RD_EDM_SFX_RISER_AIR_1
lead1 = YG_EDM_LEAD_1
lead2 = YG_EDM_LEAD_2
kick1 = YG_EDM_KICK_LIGHT_1
kick2 = ELECTRO_DRUM_MAIN_LOOPPART_001
snare = ELECTRO_DRUM_MAIN_LOOPPART_003
crash = Y50_CRASH_2
reverseFX = YG_EDM_REVERSE_FX_1

#Section 1
fitMedia(lead1, 1, 1, 17)
fitMedia(kick1, 2, 9, 17)
fitMedia(lead1, 15, 33, 44)




#Transition
fitMedia(reverseFX, 3, 16, 17)
fitMedia(synthRise, 4, 13, 17)
fitMedia(airRise, 5, 13, 17)
fitMedia(crash, 6, 17, 19)

#Section 2
fitMedia(lead2, 1, 17, 33)
fitMedia(kick2, 7, 25, 33)
fitMedia(snare, 8, 29, 33)
fitMedia(OS_CLOSEDHAT02, 3, 17, 33)
fitMedia(DUBSTEP_DRUMLOOP_MAIN_001, 11, 17, 33)

snare = OS_SNARE01
cymbal = OS_CLOSEDHAT01
beat1 = "--0---0---0---0---0---0---0---0---0----0----0--"
beat2 = "--0---0---0---0---0---0---0---0---0----0----0--"
for measure in range(5,31):
   makeBeat(snare, 9, measure, beat1)
   makeBeat(cymbal, 10, measure, beat2)
for measure in range(9,17):
       makeBeat(snare, 9, measure, beat1)
       

def sectionB(startMeasure, endMeasure):
  fitMedia(CIARA_MELANIN_DRUMBEAT_1, 12, startMeasure, endMeasure) # sparse drums
  fitMedia(RD_WORLD_PERCUSSION_SEEDSRATTLE_1, 13, startMeasure, endMeasure) # rattling
  fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_3, 14, startMeasure, startMeasure + 1) # backing
sectionB(5, 9)

#Effects
setEffect(1, VOLUME, GAIN, -50, 1, 10, 7) #Adjusting volumes for better matching
setEffect(4, VOLUME, GAIN, -20)
setEffect(7, VOLUME, GAIN, -20)
setEffect(8, VOLUME, GAIN, -20)
setEffect(9, VOLUME, GAIN, -21)
setEffect(12, VOLUME, GAIN, -50)
setEffect(13, VOLUME, GAIN, -50)
setEffect(14, VOLUME, GAIN, -50)

setEffect(15, VOLUME, GAIN, 0, 35, -50, 44) #Adjusting volumes for better matching
setEffect(11, FILTER,FILTER_FREQ, 20, 17, 2000, 33)
setEffect(11, VOLUME, GAIN, 3)
setEffect(2, FILTER,FILTER_FREQ, 20, 9, 2000, 17)
#setEffect(1, PAN, LEFT_RIGHT, -100,17,20)
#setEffect(1, PAN, LEFT_RIGHT, 100,17,20)







#Finish
finish()
