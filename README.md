# ScrappingCOVID
This is a web scrapping project which scraps various websites to inform us about the Corona Cases of different countries. It also vizualizes the data in order to present the severity of the crisis in a comprehensive manner.

# Technologies Used:
I used the following tools and technologies in order to successfully make the project: </br>
1. Python </br>
2. HTML </br>
3. CSS </br>
4. File Handling technique </br>
5. Flask (Framework) </br>
6. Web Scrapping </br>

# Project Structure
This project has  the following major parts : </br>
1. app.py : This contains Flask APIs that are used to inform the user about the Corona cases in different countries. </br>
2. send_mail.py : This Python Scripts sends an email to the users of our website whenever a demand is made </br>
3. model.py : This contains the basic code used in the web scrapping job. </br>
4. CovidTrackerIndia.ipynb : This is used in the data vizualization and represntation part and informs us about corona cases in different Indian States.

# Running the Model:
1. Ensure that you are in the project home directory. </br>
2. Run app.py using below command to start Flask API python app.py </br>
By default, flask will run on port 5000 and will inform about Global Corona Cases </br>
3. "/home" route contains the website's home page </br>
4. "/india" route contains corona details of India </br>
5. On the home page see the valid country names and "/x" route will inform you about corona cases in the entered country 'x' </br>
6. Run the send_mail.py model to send emails to the multiple users of our website </br>

# Working Snaps
Emails sent by our model to users: </br>  </br> 
![email_covid_stats](https://user-images.githubusercontent.com/51885421/85329869-f7c11b80-b4f0-11ea-9902-543a3f6a4d39.png)
</br>
Our Home Page

![home1](https://user-images.githubusercontent.com/51885421/85329985-2939e700-b4f1-11ea-9158-ad18d52f54b5.png)

Few examples of country names we can find the details about </br>  
![home2](https://user-images.githubusercontent.com/51885421/85329988-2b9c4100-b4f1-11ea-9b61-5302a5791900.png)
![home3](https://user-images.githubusercontent.com/51885421/85329989-2c34d780-b4f1-11ea-8be1-9855942a6449.png)
</br>
Corona Details of World
</br>
![global_scrapper](https://user-images.githubusercontent.com/51885421/85330549-402d0900-b4f2-11ea-8358-58a3fe72400c.png)

</br>
Corona Details of India
</br>
![india_scrapper](https://user-images.githubusercontent.com/51885421/85329990-2ccd6e00-b4f1-11ea-91a4-c849dd06bf98.png)
</br>
Examples Of Covid Scrapper of Other Nations
</br>
![others_scrapper](https://user-images.githubusercontent.com/51885421/85329993-2d660480-b4f1-11ea-99fe-fc30ec5449ad.png)
</br>
![Screenshot (81)](https://user-images.githubusercontent.com/51885421/85329995-2dfe9b00-b4f1-11ea-8ea0-a63bd35d51c2.png)
</br>
![Screenshot (83)](https://user-images.githubusercontent.com/51885421/85329997-2e973180-b4f1-11ea-8db5-5217d132145b.png)
</br>
![Screenshot (85)](https://user-images.githubusercontent.com/51885421/85330007-3525a900-b4f1-11ea-9e43-6e217c229c47.png)
</br>
![Screenshot (84)](https://user-images.githubusercontent.com/51885421/85330013-37880300-b4f1-11ea-8668-cdb3f9025a78.png)
</br>
Data Vizualization using Google Colab </br>
Bar chart of Cases in Indian states </br>
![image](https://user-images.githubusercontent.com/51885421/85330234-96e61300-b4f1-11ea-82e7-6d9e0791d7a7.png)
Pie chart of Cases in Indian states </br>
![image](https://user-images.githubusercontent.com/51885421/85330247-9f3e4e00-b4f1-11ea-8ecf-a870cb6e1a89.png)






