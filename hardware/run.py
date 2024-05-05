#!/usr/bin/env python

from rfid import *

def main():
    this_id = None
    try:
        while True:
            id, text = check_for_card()
            if this_id != id:
                if id:
                    # Check if text starts with "spotify:"
                    if text and text.startswith("spotify:"):
                        print(f"Spotify link detected: {text}")
                        # Here, you can add logic to handle the Spotify link, such as playing the track
                    else:
                        print("Card detected, but no Spotify link found.")
                        # Loop until a true response from server or card is removed
                        write_ready = False
                        while id and not write_ready:
                            print("Waiting for write permission...")
                            id, _ = check_for_card()
                            ## remeber to update write_ready with the response of svelte
                        if id:  # Still the same card and permission granted
                            print("Writing new Spotify link to the card...")
                            # Add your code here to write to the card
            else:
                # same card ovewrite?
                # Loop until a true response from server or card is removed
                write_ready = False
                while id and not write_ready:
                    print("Waiting for write permission...")
                    id, current_text = check_for_card()
                    ## remeber to update write_ready with the response of svelte
                if id:  # Still the same card and permission granted
                    print("Writing new Spotify link to the card...")
                    # Add your code here to write to the card
            this_id = id # Update this_id to the last detected card
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise    
    except Exception:
        GPIO.cleanup()
        raise    

if __name__ == "__main__":
    main()