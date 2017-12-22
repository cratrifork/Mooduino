from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Status
import json
import sys

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime, timedelta

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="bXqnhyqZPjjvgdmEKtoYXAs0b"
consumer_secret="PsjsbVGt903UYorjAGRFNqLTLUaz2kJBOMRrhZowN4MNDFKKIr"
consumer_key2="sYwNAszx8QbEour3Tx1OhqjKE"
consumer_secret2="36tsQpgq8JOgr647khs48Tw4vWrLkNbwFVKgTMhgplPcM2hL1O"
consumer_key3="69sExOlglGucwbBCwCSwiD8Ee"
consumer_secret3="V46MqSkXBdvgPfJSfREur0lRmtNAZrKyhf329kO7QHgl0en9MB"
consumer_key4="TWEojnzHGBUnpezXSpF1KL14P"
consumer_secret4="WfbvZzf9Dqm6o2hDpgZODrH9RHMOZQnICCRYk8LCb5WxGTu8DI"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="259647427-tlrBGtthKb1nRYuBOwdMfQl8qxdRjJjV08unr7Dj"
access_token_secret="gPscWlCFl0xmq47hjTFgZl388312PLbwD7HHRAUwvNkqj"
access_token2="259647427-surJ4IfJ9MvdeyC3cwTgmwHyCkkmAiBWW1nuluwE"
access_token_secret2="1V5SH7xn6xFiPGyp6GUXhfVOEqpgNtGdoj67nEuVkfGEJ"
access_token3="259647427-2dioe8EJtL3jcdHDGd9NPF55gTBrdJZJ96U75YJm"
access_token_secret3="0n0kdujMv3bhf2frI3EDATbCIAPL0lkj87kzKYry59SiZ"
access_token4="259647427-R4jgtDPMUjEBSVooq7aNx4NH1TsAKXI6hMnZaDZ7"
access_token_secret4="ES5A9kpIK1Ll114wPz4nk9XmyAieMNLDfSxFRXCbTRexX"

# Dictionary stuff!
origDict = {'love': 0, 'joy': 0, 'surprise': 0, 'anger': 0, 'envy': 0, 'sadness': 0, 'fear': 0 }
#Initial dicts filled with zeros
currentCompareDict = origDict
previousCompareDict = origDict
#Start off with clear dict:
currentMoodDict = origDict
resultDict = origDict

datetimenow = datetime.now()

#Matplotlib
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

class StdOutListener(StreamListener):
    def __init__(self, dict_key):
        self.dict_key = dict_key

    def on_data(self, raw_data):
        data = json.loads(raw_data)

        currentMoodDict[self.dict_key] = currentMoodDict[self.dict_key]+1

        #for i in currentMoodDict:
        #    print(i, currentMoodDict[i], end=', ')
        #print('') #Newline
        sys.stdout.flush() #Flush so we don't get more than one line
        return True

    def on_error(self, status_code):
        print('=====> ERROR <===== ' + status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

def animate(i):
    #plt.clf() #Clear the figure
    print("Datetime now: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    saveDataAndCompare()

    xar = [0, 0, 0, 0, 0, 0, 0]
    yar = [0, 0, 0, 0, 0, 0, 0]
    x = [0, 1, 2, 3, 4, 5, 6]
    #Love, joy, surprise, envy, sadness, anger, fear
    #    my_xticks = ['love', 'joy', 'surprise', 'envy', 'sadness', 'anger', 'fear']
    my_xticks = ['envy', 'love', 'joy', 'sadness', 'anger', 'surprise', 'fear']
    my_colors = ['green', 'pink', 'yellow', 'blue', 'red', 'purple', 'grey']

    for index, mood in enumerate(resultDict):
        yar[index] = resultDict[mood]
        
    ax1.clear()
    ax1.set_xticks(x, minor=False)
    ax1.set_xticklabels(my_xticks, fontdict=None, minor=False)
    ax1.set_title('World mood from ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #ax1.set_ylabel('Number of tweets')
    ax1.bar(x, height=yar, color=my_colors)
    #ax1.plot(x, yar)

    
     

#This is where the fun happens
def saveDataAndCompare():
    global currentMoodDict, previousCompareDict, currentCompareDict, resultDict
    
   
   
    #Save secondDict to firstDict
    previousCompareDict = currentCompareDict

    #Save new data to the second dict
    currentCompareDict = currentMoodDict

    #compare the current mood with previous compare
    for key in currentMoodDict:
        if key in previousCompareDict:
            print("Current Mood: " + str(key) + ": " + str(currentMoodDict[key]) + " Previous: " + ": " + str(previousCompareDict[key]))
            resultDict[key] = int((currentCompareDict[key] - previousCompareDict[key]))

    print("Result dict: " + str(resultDict))
    #Reset the values in the original dict
    currentMoodDict = {'love': 0, 'joy': 0, 'surprise': 0, 'anger': 0, 'envy': 0, 'sadness': 0, 'fear': 0 }

    

def setupStreams():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth2 = OAuthHandler(consumer_key2, consumer_secret2)
    auth2.set_access_token(access_token2, access_token_secret2)
    auth3 = OAuthHandler(consumer_key3, consumer_secret3)
    auth3.set_access_token(access_token3, access_token_secret3)
    auth4 = OAuthHandler(consumer_key4, consumer_secret4)
    auth4.set_access_token(access_token4, access_token_secret4)
    
    loveListener = StdOutListener('love')
    joyListener = StdOutListener('joy')
    surpriseListener = StdOutListener('surprise')
    angerListener = StdOutListener('anger')
    envyListener = StdOutListener('envy')
    sadnessListener = StdOutListener('sadness')
    fearListener = StdOutListener('fear')
    #trumpListener = StdOutListener('trump')

    loveStream = Stream(auth, loveListener)
    joyStream = Stream(auth, joyListener)
    surpriseStream = Stream(auth2, surpriseListener)
    angerStream = Stream(auth2, angerListener)
    envyStream = Stream(auth3, envyListener)
    sadnessStream = Stream(auth3, sadnessListener)
    fearStream = Stream(auth4, fearListener)
    #trumpStream = Stream(auth4, trumpListener)

    envyStream.filter(track=['i wish i', 'i\'m envious', 'i\'m jalous', 'i want to be', 'why can\'t i'], async=True)
    loveStream.filter(track=['i love you', 'i love her', 'I love him', 'all my love', 'i\'m in love', 'i really love'], async=True) 
    joyStream.filter(track=['happiest', 'so happy', 'so excited', 'I\'m happy', 'woot', 'w00t'], async=True)
    sadnessStream.filter(track=['i\'m so sad', 'I\'m heartbroken', 'I\'m so upset', 'I\'m depressed', 'I can\'t stop crying', 'so sad'], async=True)
    angerStream.filter(track=['i hate', 'really angry', 'i am mad', 'really hate', 'so angry'], async=True)
    surpriseStream.filter(track=['wow', 'O_o', 'can\'t believe', 'wtf', 'unbelievable'], async=True)
    fearStream.filter(track=['I\'m so scared', 'I\'m really scared', 'I\'m terrified', 'I\'m really afraid', 'So scared'], async=True)
    #trumpStream.filter(track=['trump'], async=True)


#Main method!
if __name__ == '__main__':

    setupStreams()

    #Set up bar chart
    ani = animation.FuncAnimation(fig, animate, interval=1000*60)
    plt.show()


