**Collaboration with Ruby Pan DP478**

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

\*\***Describe your setting, players, activity and goals here.**\*\*

_**Setting**:_ The interaction takes place in the kitchen, specifically the refrigerator. The interaction happens when the person opens the refrigerator.

_**Player**:_ There is no specific player that the device is designed to interact with. Whoever walks by the fridge or opens the door of the fridge becomes the player of the interaction.

_**Activity**:_ The color of the light outside the fridge indicates how full the refrigerator is. The green light shows that the refrigerator capacity has been filled to a certain amount (30% and above) that the person or the household members do not need to purchase extra groceries. If the light turns red, it indicates that the amount of groceries inside the fridge is now equal or below 30%, which signifies that the player should buy groceries to refill the fridge. Once the fridge holds above 30% of its capacity, the light will turn back to green.

_**Goals**:_ To help the person (and whoever sees the light!) know and to remind them what is a good time to purchase new groceries and refill the refrigerator once they open the door of the fridge.


Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 

\*\***Include a picture of your storyboard here**\*\*
Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 
![IMG_0308](https://user-images.githubusercontent.com/55099696/132140483-09af3f25-72e1-4716-8ff5-01ede406b47b.jpg)

**Feedback:**
We both thought that the “fridge alarm” is a good idea since we both do not pay enough attention to what we have in the fridge. We always find out that we run out of groceries but do not have enough time to purchase them the next day. It let us know when to purchase groceries ahead! 



## Part B. Act out the Interaction

\*\***Are there things that seemed better on paper than acted out?**\*\*
Light and device placement 
Initially, we placed the light inside the fridge. The overall experience has been good when the light is green - we know that we have enough food inside. However, as the purpose of the device is to remind the person when to purchase groceries, it should allow the person to know beforehand - what if they just found out they have below 30% of the necessary groceries but they do not have time to purchase groceries in the next two days? Therefore, we staged the light outside the fridge door since it should be placed where it is easily spotted. 


\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*
Weight vs. space measurement 
We first thought that how “full” the fridge is would be measured by the device through either weighing the groceries inside the fridge or a visual cue of how much space is taken up. However, we found out that either weight or visual cue itself could not be a standalone measurement. First, we could not guarantee that groceries purchased by the person have similar weight each time, even for similar products - what if he bought apple juice instead of apples? If the device takes clues from visual measurements, it also can’t tell if the amount of food is enough - what if the person places an empty ice cream box in it? Therefore, we have learned that the real device should deploy a complex measurement using both weight and visual space.


## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

\*\***Give us feedback on Tinkerbelle.**\*\*
All is good except for installation. :)

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 




https://user-images.githubusercontent.com/55099696/132141438-af098808-3127-47b5-9635-45654ab48a93.MOV





\*\***Show the follow-up work here.**\*\*
![IMG_5002](https://user-images.githubusercontent.com/55099696/132141428-37d210cd-f84f-40bc-8bb2-260fe512d4c4.jpg)



## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

\*\***Include sketches of what your device might look like here.**\*\*
<img width="563" alt="Screen Shot 2021-09-05 at 5 02 39 PM" src="https://user-images.githubusercontent.com/55099696/132141374-9729bae6-9bb4-4842-b8b6-f4ca0a6e06d3.png">


\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*
One concern we had while designing the device was the size of the two parts device. The one inside the fridge has to be small enough that it does not take up too much space in the fridge. It also has to be waterproof and cold-resistant so that it can function well inside the fridge. The light outside the door needs to be obvious and bright enough. For now, we only used Tinkerbelle on our phone so it is square-shaped. 

## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*


https://user-images.githubusercontent.com/55099696/132141392-019f05b2-7a63-4eff-8aa9-585b9b129666.mov




\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 
Ruby Pan - DP478


# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*
- I love the concept of having a device that can alert you of the food level in your fridge. I love that you considered weight and space issues in your implementation. I wish the device was programable so I can set at what percentage the light will be red.
Xingyu Tao , Sep 7 at 9:47pm

Hi Zhenghe, Thanks for sharing your design, I really like it. I think that it tries to tackle a problem that many people have today which is forgetting to purchase enough food storage before too late. Using the light to show is a direct and obvious way convenient for the users to notice. Two thing you may need to consider though is that 1) you may need to specify what the 30% actually means, it can be volume or weight, or you can even make it more detailed grouping by categories. 2) There are people may have different opinion about how full they want their fridge to be, so a bit personalization may make it better. Hope these two pieces of advice can help you improve the product. And thanks for the great work.
Jenny Li , Sep 8 at 1:44am

From the feedback, I found several things that we could improve on our design
1. Make it programmable so that users could set what exact percentage they hope the device can make the alert. Also, some people might have different opinion on. how full they want their fridge to be, so the "green level" should allow personalization as well.
2. Specify how the sensor works - maybe group into categories what parts use weight and what parts uses volume.

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

