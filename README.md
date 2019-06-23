# RPC Simulation using PyGame

The project comprises server and client programs to simulate Remote Procedure Calls(RPCs). The simulation is done using a graphical environment created using PyGame package. First, the server is started and when it is running, multiple clients can connect to it. For each client running, a game window with a fish is opened. Any client can control the fish using arrow keys on the keyboard. When a key is pressed by one client, the fish moves correspondingly in all the client windows. That is, remotely the procedure for the corresponding movement is called for all the clients.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyGame.

```bash
python3 -m pip install -U pygame --user
```

## Usage

Clone the [repository](https://github.com/divyab275/MeenMutti) and start the server using
```bash
python game_server.py
```
You'll see the following output when the server is up.
```bash
Socket successfully created
Socket binded to 12345
Socket is listening
Got connection from  ('127.0.0.1', 54639)
Got connection from  ('127.0.0.1', 54641)
```
Start multiple clients using
```bash
python client.py
```
For each client, a game window will be opened and the arrow keys on the keyboard can be used to control the fish.