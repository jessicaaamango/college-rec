# college-rec
GETTING STARTED (For Beginners):
    1. Install Python 
        1. https://www.python.org/downloads/ 

        2. Run the installer
            ** Make sureto check the box that says "Add Python to PATH" **

        3. Verify that Python is installed
            On Windows: Open the Command Prompt

            On MAC: Open Terminal

            Use the following commands: 
                python --version

                -- or --

                python3 --version

    2. Install Git

        1. Download git bash or github desktop 
            GIT BASH: https://git-scm.com/downloads

            -- or --

            GITHUB DESKTOP: https://desktop.github.com/download/ 

                -- or -- 

                ** FOR MAC **
                    git --version
                    IF NOT ALREADY INSTALLED brew install git
                
            
    3. Install Visual Studio Code (VS CODE)
        1. Download and Install
            https://code.visualstudio.com/

        2. Open and Navigate to Extensions on the far left hand side

        3. Downlaod Python (Microsoft), Python Debugger (Microsoft), Jupyter Notebook (Microsoft), Error Lens

        



INSTALLATION:
    1. Ensure that your github account is connected to git
        git config --global user.email "hello@example.com"

    2. Clone the repository
        git clone https://github.com/jessicaaamango/college-rec.git

    3. Navigate to the project folder
        cd recommender-system




ENVIRONMENT SETUP:
    1. Create a virtual enviornment
        python -m venv venv

    2. Activate the enviornment:
        Windows:
            venv\Scripts\activate
        
        MAC: 
            source venv\bin\activate
    
    3. Install libraries
        pip install -r requirements.txt

        
        
RUNNING THE FLASK APP:
    1. Ensure the virtual environment is activated

    2. Run the Flask app using the VS Code terminal
        python backend/app.py
        ** if you want to exit then write "deactivate"

    3. Open a web browser and open the URL you see outputted on the terminal

    4. If you want Flask to reload automatically whenever you change the code, run in development mode:
        Windows:
            set FLASK_ENV=development

        MAC:
            export FLASK_ENV=development



USING VS CODE FOR DEVELOPMENT:
