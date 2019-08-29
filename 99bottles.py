import time

bottles_of_beer = 99
first_phrase = 'bottles of beer'
preposition = 'on the wall'
second_phrase = 'take one down, pass it around'

while bottles_of_beer > 0:
    print('================')
    print(f'{bottles_of_beer} {first_phrase} {preposition}')
    print(f'{bottles_of_beer} {first_phrase}')
    print(f'{second_phrase}')
    bottles_of_beer = bottles_of_beer - 1
    if bottles_of_beer == 0:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print('Go to the store and buy some more, 99 bottles of beer on the wall!')
        print("One more time now, y'all...")
        bottles_of_beer = 99
        timer = 5
        while timer:
            mins, secs = divmod(timer, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            timer -= 1


    else:
        print(f'{bottles_of_beer} {first_phrase}')
        time.sleep(2)
