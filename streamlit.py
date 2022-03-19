import streamlit as st
from random import choice
st.set_page_config('CodingMan')
st.header('Coding Man 2.0')
st.subheader('Only 5-letter keyword included.....')
l=['false','tuple','while','break','async','await','raise','yeild','count']                       #list of 5-aplhabet keyowrds in python!
ans=choice(l)                                                                                     #the word to be found in game is selected and stored here
n=len(ans)                                                                                        #length of word since we are taking 5-letter keyword only
word='_ _ _ _ _ '                                                                                 #takes the input and update the correct letters 
w_count=0                                                                                         #win count variable
l_count=0                                                                                         #lose count variable
chances=n+4                                                                                       #technically, we are giving 5 chances to user till hangwan dies                                                                                         #chances to play
count=1                                                                                           #counter variable


display=st.empty()                                                                                #for displaying the word variable
display.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)
alpha=['','','','','','','','','','','','','','','']                                              #for making list which stores inputs



def win_meter(letter,ans):
    global w_count
    global l_count
    if letter in ans:
        w_count+=1
    else:
        l_count+=1

    if w_count==len(ans):
        st.balloons()

def update(letter,word,ans):
    letter=letter.lower()
    word=list(word)

    for i in range(n):
        if ans[i]==letter:
            word[2*i]=letter
    
    new=''
    word=new.join(word)
    display.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)
    return word


tab=st.columns(6)                                                                                 #5 columns for input and 1 for hangman pics
with tab[0]:
    t1 = st.container()
with tab[1]:
    t2 = st.container()
with tab[2]:
    t3 = st.container()
with tab[3]:
    t4 = st.container()
with tab[4]:
    t5 = st.container()
with tab[5]:
    t6=st.empty()


t6.image('hangmanpics/1.jpg')


win_meter('l',ans)
st.write(f'{w_count}')
st.write(f'{l_count}')

update('l',word,ans)




if l_count == 1:
    t6.image('hangmanpics/2.jpg')
elif l_count == 2:
    t6.image('hangmanpics/3.jpg')
elif l_count == 3:
    t6.image('hangmanpics/4.jpg')
elif l_count == 4:
    t6.image('hangmanpics/5.jpeg')






