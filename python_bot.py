from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

questions = [
    {
        "question": "1. What is the primary focus of articulatory phonetics?",
        "options": ["A) Sound waves", "B) Speech perception", "C) How speech sounds are produced",
                    "D) Sound frequencies"],
        "answer": "C) How speech sounds are produced"
    },
    {
        "question": "2. Which term refers to the smallest unit of sound that can distinguish meaning?",
        "options": ["A) ASyllable", "B) Morpheme", "C) Phoneme", "D) Allophone"],
        "answer": "C) Phoneme"
    },
    {
        "question": "3. In the word 'pit' and 'bit', the difference in the initial sound is based on:",
        "options": ["A) Manner of articulation", "B) Voicing", "C) Place of articulation", "D) Nasality"],
        "answer": "B) Voicing"
    },
    {
        "question": "4. Which organ is not directly involved in the production of speech sounds?",
        "options": ["A) Tongue", "B) Lungs", "C) Heart", "D) Vocal cords"],
        "answer": "C) Heart"
    },
    {
        "question": "5. Which of the following symbols represents a voiced bilabial stop?",
        "options": ["A) /b/", "B) /p/", "C) /m/", "D) /v/"],
        "answer": "A) /b/"
    },
    {
        "question": "6. IPA stands for:",
        "options": ["A) International Phonetic Alphabet", "B) International Phonological Association",
                    "C) Intercontinental Pronunciation Agency", "D) International Pronunciation Alphabet"],
        "answer": "A) International Phonetic Alphabet"
    },
    {
        "question": "7. What is an allophone?",
        "options": ["A) A different letter for the same word",
                    "B) A variation of a phoneme that does not change meaning", "C) A stress pattern",
                    "D) A type of vowel"],
        "answer": "C) A variation of a phoneme that does not change meaning"
    },
    {
        "question": "8. What does 'place of articulation' describe?",
        "options": ["A) The speed of speech", "B) Where in the mouth a sound is produced",
                    "Whether the sound is voiced", "The loudness of a sound"],
        "answer": "Where in the mouth a sound is produced"
    },
    {
        "question": "9. Which of the following is a nasal consonant?",
        "options": ["A) /s/", "B) /b/", "C) /n/", "D) /t/"],
        "answer": "C) /n/"
    },
    {
        "question": "10. Which pair of sounds differs by manner of articulation?",
        "options": ["A) /s/ and /z/", "B) /p/ and /b/", "C) /t/ and /n/", "D) /f/ and /v/"],
        "answer": "C) /t/ and /n/"
    },
    {
        "question": "11. Which branch of phonetics deals with the physical properties of sounds?",
        "options": ["A) Articulatory phonetics", "B) Acoustic phonetics", "C) Auditory phonetics",
                    "D) Experimental phonetics"],
        "answer": "A) Acoustic phonetics"
    },
    {
        "question": "12. The term voiced indicates that the sound is:",
        "options": ["A) Whispered", "B) Produced with vibration of vocal cords", "C) Silent",
                    "D) Produced with airflow only"],
        "answer": "B) Produced with vibration of vocal cords"
    },
    {
        "question": "13. Which of the following is a high front unrounded vowel?",
        "options": ["A) /uː/", "B) /iː/", "C) /ɔː/", "D) /æ/"],
        "answer": "B) /iː/"
    },
    {
        "question": "14. What is phonology primarily concerned with?",
        "options": ["A) The study of sound patterns in language", "B) Speech disorders", "C) Sound recording",
                    "D) Hearing loss"],
        "answer": "A) The study of sound patterns in language"
    },
    {
        "question": "15. Which sound is produced with complete closure followed by a sudden release?",
        "options": ["A) Fricative", "B) Stop", "C) Nasal", "D) Glide"],
        "answer": "B) Stop"
    },
    {
        "question": "16. Which sound is a voiceless alveolar fricative?",
        "options": ["A) /z/", "B) /s/", "C) /f/", "D) /θ/"],
        "answer": "B) /s/"
    },
    {
        "question": "17. Which of the following is not a suprasegmental feature?",
        "options": ["A) Stress", "B) Pitch", "C) Intonation", "D) Nasality"],
        "answer": "D) Nasality"
    },
    {
        "question": "18. The term 'phonotactics' refers to:",
        "options": ["A) How sounds are transcribed", "B) Rules for sound combinations in a language",
                    "C) Sound perception", "D) Stress placement"],
        "answer": "B) Rules for sound combinations in a language"
    },
    {
        "question": "19. A minimal pair is:",
        "options": ["A) Two words with the same meaning", "B) Words differing by one sound", "C) Two identical words",
                    "D) Two words with different spelling"],
        "answer": "B) Words differing by one sound"
    },
    {
        "question": "20. The English sound /ʧ/ is:",
        "options": ["A) Voiced alveolar stop", "B) Voiceless palato-alveolar affricate", "C) Voiced bilabial stop",
                    "D) Voiced velar nasal"],
        "answer": "B) Voiceless palato-alveolar affricate"
    },
    {
        "question": "21. What is the correct IPA symbol for the sound at the beginning of the word 'ship'?",
        "options": ["A) /ʃ/", "B) /s/", "C) /z/", "D) /ʒ/"],
        "answer": "A) /ʃ/"
    },
    {
        "question": "22. Which of the following is a diphthong in English?",
        "options": ["A) /æ/", "B) /uː/", "C) /aɪ/", "D) /ɪ/"],
        "answer": "C) /aɪ/"
    },
    {
        "question": "23. Which of the following describes a sound produced with the soft palate raised?",
        "options": ["A) Nasal", "B) Oral", "C) Glottal", "D) Pharyngeal"],
        "answer": "B) Oral"
    },
    {
        "question": "24. In English, aspiration occurs in which environment?",
        "options": ["A) Voiced stops in final position", "B) Voiceless stops at the beginning of stressed syllables",
                    "C) Nasals before vowels", "D) After fricatives"],
        "answer": "B) Voiceless stops at the beginning of stressed syllables"
    },
    {
        "question": "25. Which is true of the vowel /æ/?",
        "options": ["A) It is a high front vowel", "B) It is a central vowel", "C) It is a low front unrounded vowel",
                    "D) It is a back rounded vowel"],
        "answer": "C) It is a low front unrounded vowel"
    },
    {
        "question": "26. A syllable must contain:",
        "options": ["A) A consonant", "B) A vowel or syllabic consonant", "C) A diphthong", "D) An affricate"],
        "answer": "B) A vowel or syllabic consonant"
    },
    {
        "question": "27. Which word contains a velar consonant?",
        "options": ["A) Man", "B) Gap", "C) Sit", "D) Tap"],
        "answer": "B) Gap"
    },
    {
        "question": "28. Which process changes the pronunciation of a sound based on its neighbors?",
        "options": ["A) Elision", "B) Intonation", "C) Assimilation", "D) Stress"],
        "answer": "C) Assimilation"
    },
    {
        "question": "29. What is the primary purpose of the IPA?",
        "options": ["A) Teach writing systems", "B) Represent speech sounds accurately", "C) Classify languages",
                    "D) Identify grammatical patterns"],
        "answer": "B) Represent speech sounds accurately"
    },
    {
        "question": "30. What kind of sound is /w/?",
        "options": ["A) Fricative", "B) Stop", "C) Glide (semivowel)", "D) Nasal"],
        "answer": "C) Glide (semivowel)"
    },
    {
        "question": "31. The phoneme /ʤ/ is classified as:",
        "options": ["A) Voiceless fricative", "B) Voiced affricate", "C) Voiceless stop", "D) Nasal"],
        "answer": "B) Voiced affricate"
    },
    {
        "question": "32. Which symbol represents a voiceless glottal fricative?",
        "options": ["A) /g/", "B) /x/", "C) /h/", "D) /ʔ/"],
        "answer": "C) /h/"
    },
    {
        "question": "33. In which word is the final sound a lateral approximant?",
        "options": ["A) Ship", "B) Ball", "C) Cab", "D) Jog"],
        "answer": "B) Ball"
    },
    {
        "question": "34. Which of the following is a manner of articulation?",
        "options": ["A) Alveolar", "B) Bilabial", "C) Fricative", "D) Velar"],
        "answer": "C) Fricative"
    },
    {
        "question": "35. What is the term for adding a sound within a word (e.g., 'ath-e-lete')?",
        "options": ["A) Deletion", "B) Epenthesis", "C) Assimilation", "D) Elision"],
        "answer": "B) Epenthesis"
    },
    {
        "question": "36. The sound /ŋ/ is typically found:",
        "options": ["A) At the beginning of words", "B) Only in vowels", "C) In word-final position",
                    "D) In the middle of diphthongs"],
        "answer": "C) In word-final position"
    },
    {
        "question": "37. In 'cat' and 'cut,' the contrast in vowels is due to:",
        "options": ["A) Length", "B) Stress", "C) Quality", "D) Nasality"],
        "answer": "C) Quality"
    },
    {
        "question": "38. Which one is a mid-central vowel?",
        "options": ["A) /e/", "B) /iː/", "C) /ə/", "D) /uː/"],
        "answer": "A) /ə/"
    },
    {
        "question": "39. Which feature is typically analyzed in prosodic phonology?",
        "options": ["A) Voicing", "Place of articulation", "C) Stress and intonation", "D) Stop vs. fricative"],
        "answer": "C) Stress and intonation"
    },
    {
        "question": "40. What is a syllabic consonant?",
        "options": ["A) A consonant that starts a syllable", "B) A consonant that forms the nucleus of a syllable",
                    "C) A double consonant", "D) A voiced stop"],
        "answer": "B) A consonant that forms the nucleus of a syllable"
    }
]

user_progress = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Boshlash", callback_data='start_test')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user_id = update.effective_user.id
    user_progress[user_id] = 0
    await update.message.reply_text("Salom! Testni boshlash uchun quyidagi tugmani bosing:", reply_markup=reply_markup)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    index = user_progress.get(user_id, 0)
    if index >= len(questions):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Test tugadi! Rahmat.")
        return
    q = questions[index]
    buttons = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in q["options"]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=q["question"], reply_markup=reply_markup)

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    index = user_progress.get(user_id, 0)

    if query.data == 'start_test':
        await send_question(update, context)
        return

    selected = query.data
    correct = questions[index]["answer"]
    if selected == correct:
        reply = "✅ To‘g‘ri! 🎉"
    else:
        reply = f"❌ Noto‘g‘ri. To‘g‘ri javob: {correct}"

    await query.edit_message_text(text=f"{questions[index]['question']}\n\nSiz tanladingiz: {selected}\n{reply}")

    user_progress[user_id] = index + 1
    await send_question(update, context)

def main():
    app = ApplicationBuilder().token("8061266773:AAEKneALpb18B01bKlwqhbCFKSv7x38mGt8").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_answer))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
