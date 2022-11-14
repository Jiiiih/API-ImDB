# README

# Table of contents
1. [Description](#description)
2. [Prerequisites](#prerequisites)
3. [Usage](#usage)

## Description <a name="description"></a>
Python application that requests ImDB's API made in the framework of an EPF school project.
Available feature : 
- Find ratings for a specific movie 

## Prerequisites <a name="prerequisites"></a>
Python >= 3.8

## Usage <a name="usage"></a>
### Clone the repository 
```
git clone https://github.com/Jiiiih/API-ImDB.git
cd API-ImDB
```
### Get ImDb API key
1. <a href="https://imdb-api.com" target="_blank">Create ImDb's API account</a>

2. get the api key from the profile section 

### Setup the .env file 
1. Rename ```.env_modify to .env```
2. Paste your personal api key in the file 

### Run the app 
Once you avec installed the prerequisites and setup the .env file. You can run the script.
Enter the following command at the repository root directory.\
```python3 main.py```\
Then enter the name of the movie from which you want the ratings.
