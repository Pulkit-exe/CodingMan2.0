
   
import streamlit as st


st.set_page_config("CodingMan")
l_count = 0 #for tracking wrong inputs
w_count = 0 #for tracking right inputs

def win_check(letter, text):
    global l_count
    global w_count
    if letter not in text:
        l_count += 1
    else:
        w_count+= 1

    if w_count == len(text):
        st.balloons()
        st.write('You Win!!!!')


def update(letter, word, text):
   text = list(text)
   word = list(word)
   letter = letter.lower()

   for i in range(len(text)):      
      if text[i] == letter:
         word[2*i] = letter

   new = ""
   for i in word:
      new+=i
   word=new

   display.markdown( f"<h1 style='text-align: left; color: green;'>{word}</h1>", unsafe_allow_html=True)
   return word
st.header('CodingMan2.0')
st.subheader('By: Pulkit Rustagi :D')

display = st.empty() #for displaying the word

col = st.columns(2)  #4 columns for input and 1 column for hangman in desktop version, this site is not responsive

with col[0]:
    t1 = st.container()

with col[1]:
    t5 = st.empty()


                                            
ans='raise'
word = "_ _ _ _ _ "  
count = 1                              #for counting the input
letters = ['','','','','','','','','','']                                            #for storing inputs

display.markdown( f"<h1 style='text-align: left; color: cyan;'>{word}</h1>", unsafe_allow_html=True)



chances = len(ans) + 4       #4 wrong attempts are acceptable

t5.image('hangmanpics/1.jpg')


letters[0] = t1.text_input(f"Enter a letter:", max_chars = 1, key = 1 )
if letters[0] and count!=chances and l_count!=4 and w_count!=len(ans):
        win_check(letters[0],ans)
        l=update(letters[0],word,ans)             #l stands for latent-word, it is used here to initiate looping sequence
        letters[1]=t1.text_input(f'Enter a letter:', max_chars=1, key=2)
j=1
k=2
while True:
    if letters[j] and count!=chances and l_count!=4 and w_count!=len(ans):
        win_check(letters[j],ans)
        l=update(letters[j],l,ans)
        j+=1
        k+=1
        count+=1
        letters[j]=t1.text_input(f'Enter a letter:', max_chars=1, key=k)
    else:
        break



                                    

if l_count == 1:
    t5.image('hangmanpics/2.jpg')
elif l_count == 2:
    t5.image('hangmanpics/3.jpg')
elif l_count == 3:
    t5.image('hangmanpics/4.jpg')
elif l_count == 4:
    t5.image('hangmanpics/5.jpg')





