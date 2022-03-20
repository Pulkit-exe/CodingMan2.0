
   
import streamlit as st

st.set_page_config( page_title = "CodingMan")
#for page title

lose = 0 #for tracking wrong inputs
win = 0 #for tracking right inputs

def win_check(letter, text):
    global lose
    global win
    if letter not in text:
        lose += 1
    else:
        win += 1

    if win == len(text):
        st.balloons()


def update(letter, word, text):
    """ This function is to update the word after every input, to be displayed"""
    text = list(text)
    word = list(word)
    letter = letter.lower()

    for i in range(len(text)):
        if text[i] == letter:
            word[2*i] = letter

    new = ""

    word = new.join(word)
    u.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)
    return word



st.markdown("<h1 style='text-align: center; color: royalblue;'>CodingMan</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Customized Hangman For Python Programmers</h3>", unsafe_allow_html=True)

u = st.empty() #for displaying the word

col = st.columns(2)  #4 columns for input and 1 column for hangman in desktop version, this site is not responsive

with col[0]:
    t1 = st.container()

with col[1]:
    t5 = st.empty()


text = "tuple"
word = "_ _ _ _ _ "
limit = 0  #for attemted permissible inputs; which I took 4 more than the length of the word
count = 1  #for counting the input
letters = ['', '', '', '', '', '','','','','','','','','',''] #for storing inputs

u.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)



limit = len(text) + 4

t5.image('hangmanpics/1.jpg')


letters[0] = t1.text_input(f"Enter a letter:", max_chars = 1, key = 1 )

j=0
k=1
while True:
    if letters[j] and count!=chances and lose!=4 and win!=len(text):
        win_meter(alpha,ans)
        update(alpha,word,ans)
        j+=1
        k+=1
        count+=1
        letters[j]=t1.text_input(f'Enter a letter:', max_chars=1, key=k)
    else:
        break



                                    

if lose == 1:
    t5.image('hangmanpics/2.jpg')
elif lose == 2:
    t5.image('hangmanpics/3.jpg')
elif lose == 3:
    t5.image('hangmanpics/4.jpg')
elif lose == 4:
    t5.image('hangmanpics/5.jpg')





