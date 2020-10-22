# Stack Overflow Chatbot

- This project was the part of a course from Coursera named: **National Researh University Higher School of economics**

> [Link to the Course](https://www.coursera.org/learn/language-processing)

- In this project I have built a chatbot that uses the intent recognition, pre-trained chatbot for twitter and a tag classifier for Stack Overflow question answer system.

- This Chat bot was trained on the stack overflow data set where I used a previously trained model for classifying the questions into various programming languages tags.

## File Structure

```
.
├── README.md
├── chatbot -> Folder is created when chatterbot is set up for the first time. (not uploaded here)
├── thread_embeddings_by_tags -> to save the embeddings for particular tags. (not uploaded because of the size)
├── ChatBot.ipynb -> Is this notebook one can use to train the following required files
├── dialogue_manager.py -> Handles the Dialogues using Chatterbot
├── main_bot.py -> main file for the bot, this should be running for the bot to work on telegram
├── test.py
├── utils.py
├── intent_recognizer.pkl
├── mdl.tsv -> Trained model (not included due to file size)
├── sentence_tokenizer.pkl
├── tag_classifier.pkl
├── tagged_posts.tsv (not included due to file size)
└── tfidf_vectorizer.pkl
```

<br>

## Tech Stack

- Python
- Tensorflow
- nltk
- sklearn
- numpy
- pandas

### How to host?

> We are going to integrate the bot to [Telegram](https://telegram.org/) messenger. To do so, you will need to create a token and use it to run the bot.

- Talk to @BotFather in Telegram. The command "/newbot" will create a bot for you. You will be prompted to enter a name and a username for your bot. After that, you will be given a token.

- Run the 'Hello world' bot with the script provided for you: python3 main_bot.py --token=YOUR_TOKEN

- You can now talk to this bot in Telegram (make sure to talk via the messenger, not via your console).
