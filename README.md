## Notes

The program herein is a simple GUI application built with the __Tkinter__ library in Python.

The script displays a simple login page with fields for _email_ and _password_. The data from the form is sent to the backend and the user is authenticated and redirected to the dashboard.

The login page also contains a link to a signup page where a user can sign up for an account. The data is sent to the backend, a user is created, authenticated and redirected to the dashboard window.

## How to ?
To run this application in your local machine, you will need to have Python installed globally.<br>
Get the latest version of Python [here](https://www.python.org/downloads/).<br>

Follow these steps to run this app locally:
- Open your command prompt and navigate to your preferred directory with the command below:
    ```bash
    # Windows
    cd <mydirectory>
    ```
- Create a virtual environment with this command:
    ```bash
    python -m venv <virtual-env-name>
    ```
- Clone the repository by pasting the command below in your CMD.
    ```bash
    git clone https://github.com/brian-mwangi-kamau/GUI-login-page.git
    ```
- Install the project dependencies with:
    ```bash
    pip install -r requirements.txt
    ```
- Run the ```sign_in.py``` application with the command:
    ```bash
    python sign_in.py
    ```

A pop-up window should appear, that looks like this
### Login
![login](https://github.com/brian-mwangi-kamau/GUI-login-page/blob/development/media/image1.jpg)

### Signup
![signup](https://github.com/brian-mwangi-kamau/GUI-login-page/blob/development/media/image2.jpg)

### Dashboard
![dashboard](https://github.com/brian-mwangi-kamau/GUI-login-page/blob/development/media/image3.jpg)


Experiment with the application to explore its features thoroughly. If you find it necessary, consider setting up a REST API for testing purposes to ensure the functionality operates as expected.