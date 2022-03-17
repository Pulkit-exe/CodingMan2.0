import streamlit as st
from random import choice
st.set_page_config('CodingMan')
st.header('Coding Man 2.0')
st.subheader('Only 5-letter keyword included.....')
l=['false','tuple','while','break','async','await','raise','yeild','count']                       #list of 5-aplhabet keyowrds in python!
ans=choice(l)                                                                                     # the word to be found in game is selected and stored here
n=5                                                                                               #length of word since we are taking 5-letter keyword only
word='_ _ _ _ _ '                                                                                 # takes the input and update the correct letters 
w_count=0                                                                                         #win count variable
l_count=0                                                                                         #lose count variable
chances=5+4                                                                                       #technically, we are giving 5 chances to user till hangwan dies                                                                                         #chances to play
count=1                                                                                           #counter variable


display=st.empty()                                                                                #for displaying the word variable

alpha=[]                                                                                          #for making list which stores inputs
for i in range(10):
    alpha.append('')


def win_meter(letter,ans):
    global w_count
    global l_count
    
    if letter in ans:
        w_count+=1
    else:
        l_count+=1

    if w_count==5:
        st.balloons()

def update(letter,word,ans):
    letter=letter.lower()
    word=word.split()

    for i in range(n):
        if ans[i]==letter:
            word[i]=letter
    word1=''
    for i in word:
        word1+=i
    word=word1
    display.markdown( f"<h1 style='text-align: center; color: white;'>{word}</h1>", unsafe_allow_html=True)
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

def main(m):
    count+=1
    word = update(alpha[m],word,ans)
    win_meter(alpha[m],ans)

t6.image('hangmanpics/1.jpg')


alpha[0]=t1.text_input('Enter a letter:',max_chars=1)

# cannot use looping construct here because of the inability to update variable names within loops..
if alpha[0]:
    main(0)
    alpha[1]=t2.text_input('Enter a letter:',max_chars=1)

    if alpha[1]:
        main(1)
        alpha[2]=t3.text_input('Enter a letter:',max_chars=1)

        if alpha[2] and w_count!=5:
            main(2)
            alpha[3]=t4.text_input('Enter a letter:',max_chars=1)

            if alpha[3] and w_count!=5:
                main(3)
                alpha[4]=t5.text_input('Enter a letter:',max_chars=1)

                if alpha[4] and w_count!=5 and count!=chances and l_count!=4:
                    main(4)
                    alpha[5]=t1.text_input('Enter a letter:',max_chars=1)

                    if alpha[5] and w_count!=5 and count!=chances and l_count!=4:
                        main(5)
                        alpha[6]=t2.text_input('Enter a letter:',max_chars=1)

                        if alpha[6] and w_count!=5 and count!=chances and l_count!=4:
                            main(6)
                            alpha[7]=t3.text_input('Enter a letter:',max_chars=1)

                            if alpha[7] and w_count!=5 and count!=chances and l_count!=4:
                                main(7)
                                alpha[8]=t4.text_input('Enter a letter:',max_chars=1)

                                if alpha[8] and w_count!=5 and count!=chances and l_count!=4:
                                    main(8)
                                    alpha[9]=t5.text_input('Enter a letter:',max_chars=1)

                                    if alpha[9] and w_count!=5 and count!=chances and l_count!=4:
                                        main(9)
                                        alpha[10]=t1.text_input('Enter a letter:',max_chars=1)


if l_count == 1:
    t6.image('hangmanpics/2.jpg')
elif l_count == 2:
    t6.image('hangmanpics/3.jpg')
elif l_count == 3:
    t6.image('hangmanpics/4.jpg')
elif l_count == 4:
    t6.image('hangmanpics/5.jpg')
    st.write('U lose :(')






