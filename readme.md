
# [Perfect Parking](https://github.com/Rhys-LIT/perfect-parking-fyp/)

Perfect Parking aims to create a parking system that will replace outdated systems and help stop the widespread problem that is parking in our cities. The goal of this project is to improve the effectiveness of finding parking spaces and to also relieve the stress of the users looking for parking by implementing new and innovative features. This will be done by building a client-server API and website that will show the user exactly where the parking is. The server will be supported by parking monitor clients powered by OpenCV to detect if a parking spot has been filled or made empty. To read more, please see the [thesis](./docs/thesis.pdf).

## Requirements

- [Python 3.9](https://www.python.org/downloads/) - Python is a programming language that lets you work quickly and integrate systems more effectively.

### IDEs

- [VS Code](https://code.visualstudio.com/) - Code editing.Redefined. Free. Built on open source. Runs everywhere.[^vs-code]

[^vs-code]: The Extensions recommended for this project are in [extensions.json](./.vscode/extensions.json)

### Source Code Management

- [Git](https://git-scm.com/) is a free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- [GitHub](https://www.github.com) is a web-based hosting service for version control using Git. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its features.
- [GitHub Desktop](https://desktop.github.com/) - Simple collaboration from your desktop
- [WinMerge](https://winmerge.org/) is an Open Source differencing and merging tool for Windows.

## Run Application

Clone the repository

```bash
git clone https://github.com/Rhys-LIT/perfect-parking-fyp.git
```

There are three applications in this project: the website server, a client parking monitor and a mock client parking monitor.

### Website Server

1. Install dependencies
    - With Pip (To fast execute, run on Windows [pip-install.bat](./pip-install.bat))

        ```bash
        pip install -r requirements.txt
        ```

    - With conda (To fast execute, run on Windows [conda-install.bat](./conda-install.bat))

        ```bash
        conda install --file requirements.txt
        ```

2. Run the app
    Open VS Code and run the app by selecting the `Run and Debug` (`Ctrl + Shift + D`) tab and selecting `Server - Django` from the dropdown menu. Then click the green play button to run the app, or
    Open a terminal and run the following command:

    ```bash
    python manage.py runserver
    ```

3. Open the app in your browser
    <http://localhost:8000>

#### Built-in User Accounts

Built-in user accounts are:

| Username       | Password  | Role  | Note                             |
|----------------|-----------|-------|----------------------------------|
| admin          | admin     | admin | Built in admin account           |
| admin1         | letmein   | admin | Built in admin account           |
| parkingMonitor | Letmein1$ | user  | Account for parking monitor apps |

### Client Parking Monitor

For the client parking monitor to run, the server must be running.

1. Install dependencies
    - With Pip (To fast execute, run on Windows [PerfectParkingClient/pip-install.bat](./PerfectParkingClient/pip-install.bat))

        ```bash
        pip install -r PerfectParkingClient/requirements.txt
        ```

    - With conda (To fast execute, run on Windows [PerfectParkingClient/conda-install.bat](./PerfectParkingClient/conda-install.bat))

        ```bash
        conda install --file PerfectParkingClient/requirements.txt
        ```

2. The server must be running
3. Open VS Code and run the app by selecting the `Run and Debug` (`Ctrl + Shift + D`) tab and selecting `Client - ParkingLot` from the dropdown menu. Then click the green play button to run the app, or
    Open a terminal and run the following command:

    ```bash
    python PerfectParkingClient/main.py '--data' 'PerfectParkingClient/data/coordinates_1.yml' '--video' 'PerfectParkingClient/videos/parking_lot_1.mp4' '--start-frame' '400'
    ```

4. You can stop the client by pressing `q` at any time.

### Mock Client Parking Monitor

The mock client parking monitor is used to test the server without the need for a client parking monitor.  It loads the configs for five parking monitors and sends randomly generated data to the server at random times.

For the mock client parking monitor to run, the server must be running. The mock client dependencies are the same as the client parking monitor.

To run the mock client parking monitor, Open VS Code and run the app by selecting the `Run and Debug` (`Ctrl + Shift + D`) tab and selecting `Mock Client - ParkingLot` from the dropdown menu. Then click the green play button to run the app, or

Open a terminal and run the following command:

```bash
python PerfectParkingClient/mock.py
```

You can stop the mock client by pressing `q` at any time.

---
Copyright &copy; 2023, [Rhys Quilter](https://github.com/rhys-lit)
