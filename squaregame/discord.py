from pypresence import Presence
import time

client_id = '719705230941618259'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time=time.time()
RPC.update(large_image="f", large_text="A game of squares",
             small_text="  ", start=start_time)
