# Tec de Monterrey Bootcamp Final Project

## Overview

The scope of our final project consists on using multiple technologies to accomplish real world assigments for potential clients. During a three week period our team will complete certain tasks that are detailed by category and dates, from planning to executing and presenting our final results. 


### Team

As a team we decided to apply the next team roles for the entire project. The main reason being that this is a one time short-project where we neew to be focus on the task at hand by being efficient and effective with as little time as possible.

<details><summary>Team Members</summary>

- Luz Helena - https://github.com/luhlna
- Alexis Santiago - https://github.com/Alfer23
- Claudio Rocha - https://github.com/claud-e
- Daniel Tejada - https://github.com/dani1925
- Jorge Solis - https://github.com/ioshisolis

</details>

<details><summary>Team Roles</summary>
  
  ![TeamRoles](https://user-images.githubusercontent.com/37987602/153530443-7aaf8bc8-ca44-44aa-b725-17417fecaa0a.png)

</details>
  
## Results

The rubric of the project was divided in to four segments, with different tasks to be completed. We decided it to showcase our progress accordingly. Therefore our results are dived it in to the following categories: Presentation, GitHub, Machine Learning, Data Base and Dashboard. 

### Presentation

<details><summary>Segment 1</summary>
  
#### Selected topic:
- Get Twitter data through an API to perform sentiment analysis with machine learning 

#### Reason why they selected their topic
- The project consists on building a tool that can analyze tweet sentiment on specific words, based on machine learing. The user would be able to look for certain hashtags, then extrack the tweets that talk about that specific subject, apply a nlp machine learnign model to categorize the sentiment of the tweets. We have consider different potential users such as:
  - Non-profits
  - Government Agencies
  - Politicians
  - Companies 
  - Social Responsability

#### Description of their source of data
- Our data from twitter comprehends tweets, like, retweets, and location

#### Questions they hope to answer with the data
- What do peopole think about a particular subject?
- What is the tweet with the most reach?
- What is the location of the users with a positve feeling about the tweet?
- What is the location of the users with a negative feeling about the tweet

#### Description of the communication protocols
As a team we have stablished four channels of communication. 
  - Slack Conversaitons 
    - One to one conversaiots (bilingual writing)
    - Team 5 personal chat (only team members, bilingual writing)
    - Chat with TA´s and Instructor as moderators (write in english)
  - Google Meet Quick Meeting 
    - Every Day at 10:00 pm (Mexico City Time)
    - 15 to 20 min meeting 
    - We use this meeting to touch base on important issues during the day and to create pull request and merge to the main branch
  - Class Time Meetings through Zoom 
    - Tuesdays and Thurdays we get together during class time to discuss more in depth our project, also reliying on the assistance of our TA.
    - Saturdays for the Office Hours (OPTIONAL)
  - Extraordinary meeting 
    - This are schedule ahead of time through slack one to one, or in our personal chat. 
    - We discuss urgent matters, most of the time this meeting are done Saturday and Sunday afternoos.

</details>

<details><summary>Segment 2</summary>
    
</details>

<details><summary>Segment 3</summary>
    
</details>
  
  
</details>
  
  
### GitHub  


<details><summary>Segment 1</summary>
  
  Our first week includes a README.md file that includes a description of the [communicaiont protocols](https://github.com/ioshisolis/Bootcamp_Final_Project/edit/main/README.md#description-of-the-communication-protocols), individual branches and four commits per team member. 
  
  #### Individual Branches 
  ![Branches](https://user-images.githubusercontent.com/37987602/153726614-b1cd7dfb-d9ba-4415-86d5-b8c027b03d45.png)

  
</details>

<details><summary>Segment 2</summary>
  
</details>

<details><summary>Segment 3</summary>
  
</details>

<details><summary>Segment 4</summary>
  
</details>


### Machine Learning

<details><summary>Segment 1</summary>
  
  
  Provisional machine learning model accomplishes the following
  - Takes in data in from the provisional database
  - Outputs label(s) for input data
  
  Important Questions
   - Why are we using this machine learning model
   We areusing the Naive Bayes Classifiers because we assume that every tweet and their respective attributes are independant of each other, plus, the sentiment analysis we are creating is one where only two options are possible (positive or negative) thus using this algorithm makes the most sense in terms of binary classification.  
   - NLP
    - List of Stop Words (Words to ignore) and why
    According to Digital Tracking specialist, computer scientist and Master in systems analytics Gabriel Landaeta K., while dealing with tweets in spanish we must consider a number of words that do not add value to the analysis because they are not directly linked with an actual sentiment, but rather are only used as conectors that humans (and not computers) understand. These words are:
    a
    acá
    ahí
    ajena/o/s
    al
    algo
    algún/a/o/s
    allá/í
    ambos
    ante
    antes
    aquel
    aquella/o/s
    aquí
    arriba
    así
    atrás
    aun
    aunque
    bajo
    bastante
    bien
    cabe
    cada
    casi
    cierto/a/s
    como
    con
    conmigo
    conseguimos
    conseguir
    consigo
    consigue
    consiguen
    consigues
    contigo
    contra
    cual
    cuales
    cualquier/a/s
    cuan
    cuando
    cuanto/a/s
    de
    dejar
    del
    demás
    demasiada/o/s
    dentro
    desde
    donde
    dos
    el
    él
    ella/o/s
    empleáis
    emplean
    emplear
    empleas
    empleo
    en
    encima
    entonces
    entre
    era/s
    eramos
    eran
    eres
    es
    esa/e/o/s
    esta/s
    estaba
    estado
    estáis
    estamos
    están
    estar
    este/o/s
    estoy
    etc
    fin
    fue
    fueron
    fui
    fuimos
    gueno
    ha
    hace/s
    hacéis
    hacemos
    hacen
    hacer
    hacia
    hago
    hasta
    incluso
    intenta/s
    intentáis
    intentamos
    intentan
    intentar
    intento
    ir
    jamás
    junto/s
    la/o/s
    largo
    más
    me
    menos
    mi/s
    mía/s
    mientras
    mío/s
    misma/o/s
    modo
    mucha/s
    muchísima/o/s
    mucho/s
    muy
    nada
    ni
    ningún/a/o/s
    no
    nos
    nosotras/os
    nuestra/o/s
    nunca
    os
    otra/o/s
    para
    parecer
    pero
    poca/o/s
    podéis
    podemos
    poder
    podría/s
    podríais
    podríamos
    podrían
    por
    por qué
    porque
    primero
    puede/n
    puedo
    pues
    que
    qué
    querer
    quién/es
    quienesquiera
    quienquiera
    quizá/s
    sabe/s/n
    sabéis
    sabemos
    saber
    se
    según
    ser
    si
    sí
    siempre
    siendo
    sin
    sino
    so
    sobre
    sois
    solamente
    solo
    sólo
    somos
    soy
    sr
    sra
    sres
    sta
    su/s
    suya/o/s
    tal/es
    también
    tampoco
    tan
    tanta/o/s
    te
    tenéis
    tenemos
    tener
    tengo
    ti
    tiempo
    tiene
    tienen
    toda/o/s
    tomar
    trabaja/o
    trabajáis
    trabajamos
    trabajan
    trabajar
    trabajas
    tras
    tú
    tu
    tus
    tuya/o/s
    último
    ultimo
    un/a/o/s
    usa/s
    usáis
    usamos
    usan
    usar
    uso
    usted/es
    va/n
    vais
    valor
    vamos
    varias/os
    vaya
    verdadera
    vosotras/os
    voy
    vuestra/o/s
    y
    ya
    yo
    

  
</details>

<details><summary>Segment 2</summary>
  
</details>

<details><summary>Segment 3</summary>
  
</details>

<details><summary>Segment 4</summary>
  
</details>


### Data Base

<details><summary>Segment 1</summary>
 
  Provisional database accomplishes the following:
  - Sample data that mimics the expected final database structure or schema
  - Draft machine learning module is connected to the provisional database
  
  Important Questions:

  - ### Data Types of each column
    - ### Twitter_data Table
        This Table will Hold de Tweet Text scrapped by certain Keyword, and a ML algorithm will cluster it by sentiment.   

        | Columns      | Data Type | Description |
        | :---         |  :---:    |    :--- |
        | Index        | Serial Int      | Row Count |
        | User         | String   | The Screen Name of the user     |
        | User_id      | Integer   | The unique user_id Tweeter gives to each member    |
        | Tweet        | String  | The Actual Tweet of the User   |      
        | Sentiment      | String   | The cluster Assigned by ML algorithm  |


    - ### User_Data Table
      This Table will Hold the information about the user that post the tweets.

      | Columns      | Data Type | Description |
      | :---         |  :---:    |    :--- |
      | Index        | Serial Int      | Row Count |
      | User_id      | Integer   | The unique user_id Tweeter gives to each member    |
      | Re-tweet Count       | Integer  | The numer of Re-tweets a tweets had |      
      | Location      | String   | The City and Country of the user |
      | Verified_Account     | Boolean   | It shows if a Twitter Account is verified  |
      |Geo_Enabled      | Boolean   | Shows if the user had enabled the geo location |  
      | Lang      | String   | Language of the Tweet|          

      
  - Description of each column
  - Why are we using this data?
  

  
  
</details>

<details><summary>Segment 2</summary>
  
</details>

<details><summary>Segment 3</summary>
  
</details>

<details><summary>Segment 4</summary>
  
</details>


### Dashboard

<details><summary>Segment 1</summary>
  
  No work was done on the first week. The person in charge had to do research on best practices and portential capabilities for our dashboard. 
  
</details>

<details><summary>Segment 2</summary>
  
</details>

<details><summary>Segment 3</summary>
  
</details>

<details><summary>Segment 4</summary>
  
</details>

## Summary

<details><summary>CRISP Pocess Diagram</summary>
  
![CRISP-DM_Process_Diagram](https://user-images.githubusercontent.com/37987602/153728408-92d4675f-3d55-4068-94ca-8ff9974e0c97.png)

</details>
