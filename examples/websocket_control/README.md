# Example PicoWebsocket
## Intro 
This example is idea when you would like to run multiple scripts via a command line 
interface **without** re-opening the PicoScope on each run.

## Setup
1. Run example_websocket.py using `python websocket.py`. 
2. In cmd use run.bat followed by arguments e.g. `run siggen -f 10000 -a 0.8`
3. Once complete, run `run close` to close the server.