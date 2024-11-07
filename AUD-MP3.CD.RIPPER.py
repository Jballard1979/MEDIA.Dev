#--
#-- ************************************************************************************************************:
#-- ********************************************** MP3 CD RIPPER ***********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.8.15                                                                                         :
#-- Script:   AUD-MP3.CD.RIPPER.py                                                                              :
#-- Purpose:  A python script that rips mp3's from a CD.                                                        :
#-- Class:    python -m pip install gTTS                                                                        :
#-- Class:    python -m pip install speechrecognition                                                           :
#-- Class:    python -m pip install pyaudio                                                                     :
#-- Class:    python -m pip install LooseVersion                                                                :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES         :
#-- ********************************************************:
import pymedia.removable.cd as cd
import sys
#--
def readTrack( track, offset, bytes ):
  cd.init()
  if cd.getCount()== 0:
    print 'ERROR - FAILED TO DISCOVER CDROM:'
    return 0
  #--
  c= cd.CD(0)
  props= c.getProperties()
  if props[ 'type' ]!= 'AudioCD':
    print 'ERROR - MEDIA IN %s HAS TYPE %s, NOT AN AUDIO CD. FAILED TO READ AUDIO DATA:' % ( c.getName(), props[ 'type' ] )
    return 0
  #--
  tr0= c.open( props[ 'titles' ][ track- 1 ][ 'name' ] )
  tr0.seek( offset, cd.SEEK_SET )
  return tr0.read( bytes )
#--
#-- READ TRACK FROM AUDIO CD & SAVE RAW FORMAT [PCM-44100Hz; 2-CHANNEL; 16 UNSIGNED]:
if __name__== '__main__':
  if len( sys.argv )!= 5:
    print "USAGE - READ_TRACK <file_name> <track> <offset> <bytes>"
  else:
    track= int( sys.argv[ 2 ] )
    s= readTrack( track, int( sys.argv[ 3 ] ), int( sys.argv[ 4 ] ) )
    f= open( sys.argv[ 1 ], 'wb' )
    f.write( s )
    f.close()
    print 'READ OF %d BYTES FROM TRACK %d COMPLETED SUCCESSFULLY:' % ( len( s ), track )
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: