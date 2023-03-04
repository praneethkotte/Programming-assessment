<!-- ### What is this?
This `README.md` file is auto-created for all new projects.

### Why am I here?
This file opens automatically when you open a project. 

If you do not create Guides, this `README.md` will be what automatically opens for students. You can edit this file by clicking on the pencil icon in the upper right corner.

### How do I get started with Codio?
Use this [Onboarding Guide](https://codio.com/home/starter-packs/2ae8501b-e5f7-4b07-8e9f-adb155fc6d10) for an interactive tutorial through the main features of Codio. Click on the link, click **Use Pack** and then click **Create** to add it to your projects.

### How do I close this file?
At the top of your workspace you will see tabs for each open file. Click the x on the right hand side of the tab that says **README.md**.
![readMeTab](https://global.codio.com/platform/readme.resources/readMeTab.png)

### I expected to see or edit learning materials.
Select **Tools->Guide->Play** to view the Guide for this project.
![playGuide](https://global.codio.com/platform/readme.resources/playGuide.png)

Click on the **Open Guides Editor** icon to edit the Guide.
![guideEdit](https://global.codio.com/platform/readme.resources/guideEdit.png)

### How do I delete this file?
To delete this `README.md` file, right-click (ctrl-click on a Mac) on the file name in the file list.
![fileTree](https://global.codio.com/platform/readme.resources/fileTree.png) -->


Introduction:
The Flask application provides an interactive interface for users to view and analyse data from the World Bank- United States dataset. The application allows us to select and visualize various indicators and time periods using charts(pie, line) and graphs.
Development:
Started by Meticulously planning the design stages. Creating of the Git Repository and storing the data, Finding the correct database, using pares_csv.py importing the database, utilizing the Flask framework, utilizing the appropriate templates, testing the data, handling the errors, and finally publishing the complete developed application using render.
The modular approach is used to develop the application, with separate files for each components such as, Data access, Data processing, and interface. 
Implementation:
The required dependencies was installed using pip before deploying the application into the cloud-based server.
 For the World Bank-US, I have created a database-driven Flask application with 2 linked tables for this task. The following steps defines the step by step procedure,
Creating wireless frameworks, and implementing all the logics into the application development. Two csv files holding data of US world bank data. The data is parsed before being inserted into the SQLite database(datausa.db). Importing all the required libraries into the application and using them conveniently where ever required. 
Designed separate HTML files for the searches and index, and also css files for implementing the styles to the HTML format to make it appear good. Created a python program to call the data. And routed the URL’s according to the requirements and later downloading the CSV file and importing the data and passing the two tables and fetching the required data.
Usage: 
For using the application, 
1.	navigate to the home page using the link https://data.worldbank.org/ 
2.	Click on the search input field, enter the country name to search- United States.
3.	The page will be redirected to the next page https://data.worldbank.org/country/united-states 
4.	In this page we can see all the graphs, charts, data about the country, and also files to be used for download CSV, XML, Excel.
5.	Download the CSV file and unzip the zipped folder and fetch the data from the excel sheet.
6.	Fetch the data from the required Excel which are present in the rows.
7.	Unzip the csv file and import the csv data to the datasets folder.
8.	Create the parse_csv.py file and assign the data.
9.	Run the parse_csv.py to create the db.
10.	Once db is created call the db into the py application and fetch the tables accordingly.

11.	Click on the project->Box Info-> and copy the link and paste the same link into the other tab to see the tables created. If we make any changes in the program then we need to click on refresh so that the data gets populated or use app.run(host='0.0.0.0', debug=True)  to refresh the page automatically.
Git Repository address:
HTTPS connection link:
https://github.com/praneethkotte/Programming-assessment.git
SSH connection Link:
git@github.com:praneethkotte/Programming-assessment.git 
Conclusion:
Flask application provides a simple and intuitive interface for users to access and analyze data from the World Bank- United States dataset. The Use of External libraries and Modular design makes the application easy to maintain and extend.