## Part A. Plan 
**Setting**: The interaction takes place in the kitchen, specifically the refrigerator. The interaction happens when the person walks by or opens the fridge.

**Player:** There is no specific player that the device is designed to interact with. Whoever walks by the fridge or opens the door of the fridge becomes the player of the interaction.

**Activity:** The color of the light outside the fridge indicates how full the refrigerator is. The light is turned off when the refrigerator capacity has been filled to a certain amount (by default, it’s 30%, but the user could set their ideal level of the alarm) so that the person or the household members do not need to purchase extra groceries. If the light turns yellow, it shows that the user will have to fill up their fridge soon. (by default, the light turns yellow at 50% capacity, but allows personalization) If the light turns red, it indicates that the amount of groceries inside the fridge is now equal or below 30%, which signifies that the player should buy groceries to refill the fridge. Once the fridge holds above 50% of its capacity, the light will turn off.

**Goals:** To help the person (and whoever sees the light!) know and to remind them what is a good time to purchase new groceries and refill the refrigerator.

![WechatIMG196](https://user-images.githubusercontent.com/55099696/132957057-56999e50-755b-4c29-8120-36cee448d347.jpeg)


## Part B. Act out the Interaction

\*\***Are there things that seemed better on paper than acted out?**\*\*

(from Part A) Light and device placement 
Initially, we placed the light inside the fridge. The overall experience has been good when the light is green - we know that we have enough food inside. However, as the purpose of the device is to remind the person when to purchase groceries, it should allow the person to know beforehand - what if they just found out they have below 30% of the necessary groceries but they do not have time to purchase groceries in the next two days? Therefore, we staged the light outside the fridge door since it should be placed where it is easily spotted. 


\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

(from Part A) Weight vs. space measurement 
We first thought that how “full” the fridge is would be measured by the device through either weighing the groceries inside the fridge or a visual cue of how much space is taken up. However, we found out that either weight or visual cue itself could not be a standalone measurement. First, we could not guarantee that groceries purchased by the person have similar weight each time, even for similar products - what if he bought apple juice instead of apples? If the device takes clues from visual measurements, it also can’t tell if the amount of food is enough - what if the person places an empty ice cream box in it? Therefore, we have learned that the real device should deploy a complex measurement using both weight and visual space.

(from Part B)
As we stage our interaction, we found that we did not fully consider the two compartments in the fridge - freezer and refrigerator compartments. Originally, we had only one sensor in the refrigerator compartment. We now think about adding a second sensor placed in the freezer compartment. Therefore, the capacity of when the light will turn on will now be based on more complex programming. Ideally, we hope that the light takes into account how full both compartments are proportionally. For example, the freezer takes up 30% while the refrigerator takes the rest 70%. Lights will turn on based on a%of the freezer space plus b% of the refrigerator space. 

## Part C. Prototype the device

## Part D. Wizard the device



https://user-images.githubusercontent.com/55099696/132957944-1858f52c-bed0-4b46-b410-66c39dd6ba18.mp4





## Part E. Costume the device

![WechatIMG197](https://user-images.githubusercontent.com/55099696/132957855-c13d3722-7be0-4fa2-be41-e7c5997c7e2f.jpeg)


(from part A) One concern we had while designing the device was the size of the two parts device. The one inside the fridge has to be small enough that it does not take up too much space in the fridge. It also has to be waterproof and cold-resistant so that it can function well inside the fridge. The light outside the door needs to be obvious and bright enough. For now, we only used Tinkerbelle on our phone so it is square-shaped.

(from part B) Through the feedback we have received, we added a touch screen and personalization function to the light. Now the device allows users to set their ideal level of when the “yellow light” and “red light” turns on just through pressing the button and adjust the level through the bar. Therefore, the size of the light should be larger than what we designed last time. 

## Part F. Record


https://user-images.githubusercontent.com/55099696/132958492-203c3e11-e2a3-41ea-8346-dae6345e87ec.mp4


\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 
Ruby Pan - DP478

\*\***Summarize feedback from your partners here.**\*\*
We combined the feedback we received from peer review.

1. Display nothing instead of a green light where the fridge is full.
2. Use different colors to indicate different amounts of groceries. For example, add a yellow light to show the grocery is below a certain level, and a red light to show that the level is really low.
3. Use multiple light indicators for different categories. For example, one light represents fruits, and another light represents veggies. The lights could take their measurements from the shelves that you place items on, so the top shelf could be strictly for meats, the bottom shelf for veggies, and etc.
4. Make it programmable so that users can set what exact percentage they hope the device can make the alert for. Also, some people might have different opinions on. how full they want their fridge to be, so the "green level" should allow personalization as well.
5. Specify how the sensor works - maybe group into categories what parts use weight and what parts use volume.
