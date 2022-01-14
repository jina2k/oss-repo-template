# Lab 01 Report - Introduction to Open Source Software
## 1. Discord</br>
![image](https://user-images.githubusercontent.com/66571652/149579887-712184ae-1a6d-4fc6-8f9a-5bc8ebbca4c6.png)

## 2. Reading</br>

2.1</br>
The 10 criteria listed in [Open Source Definition](http://opensource.org/osd) define open source, which is summarized below:

Source code must be included in a way that it can be easily modifiable by a programmer and free to use. Those redistributing the software have to abide by the license, where the license also allows other developers to modify the source code, so long as the modified source code is kept under the same license terms. The license also must not allow discrimination of any kind (ie; race or what the software will be used for). </br>
Further definitions defined in the url describe other rules for the license to follow, mostly talking about allowing freedom with the source code when interacting with other software/licenses. 

2.2</br>
Eric Raymond's article [Smart Questions - How to ask the question The Smart Way](http://www.catb.org/esr/faqs/smart-questions.html) describes how to ask questions the smart way,
talking about how nowadays developers don't seem to put in the effort to read before asking. Many times on the Internet, more often nowadays, there are often people (not just developers) who ask a question without regard to if it was previously asked 5 minutes ago, or if the answer could be easily found in a 5 second Google search. The instantaneous sending of a message to the Internet allows for people to do this, and so there is reason to believe a question can be answered quickly after being asked. However, the other side of this is where the person answering is not monitoring chat forums 24/7, and in fact an answer can be found faster searching rather than by asking most of the time. In other words, Eric Raymond goes on to talk about asking questions that haven't already been answered. </br>
In general, Googling is a skill that is necessary for being a developer. Finding what you are looking for through key phrases and critically thinking about answers given on forums,
whilst also filtering through multiple answers is a skill that developers need to perform well. Of course, if the question you're asking is so abstract that you can't find a 
related answer on the Internet, it could be that you are asking the wrong question. Lastly, if you have to ask a question, try to describe it with enough information so that
the person on the other side can understand maybe half of what is being asked, instead of just copy-pasting your code and asking why it doesn't work.

2.3 (How To Answer Questions in a Helpful Way)</br>
- Allow critical thinking for the person asking the question, by giving them a general solution. At times, the person asking a question is asking for a very specific scenario with a very specific answer. However, there are times when there is no 1 way to go about the problem, so answering a question with a general solution in a way that causes the person asking to think about the answer will help not just the person asking, but also people who visit the forums in the future.

- Explain your solution. This can reference documentation, other forums, code, etc. By explaining your code, the user can try to understand the why, and therefore reduces the number of questions being asked in the future.

2.4 </br>
Jesse Jordan, freshman in 2002 at RPI, gets sued after making a search engine that ended up being used to pirate music. He based the search engine off of Microsoft's, and made it publically available to every student at RPI. Out of everything that the students of RPI put into Jesse's search engine, the RIAA chose to sue him for copying a search engine and essentially just making it available to students, because "music". I basically learned from this reading that redistributing software has consequences, even though Jesse barely made changes to the search engine. I also learned that society can be unfair where it costs more money to win the lawsuit rather than to settle (and that if Jesse had more money, the RIAA would have taken all of it had it been under 15 million). Artists barely made money during this time as well, so it was clear that the RIAA's intention was to profit off of the early ages of the Internet. Above all, it shows that contributing to open source can cost money, and that advancing technology should be treaded carefully, as there can be unforeseen consequences like what happened here. As someone said in the past, nothing is ever really free.

## 3. Linux </br>
![image](https://user-images.githubusercontent.com/66571652/149588646-a5d062b5-133b-4ee2-81d3-dd02691569a4.png)

## 4. Regex </br>

4.1 </br>
#1 </br>
![image](https://user-images.githubusercontent.com/66571652/149589787-9f9dd36e-1d8b-4df2-b769-30782c99bb55.png)

#2 </br>
![image](https://user-images.githubusercontent.com/66571652/149590741-1f2cc01c-a2da-44d4-bf71-95f50ed072f4.png)

#3 </br>
![image](https://user-images.githubusercontent.com/66571652/149591377-bd45987d-ebde-4334-9aaa-54c5d4c54a8a.png)

#4 </br>
![image](https://user-images.githubusercontent.com/66571652/149591847-32bbe908-a5a8-4157-8bd4-d741358f4cd4.png)

#5 </br>
![image](https://user-images.githubusercontent.com/66571652/149592058-3c9e54f1-4830-4a6e-a73f-6880cde605a9.png)

#6 </br>
![image](https://user-images.githubusercontent.com/66571652/149592220-0a397e1d-c861-4faf-9f83-ff9e4bccd5f2.png)

#7 </br>
![image](https://user-images.githubusercontent.com/66571652/149592486-6d5bf5ea-d3e3-45d8-bb0c-e02b5f15f4ae.png)

4.2 </br>

#1 </br>
![image](https://user-images.githubusercontent.com/66571652/149593754-f51f1c67-96a3-4391-a0d7-c60ed92f8f45.png)

#2 </br>
![image](https://user-images.githubusercontent.com/66571652/149593786-a5d06e37-1a5a-4ac3-a414-65c78b851421.png)

#3 </br>
![image](https://user-images.githubusercontent.com/66571652/149593814-83f6a20a-7773-4162-a572-1b9de4c27b3a.png)

#4 </br>
![image](https://user-images.githubusercontent.com/66571652/149593847-f1c5b787-df83-4dd7-a7ec-986a96b52964.png)

#5 </br>
![image](https://user-images.githubusercontent.com/66571652/149593873-c0832a28-3426-4bf6-a82f-d64c188c6cc1.png)
</br>
## 5. Blockly </br>
![image](https://user-images.githubusercontent.com/66571652/149595416-7459f878-ec9d-4478-872b-2f04099886ee.png)
</br>
<pre>
while (notDone()) {
  if (isPathForward()) {
    moveForward();
    if (isPathRight()) {
      turnRight();
    } else {
    }
  } else {
    if (isPathLeft()) {
      turnLeft();
    } else {
      if (isPathRight()) {
        turnRight();
      } else {
        turnRight();
      }
    }
  }
}
</pre>

## 6. Reflection </br>
I'm interested in working on [OpenEnergyDashboard](https://github.com/OpenEnergyDashboard/OED) as I have previously worked on it in RCOS last semester. This would allow me to get to work on problems faster as I have already been through the onboarding process for this project. </br>
Another project I am somewhat interested in is a Maplestory private server [v203.4](https://github.com/pokiuwu/v203.4) that I have forked recently. I still have not looked at the code so I am not sure how long the onboarding process will take. This project could be interesting for me to work on as I want to implement some custom features that some private servers had in the past.
