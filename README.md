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

        



    4. Clone the repository:
        1. Open a terminal:
            Windows: Open "Git Bash"
            MAC: Use the built-in terminal

        2. Ensure that your github account is connected to git
            git config --global user.email "hello@example.com"

        3. Clone the repository
            git clone https://github.com/jessicaaamango/college-rec.git

        4. Navigate to the project folder
            cd recommender-system




    5. Set up the Virtual Enviornment:
        1. Create a virtual enviornment
            python -m venv venv

        2. Activate the enviornment:
            Windows:
                venv\Scripts\activate
            
            MAC: 
                source venv\bin\activate
        
        3. Install dependencies
            pip install -r requirements.txt

        
        
    6. Running the Flash App:
        1. Ensure the virtual environment is activated
            ** ((venv)) should show in the terminal **

        2. Run the Flask app using the VS Code terminal
            python backend/app.py
            ** if you want to exit then write "deactivate"

        3. Open a web browser and open the URL you see outputted on the terminal

        4. If you want Flask to reload automatically whenever you change the code, run in development mode:

            ** you will need to deactivate the app if you haven't already then restart after running the following command **
            Windows:
                set FLASK_ENV=development

            MAC:
                export FLASK_ENV=development
        



    7. Using VS Code for Development
        1. Open the project in VS Code
            ** either go to the folder using VS Code, Go through your file explorer and open with VS Code, OR in the terminal write the following:
                code .

    8. Using Jupyter Notebooks
        1. Install Jupyter Notebook
            pip install notebook

        2. Launch Jupyter Notebook
            jupyter notebook
        
        3. Naviagte to your Notebooks

        4. Shut Down Jupyter
            **When you're done coding, press "CRTL + C" in terminal. It will ask for confirtmation, type Y and hit Enter
        
    9. VS Code Jupyter Integration
        1. Install the Jupyter Entension

        2. Open your Notebook in VS Code
        ** Right click on the .ipynb file then choose "Open with... -> Jupyter Notebook"

        3. Select the Virtual Enviornment Kernel
        ** Once the NOtebook is open, look for the kernal selector in the top right, then choose the interpreter inside the virtual enviornment "venv" **

-------------------------------------
CONTRIBUTING
    1. Fork the repo on GitHub

    2. Create a new branch
        ** This is to ensure that the main branch is always secure, if there happens to be an issue with your branch, you are able to revert back to the original code, in this case it is called MAIN **
            git checkout -b feature-branch

    3. Commit your changes
        git add .
        git commit -m "Add new feature"

    4. Push to your branch
        git push origin feature-branch
    
    5. Create a pull request on GitHub

