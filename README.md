# Tec de Monterrey Bootcamp Final Project

## Overview

The scope of our final project consists of using multiple technologies to accomplish real world assignments for potential clients. During a four-week period our team will complete certain tasks that are detailed by category and dates, from planning to executing and presenting our results.


### Team

As a team we decided to apply the next team roles for the entire project. The main reason being that this is a one-time short project where we need to be focus on the task at hand by being efficient and effective with as little time as possible.

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

The rubric of the project was divided in to four segments with different tasks to be completed. We decided it to showcase our progress accordingly, therefore our results are dived it in to the following categories: Presentation, GitHub, Machine Learning, Data Base and Dashboard.



Presentation [Link](https://docs.google.com/presentation/d/1mLjjnq5bFfYdqnkWDMU-8ioWCNJDzz2DnzwazVJTAno/edit?usp=sharing).

<details><summary>Prsentation</summary>
  
#### Selected topic:
- Get Twitter data through an API to perform sentiment analysis with machine learning 

#### Reason why they selected their topic
- The project consists of building a tool that can analyze tweet sentiment on specific words, based on machine learning. The user would be able to look for certain hashtags, then extracts the tweets that talk about that specific subject, apply the machine learning model to categorize the sentiment of the tweets. We have considered different potential users such as:
  
  - Non-profits
  - Government Agencies
  - Politicians
  - Companies 
  - Social Responsibility

#### Description of their source of data
- Our data from twitter comprehends tweets, like, retweets, and location

#### Questions they hope to answer with the data
- What do people think about a particular subject?
- What is the tweet with the most reach?
- What is the location of the users with a positive feeling about the tweet?
- What is the location of the users with a negative feeling about the tweet?

#### Description of the communication protocols
As a team we have stablished four channels of communication. 
  - Slack Conversations 
    - One to one conversations (bilingual writing)
    - Team 5 personal chat (only team members, bilingual writing)
    - Chat with TA´s and Instructor as moderators (write in english)
  - Google Meet Quick Meeting 
    - Every Day at 10:00 pm (Mexico City Time)
    - 15 to 20 min meeting 
    - We use this meeting to touch base on important issues during the day and to create pull request and merge to the main branch
  - Class Time Meetings through Zoom 
    - Tuesdays and Thursdays we get together during class time to discuss more in depth our project, also relying on the assistance of our TA.
    - Saturdays for the Office Hours (OPTIONAL)
  - Extraordinary meeting 
    - This are schedule ahead of time through slack one to one, or in our personal chat. 
    - We discuss urgent matters, most of the time this meeting are done Saturday and Sunday afternoos.

  
  
    ![CRISP-DM_Process_Diagram](https://user-images.githubusercontent.com/37987602/153728408-92d4675f-3d55-4068-94ca-8ff9974e0c97.png)
  
 #### Description of the data exploration phase of the project 

 #### Description of the analysis phase of the project
 
 #### Technologies, languages, tools, and algorithms used throughout the project
  - HTML
  - CSS
  - JavaScript
    - Leaflet
    - D3
  - Amazon Web Services
  - Python
    - Flask
    - PySpark
  - SQL - Postgress
  
 #### Result of analysis
  
 #### Recommendation for future analysis
  
 #### Anything the team would have done differently
 
</details>


<details><summary>GitHub </summary>
  
  Our first week includes a README.md file that includes a description of the [communication protocols](https://github.com/ioshisolis/Bootcamp_Final_Project/edit/main/README.md#description-of-the-communication-protocols), individual branches and four commits per team member. 
  
  #### Individual Branches 
  ![Branches](https://user-images.githubusercontent.com/37987602/153726614-b1cd7dfb-d9ba-4415-86d5-b8c027b03d45.png)

  
</details>


<details><summary>Machine Learning</summary>
  
  #### Description of data preprocessing

  #### Description of feature engineering and the feature selection, including the
team's decision-making process
  
  Provisional machine learning model accomplishes the following
  - Takes in data in from the provisional database
  - Outputs label(s) for input data
  
  Important Questions

   - Why are we using this machine learning model
   We areusing the Naive Bayes Classifiers because we assume that every tweet and their respective attributes are independant of each other, plus, the sentiment analysis we are creating is one where only two options are possible (positive or negative) thus using this algorithm makes the most sense in terms of binary classification.  

   - Why are we using this machine learning model?

   - NLP
    - List of Stop Words (Words to ignore) and why
    According to Digital Tracking specialist, computer scientist and Master in systems analytics Gabriel Landaeta K., while dealing with tweets in spanish we must consider a number of words that do not add value to the analysis because they are not directly linked with an actual sentiment, but rather are only used as conectors that humans (and not computers) understand. 

 
#### Description of how data was split into training and testing sets
  

#### Explanation of model choice, including limitations and benefits
  
#### Explanation of changes in model choice (if changes occurred between the
  
#### Segment 2 and Segment 3 deliverables)
  
#### Description of how model was trained (or retrained, if they are using an
existing model)
  
#### Description and explanation of model’s confusion matrix, including final
accuracy score

  
</details>


<details><summary>Data Base</summary>
 
  #### Database stores static data for use during the project
  
  Provisional database accomplishes the following:
  - Sample data that mimics the expected final database structure or schema
  - Draft machine learning module is connected to the provisional database

  
  #### Database interfaces with the project in some format (e.g., scraping updates
the database, or database connects to the model)
  
  Important Questions:

  
  #### Includes at least two tables (or collections, if using MongoDB)
  
  
  - ### Data Types of each column
    - ### Twitter data Table
        This Table will Hold de Tweet Text scrapped by certain Keyword, and a ML algorithm will cluster it by sentiment.   

        | Columns      | Data Type | Description |
        | :---         |  :---:    |    :--- |
        | Index        | Serial Int      | Row Count |
        | User         | String   | The Screen Name of the user     |
        | User_id      | Integer   | The unique user_id Tweeter gives to each member    |
        | Tweet        | String  | The Actual Tweet of the User   |      
        | Sentiment      | String   | The cluster Assigned by ML algorithm  |


    - ### User Data Table
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


#### Includes at least one join using the database language (not including any
joins in Pandas)
  
  
  - Why are we using this data?

    The twitter_data table stores the text of the tweets collected on a keyword, with the aim of classifying the data to find out the general feeling of the community on twitter about a topic.

    The User_data table stores user data. These data help us to filter the information by languages ​​or number of followers as well as their location to know where more than one specific topic is discussed.

    ## Test Join 

        SELECT *
        FROM "Twitter_data"
        INNER JOIN "User_Data"
        On "User_Data"."User_id" = "Twitter_data"."User_id";

    ![JOIN](https://github.com/ioshisolis/Bootcamp_Final_Project/blob/main/Data/DB_Join.png)

    
 #### Includes at least one connection string (using SQLAlchemy or PyMongo) 
  
</details>


<details><summary>Dashboard</summary>
  
For this first segment, we schetched out the first draft of the dashboard to get a visual representation on how the data should be prepare in order to be presented at the last stage.

  ![Dashboard_FirstDraft](https://user-images.githubusercontent.com/37987602/153799300-8ecf4995-cb17-4f25-b419-0b47c25c9046.jpeg)

#### Images from the initial analysis
  ![First draft](https://user-images.githubusercontent.com/37987602/157785331-1be13814-d39c-4e97-a5de-10072d77aa03.png)

#### Data (images or report) from the machine learning task
  
#### At least one interactive element
  
  ![DashBoard](https://user-images.githubusercontent.com/37987602/157783775-bb45a558-0303-476b-b284-ea05bbe42f9a.png)
  ![TopRetweets](https://user-images.githubusercontent.com/37987602/157783924-378eee70-0ea9-4980-82a7-7131df5cce43.png)
  ![InteractiveMap](https://user-images.githubusercontent.com/37987602/157783603-2040cbcb-1ea8-4e17-9866-905991361235.png)

  
</details>


