import random
import tkinter as tk

# Step 1: Create and store affirmations
affirmations = [

    
    "Keep your friends close, but your enemies closer. - The Godfather Part II",
    "Do, or do not. There is no try. - Star Wars: The Empire Strikes Back",
    "It`s a hard pill to swallow, but yes, some people are just born lucky. The coincidences for luck are just too frequent for them. - Ellven Derananta",
    "Perhaps I deserve nice things because I am paying for sins I don't remember. - Nazilah Achmad",
    "You matter - Chelsea Sergius",
    "Because my future needs me, not my yesterday. -Sherlyn ",
    "I guess for you I wouldn't mind being a hostel untill you found your home",
    "If you live everyday as if it is your last, One day you will be right. - Steve Jobs",
    "The greatest glory in living lies not in the never falling, but in rising every time we fall. - Nelson Mandela",
    "If you cannot decide, the answer is no, - Naval Ravikant",
    "No man ever steps in the same river twice, for it is not the same river and he is not the same man. - Heraclitus",
    "One day you will wake up and there won't be any more time to do things you've always wanted. Do it now. - Paulo Coelho",
    "Somewhere between try harder and why bother",
    "There's no place like home. - The Wizard of Oz",
    "Good morning, and in case I don't see ya, good afternoon, good evening, and good night! - Jim Carrey",
    "Carpe diem. Seize the day, boys. Make your lives extraordinary. - Dead Poets Society",
    "The eyes chico,they never lie - Tony Montana",
    "Just keep swimming. - Finding Nemo",
    "To infinity and beyond! - Toy Story",
    "You is kind. You is smart. You is important. - The Help",
    "I'm the king of the world! - Titanic",
    "Why so serious? - The Dark Knight",
    "The flower that blooms in adversity is the most rare and beautiful of all. - Mulan",
    "Life is like a box of chocolates. You never know what you're gonna get. - Forrest Gump",
    "Hakuna Matata. It means no worries. - The Lion King",
    "You're gonna need a bigger boat. - Jaws",
    "The only limit is the sky",
    "With great power comes great responsibility. - Spider-Man",
    "The force will be with you, always. - Star Wars",
    "How wonderful it is to have something that makes it so hard to say goodbye. - Winnie the Pooh",
    "I'll be back. - The Terminator",
    "It's a beautiful day to save lives. - Grey's Anatomy",
    "Keep moving forward. - Meet the Robinsons",
    "Death is nothing, but to live without victory and glory is to die every day ",
    "The stuff that dreams are made of. - The Maltese Falcon",
    "You have to do the best with what God gave you. - Forrest Gump",
    "After all, tomorrow is another day! - Gone with the Wind",
    "Wake up! Maybe you’ll actually become a millionaire today",
    "The greatest thing you'll ever learn is just to love and be loved in return. - Moulin Rouge!",
    "You're only supposed to blow the bloody doors off! - The Italian Job",
    "What we do in life echoes in eternity. - Gladiator",
    "To love and be loved is to feel the sun from both sides.- David Viscott",
    "Every man dies, but not every man really lives. - Braveheart",
    "If there ever comes a day when you feel like you’ve lost you, you probably haven't",
    "Magic Mirror on the wall, who is the fairest one of all? - Snow White and the Seven Dwarfs",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "You had me at ‘hello.’ - Jerry Maguire",
    "A boy's best friend is his mother. - Psycho",
    "In the end, only three things matter: how much you loved, how gently you lived, and how gracefully you let go of things not meant for you.- Buddha",
    "Keep your face always toward the sunshine - and shadows will fall behind you. - Walt Whitman",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart- Helen Keller",
    "I'm sad but I smile. That's my life",
    "That's what she said. - Michael Scott, The Office",
    "Winter is coming. - Ned Stark, Game of Thrones",
    "How you doin'? - Joey Tribbiani, Friends",
    "Remember, metal must burn before it becomes a blade - Death Stroke",
    "I'm starting with the man in the mirror. - Michael Jackson",
    "I will always love you. - Whitney Houston, I Will Always Love You",
    "Don't stop believin'. - Journey, Don't Stop Believin'",
    "You can't always get what you want. - The Rolling Stones, You Can't Always Get What You Want",
    "It's like rain on your wedding day. - Alanis Morissette, Ironic ",
    "A good dancer must know when to leave the stage",
    "Oh, bother. - Winnie the Pooh " ,
    "You are forever gonna say 'I got this' with tears in your eyes",
    "In three words I can sum up everything I've learned about life: It goes on. - Robert Frost",
    "I have a dream. - Martin Luther King Jr.",
    "Float like a butterfly, sting like a bee. - Muhammad Ali",
    "Above all, try ",
    "On the train ride,we switched seats. You wanted to look outside and I wanted to look outside",
    "Viva La Vida! - Long Live Life",
    "Ad Meliora - Towards better things",
    "Acta non verba - actions not words",
    "Crasses Noster - Tomorrow, be Ours",
    "Age Quod Agis - do well, whatever you do",
    "Unless someone has lived your life,no one has the right to say anything about it. Whether you survive like a coackroach or like an emperor, We have to survive",
    "To die would be an awfully big adventure",
    "To whom do I owe the biggest apoloy, nobody has been crueler to me than i have been to myself",
    "Look at you, comforting others with words you wished to hear yourself",
    "My lover's got humour, she's the giggle at a funeral - Hozier",
    "Excuses don't win championships - Harvey Spector",
    "There's nothing noble about being poor",
    "Heaven can wait we are only watching the skies- Alphaville",
    "The mystery of humann existence lies not in just staying alive , but in finding something to live for",
    "Do not underestimate the allure of darkness Stefan, even the purest of hearts are drawn to it - Klaus Michaelson",
    "I am too young and I have loved too much",
    "Your worst sin is that you have destroyed and betrayed yourself for nothing",
    "Well, if God does not exist,who is laughing at us? - Dostoyevsky",
    "When a child is punished for their honesty, they begin to lie",
    "Be yourself; everyone else is already taken. - Oscar Wilde" 
]
    

   


# Step 2: Display a random affirmation
def get_random_affirmation():
    return random.choice(affirmations)

# Step 3: Main function to set up the UI
def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Affirmations App")
    root.geometry("400x400")
    root.config(bg="orange")

    # Step 5: Display affirmation by creating a label first
    affirmation_label = tk.Label(root, text="Welcome to the Affirmations and Quotes App!", font=("Times New Roman", 40), bg="orange", fg="black", wraplength=900)
    affirmation_label.pack(pady=20)

   


    # Step 4: Function to refresh the displayed affirmation
    def refresh_affirmation():
        affirmation_label.config(text=get_random_affirmation())

    # Step 5: Add a refresh button
    refresh_button = tk.Button(root, text="Refresh", command=refresh_affirmation)
    refresh_button.pack()

    # Step 6: Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()







    