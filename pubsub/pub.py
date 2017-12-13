import redis
import random
import time


def main():
    r = redis.client.StrictRedis()
    while True:
        participants = ['KATY PERRY','Justin Bieber','Taylor Swift','Rihanna','The Countess','Justin Timberlake',
                       'Ellen DeGeneres','Britney Spears','Cristiano Ronaldo','Kim Kardashian West','Shakira',
                       'Selena Gomez','Jennifer Lopez','Ariana Grande','Demi Lovato','Jimmy Fallon','Oprah Winfrey',
                       'P!nk','Drizzy','Harry Styles.','One Direction','Bill Gates','LeBron James','Lil Wayne WEEZY F',
                       'Bruno Mars','Kaka','Adele','Niall Horan','Miley Ray Cyrus','Alicia Keys','Kevin Hart','Cameron',
                       'Pitbull','Liam','Louis Tomlinson','NICKI MINAJ','Neymar Jr','Marshall Mathers','Emma Watson',
                       'Avril Lavigne','Neil Patrick Harris','daniel tosh','David Guetta','Amitabh Bachchan',
                       'Ashton kutcher','Kourtney Kardashian','zayn','Shah Rukh Khan','Coldplay','Mariah Carey',
                       'Ed Sheeran','Christina Aguilera','Jim Carrey','KANYE WEST','Chris Brown','Aamir Khan',
                       'Salman Khan','AGNEZ MO','Blake Shelton','Ryan Seacrest']
        meats = ['Bear','Beef','Beef heart','Beef liver','Beef tongue','Bison','Calf liver','Caribou','Goat','Ham',
                   'Horse','Kangaroo','Lamb','Marrow soup','Moose','Mutton','Opossum','Organ Meats','Pork','Bacon',
                   'Rabbit','Snake','Squirrel','Sweetbreads','Tripe','Turtle','Veal','Venison','Chicken',
                   'Chicken Liver','Cornish Game Hen','Duck','Duck Liver','Emu','Gizzards','Goose','Goose Liver',
                   'Grouse','Guinea Hen','Liver','Organs','Ostrich','Partridge','Pheasant','Quail','Squab','Turkey']


        send = 'Sending %s chewing %s' % (random.choice(participants), random.choice(meats))
        print send
        r.publish('celebrity:meats', send)
        time.sleep(1)


if __name__ == '__main__':
    main()
