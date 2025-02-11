# AdvisorBot 🤖🎓  
*A Discord Chatbot for Academic Advising*  

## 📌 Project Overview  
**AdvisorBot** is a conversational chatbot designed to assist students with academic advising on **Discord**. The bot provides automated responses to common advising questions, helping to reduce the workload on human advisors while ensuring students receive timely and accurate information.

This project follows an **intent-driven** conversation model and utilizes **Python**, **MongoDB**, **Docker**, and **Machine Learning** for chatbot training. The bot retrieves data using web services and a trained AI model to enhance the advising experience.

---

## 🎯 Features  
- **Student Assistance:**  
  - Provides course descriptions, prerequisites, and scheduling information.  
  - Retrieves advisor contact details and office hours.  
  - Offers career development, tutoring, and extracurricular activity information.  
- **University Resources:**  
  - Returns building hours, dining schedules, and parking details.  
  - Provides information about scholarships and transcript requests.  
- **Academic Planning:**  
  - Guides students through major/minor selection and course substitutions.  
  - Assists transfer students with credit evaluations.  
- **Advisor Support:**  
  - Notifies advisors when a student requests direct consultation.  
  - Generates transcripts of bot-student interactions for record-keeping.  
- **User Experience Enhancements:**  
  - Supports natural conversations using **state-driven interactions**.  
  - Allows students to save chat transcripts for later reference.  

---

## 🏗️ Tech Stack  
- **Programming Language:** Python  
- **Bot Platform:** Discord  
- **Database:** MongoDB (for storing chat logs and training data)  
- **Web Services:** REST APIs for retrieving university data  
- **Machine Learning:** Trained AI model for intent classification  
- **Deployment:** Docker for containerized execution  

---

## 📂 Project Structure  
Academic-Discord-Bot/
│── data/               # JSON files needed to train the system
│── images/             # Stores images used for documentation
│── modules/            # All source files for the project minus bot.py
│   ├── states/         # Conversation state management
│   ├── context/        # API handlers for course & directory queries
│── tests/              # Test files using unittest for the project
│── bot.py              # Main driver class for the discord chatbot
│── train.py            # Python program needed to train the learner
│── requirements.txt    # Listing of all the external modules needed for the program
│── .env                # Environment variables (bot token, API keys)
└── README.md           # Project documentation

---

## 🚀 Setup & Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone <repo-url>
cd AdvisorBot
```

### **2️⃣ Set Up a Python Virtual Environment

#### For Mac/Linux:

```bash
    python -m venv venv
    source venv/bin/activate
```

#### For Windows (Command Prompt):

```bash
    python -m venv venv
    .\venv\Scripts\activate.bat
```
#### For Windows (PowerShell):

```bash
    python -m venv venv
    .\venv\Scripts\activate.ps1
```

### **3️⃣ Install Dependencies

```bash
    pip install -r requirements.txt
```

### 🚨 Mac Users:
If you are using MacOS, replace tensorflow in requirements.txt with:

```bash
    tensorflow-macos
```

## 🗄️ Database Setup (MongoDB & Docker)
### **1️⃣ Start MongoDB Using Docker
You need to start Docker and run MongoDB, which was configured during Lab 1.
Use Docker Desktop to start the MongoDB container.

### **2️⃣ Create the Chatbot Database
Once MongoDB is running, create a database named chatbot-database:
```bash
    mongo
    use chatbot-database
```

### **3️⃣ Import Training Data

```bash
    mongoimport --db chatbot-database --collection dictionary --type json --jsonArray --uri mongodb://localhost
    mongoimport --db chatbot-database --collection intents --type json --jsonArray --uri mongodb://localhost
```

## 🔧 Configure Environment Variables
Modify the .env file to include your Discord Bot Token and API keys:

.env
    DISCORD_BOT_TOKEN="your-bot-token"
    DIRECTORY_API_KEY="your-directory-api-key"

## 🏋️‍♂️ Training the AI Model
Once MongoDB is running, train the chatbot's AI model using:

```bash
    python train.py
```
This command should be run twice:

In the main project directory (advisor_bot)
In the advisor_bot/test directory

## 🔄 Development Process  

### **Phase 1: Concept Initiation**  
- Brainstormed features & identified user needs.  
- Created **user stories**:
  - *"As a student, I want to retrieve my advisor’s contact info so that I can schedule an appointment."*  
  - *"As an advisor, I want to be notified when a student needs help so that I can follow up promptly."*  
- Designed **use case diagrams** and conversation workflows.  

### **Phase 2: Iterative Development**  
- **Iteration 0:**  
  - Set up **Discord bot**, configured the development server.  
  - Integrated **MongoDB** and **Docker** for scalability.  
- **Iteration 1:**  
  - Implemented the **State Design Pattern** to handle conversation flow.  
  - Developed core conversation states: *Initiation, Preview, Business, Feedback, Closing.*  
- **Iteration 2:**  
  - Integrated **web services** for retrieving course information and faculty directory data.  
  - Implemented error handling for API requests (e.g., network failures, invalid inputs).  

---

## ▶️ Running the Chatbot  

### **1️⃣ Start MongoDB**  
Make sure MongoDB is running inside Docker.  

### **2️⃣ Run the Chatbot**  
```bash
    python bot.py
```



