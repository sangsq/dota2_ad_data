from funcs import *
import time

num = read_seq_num()
wait = 1.5
rest = 10
max_fail = 10

while True:
    fail = 0
    while True:
        try:
            while True:
                s = fetch_ad_games_by_sequence_number(num)
                print(s)
                num -= 100
                time.sleep(wait)
                fail = 0
        except:
            save_seq_num(num+100)
            fail += 1
        
        if fail < max_fail:
            print("rest...")
            time.sleep(rest)
        else:
            break
    time.sleep(1800)