from pypresence import Presence
import time

"""
You need to upload your image(s) here:
https://discord.com/developers/applications/719705230941618259/rich-presence/assets
"""

client_id = ''  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time=time.time()
RPC.update(large_image="f", large_text="A game of squares",
             small_text="  ", start=start_time)
