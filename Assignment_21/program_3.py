import threading
import time

shared_counter = 0
counter_lock = threading.Lock()

def update_counter():
    global shared_counter
    
    with counter_lock:
        current_value = shared_counter
        time.sleep(0.1)
        shared_counter = current_value + 1

def main():
    threads = []
    for _ in range(5):
        t = threading.Thread(target=update_counter)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value: {shared_counter}") 

if __name__ == "__main__":
    main()