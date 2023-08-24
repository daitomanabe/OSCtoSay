
# OSCtoSay

## Description
`OSCtoSay` is a simple Python script that sets up an OSC (Open Sound Control) server to listen for incoming OSC messages. When a message is received at the `/say` endpoint, the script triggers the macOS `say` command to convert text to speech.

## Requirements
- Python 3.x
- `pythonosc` library

## Usage
1. Run the script: `python3 OSCtoSay.py`
2. Send an OSC message to the server's IP address (default is `127.0.0.1`) on port `8000` with the `/say` endpoint. The message should contain two arguments: `voice` (the voice to be used for text-to-speech) and `text` (the text to be spoken).

## Example
To make the macOS `say` command speak the text "Hello, world!" with the "Alex" voice, send the following OSC message:
```
/say Alex "Hello, world!"
```
