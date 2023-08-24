
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import subprocess
import argparse

def say_handler(unused_addr, voice, *args):
    """ Handle the OSC message to trigger the 'say' command """
    text = ' '.join(map(str, args))
    
    # Construct the command with volume and rate options if provided
    command = ["say", "-v", f"{voice}:{volume}" if volume else voice]
    if rate:
        command.extend(["-r", str(rate)])
    command.append(text)
    
    subprocess.run(command)

if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description='OSC to Say Command Server.')
    parser.add_argument('--port', type=int, default=8000, help='Port number to listen on. Default is 8000.')
    parser.add_argument('--volume', type=float, help='Volume level for the say command. Between 0 and 1.')
    parser.add_argument('--rate', type=int, help='Speaking rate for the say command. Words per minute.')
    args = parser.parse_args()

    # Extract volume and rate for use in the say_handler
    volume = args.volume
    rate = args.rate

    # OSCメッセージのディスパッチャをセットアップ
    dispatcher = Dispatcher()
    dispatcher.map("/say", say_handler)

    # OSCサーバーを起動
    server = BlockingOSCUDPServer(("127.0.0.1", args.port), dispatcher)
    print(f"Serving on {server.server_address}")
    server.serve_forever()
