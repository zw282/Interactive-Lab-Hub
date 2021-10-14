**In collaboration with Ruby Pan dp478**

# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*
![IMG_0341](https://user-images.githubusercontent.com/55099696/135774127-617a7a27-6227-44ba-9f1b-43240987a1ee.jpg)
![IMG_0342](https://user-images.githubusercontent.com/55099696/135774133-4e6dc6e1-ca33-4b68-a965-e82d2a4f190c.jpg)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

We designed a **smart planter that allows plants and flowers to talk**. We listed several possible dialogs before we act out the interaction:

U: user P: Plant
U: How are you feeling today? 
P: I am feeling great! / It’s too hot(cold) for me./ I need some water./I need sunbathing./ I feel bugs.

U: Do you like the temperature here?
P: I’m ok!/ It’s too hot (cold) for me.

U: What’s your ideal room temperature? / What’s your ideal room humidity? 
P: It’s xxx (eg. 22 celsius degree) / It’s 50%.

U: Do you need watering/fertilizing? 
P: Yes/No.

U: Can you tell me when should I water you / add fertilizers next?
P: In 2 days.

U: Do you need sunbathing? 
P: Yes. (For xxx hours please) / No. / I don’t like sunlight. 

U: Do you feel like now you’re having too much/little sunlight?
P: Yes, please move me to somewhere with shades. / Yes, I need sunbathing! 

U: Are you lonely?
P: Yes, I need some friends. / No, I’d love to be your only one. 

U: When will you begin to bloom?
P: In xxx days. / I won’t bloom anymore. / I'm a green plant, I don’t.

U: Do you generate oxygen? 
P: Yes. / No. 

brainstorming process: 
![WechatIMG747](https://user-images.githubusercontent.com/55099696/135773797-cc3867d6-f0fd-4a68-aeff-ce596c353be8.jpeg)
![WechatIMG746](https://user-images.githubusercontent.com/55099696/135773800-8d437fe7-e417-470b-8815-e53ca4259a64.jpeg)

\*\***Please describe and document your process.**\*\*

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).


https://user-images.githubusercontent.com/55099696/135774614-72d168ca-857b-49ee-96f8-4a8845be7c40.mp4


\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*
The interaction was similar to what we had planned. The user asked questions regarding blooming, water, and sunlight. One thing the user asked that was not in our planned dialog - setting alarms. He first asked about what’s a good time to water next and then asked if the plant could set up an alarm for it. It sounds like a good feature to take into consideration in the next part.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

Peer Review:
![WechatIMG360](https://user-images.githubusercontent.com/55099696/137246895-00372552-276b-445c-acb9-42bbefb78ded.jpeg)
![WechatIMG361](https://user-images.githubusercontent.com/55099696/137246899-1edab2e5-8620-4396-ac3d-fecd2dfa3a1b.jpeg)
![WechatIMG362](https://user-images.githubusercontent.com/55099696/137246908-8108fc0c-f05e-4f00-9a05-5aad9f61001c.jpeg)

Based on what we discussed and the peer reviews, we wanted to include specific plant information about the plant in this part. For example, different plants might need different amount of watering and sunlight. Many users do not really understand what the plant needs, so we are including a fun self-introduction for the plant at the beginning of the conversation. Also, we wanted a fun interaction between the user and the plant. 

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

In this part, we will ask the users to move the plant around so that the sensor can check different temperatures at different places. We planned this interaction because in a room, there might be a corner that is getting ample direct sunlight while some other corner might be darker and colder instead. The smart plant will instruct users to "move it around" directly so users won't get confused.

3. Make a new storyboard, diagram and/or script based on these reflections.
![WechatIMG878](https://user-images.githubusercontent.com/55099696/137246460-f6666a36-c811-45dc-a585-6d9a36c2054b.jpeg)


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

The system works as a smart plant communication device. We designed it to be like a wearable "collar" for the plant. We used a sensor for detecting the temperature in the room, more specifically the place the plant is put. First, the system will ask the user to identify itself. We offered a few plants available to choose, they are cactus, airplant, sunflower, and orchid. All the four types of plant will introduce themselves once identified. Then, the system will ask the user to move the plant around. Once users say "done", the sensor will detect the temperature and let the user know whether this is a good place for the plant to grow. Then, it allows users to ask different questions regarding the plant. For example, users can ask "do you need water?" "do you need friend?".etc Users can also ask other questions.

*Include videos or screencaptures of both the system and the controller.*
![WechatIMG879](https://user-images.githubusercontent.com/55099696/137246504-feae746d-0293-4920-9dfe-6489e0b4a384.jpeg)

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Participant 1 - Hongyu Shen hs692

https://user-images.githubusercontent.com/55099696/137247945-0391b7f3-c9e5-4172-8a2b-bbc632b7164d.mp4

Participant 2 - Xy Fang xf48

https://user-images.githubusercontent.com/55099696/137248225-e7021d58-58e5-4dde-befc-2d3eaeca68a8.mp4


Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

In general, we found that the conversation with the plant went well. It felt natural for the plant to lead the conversation and give humorous responses. The users both agreed that the flow of the conversation was natural. 
However, voice recognition of the names of the plant was hard at the beginning when we were testing it out. The volume was a little bit low and we did not understand how to adjust the volume. Lastly, due to the fact that our pi was connected with a short cable, the users were not able to move the device around the room a lot. 

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

In this case, we have already made the system autonomous. Users won't have to use a controller to navigate but only have to ask and talk to the device. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*

We found out that communication between human and human with computer could be highly different. When we were engaging in conversation with our peers, wordings we used were natural and informal. Sometimes we even used long sentences to ask questions. But while we tried to interact with the system, we just naturally used more formal languages and shorter sentences. It might be due to the fact that we don't expect the machine to be very smart, or, we thought that it could only take certain imput. Therefore, we found out that making the machine / device we're talking to more "humanlike" might be better.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

We might get a dataset for the most frequently asked questions as a plant owner. For example, the device takes note and uploads to the cloud service everytime the user talks or asks a question to the device. From there, we can analyze what global plant owners concern the most about. We can also have the device record pairs of temperature and location data in the room. For example, at 6 am in the morning, the southwest corner of the room is the coldest, while at 8 pm, the northwest corner is the warmest. Users can access these data from their mobile devices if possible. 

In terms of sensors, one thing we were not able to achieve was detecting the humidity of the room, which is important for plant growing. We really wish that there could be a sensor that can help us detect humidity. 
