from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

questions_eng1 = [
    {
        "question": "1. Which of the following is an example of a lexical expressive means?",
        "options": ["A) Hyperbole", "B) Epithet", "C) Irony", "D) Metaphor"],
        "answer": "B) Epithet"
    },
    {
        "question": "2. Which of these stylistic devices uses the substitution of one concept with another based on association?",
        "options": ["A) Simile", "B) Irony", "C) Metonymy", "D) Epithet"],
        "answer": "C) Metonymy"
    },
    {
        "question": "3. Which stylistic device is characterized by the combination of contradictory terms?",
        "options": ["A) Metaphor", "B) Oxymoron", "C) Paradox", "D) Epithet"],
        "answer": "B) Oxymoron"
    },
    {
        "question": "4. An epithet is primarily used to:",
        "options": ["A) Describe facts", "B) Exaggerate ideas", "C) Add emotional coloring to a noun",
                    "D) Create dialogues"],
        "answer": "C) Add emotional coloring to a noun"
    },
    {
        "question": "5. Which lexico-syntactical stylistic device compares two things directly?",
        "options": ["A) Metaphor", "B) Irony", "C) Simile", "D) Hyperbole"],
        "answer": "C) Simile"
    },
    {
        "question": "6. The phrase 'The White House issued a statement' is an example of:",
        "options": ["A) Metaphor", "B) Epithet", "C) Metonymy", "D) Synecdoche"],
        "answer": "C) Metonymy"
    },
    {
        "question": "7. What is the main purpose of hyperbole?",
        "options": ["A) Understatement", "B) Precision", "C) Humor", "D) Exaggeration for emphasis"],
        "answer": "D) Exaggeration for emphasis"
    },
    {
        "question": "8. Litotes is a stylistic device that uses:",
        "options": ["A) Direct expression", "B) Understatement through negation", "C) Overstatement", "D) Sarcasm"],
        "answer": "B) Understatement through negation"
    },
    {
        "question": "9. Periphrasis is used to:",
        "options": ["A) Express ideas directly", "B) Say things in an indirect or roundabout way",
                    "C) Compare two things", "D) Praise the noun"],
        "answer": "B) Say things in an indirect or roundabout way"
    },
    {
        "question": "10. Repetition in a text is primarily used to:",
        "options": ["A) Add stylistic color", "B) Understate ideas", "C) Emphasize a theme or idea",
                    "D) Complicate syntax"],
        "answer": "C) Emphasize a theme or idea"
    },
    {
        "question": "11. Which type of question is intended to prompt reflection rather than an answer?",
        "options": ["A) Literal question", "B) Closed question", "C) Negative question", "D) Rhetorical question"],
        "answer": "D) Rhetorical question"
    },
    {
        "question": "12. Which phonetic device involves the repetition of initial consonant sounds?",
        "options": ["A) Consonance", "B) Assonance", "C) Alliteration", "D) Onomatopoeia"],
        "answer": "C) Alliteration"
    },
    {
        "question": "13. Stylistic synonyms are primarily used in literature to:",
        "options": ["A) Create simplicity", "B) Reduce complexity", "C) Add nuance and variation",
                    "D) Simplify syntax"],
        "answer": "C) Add nuance and variation"
    },
    {
        "question": "14. The idiom “kick the bucket” is an example of:",
        "options": ["A) Metaphor", "B) Euphemism", "C) Irony", "D) Metonymy"],
        "answer": "B) Euphemism"
    },
    {
        "question": "15. The proverb “Actions speak louder than words” is an example of:",
        "options": ["A) Irony", "B) Metaphor", "C) Didactic expression", "D) Paradox"],
        "answer": "C) Didactic expression"
    },
    {
        "question": "16. What is the primary stylistic function of borrowings in English literature?",
        "options": ["A) Strengthen grammar", "B) Complicate structure", "C) Add foreign flavor and precision",
                    "D) Simplify expression"],
        "answer": "C) Add foreign flavor and precision"
    },
    {
        "question": "17. Which stylistic style is focused on persuading the reader and appealing to emotions?",
        "options": ["A) Belles-lettres style", "B) Academic style", "C) Oratorical style", "D) Journalistic style"],
        "answer": "C) Oratorical style"
    },
    {
        "question": "18. Which of these devices is primarily a feature of poetic style?",
        "options": ["A) Prose", "B) Academic tone", "C) Reported speech", "D) Rhyme"],
        "answer": "D) Rhyme"
    },
    {
        "question": "19. The repetition of consonant sounds in the middle or end of words is called:",
        "options": ["A) Alliteration", "B) Consonance", "C) Assonance", "D) Onomatopoeia"],
        "answer": "B) Consonance"
    },
    {
        "question": "20. Simile can best be defined as:",
        "options": ["A) Indirect comparison without indicators", "B) A direct comparison using “like” or “as”",
                    "C) Understatement by negation", "D) A vivid image"],
        "answer": "B) A direct comparison using “like” or “as”"
    },
    {
        "question": "21. Antonomasia involves:",
        "options": ["A) Repetition of sounds",
                    "B) Substitution of a proper name with a descriptive phrase or vice versa", "C) Creating paradoxes",
                    "D) Understatement"],
        "answer": "B) Substitution of a proper name with a descriptive phrase or vice versa"
    },
    {
        "question": "22. Which type of simile is implicit rather than explicitly stated?",
        "options": ["A) Direct simile", "B) Concealed simile", "C) Antonomasia", "D) Hyperbole"],
        "answer": "B) Concealed simile"
    },
    {
        "question": "23. In linguocultural studies, litotes is used to:",
        "options": ["A) Exaggerate cultural facts", "B) Show politeness or modesty through understatement",
                    "C) Make metaphors stronger", "D) Add humor"],
        "answer": "B) Show politeness or modesty through understatement"
    },
    {
        "question": "24. In literature, periphrasis can create an effect of:",
        "options": ["A) Simplicity", "B) Elevated or poetic tone", "C) Ambiguity", "D) Sarcasm"],
        "answer": "B) Elevated or poetic tone"
    },
    {
        "question": "25. What is the main purpose of rhetorical questions in literature?",
        "options": ["A) To get a direct answer", "B) To provoke thought or emphasize a point",
                    "C) To simplify language", "D) To describe actions"],
        "answer": "B) To provoke thought or emphasize a point"
    },
    {
        "question": "26. Which of these is a phonetic stylistic device?",
        "options": ["A) Metaphor", "B) Assonance", "C) Simile", "D) Irony"],
        "answer": "B) Assonance"
    },
    {
        "question": "27. What effect do stylistic synonyms add to literary speech?",
        "options": ["A) Repetition", "B) Variety and subtle shades of meaning", "C) Simplicity", "D) Irony"],
        "answer": "B) Variety and subtle shades of meaning"
    },
    {
        "question": "28. In idioms, what role does cultural context play?",
        "options": ["A) None", "B) It clarifies grammar rules", "C) It determines meaning and usage",
                    "D) It adds humor"],
        "answer": "C) It determines meaning and usage"
    },
    {
        "question": "29. Proverbs often provide:",
        "options": ["A) Confusion", "B) Moral or practical advice", "C) Detailed instructions", "D) Humor"],
        "answer": "B) Moral or practical advice"
    },
    {
        "question": "30. Borrowed words in English typically contribute:",
        "options": ["A) Complexity in spelling", "B) Precision and stylistic richness", "C) Confusion",
                    "D) Obsolete expressions"],
        "answer": "B) Precision and stylistic richness"
    },
    {
        "question": "31. Functional styles are best understood as:",
        "options": ["A) Random language choices", "B) Systematic ways language is used in specific contexts",
                    "C) Synonyms of dialects", "D) Literary genres"],
        "answer": "B) Systematic ways language is used in specific contexts"
    },
    {
        "question": "32. Which style focuses primarily on artistic expression and emotion?",
        "options": ["A) Scientific", "B) Belles-lettres", "C) Official", "D) Neutral"],
        "answer": "B) Belles-lettres"
    },
    {
        "question": "33. The poetic style in literature often includes:",
        "options": ["A) Technical language", "B) Imagery, rhythm, and sound devices", "C) Long explanations",
                    "D) Abstract terms only"],
        "answer": "B) Imagery, rhythm, and sound devices"
    },
    {
        "question": "34. The use of synonyms in a literary text helps to:",
        "options": ["A) Repeat ideas", "B) Create humor", "C) Avoid monotony and enrich meaning",
                    "D) Confuse the reader"],
        "answer": "C) Avoid monotony and enrich meaning"
    },
    {
        "question": "35. Which stylistic feature is often found in proverbs?",
        "options": ["A) Rhetorical questions", "B) Scientific terms", "C) Elliptical structure and metaphor",
                    "D) Alliteration"],
        "answer": "C) Elliptical structure and metaphor"
    },
    {
        "question": "36. The use of functional styles is aimed at:",
        "options": ["A) Entertainment only", "B) Meeting specific communicative goals", "C) Breaking grammar rules",
                    "D) Fiction writing"],
        "answer": "B) Meeting specific communicative goals"
    },
    {
        "question": "37. Which of the following is a stylistic aspect of poetry?",
        "options": ["A) Passive voice", "B) Official language", "C) Rhyme and rhythm", "D) Logical arguments"],
        "answer": "C) Rhyme and rhythm"
    },
    {
        "question": "38. An example of an idiom in English might be:",
        "options": ["A) The sun is shining", "B) Spill the beans", "C) It is raining heavily", "D) Go to school"],
        "answer": "B) Spill the beans"
    },
    {
        "question": "39. The stylistic device of periphrasis is often used to:",
        "options": ["A) State things directly", "B) Add sophistication or poetic tone", "C) Mislead readers",
                    "D) Imitate speech"],
        "answer": "B) Add sophistication or poetic tone"
    },
    {
        "question": "40. Which stylistic device is used to soften the harshness of an expression by using a more polite or indirect term?",
        "options": ["A) Metonymy", "B) Hyperbole", "C) Euphemism", "D) Pun"],
        "answer": "C) Euphemism"
    },
    {
        "question": "41. What is stylistics primarily concerned with?",
        "options": ["A) Historical development of language", "B) The study of style and expressive means in language",
                    "C) Only poetry", "D) Grammar rules"],
        "answer": "B) The study of style and expressive means in language"
    },
    {
        "question": "42. Which field is most closely related to stylistics?",
        "options": ["A) Engineering", "B) Linguistics", "C) Biology", "D) Astronomy"],
        "answer": "B) Linguistics"
    },
    {
        "question": "43. What does literary stylistics focus on?",
        "options": ["A) Dialectal variation", "B) Analysis of style in literary texts", "C) Phonetic change",
                    "D) Political speeches only"],
        "answer": "B) Analysis of style in literary texts"
    },
    {
        "question": "44. What is foregrounding in stylistics?",
        "options": ["A) Grammar simplification", "B) Making certain elements more prominent or noticeable",
                    "C) Removing unnecessary words", "D) Using slang expressions"],
        "answer": "B) Making certain elements more prominent or noticeable"
    },
    {
        "question": "45. Who is considered a pioneer in stylistics?",
        "options": ["A) William Wordsworth", "B) Roman Jakobson", "C) George Orwell", "D) Noam Chomsky"],
        "answer": "B) Roman Jakobson"
    },
    {
        "question": "46. What does the term \"deviation\" refer to in stylistics?",
        "options": ["A) Following norms strictly", "B) Breaking linguistic norms for effect", "C) Misspelling",
                    "D) Dialectal errors"],
        "answer": "B) Breaking linguistic norms for effect"
    },
    {
        "question": "47. Which is a type of stylistic foregrounding?",
        "options": ["A) Literalness", "B) Parallelism", "C) Misuse", "D) Generalization"],
        "answer": "B) Parallelism"
    },
    {
        "question": "48. Which of the following is a figure of speech often analyzed in stylistics?",
        "options": ["A) Inflection", "B) Metaphor", "C) Syllabification", "D) Sentence fragments"],
        "answer": "B) Metaphor"
    },
    {
        "question": "49. What does lexical choice involve?",
        "options": ["A) Spelling words properly", "B) Avoiding foreign words",
                    "C) Selecting words to suit style, tone, and purpose", "D) Reading aloud"],
        "answer": "C) Selecting words to suit style, tone, and purpose"
    },
    {
        "question": "50. What is metaphor an example of?",
        "options": ["A) Phonetic device", "B) Grammatical category", "C) Figurative language",
                    "D) Structural cohesion"],
        "answer": "C) Figurative language"
    },
    {
        "question": "51. What is one goal of stylistic analysis?",
        "options": ["A) Memorizing definitions", "B) Understanding how language creates meaning and effect",
                    "C) Translating texts", "D) Changing dialects"],
        "answer": "B) Understanding how language creates meaning and effect"
    },
    {
        "question": "52. What type of stylistics analyzes real-life texts?",
        "options": ["A) Literary stylistics", "B) Functional stylistics", "C) Diachronic stylistics",
                    "D) Theoretical phonetics"],
        "answer": "B) Functional stylistics"
    },
    {
        "question": "53. Which level of language does stylistics NOT ignore?",
        "options": ["A) Only phonological", "B) All levels: phonetic, lexical, syntactic, semantic",
                    "C) Only grammatical", "D) Only morphological"],
        "answer": "B) All levels: phonetic, lexical, syntactic, semantic"
    },
    {
        "question": "54. What does 'register' refer to in stylistics?",
        "options": ["A) Grammar form", "B) Dictionary definitions",
                    "C) Language variety used in a specific social situation", "D) Author's biography"],
        "answer": "C) Language variety used in a specific social situation"
    },
    {
        "question": "55. Which of the following is a stylistic device?",
        "options": ["A) Inflection", "B) Irony", "C) Verb tense", "D) Syllable count"],
        "answer": "B) Irony"
    },
    {
        "question": "56. Syntax in stylistics refers to:",
        "options": ["A) Word origins", "B) Word endings", "C) Sentence structure and arrangement",
                    "D) Rhyming patterns"],
        "answer": "C) Sentence structure and arrangement"
    },
    {
        "question": "57. In stylistics, cohesion relates to:",
        "options": ["A) Random word usage", "B) Paragraph spacing", "C) How parts of a text are logically connected",
                    "D) Sentence length"],
        "answer": "C) How parts of a text are logically connected"
    },
    {
        "question": "58. Style-shifting occurs when:",
        "options": ["A) A text is rewritten", "B) Language style changes according to context or situation",
                    "C) Words are translated", "D) Grammar rules are changed"],
        "answer": "B) Language style changes according to context or situation"
    },
    {
        "question": "59. What is irony in stylistics?",
        "options": ["A) A direct statement", "B) Saying the opposite of what is meant for effect",
                    "C) A logical argument", "D) A formal tone"],
        "answer": "B) Saying the opposite of what is meant for effect"
    },
    {
        "question": "60. Which is an element of discourse analysis?",
        "options": ["A) Rhyme", "B) Metaphor", "C) Turn-taking in conversation", "D) Spelling rules"],
        "answer": "C) Turn-taking in conversation"
    },
    {
        "question": "61. Phonostylistics studies:",
        "options": ["A) Sentence structures only", "B) Sound features and their stylistic function", "C) Word origins",
                    "D) Figurative language"],
        "answer": "B) Sound features and their stylistic function"
    },
    {
        "question": "62. What does the term 'idiolect' refer to?",
        "options": ["A) A regional dialect", "B) An individual’s unique use of language", "C) A literary genre",
                    "D) A slang expression"],
        "answer": "B) An individual’s unique use of language"
    },
    {
        "question": "63. Which genre typically uses formal register?",
        "options": ["A) Informal emails", "B) Dialogue in fiction", "C) Academic writing", "D) Personal diary entries"],
        "answer": "C) Academic writing"
    },
    {
        "question": "64. Repetition is used in stylistics to:",
        "options": ["A) Fill space in text", "B) Confuse the reader", "C) Emphasize ideas and create rhythm",
                    "D) Introduce new vocabulary"],
        "answer": "C) Emphasize ideas and create rhythm"
    },
    {
        "question": "65. Which of the following is a narrative technique?",
        "options": ["A) Hyperbole", "B) Euphemism", "C) Stream of consciousness", "D) Rhyme"],
        "answer": "C) Stream of consciousness"
    },
    {
        "question": "66. A simile is a comparison using:",
        "options": ["A) Nor or yet", "B) Like or as", "C) And or but", "D) If or then"],
        "answer": "B) Like or as"
    },
    {
        "question": "67. Connotation refers to:",
        "options": ["A) Literal meaning of a word", "B) Emotional or cultural associations with a word",
                    "C) Word spelling", "D) Root of the word"],
        "answer": "B) Emotional or cultural associations with a word"
    },
    {
        "question": "68. What is denotation?",
        "options": ["A) A figure of speech", "B) The literal, dictionary meaning of a word", "C) A poetic form",
                    "D) A type of simile"],
        "answer": "B) The literal, dictionary meaning of a word"
    },
    {
        "question": "69. Which of the following is used to create mood in literature?",
        "options": ["A) Punctuation", "B) Imagery and descriptive language", "C) Paragraph length", "D) Footnotes"],
        "answer": "B) Imagery and descriptive language"
    },
    {
        "question": "70. Stylistic variation can occur across:",
        "options": ["A) Only in poetry", "B) Genres, speakers, and contexts", "C) Grammatical rules only",
                    "D) Spelling conventions"],
        "answer": "B) Genres, speakers, and contexts"
    },
    {
        "question": "71. Which of the following is an element of poetic language?",
        "options": ["A) Thesis statement", "B) Rhythm and meter", "C) Passive voice", "D) Footnotes"],
        "answer": "B) Rhythm and meter"
    },
    {
        "question": "72. Which language function did Jakobson highlight for poetry?",
        "options": ["A) Referential", "B) Poetic", "C) Conative", "D) Metalinguistic"],
        "answer": "B) Poetic"
    },
    {
        "question": "73. Discourse is defined as:",
        "options": ["A) A word’s origin", "B) Language use in communication beyond the sentence", "C) Poetry structure",
                    "D) Grammar usage"],
        "answer": "B) Language use in communication beyond the sentence"
    },
    {
        "question": "74. Cohesion differs from coherence in that cohesion is:",
        "options": ["A) About text meaning", "B) About formal linguistic links between parts of a text",
                    "C) Reader interpretation only", "D) Related to dialect"],
        "answer": "B) About formal linguistic links between parts of a text"
    },
    {
        "question": "75. A hyperbole is:",
        "options": ["A) A polite expression", "B) A deliberate exaggeration for effect", "C) A literal statement",
                    "D) A rhyme pattern"],
        "answer": "B) A deliberate exaggeration for effect"
    },
    {
        "question": "76. Style is often influenced by:",
        "options": ["A) Only grammar rules", "B) Length of the text", "C) Context, purpose, and audience",
                    "D) Random choices"],
        "answer": "C) Context, purpose, and audience"
    },
    {
        "question": "77. Stylistics can be applied to:",
        "options": ["A) Only poetry", "B) Only formal texts", "C) Any type of text, spoken or written",
                    "D) Grammar books only"],
        "answer": "C) Any type of text, spoken or written"
    },
    {
        "question": "78. In stylistic analysis, tone refers to:",
        "options": ["A) Grammar structure", "B) The writer’s attitude or emotional coloring", "C) Phonemes",
                    "D) Figurative meaning"],
        "answer": "B) The writer’s attitude or emotional coloring"
    },
    {
        "question": "79. What is alliteration?",
        "options": ["A) Use of rhyme", "B) Repetition of initial consonant sounds", "C) Use of metaphors",
                    "D) Breaking grammar rules"],
        "answer": "B) Repetition of initial consonant sounds"
    },
    {
        "question": "80. Which term refers to polite or indirect expressions?",
        "options": ["A) Irony", "B) Hyperbole", "C) Euphemism", "D) Litotes"],
        "answer": "C) Euphemism"
    },
    {
        "question": "81. Intertextuality refers to:",
        "options": ["A) Language errors", "B) The relationship between texts and how they reference each other",
                    "C) Repetition in poetry", "D) Translation techniques"],
        "answer": "B) The relationship between texts and how they reference each other"
    },
    {
        "question": "82. Functional stylistics is concerned with:",
        "options": ["A) Figurative language only", "B) How style varies in different functional types of texts",
                    "C) Word origins", "D) Literary symbolism"],
        "answer": "B) How style varies in different functional types of texts"
    },
    {
        "question": "83. In stylistics, deixis refers to:",
        "options": ["A) Rhyming patterns", "B) Words or phrases that point to time, place, or person",
                    "C) Sentence complexity", "D) Literary plots"],
        "answer": "B) Words or phrases that point to time, place, or person"
    },
    {
        "question": "84. A rhetorical question expects:",
        "options": ["A) A factual answer", "B) A yes or no", "C) No direct answer, just reflection or emphasis",
                    "D) A written explanation"],
        "answer": "C) No direct answer, just reflection or emphasis"
    },
    {
        "question": "85. The term persona in stylistics refers to:",
        "options": ["A) A real person", "B) The fictional voice or speaker in a text", "C) The narrator’s friend",
                    "D) A type of adjective"],
        "answer": "B) The fictional voice or speaker in a text"
    },
    {
        "question": "86. Parallelism in stylistics creates:",
        "options": ["A) Confusion", "B) Balance and rhythm through repeated structures", "C) Unexpected contrasts",
                    "D) Irony"],
        "answer": "B) Balance and rhythm through repeated structures"
    },
    {
        "question": "87. A pun involves:",
        "options": ["A) Long metaphor", "B) A play on words with similar sounds but different meanings",
                    "C) Complex grammar", "D) Historical references"],
        "answer": "B) A play on words with similar sounds but different meanings"
    },
    {
        "question": "88. Discourse markers help in:",
        "options": ["A) Making rhymes", "B) Organizing speech or writing and guiding the reader/listener",
                    "C) Confusing the audience", "D) Repeating sentences"],
        "answer": "B) Organizing speech or writing and guiding the reader/listener"
    },
    {
        "question": "89. Stylistics helps readers:",
        "options": ["A) Memorize definitions", "B) Understand how language works to create meaning and effect",
                    "C) Ignore form", "D) Avoid literary texts"],
        "answer": "B) Understand how language works to create meaning and effect"
    },
    {
        "question": "90. Lexico-grammatical choices refer to:",
        "options": ["A) Foreign words", "B) Word and grammar selections that affect style", "C) Dictionary entries",
                    "D) Typography"],
        "answer": "B) Word and grammar selections that affect style"
    },
    {
        "question": "91. What does stylistics explore in advertisements?",
        "options": ["A) Brand logos", "B) Persuasive language and stylistic features", "C) Store locations",
                    "D) Product prices"],
        "answer": "B) Persuasive language and stylistic features"
    },
    {
        "question": "92. Figurative language is used to:",
        "options": ["A) Follow rules strictly", "B) Create confusion", "C) Add depth, imagery, and indirect meaning",
                    "D) Simplify content"],
        "answer": "C) Add depth, imagery, and indirect meaning"
    },
    {
        "question": "93. Ellipsis is used in stylistics to:",
        "options": ["A) Correct grammar", "B) Add more detail",
                    "C) Omit parts of a sentence for stylistic or rhetorical effect", "D) Explain metaphors"],
        "answer": "C) Omit parts of a sentence for stylistic or rhetorical effect"
    },
    {
        "question": "94. Code-switching involves:",
        "options": ["A) Switching fonts", "B) Correcting grammar",
                    "C) Alternating between languages or language varieties", "D) Removing slang"],
        "answer": "C) Alternating between languages or language varieties"
    },
    {
        "question": "95. Consonance is:",
        "options": ["A) Repetition of vowel sounds", "B) Repetition of consonant sounds at the end or middle of words",
                    "C) Grammar mistake", "D) Use of formal vocabulary"],
        "answer": "B) Repetition of consonant sounds at the end or middle of words"
    },
    {
        "question": "96. Antithesis refers to:",
        "options": ["A) Use of synonyms", "B) Juxtaposition of contrasting ideas in a balanced way", "C) Slang usage",
                    "D) Old English vocabulary"],
        "answer": "B) Juxtaposition of contrasting ideas in a balanced way"
    },
    {
        "question": "97. Stylistics in film analysis focuses on:",
        "options": ["A) Costume design", "B) Language, dialogue, tone, and narrative techniques", "C) Ticket prices",
                    "D) Studio names"],
        "answer": "B) Language, dialogue, tone, and narrative techniques"
    },
    {
        "question": "98. Which of the following is a stylistic effect?",
        "options": ["A) Using only one sentence", "B) Creating emphasis or contrast", "C) Removing verbs",
                    "D) Reading aloud"],
        "answer": "B) Creating emphasis or contrast"
    },
    {
        "question": "99. What is the purpose of stylistic features?",
        "options": ["A) To follow traditional grammar rules", "B) To enhance meaning and aesthetic value of a text",
                    "C) To confuse readers", "D) To replace vocabulary"],
        "answer": "B) To enhance meaning and aesthetic value of a text"
    },
    {
        "question": "100. What is the value of stylistics in education?",
        "options": ["A) Memorizing authors’ names", "B) Improving reading, interpretation, and language awareness",
                    "C) Learning dates in history", "D) Writing lists only"],
        "answer": "B) Improving reading, interpretation, and language awareness"
    },
]
questions_eng2 = [
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
        "answer": "B) A variation of a phoneme that does not change meaning"
    },
    {
        "question": "8. What does 'place of articulation' describe?",
        "options": ["A) The speed of speech", "B) Where in the mouth a sound is produced",
                    "C) Whether the sound is voiced", "D) The loudness of a sound"],
        "answer": "B) Where in the mouth a sound is produced"
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
        "answer": "B) Acoustic phonetics"
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
        "answer": "C) /ə/"
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
    },
    {
        "question": "41. Which sound is a voiced dental fricative?",
        "options": ["A) /θ/", "B) /ð/", "C) /f/", "D) /s/"],
        "answer": "B) /ð/"
    },
    {
        "question": "42. What term describes when two phonemes become one, as in “did you” → /dɪʤu/?",
        "options": ["A) Elision", "B) Epenthesis", "C) Coalescence", "D) Assimilation"],
        "answer": "C) Coalescence"
    },
    {
        "question": "43. The primary articulator involved in the production of /t/ is:",
        "options": ["A) Velum", "B) Lips", "C) Tongue tip", "D) Vocal folds"],
        "answer": "C) Tongue tip"
    },
    {
        "question": "44. Which term refers to the study of sound systems within a specific language?",
        "options": ["A) Phonetics", "B) Phonology", "C) Syntax", "D) Morphology"],
        "answer": "B) Phonology"
    },
    {
        "question": "45. The schwa /ə/ is typically found in:",
        "options": ["A) Emphasized syllables", "B) Unstressed syllables", "C) Word-final vowels",
                    "D) Consonant clusters"],
        "answer": "B) Unstressed syllables"
    },
    {
        "question": "46. Which of the following pairs are allophones of the same phoneme in English?",
        "options": ["A) /t/ and /d/", "B) [tʰ] and [t]", "C) /s/ and /ʃ/", "D) /i/ and /u/"],
        "answer": "B) [tʰ] and [t]"
    },
    {
        "question": "47. Which of the following is a glide (or semivowel)?",
        "options": ["A) /l/", "B) /r/", "C) /j/", "D) /ʒ/"],
        "answer": "C) /j/"
    },
    {
        "question": "48. A sound produced with turbulent airflow is known as:",
        "options": ["A) Nasal", "B) Fricative", "C) Glide", "D) Lateral"],
        "answer": "B) Fricative"
    },
    {
        "question": "49. A minimal pair demonstrates:",
        "options": ["A) Intonation differences", "B) Contrastive phonemes", "C) Suprasegmental stress",
                    "D) Allophonic variation"],
        "answer": "B) Contrastive phonemes"
    },
    {
        "question": "50. Which of the following words begins with a voiceless palato-alveolar fricative?",
        "options": ["A) Ship", "B) Zip", "C) Gym", "D) Ship"],
        "answer": "D) Ship"
    },
    {
        "question": "51. What kind of vowel is /ɔː/?",
        "options": ["A) High front", "B) Mid back rounded", "C) Low front", "D) Central unrounded"],
        "answer": "B) Mid back rounded"
    },
    {
        "question": "52. The process of weakening or omitting a sound in rapid speech is called:",
        "options": ["A) Insertion", "B) Elision", "C) Coalescence", "D) Nasalization"],
        "answer": "B) Elision"
    },
    {
        "question": "53. Which consonant is produced with both the lips and teeth?",
        "options": ["A) /p/", "B) /f/", "C) /m/", "D) /s/"],
        "answer": "B) /f/"
    },
    {
        "question": "54. What is the voiced counterpart of /s/?",
        "options": ["A) /ʃ/", "B) /z/", "C) /t/", "D) /θ/"],
        "answer": "B) /z/"
    },
    {
        "question": "55. In phonological rules, what symbol typically means 'becomes'?",
        "options": ["A) →", "B) /", "C) []", "D) →"],
        "answer": "D) →"
    },
    {
        "question": "56. In terms of voicing, which of the following is different from the others?",
        "options": ["A) /b/", "B) /d/", "C) /g/", "D) /p/"],
        "answer": "D) /p/"
    },
    {
        "question": "57. The place of articulation for /m/ is:",
        "options": ["A) Dental", "B) Bilabial", "C) Alveolar", "D) Velar"],
        "answer": "B) Bilabial"
    },
    {
        "question": "58. Which of the following is not a typical component of a syllable?",
        "options": ["A) Onset", "B) Nucleus", "C) Morpheme", "D) Coda"],
        "answer": "C) Morpheme"
    },
    {
        "question": "59. An alveolar lateral approximant is represented by:",
        "options": ["A) /r/", "B) /l/", "C) /j/", "D) /n/"],
        "answer": "B) /l/"
    },
    {
        "question": "60. What is coarticulation?",
        "options": ["A) Deletion of vowels", "B) Overlapping of speech sounds in production", "C) Changing stress",
                    "D) Syllable division"],
        "answer": "B) Overlapping of speech sounds in production"
    },
    {
        "question": "61. What feature do all nasal consonants share?",
        "options": ["Voicelessness", "Airflow through the nose", "Bilabial articulation", "Use of the glottis"],
        "answer": "Airflow through the nose"
    },
    {
        "question": "62. Which sound is a voiced palato-alveolar affricate?",
        "options": ["/ʧ/", "/ʤ/", "/ʃ/", "/z/"],
        "answer": "/ʤ/"
    },
    {
        "question": "63. The process of pronouncing a word as a single unit (e.g., “going to” → “gonna”) is:",
        "options": ["Epenthesis", "Connected speech / reduction", "Metathesis", "Stress shift"],
        "answer": "Connected speech / reduction"
    },
    {
        "question": "64. Which of the following is an example of a back vowel?",
        "options": ["/iː/", "/uː/", "/e/", "/æ/"],
        "answer": "/uː/"
    },
    {
        "question": "65. Which place of articulation involves the back of the tongue and the soft palate?",
        "options": ["Alveolar", "Velar", "Glottal", "Labiodental"],
        "answer": "Velar"
    },
    {
        "question": "66. Which vowel is represented in the word “seat”?",
        "options": ["A) /ɪ/", "B) /iː/", "C) /e/", "D) /ʌ/"],
        "answer": "B) /iː/"
    },
    {
        "question": "67. A sound made with a complete closure in the oral cavity and release is a:",
        "options": ["A) Fricative", "B) Nasal", "C) Plosive (stop)", "D) Glide"],
        "answer": "C) Plosive (stop)"
    },
    {
        "question": "68. Which symbol represents the voiced alveolar stop?",
        "options": ["A) /t/", "B) /d/", "C) /n/", "D) /g/"],
        "answer": "B) /d/"
    },
    {
        "question": "69. Which sound is a voiceless labiodental fricative?",
        "options": ["A) /v/", "B) /s/", "C) /f/", "D) /z/"],
        "answer": "C) /f/"
    },
    {
        "question": "70. What distinguishes /ʒ/ from /ʃ/?",
        "options": ["A) Place of articulation", "B) Voicing", "C) Length", "D) Stress"],
        "answer": "B) Voicing"
    },
    {
        "question": "71. What is the glottis?",
        "options": ["A) The nasal cavity", "B) The area behind the tongue", "C) The space between the vocal folds",
                    "D) The alveolar ridge"],
        "answer": "C) The space between the vocal folds"
    },
    {
        "question": "72. Which of the following is a central vowel?",
        "options": ["A) /iː/", "B) /ɜː/", "C) /æ/", "D) /uː/"],
        "answer": "B) /ɜː/"
    },
    {
        "question": "73. The onset of a syllable refers to:",
        "options": ["A) The initial consonant(s) before the vowel", "B) The main vowel", "C) The final consonant",
                    "D) A suprasegmental element"],
        "answer": "A) The initial consonant(s) before the vowel"
    },
    {
        "question": "74. What is the articulatory feature of /h/?",
        "options": ["A) Voiced stop", "B) Nasal plosive", "C) Voiceless glottal fricative",
                    "D) Voiced bilabial fricative"],
        "answer": "C) Voiceless glottal fricative"
    },
    {
        "question": "75. In the word judge, the medial sound is:",
        "options": ["A) /d/", "B) /ʒ/", "C) /ʤ/", "D) /tʃ/"],
        "answer": "C) /ʤ/"
    },
    {
        "question": "76. Which of the following words contains a diphthong?",
        "options": ["A) Sit", "B) Cup", "C) Coin", "D) Cat"],
        "answer": "C) Coin"
    },
    {
        "question": "77. What type of sound is /r/ in most dialects of English?",
        "options": ["A) Fricative", "B) Approximant", "C) Nasal", "D) Stop"],
        "answer": "B) Approximant"
    },
    {
        "question": "78. Which transcription is correct for the word thing?",
        "options": ["A) /θɪŋg/", "B) /ðɪŋ/", "C) /θɪŋ/", "D) /fɪŋ/"],
        "answer": "C) /θɪŋ/"
    },
    {
        "question": "79. In the pair /iː/ vs. /ɪ/, the difference lies mainly in:",
        "options": ["A) Voicing", "B) Lip rounding", "C) Length and tongue height", "D) Nasality"],
        "answer": "C) Length and tongue height"
    },
    {
        "question": "80. Which vowel is typically stressed in the English word about?",
        "options": ["A) /e/", "B) /aʊ/", "C) /ə/", "D) /ɒ/"],
        "answer": "B) /aʊ/"
    },
    {
        "question": "81. What phonetic process is occurring in the pronunciation of handbag as /ˈhæmbæɡ/?",
        "options": ["A) Elision", "B) Assimilation", "C) Epenthesis", "D) Intonation"],
        "answer": "B) Assimilation"
    },
    {
        "question": "82. What is the correct IPA transcription for the word church?",
        "options": ["A) /ʧɜːʧ/", "B) /ʧɜːtʃ/", "C) /tʃəʧ/", "D) /ʧʌʧ/"],
        "answer": "B) /ʧɜːtʃ/"
    },
    {
        "question": "83. Which sound is a voiceless alveolar plosive?",
        "options": ["A) /d/", "B) /t/", "C) /p/", "D) /k/"],
        "answer": "B) /t/"
    },
    {
        "question": "84. The term lenition refers to:",
        "options": ["A) Strengthening a sound", "B) Weakening a sound", "C) Voicing a sound",
                    "D) Aspiration of a sound"],
        "answer": "B) Weakening a sound"
    },
    {
        "question": "85. A glottal stop is represented in IPA as:",
        "options": ["A) /ɣ/", "B) /ʔ/", "C) /ʕ/", "D) /ʡ/"],
        "answer": "B) /ʔ/"
    },
    {
        "question": "86. In English phonology, /l/ in lip and full are examples of:",
        "options": ["A) Vowels", "B) Allophones", "C) Diphthongs", "D) Syllables"],
        "answer": "B) Allophones"
    },
    {
        "question": "87. Which of the following is an example of a tense vowel?",
        "options": ["A) /ɪ/", "B) /iː/", "C) /ʊ/", "D) /ə/"],
        "answer": "B) /iː/"
    },
    {
        "question": "88. What is the term for a sound change due to influence from a neighboring word (e.g., “a apple” → “an apple”)?",
        "options": ["A) Assimilation", "B) Sandhi", "C) Metathesis", "D) Lenition"],
        "answer": "B) Sandhi"
    },
    {
        "question": "89. In phonology, contrastive distribution refers to:",
        "options": ["A) Allophonic variation", "B) Sounds that signal a change in meaning", "C) Stress placement",
                    "D) Phonotactics"],
        "answer": "B) Sounds that signal a change in meaning"
    },
    {
        "question": "90. The phonetic environment of a sound refers to:",
        "options": ["A) The surrounding sounds", "B) The dialect", "C) Its spelling", "D) Morphological category"],
        "answer": "A) The surrounding sounds"
    },
    {
        "question": "91. Which sound is an example of a voiced velar stop?",
        "options": ["A) /t/", "B) /k/", "C) /g/", "D) /ʔ/"],
        "answer": "C) /g/"
    },
    {
        "question": "92. What is the stress pattern of the word banana?",
        "options": ["A) First syllable stressed", "B) Second syllable stressed", "C) Third syllable stressed",
                    "D) All syllables stressed equally"],
        "answer": "B) Second syllable stressed"
    },
    {
        "question": "93. A phonemic transcription differs from a phonetic transcription in that it:",
        "options": ["A) Uses slashes and omits fine detail", "B) Uses brackets and shows exact pronunciation",
                    "C) Only marks vowels", "D) Uses numbers"],
        "answer": "A) Uses slashes and omits fine detail"
    },
    {
        "question": "94. In syllable structure, what is a coda?",
        "options": ["A) Initial consonant(s)", "B) Final consonant(s)", "C) Vowel nucleus",
                    "D) Suprasegmental element"],
        "answer": "B) Final consonant(s)"
    },
    {
        "question": "95. What feature do all approximants share?",
        "options": ["A) Complete oral closure", "B) Minimal obstruction to airflow", "C) Nasality",
                    "D) Vocal fold vibration"],
        "answer": "B) Minimal obstruction to airflow"
    },
    {
        "question": "96. The English word ring ends with which nasal sound?",
        "options": ["A) /n/", "B) /m/", "C) /ŋ/", "D) /ɲ/"],
        "answer": "C) /ŋ/"
    },
    {
        "question": "97. What type of sound is /ʍ/ in Scottish English or older RP?",
        "options": ["A) Voiced bilabial", "B) Voiceless labiovelar fricative", "C) Glide", "D) Nasal"],
        "answer": "B) Voiceless labiovelar fricative"
    },
    {
        "question": "98. Which vowel is typically centralized in connected speech?",
        "options": ["A) /iː/", "B) /æ/", "C) /ə/", "D) /e/"],
        "answer": "C) /ə/"
    },
    {
        "question": "99. The primary acoustic cue for voicing is:",
        "options": ["A) Vocal fold vibration", "B) Tongue height", "C) Lip rounding", "D) Stress"],
        "answer": "A) Vocal fold vibration"
    },
    {
        "question": "100. The term phonotactics refers to:",
        "options": ["A) Stress patterns", "B) Rules about permissible sound combinations in a language",
                    "C) Vowel length rules", "D) Nasal assimilation"],
        "answer": "B) Rules about permissible sound combinations in a language"
    },
]

questions_eng3 = [
{
        "question": "1. The Normans were originally from:",
        "options": ["A) France", "B) England", "C) Scandinavia", "D) Germany"],
        "answer": "C) Scandinavia"
    },
    {
        "question": "2. According to its vocabulary, English is partly a Germanic and partly a:",
        "options": ["A) Slavic", "B) Celtic", "C) Romance", "D) Baltic"],
        "answer": "C) Romance"
    },
    {
        "question": "3. Which word seems odd in the list below?",
        "options": ["A) Bread", "B) Cheese", "C) Pizza", "D) Butter"],
        "answer": "C) Pizza"
    },
    {
        "question": "4. Which word seems odd in the list below?",
        "options": ["A) Plough", "B) Axe", "C) Robot", "D) Hoe"],
        "answer": "C) Robot"
    },
    {
        "question": "5. The greatest author of the Middle English period is:",
        "options": ["A) William Shakespeare", "B) John Milton", "C) Geoffrey Chaucer", "D) Thomas Malory"],
        "answer": "C) Geoffrey Chaucer"
    },
    {
        "question": "6. “Whan that April with his shoures soote” is the beginning of:",
        "options": ["A) Beowulf", "B) The Bible", "C) Sir Gawain and the Green Knight", "D) The Canterbury Tales"],
        "answer": "D) The Canterbury Tales"
    },
    {
        "question": "7. Which word seems odd in the list below?",
        "options": ["A) Hammer", "B) Spade", "C) Saw", "D) Computer"],
        "answer": "D) Computer"
    },
    {
        "question": "8. Among the main dialect groups in the 14th century, which one did NOT exist?",
        "options": ["A) East Midland", "B) Kentish", "C) Northern-Western", "D) Southern"],
        "answer": "C) Northern-Western"
    },
    {
        "question": "9. English was first used in Parliament in:",
        "options": ["A) 1066", "B) 1200", "C) 1362", "D) 1500"],
        "answer": "C) 1362"
    },
    {
        "question": "10. The history of Middle English started after the Battle of:",
        "options": ["A) Waterloo", "B) Hastings", "C) Agincourt", "D) Yorktown"],
        "answer": "B) Hastings"
    },
    {
        "question": "11. The phonetic phenomenon that caused spelling/pronunciation change is:",
        "options": [
            "A) Consonant Shift",
            "B) The Great Vowel Shift",
            "C) Back Mutation",
            "D) Nasalization"
        ],
        "answer": "B) The Great Vowel Shift"
    },
    {
        "question": "12. The 3rd person plural “they” is borrowed from:",
        "options": [
            "A) Latin",
            "B) French",
            "C) Old Norse",
            "D) Gothic"
        ],
        "answer": "C) Old Norse"
    },
    {
        "question": "13. Which word seems odd in the list below?",
        "options": [
            "A) Fish",
            "B) Bread",
            "C) Sushi",
            "D) Milk"
        ],
        "answer": "C) Sushi"
    },
    {
        "question": "14. Which word seems odd in the list below?",
        "options": [
            "A) Apple",
            "B) Pear",
            "C) Banana",
            "D) Plum"
        ],
        "answer": "C) Banana"
    },
    {
        "question": "15. After the Norman conquest, teaching in England was mostly in:",
        "options": [
            "A) English",
            "B) French",
            "C) Latin",
            "D) German"
        ],
        "answer": "C) Latin"
    },
    {
        "question": "16. The first book printed in English was:",
        "options": [
            "A) Utopia",
            "B) The Canterbury Tales",
            "C) The Bible",
            "D) The Recuyell of the Historyes of Troye"
        ],
        "answer": "D) The Recuyell of the Historyes of Troye"
    },
    {
        "question": "17. The Middle English word “ich” meant:",
        "options": [
            "A) You",
            "B) He",
            "C) They",
            "D) I"
        ],
        "answer": "D) I"
    },
    {
        "question": "18. William Tyndale is famous for:",
        "options": [
            "A) Inventing printing",
            "B) Creating dictionaries",
            "C) Translating the Bible",
            "D) Writing poems"
        ],
        "answer": "C) Translating the Bible"
    },
    {
        "question": "19. Which sound first appeared in Middle English?",
        "options": [
            "A) [θ]",
            "B) [ʃ]",
            "C) [ʒ]",
            "D) [f]"
        ],
        "answer": "C) [ʒ]"
    },
    {
        "question": "20. In Middle English, the short [u] sound changed to:",
        "options": [
            "A) [e]",
            "B) [o]",
            "C) [ʌ]",
            "D) [i]"
        ],
        "answer": "C) [ʌ]"
    },
    {
        "question": "21. The Germanic group belongs to what wider language family?",
        "options": [
            "A) Semitic",
            "B) Uralic",
            "C) Finno-Ugric",
            "D) Indo-European"
        ],
        "answer": "D) Indo-European"
    },
    {
        "question": "22. Old English is part of which language group?",
        "options": [
            "A) East Germanic",
            "B) North Germanic",
            "C) West Germanic",
            "D) Romance"
        ],
        "answer": "C) West Germanic"
    },
    {
        "question": "23. Old English shares most features with:",
        "options": [
            "A) Old French",
            "B) Old High German",
            "C) Latin",
            "D) Gothic"
        ],
        "answer": "B) Old High German"
    },
    {
        "question": "24. Who introduced the Latin alphabet to Old English?",
        "options": [
            "A) Vikings",
            "B) Celtic druids",
            "C) Christian missionaries",
            "D) Roman emperors"
        ],
        "answer": "C) Christian missionaries"
    },
    {
        "question": "25. Which letter existed in Old English but not in Modern English?",
        "options": [
            "A) Q",
            "B) Z",
            "C) Þ (thorn)",
            "D) R"
        ],
        "answer": "C) Þ (thorn)"
    },
    {
        "question": "26. Syntax studies:",
        "options": [
            "A) Word meaning",
            "B) Pronunciation",
            "C) Sentence structure",
            "D) Vocabulary origin"
        ],
        "answer": "C) Sentence structure"
    },
    {
        "question": "27. A key difference in Old English syntax is:",
        "options": [
            "A) Lack of verbs",
            "B) Greater word order flexibility",
            "C) No pronouns",
            "D) Use of rhymes"
        ],
        "answer": "B) Greater word order flexibility"
    },
    {
        "question": "28. A “kenning” is:",
        "options": [
            "A) A rhyme",
            "B) A word puzzle",
            "C) A compound metaphor",
            "D) A grammatical rule"
        ],
        "answer": "C) A compound metaphor"
    },
    {
        "question": "29. Old English poetry is structured with:",
        "options": [
            "A) Rhyming couplets",
            "B) Sonnets",
            "C) Alliteration",
            "D) Free verse"
        ],
        "answer": "C) Alliteration"
    },
    {
        "question": "30. Subject pronouns were often omitted in Old English because:",
        "options": [
            "A) They were unknown",
            "B) They were unnecessary",
            "C) Verb endings showed the subject",
            "D) It was poetic tradition"
        ],
        "answer": "C) Verb endings showed the subject"
    },
    {
        "question": "31. What historical event marks the beginning of Middle English?",
        "options": ["A) Printing press invention", "B) Norman Conquest", "C) Viking invasions", "D) Black Death"],
        "answer": "B) Norman Conquest"
    },
    {
        "question": "32. Which dialect influenced Standard Middle English the most?",
        "options": ["A) Kentish", "B) Northumbrian", "C) East Midland", "D) Mercian"],
        "answer": "C) East Midland"
    },
    {
        "question": "33. What happened to Old English grammar in the Middle English period?",
        "options": ["A) It became more complex", "B) It remained unchanged", "C) It was simplified",
                    "D) It was replaced by Latin"],
        "answer": "C) It was simplified"
    },
    {
        "question": "34. One of the most famous Middle English literary works is:",
        "options": ["A) Beowulf", "B) Hamlet", "C) The Canterbury Tales", "D) Utopia"],
        "answer": "C) The Canterbury Tales"
    },
    {
        "question": "35. Major pronunciation change in Middle English was:",
        "options": ["A) Nasalization", "B) The Great Vowel Shift", "C) Grimm’s Law", "D) Palatalization"],
        "answer": "B) The Great Vowel Shift"
    },
    {
        "question": "36. A notable writer of Middle English is:",
        "options": ["A) Shakespeare", "B) Caxton", "C) Chaucer", "D) Tyndale"],
        "answer": "C) Chaucer"
    },
    {
        "question": "37. The standard that influenced Early Modern English is called:",
        "options": ["A) Royal English", "B) Chancery Standard", "C) Wessex Standard", "D) National English"],
        "answer": "B) Chancery Standard"
    },
    {
        "question": "38. Middle English covered which period?",
        "options": ["A) 900–1200", "B) 1000–1300", "C) 1150–1500", "D) 1066–1700"],
        "answer": "C) 1150–1500"
    },
    {
        "question": "39. What transition occurred between 1150s–1180s?",
        "options": ["A) French invasion", "B) Shift from Old to Middle English", "C) Birth of Chaucer",
                    "D) End of Latin use"],
        "answer": "B) Shift from Old to Middle English"
    },
    {
        "question": "40. What did Old Norse mostly influence in English?",
        "options": ["A) Alphabet", "B) Syntax", "C) Grammar and basic vocabulary", "D) Literature"],
        "answer": "C) Grammar and basic vocabulary"
    },
    {
        "question": "41. The National English language formed in the:",
        "options": ["A) 13th century", "B) Early 14th century", "C) Late 14th to early 30th century",
                    "D) 12th century"],
        "answer": "C) Late 14th to early 30th century"
    },
    {
        "question": "42. National English was based on which dialect?",
        "options": ["A) Northern", "B) Southern", "C) London East Midland", "D) West Saxon"],
        "answer": "C) London East Midland"
    },
    {
        "question": "43. Which of the following developed from Vulgar Latin?",
        "options": ["A) Old English", "B) Old Norse", "C) Spanish, Italian French", "D) Gothic"],
        "answer": "C) Spanish, Italian French"
    },
    {
        "question": "44. When was English spoken only in the British Isles?",
        "options": ["A) Pre-17th century", "B) 18th century", "C) 12th century", "D) During WWI"],
        "answer": "A) Pre-17th century"
    },
    {
        "question": "45. The English spoken from 1700 to today is:",
        "options": ["A) Middle English", "B) Old English", "C) Early Modern English", "D) Modern English"],
        "answer": "D) Modern English"
    },
    {
        "question": "46. English in the Old English period was a ___ language.",
        "options": ["A) Analytic", "B) Synthetic", "C) Creole", "D) Romance"],
        "answer": "B) Synthetic"
    },
    {
        "question": "47. In the New English period, English is a/an:",
        "options": ["A) Synthetic", "B) Isolated", "C) Analytic ,global", "D) Mixed"],
        "answer": "C) Analytic ,global"
    },
    {
        "question": "48. How many tenses existed in Old English?",
        "options": ["A) Four", "B) Three", "C) Two", "D) Six"],
        "answer": "C) Two"
    },
    {
        "question": "49. Typologically, Old English was a/an:",
        "options": ["A) Analytic language", "B) Isolating language", "C) Synthetic language", "D) Creole"],
        "answer": "C) Synthetic language"
    },
    {
        "question": "50. Runes were NOT written on:",
        "options": ["A) Wood", "B) Stone", "C) Metal", "D) Paper"],
        "answer": "D) Paper"
    },
    {
        "question": "51. When did William Caxton introduce the printing press to England?",
        "options": ["A) 1066", "B) 1215", "C) 1476", "D) 1604"],
        "answer": "C) 1476"
    },
    {
        "question": "52. Who brought Latin to Britain?",
        "options": ["A) Celts", "B) Anglo-Saxons", "C) Romans", "D) Normans"],
        "answer": "C) Romans"
    },
    {
        "question": "53. What dialect was used by Shakespeare?",
        "options": ["A) Middle English", "B) Northern", "C) Early Modern English", "D) Kentish"],
        "answer": "C) Early Modern English"
    },
    {
        "question": "54. Who commissioned the first English Bible translation?",
        "options": ["A) Henry VIII", "B) William I", "C) King James I", "D) Edward the Confessor"],
        "answer": "C) King James I"
    },
    {
        "question": "55. Which language had the least influence on Old English vocabulary?",
        "options": ["A) French", "B) Latin", "C) Celtic", "D) Norse"],
        "answer": "C) Celtic"
    },
    {
        "question": "56. Old English refers to English from:",
        "options": ["A) 10th to 13th centuries", "B) 5th to 11th centuries", "C) 12th to 15th centuries",
                    "D) 1st to 5th centuries"],
        "answer": "B) 5th to 11th centuries"
    },
    {
        "question": "57. The West Saxon dialect was spoken in:",
        "options": ["A) Mercia", "B) Wessex", "C) Kent", "D) Northumbria"],
        "answer": "B) Wessex"
    },
    {
        "question": "58. The shift to Middle English was mainly caused by:",
        "options": ["A) The Black Death", "B) The Viking raids", "C) The Norman Conquest", "D) Printing press"],
        "answer": "C) The Norman Conquest"
    },
    {
        "question": "59. Whose work helped stabilize Early Modern English spelling?",
        "options": ["A) John Milton", "B) Geoffrey Chaucer", "C) William Shakespeare", "D) Bede"],
        "answer": "C) William Shakespeare"
    },
    {
        "question": "60. Who published the first major English dictionary (1755)?",
        "options": ["A) Caxton", "B) Samuel Johnson", "C) Noah Webster", "D) William Tyndale"],
        "answer": "B) Samuel Johnson"
    },
{
    "question": "61. How many traditional periods are in the history of English?",
    "options": ["A) Two", "B) Three", "C) Four", "D) Five"],
    "answer": "B) Three"
  },
  {
    "question": "62. The shift of consonants in Germanic from Indo-European is called:",
    "options": ["A) Grimm’s Law", "B) Verner’s Law", "C) The Great Vowel Shift", "D) Sound Shift Law"],
    "answer": "A) Grimm’s Law"
  },
  {
    "question": "63. Which of these is NOT a Germanic language?",
    "options": ["A) German", "B) Dutch", "C) French", "D) Icelandic"],
    "answer": "C) French"
  },
  {
    "question": "64. Which extinct Germanic language is no longer spoken?",
    "options": ["A) Danish", "B) Gothic", "C) Swedish", "D) Frisian"],
    "answer": "B) Gothic"
  },
  {
    "question": "65. Which Germanic language has many Hebrew and Slavic borrowings?",
    "options": ["A) Norwegian", "B) Yiddish", "C) Frisian", "D) Dutch"],
    "answer": "B) Yiddish"
  },
  {
    "question": "66. Which Germanic language has no close ties to the Netherlands?",
    "options": ["A) Afrikaans", "B) Flemish", "C) Icelandic", "D) Dutch"],
    "answer": "C) Icelandic"
  },
  {
    "question": "67. The word “saga” is from which folklore tradition?",
    "options": ["A) Celtic", "B) German", "C) Norse/Icelandic", "D) Roman"],
    "answer": "C) Norse/Icelandic"
  },
  {
    "question": "68. The Younger and Older Edda are collections of:",
    "options": ["A) Fairy tales", "B) Norse mythology and poetry", "C) Latin hymns", "D) Germanic laws"],
    "answer": "B) Norse mythology and poetry"
  },
  {
    "question": "69. Which Germanic tribe gave its name to a Spanish province?",
    "options": ["A) Visigoths", "B) Vandals", "C) Franks", "D) Saxons"],
    "answer": "B) Vandals"
  },
  {
    "question": "70. Which Germanic language is NOT spoken in Europe?",
    "options": ["A) German", "B) Afrikaans", "C) Dutch", "D) Norwegian"],
    "answer": "B) Afrikaans"
  },
  {
    "question": "71. Until the early 20th century, Norway’s literary language was:",
    "options": ["A) Swedish", "B) Old Norse", "C) Danish", "D) English"],
    "answer": "C) Danish"
  },
  {
    "question": "72. English borrowed about half of its vocabulary from:",
    "options": ["A) Latin", "B) French", "C) German", "D) Dutch"],
    "answer": "B) French"
  },
  {
    "question": "73. Which Germanic language did NOT use the Latin alphabet?",
    "options": ["A) Gothic", "B) English", "C) Norwegian", "D) Yiddish"],
    "answer": "A) Gothic"
  },
  {
    "question": "74. East Gothic was spoken in modern-day:",
    "options": ["A) Germany and Austria", "B) France and Italy", "C) Ukraine and the Balkans", "D) Spain and Portugal"],
    "answer": "C) Ukraine and the Balkans"
  },
  {
    "question": "75. Yiddish is basically a dialect of:",
    "options": ["A) Hebrew", "B) Slavic", "C) German", "D) Latin"],
    "answer": "C) German"
  },
  {
    "question": "76. 1,500 years ago, the closest language to Old English was:",
    "options": ["A) Old High German", "B) Old Frisian", "C) Latin", "D) Gothic"],
    "answer": "B) Old Frisian"
  },
  {
    "question": "77. Which language has High and Low variants?",
    "options": ["A) French", "B) Dutch", "C) German", "D) Swedish"],
    "answer": "C) German"
  },
  {
    "question": "78. The state language of Finland (of Scandinavian origin) is:",
    "options": ["A) Finnish", "B) Norwegian", "C) Swedish", "D) Danish"],
    "answer": "C) Swedish"
  },
  {
    "question": "79. Which European country was named after a Germanic tribe?",
    "options": ["A) Germany", "B) France", "C) Spain", "D) Hungary"],
    "answer": "B) France"
  },
  {
    "question": "80. The people of which country are named after a Germanic tribe?",
    "options": ["A) Dutch (Netherlands)", "B) Irish", "C) Scots", "D) Italians"],
    "answer": "A) Dutch (Netherlands)"
  },
  {
    "question": "81. Old English borrowed many words from:",
    "options": ["A) Old Norse", "B) Greek", "C) Latin", "D) Celtic"],
    "answer": "C) Latin"
  },
  {
    "question": "82. How many cases did Old English nouns have?",
    "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
    "answer": "C) 5"
  },
  {
    "question": "83. How many grammatical genders were in Old English?",
    "options": ["A) Two", "B) Four", "C) Three", "D) None"],
    "answer": "C) Three"
  },
  {
    "question": "84. The letter Ɯ in Old English represented the sound:",
    "options": ["A) [ʃ]", "B) [w]", "C) [θ]", "D) [j]"],
    "answer": "B) [w]"
  },
  {
    "question": "85. The runic alphabet avoided:",
    "options": ["A) Straight lines", "B) Angles", "C) Curves", "D) Circles"],
    "answer": "C) Curves"
  },
  {
    "question": "86. The great Old English epic poem is:",
    "options": ["A) The Seafarer", "B) Beowulf", "C) The Dream of the Rood", "D) Sir Gawain"],
    "answer": "B) Beowulf"
  },
  {
    "question": "87. Runes were written on:",
    "options": ["A) Parchment", "B) Paper", "C) Wood, stone, and metal", "D) Leather only"],
    "answer": "C) Wood, stone, and metal"
  },
  {
    "question": "88. How many Anglo-Saxon kingdoms were in Britain?",
    "options": ["A) Five", "B) Six", "C) Seven", "D) Nine"],
    "answer": "C) Seven"
  },
  {
    "question": "89. Old English verbs had how many verbals?",
    "options": ["A) One", "B) Two", "C) Three", "D) Four"],
    "answer": "C) Three"
  },
  {
    "question": "90. How many numbers did Old English nouns show?",
    "options": ["A) One", "B) Two", "C) Three", "D) Four"],
    "answer": "B) Two"
  },
  {
    "question": "91. English belongs to which language family?",
    "options": ["A) Semitic", "B) Uralic", "C) Indo-European", "D) Altaic"],
    "answer": "C) Indo-European"
  },
  {
    "question": "92. Which invasion most influenced English?",
    "options": ["A) Roman", "B) Viking", "C) Norman", "D) Saxon"],
    "answer": "C) Norman"
  },
  {
    "question": "93. The earliest form of English is called:",
    "options": ["A) Anglo-Latin", "B) Anglo-Norman", "C) Old English", "D) Early Modern English"],
    "answer": "C) Old English"
  },
  {
    "question": "94. Which tribes created Old English?",
    "options": ["A) Celts, Picts, Britons", "B) Romans, Gauls", "C) Angles, Saxons, Jutes", "D) Vikings, Normans"],
    "answer": "C) Angles, Saxons, Jutes"
  },
  {
    "question": "95. Who wrote Beowulf?",
    "options": ["A) Chaucer", "B) Bede", "C) Anonymous", "D) Caedmon"],
    "answer": "C) Anonymous"
  },
  {
    "question": "96. What helped standardize English spelling and grammar?",
    "options": ["A) Norman conquest", "B) Viking invasions", "C) Printing press", "D) Industrial Revolution"],
    "answer": "C) Printing press"
  },
  {
    "question": "97. In which period did Shakespeare write?",
    "options": ["A) Middle English", "B) Old English", "C) Early Modern English", "D) Modern English"],
    "answer": "C) Early Modern English"
  },
  {
    "question": "98. Main result of the Norman Invasion?",
    "options": ["A) English became extinct", "B) Latin was revived", "C) French vocabulary entered English", "D) Old English grammar was restored"],
    "answer": "C) French vocabulary entered English"
  },
  {
    "question": "99. Which language most influenced Middle English vocabulary?",
    "options": ["A) Latin", "B) Norse", "C) French", "D) German"],
    "answer": "C) French"
  },
  {
    "question": "100. What was the Great Vowel Shift?",
    "options": ["A) Spelling reform", "B) Syntactic simplification", "C) Major pronunciation change", "D) Invention of rhyming poetry"],
    "answer": "C) Major pronunciation change"
  }
]

questions_eng4 = [
    {
        "question": "1. What does Lexicology study?",
        "options": ["A) Grammar", "B) Pronunciation", "C) Vocabulary and word structure", "D) Speech patterns"],
        "answer": "C) Vocabulary and word structure"
    },
    {
        "question": "2. What is the smallest meaningful unit of language?",
        "options": ["A) Word", "B) Sentence", "C) Phoneme", "D) Morpheme"],
        "answer": "D) Morpheme"
    },
    {
        "question": "3. Which words are called homonyms?",
        "options": ["A) Words with similar spelling and meaning", "B) Words with the same form but different meanings",
                    "C) Words with opposite meanings", "D) Words from the same root"],
        "answer": "B) Words with the same form but different meanings"
    },
    {
        "question": "4. What is the common term for “set expressions, fixed phrases”?",
        "options": ["A) Collocations", "B) Proverbs", "C) Idioms", "D) Phraseological units"],
        "answer": "D) Phraseological units"
    },
    {
        "question": "5. Homonyms with the same pronunciation are called:",
        "options": ["A) Homographs", "B) Homophones", "C) Synonyms", "D) Antonyms"],
        "answer": "B) Homophones"
    },
    {
        "question": "6. Suffixes -let, -ette, -ling indicate:",
        "options": ["A) Time", "B) Large size", "C) Diminutives", "D) Gender"],
        "answer": "C) Diminutives"
    },
    {
        "question": "7. Local varieties of language are called:",
        "options": ["A) Accents", "B) Slang", "C) Dialects", "D) Jargon"],
        "answer": "C) Dialects"
    },
    {
        "question": "8. Diachronic study investigates:",
        "options": ["A) Language as it is now", "B) Language history and changes", "C) Language pronunciation",
                    "D) Grammar only"],
        "answer": "B) Language history and changes"
    },
    {
        "question": "9. What is derivation?",
        "options": ["A) Changing meaning through spelling", "B) Adding a prefix or suffix to form a new word",
                    "C) Shortening a word", "D) Blending words"],
        "answer": "B) Adding a prefix or suffix to form a new word"
    },
    {
        "question": "10. Which parts of speech are most affected by conversion?",
        "options": ["A) Prepositions and articles", "B) Adjectives and adverbs", "C) Nouns and verbs",
                    "D) Conjunctions and interjections"],
        "answer": "C) Nouns and verbs"
    },
{
        "question": "11. All morphemes are subdivided into two large classes:",
        "options": ["A) Roots and Suffixes", "B) Simple and Complex", "C) Root and affixes Free and Bound", "D) Open and Closed"],
        "answer": "C) Root and affixes Free and Bound"
    },
    {
        "question": "12. Word-building by combining two or more stems is called:",
        "options": ["A) Derivation", "B) Compounding", "C) Conversion", "D) Abbreviation"],
        "answer": "B) Compounding"
    },
    {
        "question": "13. Words denoting outdated notions are called:",
        "options": ["A) Archaic words", "B) Obsolete words", "C) Historical words", "D) Rare words"],
        "answer": "C) Historical words"
    },
    {
        "question": "14. Native words are subdivided into:",
        "options": ["A) Slang and formal words", "B) Indo-European, Germanic, and English proper", "C) Borrowed and invented", "D) Common and proper nouns"],
        "answer": "B) Indo-European, Germanic, and English proper"
    },
    {
        "question": "15. Regional varieties of standard literary language are:",
        "options": ["A) Slang", "B) Pidgins", "C) Territorial dialects", "D) Vernaculars"],
        "answer": "C) Territorial dialects"
    },
    {
        "question": "16. The denotative component of meaning is:",
        "options": ["A) Emotional tone", "B) Grammar function", "C) Main conceptual meaning", "D) Stylistic usage"],
        "answer": "C) Main conceptual meaning"
    },
    {
        "question": "17. Polysemy refers to:",
        "options": ["A) Having one meaning", "B) Having opposite meanings", "C) Having multiple meanings", "D) Being a synonym"],
        "answer": "C) Having multiple meanings"
    },
    {
        "question": "18. On what level is the word studied in vocabulary systems?",
        "options": ["A) Syntax", "B) Pragmatics", "C) Lexical", "D) Phonological"],
        "answer": "C) Lexical"
    },
    {
        "question": "19. Etymological doublets are:",
        "options": ["A) Synonyms from same origin but different forms", "B) Repeated morphemes", "C) Parallel suffixes", "D) Borrowed idioms"],
        "answer": "A) Synonyms from same origin but different forms"
    },
    {
        "question": "20. Syntagmatic relationships are based on:",
        "options": ["A) Association in the mind", "B) Word form similarity", "C) Word combination in speech", "D) Dictionary definitions"],
        "answer": "C) Word combination in speech"
    },
    {
        "question": "21. Completely non-motivated word-groups are called:",
        "options": ["A) Free word-groups", "B) Idioms", "C) Collocations", "D) Compound words"],
        "answer": "B) Idioms"
    },
    {
        "question": "22. Phraseological units are classified according to:",
        "options": ["A) Grammar", "B) Syntax", "C) Semantic principle", "D) Word class"],
        "answer": "C) Semantic principle"
    },
    {
        "question": "23. The source of borrowing is:",
        "options": ["A) Dialects", "B) Grammar", "C) Donor language", "D) Prefixes"],
        "answer": "C) Donor language"
    },
    {
        "question": "24. Ideographic synonyms are words that:",
        "options": ["A) Are spelled alike", "B) Differ in style",
                    "C) Differ in shades of meaning but belong to the same field", "D) Have opposite meanings"],
        "answer": "C) Differ in shades of meaning but belong to the same field"
    },
    {
        "question": "25. Groups of words based on semantic relations are:",
        "options": ["A) Registers", "B) Lexical sets", "C) Jargons", "D) Phonemes"],
        "answer": "B) Lexical sets"
    },
    {
        "question": "26. Antonyms are words that differ in:",
        "options": ["A) Form", "B) Language origin", "C) Meaning", "D) Function"],
        "answer": "C) Meaning"
    },
    {
        "question": "27. Excluded from semasiology’s study is:",
        "options": ["A) Meaning", "B) Form", "C) Sound", "D) Style"],
        "answer": "C) Sound"
    },
    {
        "question": "28. The area of lexicology focused on word meaning is called:",
        "options": ["A) Syntax", "B) Semasiology", "C) Morphology", "D) Phonetics"],
        "answer": "B) Semasiology"
    },
    {
        "question": "29. Words opposite in meaning are called:",
        "options": ["A) Synonyms", "B) Homonyms", "C) Antonyms", "D) Acronyms"],
        "answer": "C) Antonyms"
    },
    {
        "question": "30. Lexicography studies:",
        "options": ["A) Grammar rules", "B) Word meanings", "C) Dictionary making", "D) Sound systems"],
        "answer": "C) Dictionary making"
    },
    {
        "question": "31. The largest group of borrowings in English is from:",
        "options": ["A) Latin", "B) French", "C) German", "D) Spanish"],
        "answer": "A) Latin"
    },
    {
        "question": "32. The most general term in a synonymic group is the:",
        "options": ["A) Slang word", "B) Formal word", "C) Dominant synonym", "D) Archaic word"],
        "answer": "C) Dominant synonym"
    },
    {
        "question": "33. A borrowing is a word that came:",
        "options": ["A) From a dialect", "B) From another language", "C) From abbreviation", "D) From slang"],
        "answer": "B) From another language"
    },
    {
        "question": "34. Words with similar meaning but different forms are:",
        "options": ["A) Homonyms", "B) Antonyms", "C) Synonyms", "D) Neologisms"],
        "answer": "C) Synonyms"
    },
    {
        "question": "35. Homonyms proper are:",
        "options": ["A) Same in form, unrelated in meaning", "B) Opposite in meaning", "C) Similar in sound",
                    "D) Blended words"],
        "answer": "A) Same in form, unrelated in meaning"
    },
    {
        "question": "36. Historical Lexicology studies:",
        "options": ["A) Dialects", "B) Word history and development", "C) Grammar rules", "D) Etymological roots only"],
        "answer": "B) Word history and development"
    },
    {
        "question": "37. Semantics studies:",
        "options": ["A) Word formation", "B) Word pronunciation", "C) Word meaning", "D) Word spelling"],
        "answer": "C) Word meaning"
    },
    {
        "question": "38. Conversion, derivation, and composition are types of:",
        "options": ["A) Syntax", "B) Grammar", "C) Word formation", "D) Sound change"],
        "answer": "C) Word formation"
    },
    {
        "question": "39. Affixation creates new words by:",
        "options": ["A) Mixing two words", "B) Adding affixes", "C) Changing word order", "D) Stressing syllables"],
        "answer": "B) Adding affixes"
    },
    {
        "question": "40. Suffixes -ard, -th are:",
        "options": ["A) Active suffixes", "B) Active suffixes,non-productive Obsolete suffixes", "C) Prefixes", "D) Foreign morphemes"],
        "answer": "B) Active suffixes,non-productive Obsolete suffixes"
    },
    {
        "question": "41. A word from original English stock is:",
        "options": ["A) Phoneme", "B) Native word", "C) Borrowed word", "D) Neologism"],
        "answer": "B) Native word"
    },
    {
        "question": "42. Types of shortening include:",
        "options": ["A) Conversion and derivation", "B) Compounding and blending", "C) Clipping, blending, acronyms",
                    "D) Homonymy and antonymy"],
        "answer": "C) Clipping, blending, acronyms"
    },
    {
        "question": "43. Major types of semantic relations are:",
        "options": ["A) Conversion and blending", "B) Synonymy, antonymy, polysemy", "C) Derivation and inflection",
                    "D) Affixation and composition"],
        "answer": "B) Synonymy, antonymy, polysemy"
    },
    {
        "question": "44. Words are divisible into:",
        "options": ["A) Letters", "B) Phonemes", "C) Morphemes", "D) Dialects"],
        "answer": "C) Morphemes"
    },
    {
        "question": "45. A thing to which a word refers is called:",
        "options": ["A) Concept", "B) Referent", "C) Lexeme", "D) Phrase"],
        "answer": "B) Referent"
    },
    {
        "question": "46. Words not assimilated from other languages are:",
        "options": ["A) Loan-blends", "B) Translation loans", "C) Barbarisms", "D) Compounds"],
        "answer": "C) Barbarisms"
    },
    {
        "question": "47. Compound-affixed words consist of:",
        "options": ["A) One morpheme", "B) Root and suffix", "C) Compound + affix", "D) Free morpheme only"],
        "answer": "C) Compound + affix"
    },
    {
        "question": "48. The system of all word forms is called:",
        "options": ["A) Dictionary", "B) Collocation", "C) Paradigm", "D) Word family"],
        "answer": "C) Paradigm"
    },
    {
        "question": "49. Words with elements from different languages are:",
        "options": ["A) Native", "B) Mixed-origin", "C) Neologisms", "D) Clippings"],
        "answer": "B) Mixed-origin"
    },
    {
        "question": "50. Borrowing identification depends on:",
        "options": ["A) Spelling", "B) Stress", "C) Phonetic, morphological, semantic criteria", "D) Alphabet"],
        "answer": "C) Phonetic, morphological, semantic criteria"
    },
    {
        "question": "51. Allomorphs are:",
        "options": ["A) Different meanings of the same word", "B) Variants of a morpheme with the same function",
                    "C) Word endings", "D) Phonemes in context"],
        "answer": "B) Variants of a morpheme with the same function"
    },
    {
        "question": "52. Hyponymy is the semantic relation of:",
        "options": ["A) Similarity", "B) Generalization", "C) Inclusion", "D) Opposition"],
        "answer": "C) Inclusion"
    },
    {
        "question": "53. External structure of the word refers to:",
        "options": ["A) The way it sounds", "B) The way it is written", "C) Its morphological composition",
                    "D) Its grammatical function"],
        "answer": "C) Its morphological composition"
    },
    {
        "question": "54. The study of vocabulary is called:",
        "options": ["A) Morphology", "B) Syntax", "C) Lexicology", "D) Phonetics"],
        "answer": "C) Lexicology"
    },
    {
        "question": "55. The smallest unit of meaning is:",
        "options": ["A) Phoneme", "B) Word", "C) Morpheme", "D) Phrase"],
        "answer": "C) Morpheme"
    },
    {
        "question": "56. A word with same spelling and pronunciation but different meanings is:",
        "options": ["A) Antonym", "B) Polyseme", "C) Homonym", "D) Synonym"],
        "answer": "C) Homonym"
    },
    {
        "question": "57. Forming a new word by adding prefixes or suffixes is:",
        "options": ["A) Conversion", "B) Blending", "C) Affixation", "D) Compounding"],
        "answer": "C) Affixation"
    },
    {
        "question": "58. Combining parts of two words to form a new one is:",
        "options": ["A) Clipping", "B) Acronym", "C) Blending", "D) Conversion"],
        "answer": "C) Blending"
    },
    {
        "question": "59. A word borrowed from another language is called:",
        "options": ["A) Native word", "B) Derivative", "C) Loanword", "D) Compound"],
        "answer": "C) Loanword"
    },
    {
        "question": "60. Meaning based on dictionary definition is:",
        "options": ["A) Connotative meaning", "B) Denotative meaning", "C) Figurative meaning", "D) Emotional meaning"],
        "answer": "B) Denotative meaning"
    },
    {
        "question": "61. A synonym is a word:",
        "options": ["A) With the opposite meaning", "B) With the same or nearly the same meaning",
                    "C) With a different form", "D) Borrowed from Latin"],
        "answer": "B) With the same or nearly the same meaning"
    },
    {
        "question": "62. Which is a compound word?",
        "options": ["A) Teacher", "B) Notebook", "C) Teach", "D) Teachful"],
        "answer": "B) Notebook"
    },
    {
        "question": "63. The historical study of word origins is called:",
        "options": ["A) Morphology", "B) Semasiology", "C) Etymology", "D) Lexicography"],
        "answer": "C) Etymology"
    },
    {
        "question": "64. When a word changes part of speech without changing form, it's called:",
        "options": ["A) Derivation", "B) Blending", "C) Conversion", "D) Affixation"],
        "answer": "C) Conversion"
    },
    {
        "question": "65. An antonym is a word:",
        "options": ["A) That sounds similar", "B) From the same root", "C) Opposite in meaning",
                    "D) That forms part of an idiom"],
        "answer": "C) Opposite in meaning"
    },
    {
        "question": "66. Which word is a neologism?",
        "options": ["A) Table", "B) Selfie", "C) Love", "D) Chair"],
        "answer": "B) Selfie"
    },
    {
        "question": "67. The morpheme carrying core meaning is the:",
        "options": ["A) Prefix", "B) Infix", "C) Root", "D) Suffix"],
        "answer": "C) Root"
    },
    {
        "question": "68. A word that imitates sound is:",
        "options": ["A) Onomatopoeia", "B) Blend", "C) Compound", "D) Acronym"],
        "answer": "A) Onomatopoeia"
    },
    {
        "question": "69. A shortened form like “ad” from “advertisement” is:",
        "options": ["A) Clipping", "B) Conversion", "C) Blending", "D) Acronym"],
        "answer": "A) Clipping"
    },
    {
        "question": "70. A dictionary of synonyms and antonyms is a:",
        "options": ["A) Glossary", "B) Thesaurus", "C) Lexicon", "D) Phrasebook"],
        "answer": "B) Thesaurus"
    },
    {
        "question": "71. A morpheme that cannot stand alone is:",
        "options": ["A) Free morpheme", "B) Bound morpheme", "C) Lexeme", "D) Word"],
        "answer": "B) Bound morpheme"
    },
    {
        "question": "72. An example of a lexical field is:",
        "options": ["A) Eat, sleep, run", "B) Doctor, nurse, hospital", "C) High, tall, long", "D) It, is, the"],
        "answer": "B) Doctor, nurse, hospital"
    },
    {
        "question": "73. A polysemantic word has:",
        "options": ["A) No meaning", "B) One meaning", "C) Several related meanings", "D) Opposite meanings"],
        "answer": "C) Several related meanings"
    },
    {
        "question": "74. Idioms and similar units are called:",
        "options": ["A) Collocations", "B) Morphemes", "C) Phraseological units", "D) Suffixes"],
        "answer": "C) Phraseological units"
    },
    {
        "question": "75. Which is a compound noun?",
        "options": ["A) Singer", "B) Blackboard", "C) Tall", "D) Happily"],
        "answer": "B) Blackboard"
    },
    {
        "question": "76. Social/emotional meaning of a word is called:",
        "options": ["A) Denotation", "B) Connotation", "C) Reference", "D) Definition"],
        "answer": "B) Connotation"
    },
    {
        "question": "77. A lexeme is:",
        "options": ["A) A synonym", "B) A unit of lexical meaning", "C) A phonetic form", "D) A grammatical case"],
        "answer": "B) A unit of lexical meaning"
    },
    {
        "question": "78. Which is a derived word?",
        "options": ["A) Beauty", "B) Beautiful", "C) Blue", "D) But"],
        "answer": "B) Beautiful"
    },
    {
        "question": "79. Which word contains a prefix?",
        "options": ["A) Teacher", "B) Unhappy", "C) Walking", "D) Quickly"],
        "answer": "B) Unhappy"
    },
    {
        "question": "80. Main source of new vocabulary today is:",
        "options": ["A) Poetry", "B) Technology", "C) Fiction", "D) Latin"],
        "answer": "B) Technology"
    },
    {
        "question": "81. A dictionary for specialized fields is a:",
        "options": ["A) Thesaurus", "B) Terminological dictionary", "C) Phrasebook", "D) Glossary"],
        "answer": "B) Terminological dictionary"
    },
    {
        "question": "82. An acronym is:",
        "options": ["A) Word from initials pronounced as a word", "B) Word from two roots",
                    "C) Word with many meanings", "D) Word opposite in meaning"],
        "answer": "A) Word from initials pronounced as a word"
    },
    {
        "question": "83. Forming a word by combining two full words is:",
        "options": ["A) Clipping", "B) Conversion", "C) Compounding", "D) Abbreviation"],
        "answer": "C) Compounding"
    },
    {
        "question": "84. Main function of a suffix is:",
        "options": ["A) Change sound", "B) Change part of speech or meaning", "C) Add stress", "D) Form compound"],
        "answer": "B) Change part of speech or meaning"
    },
    {
        "question": "85. Total stock of words in a language is called:",
        "options": ["A) Lexicon", "B) Syntax", "C) Grammar", "D) Thesaurus"],
        "answer": "A) Lexicon"
    },
    {
        "question": "86. Which is a blend word?",
        "options": ["A) Cupboard", "B) Motel", "C) Keyboard", "D) Blackberry"],
        "answer": "B) Motel"
    },
    {
        "question": "87. A monosemantic word has:",
        "options": ["A) Many meanings", "B) One meaning", "C) Figurative meaning", "D) No usage"],
        "answer": "B) One meaning"
    },
    {
        "question": "88. Ability of words to combine is called:",
        "options": ["A) Syntax", "B) Collocability", "C) Word formation", "D) Derivation"],
        "answer": "B) Collocability"
    },
    {
        "question": "89. Lexicography is the study of:",
        "options": ["A) Word order", "B) Word origin", "C) Dictionary compilation", "D) Grammar"],
        "answer": "C) Dictionary compilation"
    },
    {
        "question": "90. Monolingual dictionaries:",
        "options": ["A) Use two languages", "B) Include idioms", "C) Give definitions in one language",
                    "D) Have pictures"],
        "answer": "C) Give definitions in one language"
    },
    {
        "question": "91. The word being defined in a dictionary is the:",
        "options": ["A) Gloss", "B) Entry", "C) Keyword", "D) Lexicon"],
        "answer": "B) Entry"
    },
    {
        "question": "92. Etymological dictionary focuses on:",
        "options": ["A) Word meaning", "B) Grammar", "C) Word origin and history", "D) Pronunciation"],
        "answer": "C) Word origin and history"
    },
    {
        "question": "93. Dictionary for legal or medical terms is a:",
        "options": ["A) General dictionary", "B) Synonym dictionary", "C) Special dictionary", "D) Pocket dictionary"],
        "answer": "C) Special dictionary"
    },
    {
        "question": "94. A prescriptive dictionary:",
        "options": ["A) Describes actual usage", "B) Records slang", "C) Tells how words should be used",
                    "D) Contains idioms only"],
        "answer": "C) Tells how words should be used"
    },
    {
        "question": "95. Dictionary giving equivalents between two languages is:",
        "options": ["A) Thesaurus", "B) Monolingual", "C) Bilingual", "D) Special"],
        "answer": "C) Bilingual"
    },
    {
        "question": "96. Word formation by adding affixes is called:",
        "options": ["A) Clipping", "B) Conversion", "C) Affixation", "D) Blending"],
        "answer": "C) Affixation"
    },
    {
        "question": "97. 'To google' from 'Google' is an example of:",
        "options": ["A) Borrowing", "B) Conversion", "C) Blending", "D) Back-formation"],
        "answer": "B) Conversion"
    },
    {
        "question": "98. Formation of 'ad' from 'advertisement' is:",
        "options": ["A) Acronym", "B) Clipping", "C) Derivation", "D) Conversion"],
        "answer": "B) Clipping"
    },
    {
        "question": "99. Word 'sunflower' is formed through:",
        "options": ["A) Derivation", "B) Blending", "C) Compounding", "D) Acronym"],
        "answer": "C) Compounding"
    },
    {
        "question": "100. NATO is formed by:",
        "options": ["A) Blending", "B) Clipping", "C) Acronym", "D) Compounding"],
        "answer": "C) Acronym"
    }
]

topik_questions_kor5 = [
    {
        "question": "1. '안녕하세요'는 무슨 뜻입니까?",
        "options": ["A) 감사합니다", "B) 안녕히 가세요", "C) 안녕하십니까", "D) 안녕하세요"],
        "answer": "D) 안녕하세요"
    },
    {
        "question": "2. '학교'는 무엇입니까?",
        "options": ["A) 밥", "B) 병원", "C) 공부하는 곳", "D) 시장"],
        "answer": "C) 공부하는 곳"
    },
    {
        "question": "3. '밥을 먹어요'는 무슨 뜻입니까?",
        "options": ["A) 잠을 자요", "B) 밥을 사요", "C) 밥을 먹어요", "D) 밥을 줘요"],
        "answer": "C) 밥을 먹어요"
    },
    {
        "question": "4. '감사합니다'는 언제 사용합니까?",
        "options": ["A) 잘 가요", "B) 미안해요", "C) 고마울 때", "D) 배고플 때"],
        "answer": "C) 고마울 때"
    },
    {
        "question": "5. '의자'는 무엇입니까?",
        "options": ["A) 책", "B) 앉는 것", "C) 먹는 것", "D) 자는 것"],
        "answer": "B) 앉는 것"
    },
    {
        "question": "6. '저는 학생이에요.'의 뜻은?",
        "options": ["A) 나는 선생님이에요", "B) 나는 의사예요", "C) 나는 학생이에요", "D) 나는 친구예요"],
        "answer": "C) 나는 학생이에요"
    },
    {
        "question": "7. '물'은 무엇입니까?",
        "options": ["A) 우유", "B) 음료수", "C) 물건", "D) 물"],
        "answer": "D) 물"
    },
    {
        "question": "8. '어디 가요?'의 뜻은?",
        "options": ["A) 뭐 해요?", "B) 어디 있어요?", "C) 어디 가요?", "D) 언제 와요?"],
        "answer": "C) 어디 가요?"
    },
    {
        "question": "9. '책상 위에 있어요.'에서 '위'는?",
        "options": ["A) 아래", "B) 옆", "C) 앞", "D) 위"],
        "answer": "D) 위"
    },
    {
        "question": "10. '학교에 가요'는 무엇입니까?",
        "options": ["A) 학교에서 자요", "B) 학교에 와요", "C) 학교에 가요", "D) 학교를 닫아요"],
        "answer": "C) 학교에 가요"
    },
    {
        "question": "11. '친구'는 누구입니까?",
        "options": ["A) 가족", "B) 선생님", "C) 함께 노는 사람", "D) 의사"],
        "answer": "C) 함께 노는 사람"
    },
    {
        "question": "12. '사과를 먹어요'는 무슨 뜻입니까?",
        "options": ["A) 사과를 사요", "B) 사과를 마셔요", "C) 사과를 먹어요", "D) 사과를 줘요"],
        "answer": "C) 사과를 먹어요"
    },
    {
        "question": "13. '이것은 뭐예요?'의 뜻은?",
        "options": ["A) 이것 주세요", "B) 이게 뭐예요?", "C) 저것은 뭐예요?", "D) 무엇을 사요?"],
        "answer": "B) 이게 뭐예요?"
    },
    {
        "question": "14. '나는 밥을 먹어요'에서 '먹어요'는?",
        "options": ["A) 자다", "B) 마시다", "C) 먹다", "D) 오다"],
        "answer": "C) 먹다"
    },
    {
        "question": "15. '집'은 무엇입니까?",
        "options": ["A) 일하는 곳", "B) 자는 곳", "C) 공부하는 곳", "D) 물건 사는 곳"],
        "answer": "B) 자는 곳"
    },
    {
        "question": "16. '전화해요'는 무엇을 합니까?",
        "options": ["A) 말해요", "B) 전화해요", "C) 일해요", "D) 공부해요"],
        "answer": "B) 전화해요"
    },
    {
        "question": "17. '얼마예요?'는 언제 물어봐요?",
        "options": ["A) 시간", "B) 가격", "C) 이름", "D) 장소"],
        "answer": "B) 가격"
    },
    {
        "question": "18. '화장실이 어디예요?'에서 '화장실'은?",
        "options": ["A) 방", "B) 부엌", "C) 목욕탕", "D) 화장실"],
        "answer": "D) 화장실"
    },
    {
        "question": "19. '오늘 날씨가 어때요?'에 대한 좋은 대답은?",
        "options": ["A) 예뻐요", "B) 맛있어요", "C) 좋아요", "D) 많아요"],
        "answer": "C) 좋아요"
    },
    {
        "question": "20. '저는 우즈베키스탄 사람이에요.'는?",
        "options": ["A) 나는 학생이에요", "B) 나는 한국 사람이에요", "C) 나는 일본 사람이에요", "D) 나는 우즈베키스탄 사람이에요"],
        "answer": "D) 나는 우즈베키스탄 사람이에요"
    },
    {
        "question": "21. '학교에서 공부해요.'는 무엇입니까?",
        "options": ["A) 학교에 자요", "B) 학교에서 운동해요", "C) 학교에서 공부해요", "D) 학교에 가요"],
        "answer": "C) 학교에서 공부해요"
    },
    {
        "question": "22. '가방 안에 있어요'에서 '안'의 의미는?",
        "options": ["A) 위", "B) 밖", "C) 아래", "D) 안"],
        "answer": "D) 안"
    },
    {
        "question": "23. '무엇을 해요?'는 무엇을 묻습니까?",
        "options": ["A) 언제", "B) 어디서", "C) 누구", "D) 무엇"],
        "answer": "D) 무엇"
    },
    {
        "question": "24. '빵집'은 무엇을 파는 곳입니까?",
        "options": ["A) 물", "B) 빵", "C) 밥", "D) 라면"],
        "answer": "B) 빵"
    },
    {
        "question": "25. '저는 학생입니다.'의 반말은?",
        "options": ["A) 나는 학생이야", "B) 나는 학생입니다", "C) 나는 친구야", "D) 저는 학생이야"],
        "answer": "A) 나는 학생이야"
    },
    {
        "question": "26. '오늘은 일요일이에요.' 무슨 뜻입니까?",
        "options": ["A) 오늘은 월요일이에요", "B) 오늘은 쉬는 날이에요", "C) 오늘은 학교 가는 날이에요", "D) 오늘은 시험이에요"],
        "answer": "B) 오늘은 쉬는 날이에요"
    },
    {
        "question": "27. '얼굴이 예뻐요'는?",
        "options": ["A) 얼굴이 커요", "B) 얼굴이 예뻐요", "C) 얼굴이 작아요", "D) 얼굴이 나빠요"],
        "answer": "B) 얼굴이 예뻐요"
    },
    {
        "question": "28. '지금 뭐 해요?'에 대한 대답은?",
        "options": ["A) 지금 학교", "B) 지금 집이에요", "C) 지금 밥 먹어요", "D) 지금 가요"],
        "answer": "C) 지금 밥 먹어요"
    },
    {
        "question": "29. '우산'은 언제 써요?",
        "options": ["A) 눈 올 때", "B) 비 올 때", "C) 더울 때", "D) 바람 불 때"],
        "answer": "B) 비 올 때"
    },
    {
        "question": "30. '학교에서 만나요'는?",
        "options": ["A) 학교에 가요", "B) 학교에서 자요", "C) 학교에서 만나요", "D) 학교를 봐요"],
        "answer": "C) 학교에서 만나요"
    },
    {
        "question": "31. '옷을 입어요'의 뜻은?",
        "options": ["A) 옷을 벗어요", "B) 옷을 입어요", "C) 옷을 줘요", "D) 옷을 사요"],
        "answer": "B) 옷을 입어요"
    },
    {
        "question": "32. '오늘은 더워요'는 무슨 뜻입니까?",
        "options": ["A) 추워요", "B) 시원해요", "C) 더워요", "D) 비 와요"],
        "answer": "C) 더워요"
    },
    {
        "question": "33. '한국어 공부해요'는?",
        "options": ["A) 영어 공부해요", "B) 한국어 공부해요", "C) 한국어 말해요", "D) 한국에 가요"],
        "answer": "B) 한국어 공부해요"
    },
    {
        "question": "34. '저는 회사에 다녀요'는?",
        "options": ["A) 회사에 가요", "B) 회사에 자요", "C) 회사에서 공부해요", "D) 회사에 다녀요"],
        "answer": "D) 회사에 다녀요"
    },
    {
        "question": "35. '배고파요'는 무슨 뜻입니까?",
        "options": ["A) 목말라요", "B) 졸려요", "C) 배고파요", "D) 피곤해요"],
        "answer": "C) 배고파요"
    },
    {
        "question": "36. '커피 마셔요'는?",
        "options": ["A) 커피 마셔요", "B) 커피 사요", "C) 커피 줘요", "D) 커피 봐요"],
        "answer": "A) 커피 마셔요"
    },
    {
        "question": "37. '공부해요'는 무엇을 합니까?",
        "options": ["A) 일해요", "B) 공부해요", "C) 자요", "D) 놀아요"],
        "answer": "B) 공부해요"
    },
    {
        "question": "38. '냉장고'는 무엇입니까?",
        "options": ["A) 밥솥", "B) 텔레비전", "C) 음식을 차게 하는 것", "D) 세탁기"],
        "answer": "C) 음식을 차게 하는 것"
    },
    {
        "question": "39. '책을 사요'는?",
        "options": ["A) 책을 읽어요", "B) 책을 줘요", "C) 책을 사요", "D) 책을 덮어요"],
        "answer": "C) 책을 사요"
    },
    {
        "question": "40. '텔레비전을 봐요'는?",
        "options": ["A) 텔레비전을 들어요", "B) 텔레비전을 꺼요", "C) 텔레비전을 봐요", "D) 텔레비전을 팔아요"],
        "answer": "C) 텔레비전을 봐요"
    },
    {
        "question": "41. '한국 음식'은 무엇입니까?",
        "options": ["A) 스파게티", "B) 초밥", "C) 불고기", "D) 햄버거"],
        "answer": "C) 불고기"
    },
    {
        "question": "42. '일곱 시에 일어나요'는?",
        "options": ["A) 일곱 시에 자요", "B) 일곱 시에 먹어요", "C) 일곱 시에 일어나요", "D) 일곱 시에 운동해요"],
        "answer": "C) 일곱 시에 일어나요"
    },
    {
        "question": "43. '운동해요'는 무슨 뜻입니까?",
        "options": ["A) 공부해요", "B) 청소해요", "C) 운동해요", "D) 자요"],
        "answer": "C) 운동해요"
    },
    {
        "question": "44. '어머니'는 누구입니까?",
        "options": ["A) 친구", "B) 선생님", "C) 엄마", "D) 동생"],
        "answer": "C) 엄마"
    },
    {
        "question": "45. '한국에 가요'는?",
        "options": ["A) 한국에 와요", "B) 한국에 가요", "C) 한국에서 와요", "D) 한국을 봐요"],
        "answer": "B) 한국에 가요"
    },
    {
        "question": "46. '시간이 없어요'는?",
        "options": ["A) 시간이 많아요", "B) 시간이 없어요", "C) 시간이 길어요", "D) 시간이 늦어요"],
        "answer": "B) 시간이 없어요"
    },
    {
        "question": "47. '학생'은 누구입니까?",
        "options": ["A) 공부하는 사람", "B) 일하는 사람", "C) 자는 사람", "D) 말하는 사람"],
        "answer": "A) 공부하는 사람"
    },
    {
        "question": "48. '버스를 타요'는?",
        "options": ["A) 버스를 봐요", "B) 버스를 사요", "C) 버스를 타요", "D) 버스를 내려요"],
        "answer": "C) 버스를 타요"
    },
    {
        "question": "49. '영화를 봐요'는?",
        "options": ["A) 영화를 먹어요", "B) 영화를 봐요", "C) 영화를 사요", "D) 영화를 줘요"],
        "answer": "B) 영화를 봐요"
    },
    {
        "question": "50. '책을 읽어요'는 무슨 뜻입니까?",
        "options": ["A) 책을 닫아요", "B) 책을 읽어요", "C) 책을 사요", "D) 책을 들어요"],
        "answer": "B) 책을 읽어요"
    }
]

topik_questions_kor6 = [
{
        "question": "1. '저는 우유를 좋아해요.'에서 '우유'는 무엇입니까?",
        "options": ["A) 물", "B) 차", "C) 우유", "D) 주스"],
        "answer": "C) 우유"
    },
    {
        "question": "2. '시장에 가요'는 무슨 뜻입니까?",
        "options": ["A) 시장에서 자요", "B) 시장에서 만나요", "C) 시장에 가요", "D) 시장을 닫아요"],
        "answer": "C) 시장에 가요"
    },
    {
        "question": "3. '고양이'는 어떤 동물입니까?",
        "options": ["A) 강아지", "B) 고양이", "C) 토끼", "D) 사자"],
        "answer": "B) 고양이"
    },
    {
        "question": "4. '색연필'은 어디에 사용합니까?",
        "options": ["A) 먹을 때", "B) 잴 때", "C) 그림 그릴 때", "D) 노래할 때"],
        "answer": "C) 그림 그릴 때"
    },
    {
        "question": "5. '텔레비전을 꺼요'는?",
        "options": ["A) 텔레비전을 켜요", "B) 텔레비전을 꺼요", "C) 텔레비전을 사요", "D) 텔레비전을 봐요"],
        "answer": "B) 텔레비전을 꺼요"
    },
    {
        "question": "6. '신발'은 어디에 신어요?",
        "options": ["A) 머리", "B) 손", "C) 발", "D) 얼굴"],
        "answer": "C) 발"
    },
    {
        "question": "7. '형'은 누구입니까?",
        "options": ["A) 남동생", "B) 오빠", "C) 형", "D) 아버지"],
        "answer": "C) 형"
    },
    {
        "question": "8. '시계'는 무엇을 봅니까?",
        "options": ["A) 시간", "B) 날씨", "C) 날짜", "D) 요일"],
        "answer": "A) 시간"
    },
    {
        "question": "9. '도서관에서 책을 빌려요.'의 뜻은?",
        "options": ["A) 책을 팔아요", "B) 책을 사요", "C) 책을 빌려요", "D) 책을 읽어요"],
        "answer": "C) 책을 빌려요"
    },
    {
        "question": "10. '음악을 들어요'는?",
        "options": ["A) 음악을 봐요", "B) 음악을 말해요", "C) 음악을 들어요", "D) 음악을 줘요"],
        "answer": "C) 음악을 들어요"
    },
{
        "question": "11. '냉면'은 어떤 음식입니까?",
        "options": ["A) 따뜻한 음식", "B) 차가운 음식", "C) 단 음식", "D) 매운 음식"],
        "answer": "B) 차가운 음식"
    },
    {
        "question": "12. '학생들이 운동장에서 축구해요.'에서 '운동장'은 어디입니까?",
        "options": ["A) 교실", "B) 병원", "C) 밖에서 노는 곳", "D) 식당"],
        "answer": "C) 밖에서 노는 곳"
    },
    {
        "question": "13. '병원에 가요'는 왜 갑니까?",
        "options": ["A) 밥을 먹으러", "B) 책을 사러", "C) 아파서", "D) 놀러"],
        "answer": "C) 아파서"
    },
    {
        "question": "14. '지하철을 타요'는 무엇입니까?",
        "options": ["A) 걸어요", "B) 운전해요", "C) 버스를 타요", "D) 전철을 타요"],
        "answer": "D) 전철을 타요"
    },
    {
        "question": "15. '방이 넓어요'는 어떤 뜻입니까?",
        "options": ["A) 방이 좁아요", "B) 방이 커요", "C) 방이 어두워요", "D) 방이 작아요"],
        "answer": "B) 방이 커요"
    },
    {
        "question": "16. '저는 매일 운동해요'에서 '매일'은?",
        "options": ["A) 어제", "B) 오늘", "C) 매주", "D) 매일"],
        "answer": "D) 매일"
    },
    {
        "question": "17. '도착했어요'는 언제 말합니까?",
        "options": ["A) 출발할 때", "B) 도착했을 때", "C) 준비할 때", "D) 공부할 때"],
        "answer": "B) 도착했을 때"
    },
    {
        "question": "18. '아버지는 회사에 다녀요'는 무슨 뜻입니까?",
        "options": ["A) 아버지는 집에 있어요", "B) 아버지는 학교에 다녀요", "C) 아버지는 회사에 다녀요", "D) 아버지는 쉬어요"],
        "answer": "C) 아버지는 회사에 다녀요"
    },
    {
        "question": "19. '공책에 글을 써요'는 무엇입니까?",
        "options": ["A) 그림을 그려요", "B) 글을 써요", "C) 색칠해요", "D) 노래해요"],
        "answer": "B) 글을 써요"
    },
    {
        "question": "20. '창문을 열어요'의 반대말은?",
        "options": ["A) 문을 열어요", "B) 창문을 닫아요", "C) 불을 켜요", "D) 창을 닦아요"],
        "answer": "B) 창문을 닫아요"
    },
    {
        "question": "21. '컴퓨터를 켜요'는 무엇을 하나요?",
        "options": ["A) 컴퓨터를 꺼요", "B) 컴퓨터를 들어요", "C) 컴퓨터를 켜요", "D) 컴퓨터를 닫아요"],
        "answer": "C) 컴퓨터를 켜요"
    },
    {
        "question": "22. '점심을 먹어요'는 어느 시간입니까?",
        "options": ["A) 아침", "B) 점심", "C) 저녁", "D) 새벽"],
        "answer": "B) 점심"
    },
    {
        "question": "23. '비행기를 타요'는 어디에 갈 때 사용합니까?",
        "options": ["A) 멀리", "B) 근처", "C) 시장", "D) 학교"],
        "answer": "A) 멀리"
    },
    {
        "question": "24. '우산을 써요'는 언제입니까?",
        "options": ["A) 더울 때", "B) 비 올 때", "C) 추울 때", "D) 눈 올 때"],
        "answer": "B) 비 올 때"
    },
    {
        "question": "25. '가게에서 물건을 사요'는 무엇입니까?",
        "options": ["A) 공부해요", "B) 일해요", "C) 쇼핑해요", "D) 쉬어요"],
        "answer": "C) 쇼핑해요"
    },
    {
        "question": "26. '지금 쉬고 있어요'는 무엇입니까?",
        "options": ["A) 일해요", "B) 운동해요", "C) 쉬어요", "D) 자요"],
        "answer": "C) 쉬어요"
    },
    {
        "question": "27. '시험을 봐요'는 어떤 상황입니까?",
        "options": ["A) 밥을 먹어요", "B) 친구를 만나요", "C) 공부해요", "D) 시험해요"],
        "answer": "D) 시험해요"
    },
    {
        "question": "28. '밖에 나가요'는 무엇입니까?",
        "options": ["A) 안에 있어요", "B) 집에 있어요", "C) 밖에 나가요", "D) 누워요"],
        "answer": "C) 밖에 나가요"
    },
    {
        "question": "29. '전화번호를 알아요'의 의미는?",
        "options": ["A) 전화기를 알아요", "B) 번호를 말해요", "C) 전화번호를 알아요", "D) 전화해요"],
        "answer": "C) 전화번호를 알아요"
    },
    {
        "question": "30. '생일 축하해요'는 언제 말합니까?",
        "options": ["A) 졸업식", "B) 생일", "C) 시험", "D) 결혼식"],
        "answer": "B) 생일"
    },
    {
        "question": "31. '도와주세요'는 어떤 상황입니까?",
        "options": ["A) 혼자 할 수 있어요", "B) 필요 없어요", "C) 도움이 필요해요", "D) 공부하고 있어요"],
        "answer": "C) 도움이 필요해요"
    },
    {
        "question": "32. '방이 깨끗해요'는 무슨 뜻입니까?",
        "options": ["A) 방이 더러워요", "B) 방이 깨끗해요", "C) 방이 커요", "D) 방이 좁아요"],
        "answer": "B) 방이 깨끗해요"
    },
    {
        "question": "33. '눈이 와요'는 어떤 날씨입니까?",
        "options": ["A) 비가 와요", "B) 해가 나요", "C) 바람이 불어요", "D) 눈이 와요"],
        "answer": "D) 눈이 와요"
    },
    {
        "question": "34. '여름'은 어떤 계절입니까?",
        "options": ["A) 더운 계절", "B) 추운 계절", "C) 비 오는 계절", "D) 눈 오는 계절"],
        "answer": "A) 더운 계절"
    },
    {
        "question": "35. '학교에 늦었어요'는 무슨 뜻입니까?",
        "options": ["A) 제시간에 갔어요", "B) 빨리 갔어요", "C) 늦게 갔어요", "D) 가지 않았어요"],
        "answer": "C) 늦게 갔어요"
    },
    {
        "question": "36. '책을 펴요'는 무엇을 하나요?",
        "options": ["A) 책을 닫아요", "B) 책을 던져요", "C) 책을 펴요", "D) 책을 써요"],
        "answer": "C) 책을 펴요"
    },
    {
        "question": "37. '영수증 주세요'는 어디서 말합니까?",
        "options": ["A) 학교", "B) 식당", "C) 가게", "D) 도서관"],
        "answer": "C) 가게"
    },
    {
        "question": "38. '우체국에 가요'는 무엇을 하기 위해서입니까?",
        "options": ["A) 책을 빌리러", "B) 우편을 보내러", "C) 밥을 먹으러", "D) 돈을 찾으러"],
        "answer": "B) 우편을 보내러"
    },
    {
        "question": "39. '한국어 수업이 재미있어요'는?",
        "options": ["A) 수업이 지루해요", "B) 수업이 좋아요", "C) 수업이 많아요", "D) 수업이 어려워요"],
        "answer": "B) 수업이 좋아요"
    },
    {
        "question": "40. '밤에 자요'는 어느 시간입니까?",
        "options": ["A) 아침", "B) 점심", "C) 저녁", "D) 밤"],
        "answer": "D) 밤"
    },
    {
        "question": "41. '영화를 예매해요'는 무엇을 합니까?",
        "options": ["A) 영화를 사요", "B) 영화를 미뤄요", "C) 영화를 예약해요", "D) 영화를 꺼요"],
        "answer": "C) 영화를 예약해요"
    },
    {
        "question": "42. '여권이 있어요?'는 언제 물어봅니까?",
        "options": ["A) 병원에서", "B) 비행기를 탈 때", "C) 가게에서", "D) 도서관에서"],
        "answer": "B) 비행기를 탈 때"
    },
    {
        "question": "43. '사진을 찍어요'는 무엇입니까?",
        "options": ["A) 사진을 말해요", "B) 사진을 줘요", "C) 사진을 찍어요", "D) 사진을 사요"],
        "answer": "C) 사진을 찍어요"
    },
    {
        "question": "44. '휴대폰을 충전해요'는?",
        "options": ["A) 휴대폰을 꺼요", "B) 휴대폰을 빌려요", "C) 휴대폰을 충전해요", "D) 휴대폰을 팔아요"],
        "answer": "C) 휴대폰을 충전해요"
    },
    {
        "question": "45. '공항에 도착했어요'는 무슨 뜻입니까?",
        "options": ["A) 아직 안 갔어요", "B) 출발했어요", "C) 도착했어요", "D) 기다려요"],
        "answer": "C) 도착했어요"
    },
    {
        "question": "46. '오늘은 토요일이에요'는 무슨 날입니까?",
        "options": ["A) 평일", "B) 주말", "C) 시험날", "D) 생일"],
        "answer": "B) 주말"
    },
    {
        "question": "47. '학교에 지각했어요'는?",
        "options": ["A) 일찍 갔어요", "B) 늦게 갔어요", "C) 안 갔어요", "D) 자고 있어요"],
        "answer": "B) 늦게 갔어요"
    },
    {
        "question": "48. '날씨가 흐려요'는 어떤 날씨입니까?",
        "options": ["A) 맑아요", "B) 더워요", "C) 흐려요", "D) 시원해요"],
        "answer": "C) 흐려요"
    },
    {
        "question": "49. '택시를 잡아요'는 무슨 뜻입니까?",
        "options": ["A) 택시를 사요", "B) 택시를 타요", "C) 택시를 빌려요", "D) 택시를 만들어줘요"],
        "answer": "B) 택시를 타요"
    },
    {
        "question": "50. '오늘 몇 월 며칠이에요?'는 무엇을 물어요?",
        "options": ["A) 시간", "B) 날짜", "C) 이름", "D) 요일"],
        "answer": "B) 날짜"
    }
]
topik_questions_kor7 = [
{
        "question": "1. 다음 중 병원에서 할 수 있는 일은 무엇입니까?",
        "options": ["A) 책을 읽어요", "B) 밥을 먹어요", "C) 진찰을 받아요", "D) 운동을 해요"],
        "answer": "C) 진찰을 받아요"
    },
    {
        "question": "2. 아침에 일어나서 가장 먼저 하는 일은 무엇입니까?",
        "options": ["A) 잠을 자요", "B) 인사를 해요", "C) 세수를 해요", "D) 학교에 가요"],
        "answer": "C) 세수를 해요"
    },
    {
        "question": "3. 한국에서 설날에 주로 하는 일은 무엇입니까?",
        "options": ["A) 수영해요", "B) 세배를 해요", "C) 김밥을 먹어요", "D) 산책해요"],
        "answer": "B) 세배를 해요"
    },
    {
        "question": "4. 다음 중 날씨가 추울 때 입는 것은 무엇입니까?",
        "options": ["A) 반바지", "B) 치마", "C) 외투", "D) 티셔츠"],
        "answer": "C) 외투"
    },
    {
        "question": "5. 다음 중 학교에서 할 수 없는 것은 무엇입니까?",
        "options": ["A) 공부해요", "B) 수업을 들어요", "C) 시험을 봐요", "D) 요리를 해요"],
        "answer": "D) 요리를 해요"
    },
    {
        "question": "6. 친구를 처음 만났을 때 하는 인사는 무엇입니까?",
        "options": ["A) 잘 자요", "B) 안녕히 계세요", "C) 안녕하세요", "D) 감사합니다"],
        "answer": "C) 안녕하세요"
    },
    {
        "question": "7. 다음 중 음식이 아닌 것은 무엇입니까?",
        "options": ["A) 김치", "B) 불고기", "C) 바나나", "D) 연필"],
        "answer": "D) 연필"
    },
    {
        "question": "8. 물건을 사기 전에 해야 하는 일은 무엇입니까?",
        "options": ["A) 돈을 받아요", "B) 물건을 버려요", "C) 가격을 물어요", "D) 길을 물어요"],
        "answer": "C) 가격을 물어요"
    },
    {
        "question": "9. 다음 중 교통수단이 아닌 것은 무엇입니까?",
        "options": ["A) 자전거", "B) 버스", "C) 지하철", "D) 텔레비전"],
        "answer": "D) 텔레비전"
    },
    {
        "question": "10. 날씨가 맑을 때 하는 활동은 무엇입니까?",
        "options": ["A) 우산을 써요", "B) 산책을 해요", "C) 창문을 닫아요", "D) 집에 있어요"],
        "answer": "B) 산책을 해요"
    },
{
        "question": "11. 다음 중 아침에 먹는 음식으로 알맞은 것은?",
        "options": ["A) 라면", "B) 삼겹살", "C) 김밥", "D) 밥과 국"],
        "answer": "D) 밥과 국"
    },
    {
        "question": "12. 지하철을 타려면 먼저 무엇을 해야 합니까?",
        "options": ["A) 표를 사요", "B) 물을 마셔요", "C) 노래를 해요", "D) 책을 읽어요"],
        "answer": "A) 표를 사요"
    },
    {
        "question": "13. 도서관에서는 어떻게 해야 합니까?",
        "options": ["A) 크게 말해요", "B) 뛰어요", "C) 조용히 해요", "D) 사진을 찍어요"],
        "answer": "C) 조용히 해요"
    },
    {
        "question": "14. 친구에게 생일 선물을 줄 때 하는 말은?",
        "options": ["A) 잘 가요", "B) 생일 축하해요", "C) 안녕히 계세요", "D) 미안해요"],
        "answer": "B) 생일 축하해요"
    },
    {
        "question": "15. 다음 중 옷을 사는 곳은 어디입니까?",
        "options": ["A) 병원", "B) 서점", "C) 옷가게", "D) 영화관"],
        "answer": "C) 옷가게"
    },
    {
        "question": "16. 한국에서 여름은 어떤 계절입니까?",
        "options": ["A) 춥고 눈이 와요", "B) 더워요", "C) 바람이 불어요", "D) 시원해요"],
        "answer": "B) 더워요"
    },
    {
        "question": "17. 다음 중 학교에서 할 수 있는 것은?",
        "options": ["A) 빨래를 해요", "B) 숙제를 해요", "C) 요리를 해요", "D) 잠을 자요"],
        "answer": "B) 숙제를 해요"
    },
    {
        "question": "18. 다음 중 겨울에 입는 옷은?",
        "options": ["A) 반팔", "B) 반바지", "C) 모자", "D) 코트"],
        "answer": "D) 코트"
    },
    {
        "question": "19. 식당에서 음식을 주문하려면 어떻게 말합니까?",
        "options": ["A) 얼마예요?", "B) 주세요", "C) 안녕히 가세요", "D) 괜찮아요"],
        "answer": "B) 주세요"
    },
    {
        "question": "20. 다음 중 한국 돈 단위는?",
        "options": ["A) 달러", "B) 유로", "C) 엔", "D) 원"],
        "answer": "D) 원"
    },
    {
        "question": "21. 도로에서 길을 건널 때 필요한 것은?",
        "options": ["A) 신호등", "B) 창문", "C) 시계", "D) 버스"],
        "answer": "A) 신호등"
    },
    {
        "question": "22. 한국에서 음식을 먹기 전에 하는 말은?",
        "options": ["A) 잘 먹겠습니다", "B) 잘 지냈어요", "C) 안녕히 계세요", "D) 감사합니다"],
        "answer": "A) 잘 먹겠습니다"
    },
    {
        "question": "23. 편지를 보내려면 어디로 가야 합니까?",
        "options": ["A) 도서관", "B) 우체국", "C) 식당", "D) 백화점"],
        "answer": "B) 우체국"
    },
    {
        "question": "24. 비가 올 때 필요한 것은?",
        "options": ["A) 모자", "B) 우산", "C) 안경", "D) 수건"],
        "answer": "B) 우산"
    },
    {
        "question": "25. 다음 중 가족이 아닌 사람은?",
        "options": ["A) 어머니", "B) 친구", "C) 형", "D) 누나"],
        "answer": "B) 친구"
    },
    {
        "question": "26. 다음 중 낮에 하는 일은?",
        "options": ["A) 잠을 자요", "B) 식사를 해요", "C) 별을 봐요", "D) 불을 꺼요"],
        "answer": "B) 식사를 해요"
    },
    {
        "question": "27. 다음 중 마실 수 없는 것은?",
        "options": ["A) 물", "B) 주스", "C) 우유", "D) 샴푸"],
        "answer": "D) 샴푸"
    },
    {
        "question": "28. 학교에 지각하면 어떻게 됩니까?",
        "options": ["A) 선생님이 칭찬해요", "B) 늦게 도착해요", "C) 상을 받아요", "D) 일찍 가요"],
        "answer": "B) 늦게 도착해요"
    },
    {
        "question": "29. 다음 중 저녁 인사는?",
        "options": ["A) 안녕히 주무세요", "B) 안녕하세요", "C) 잘 가요", "D) 만나서 반가워요"],
        "answer": "A) 안녕히 주무세요"
    },
    {
        "question": "30. 수업 시간에 무엇을 합니까?",
        "options": ["A) 먹어요", "B) 자요", "C) 공부해요", "D) 게임해요"],
        "answer": "C) 공부해요"
    },
    {
        "question": "31. 한국의 수도는 어디입니까?",
        "options": ["A) 부산", "B) 인천", "C) 대구", "D) 서울"],
        "answer": "D) 서울"
    },
    {
        "question": "32. 전화할 때 먼저 하는 말은?",
        "options": ["A) 감사합니다", "B) 여보세요", "C) 잘 가요", "D) 미안해요"],
        "answer": "B) 여보세요"
    },
    {
        "question": "33. 배가 고프면 무엇을 해야 합니까?",
        "options": ["A) 자요", "B) 공부해요", "C) 먹어요", "D) 씻어요"],
        "answer": "C) 먹어요"
    },
    {
        "question": "34. 다음 중 과일이 아닌 것은?",
        "options": ["A) 사과", "B) 바나나", "C) 오렌지", "D) 김치"],
        "answer": "D) 김치"
    },
    {
        "question": "35. 도서관에서 할 수 없는 것은?",
        "options": ["A) 책을 읽어요", "B) 조용히 해요", "C) 이야기해요", "D) 공부해요"],
        "answer": "C) 이야기해요"
    },
    {
        "question": "36. 몸이 아플 때 가는 곳은?",
        "options": ["A) 공원", "B) 병원", "C) 극장", "D) 시장"],
        "answer": "B) 병원"
    },
    {
        "question": "37. 시험을 잘 보면 어떻게 말합니까?",
        "options": ["A) 축하해요", "B) 미안해요", "C) 잘 자요", "D) 안녕히 계세요"],
        "answer": "A) 축하해요"
    },
    {
        "question": "38. 친구를 만난 후 헤어질 때 하는 말은?",
        "options": ["A) 안녕히 가세요", "B) 안녕히 주무세요", "C) 여보세요", "D) 감사합니다"],
        "answer": "A) 안녕히 가세요"
    },
    {
        "question": "39. 더운 날씨에는 무엇을 마십니까?",
        "options": ["A) 뜨거운 물", "B) 찬 물", "C) 국", "D) 커피"],
        "answer": "B) 찬 물"
    },
    {
        "question": "40. 다음 중 직업이 아닌 것은?",
        "options": ["A) 선생님", "B) 요리사", "C) 경찰", "D) 모자"],
        "answer": "D) 모자"
    },
    {
        "question": "41. 학교에 갈 때 무엇을 타요?",
        "options": ["A) 자전거", "B) 비행기", "C) 기차", "D) 배"],
        "answer": "A) 자전거"
    },
    {
        "question": "42. 저녁을 먹은 후 하는 일은?",
        "options": ["A) 샤워해요", "B) 점심 먹어요", "C) 아침 먹어요", "D) 공부해요"],
        "answer": "A) 샤워해요"
    },
    {
        "question": "43. 다음 중 시간 표현이 아닌 것은?",
        "options": ["A) 오전", "B) 오후", "C) 어제", "D) 요일"],
        "answer": "D) 요일"
    },
    {
        "question": "44. 친구에게 선물을 주고 싶은 이유는?",
        "options": ["A) 싸웠어요", "B) 생일이에요", "C) 시험이에요", "D) 여행가요"],
        "answer": "B) 생일이에요"
    },
    {
        "question": "45. 비행기를 타려면 어디로 가야 합니까?",
        "options": ["A) 공항", "B) 정류장", "C) 병원", "D) 시장"],
        "answer": "A) 공항"
    },
    {
        "question": "46. 친구와 약속이 있을 때 어떻게 합니까?",
        "options": ["A) 안 가요", "B) 늦게 가요", "C) 약속 장소에 가요", "D) 모른 척해요"],
        "answer": "C) 약속 장소에 가요"
    },
    {
        "question": "47. 집에서 나가기 전에 해야 할 일은?",
        "options": ["A) 문을 열어요", "B) 옷을 갈아입어요", "C) 밥을 안 먹어요", "D) 불을 켜요"],
        "answer": "B) 옷을 갈아입어요"
    },
    {
        "question": "48. 한국의 대표 음식은?",
        "options": ["A) 햄버거", "B) 김치", "C) 피자", "D) 샐러드"],
        "answer": "B) 김치"
    },
    {
        "question": "49. 밤에 잘 때 필요한 것은?",
        "options": ["A) 모자", "B) 안경", "C) 이불", "D) 신발"],
        "answer": "C) 이불"
    },
    {
        "question": "50. 친구를 초대하면 보통 어디로 부릅니까?",
        "options": ["A) 집", "B) 병원", "C) 시장", "D) 학교"],
        "answer": "A) 집"
    }
]
topik_questions_grammar_kor8 = [
{
        "grammar": "1. -도록",
        "meaning": "... qilish uchun / ... bo‘lishi uchun",
        "example": "늦지 않도록 일찍 출발하세요 – Kechikmaslik uchun erta jo‘nang"
    },
    {
        "grammar": "2. -기는 하지만",
        "meaning": "... bo‘lsa ham / ... lekin",
        "example": "맛있기는 하지만 비싸요 – Mazali bo‘lsa ham qimmat"
    },
    {
        "grammar": "3. -았/었으면 좋겠다",
        "meaning": "Iltimos, shunday bo‘lsa edi / umid bildiradi",
        "example": "돈이 많았으면 좋겠어요 – Pulim ko‘p bo‘lsa edi"
    },
    {
        "grammar": "4. -거든요",
        "meaning": "chunki / aslida ... da",
        "example": "오늘 못 가요. 약속이 있거든요 – Bugun bora olmayman. Uchrashuvim bor-da"
    },
    {
        "grammar": "5. -느라고",
        "meaning": "... qilayotganim uchun (salbiy natija)",
        "example": "게임하느라고 숙제를 못 했어요 – O‘yin o‘ynab turib, uy vazifasini bajara olmadim"
    },
    {
        "grammar": "6. -자마자",
        "meaning": "... bilanoq / ... zahoti",
        "example": "집에 도착하자마자 잠들었어요 – Uyga yetib kelishim bilanoq uxlab qoldim"
    },
    {
        "grammar": "7. -ㄴ/는다면",
        "meaning": "... bo‘lsa (faraz)",
        "example": "돈이 많다면 여행을 가고 싶어요 – Agar pulim bo‘lsa, sayohatga bormoqchiman"
    },
    {
        "grammar": "8. -도록 하다",
        "meaning": "... qilishga harakat qilmoq / shunday qilaylik",
        "example": "내일부터 운동하도록 하세요 – Ertadan boshlab mashq qiling"
    },
    {
        "grammar": "9. -다 보니(까)",
        "meaning": "... qilayotganimda shunday bo‘ldi",
        "example": "계속 연습하다 보니까 실력이 늘었어요 – Doimiy mashq qilib turib, ko‘nikmam oshdi"
    },
    {
        "grammar": "10. -ㄹ/을 뿐만 아니라",
        "meaning": "nafaqat ... balki ... ham",
        "example": "그 사람은 친절할 뿐만 아니라 똑똑해요 – U odam nafaqat mehribon, balki aqlli ham"
    },
    {
        "grammar": "11. -아요/어요",
        "meaning": "Hozirgi zamon fe’l shakli",
        "example": "먹어요 – yeyapti / 가요 – ketmoqda"
    },
    {
        "grammar": "12. -았어요/었어요",
        "meaning": "O‘tgan zamon fe’l shakli",
        "example": "봤어요 – ko‘rdim / 먹었어요 – yedim"
    },
    {
        "grammar": "13. -고 있어요",
        "meaning": "Hozirgi davomiy harakat",
        "example": "공부하고 있어요 – O‘qiyapman"
    },
    {
        "grammar": "14. -고 싶어요",
        "meaning": "Xohish bildirish",
        "example": "자고 싶어요 – Uxlamoqchiman"
    },
    {
        "grammar": "15. -지 않아요",
        "meaning": "Inkor (qilmayapti)",
        "example": "가지 않아요 – Bormayapti"
    },
    {
        "grammar": "16. -지 마세요",
        "meaning": "Ta’qiqlash (qilmang)",
        "example": "먹지 마세요 – Yemang"
    },
    {
        "grammar": "17. -을/를",
        "meaning": "To‘g‘ridan-to‘g‘ri maqsad holati (object particle)",
        "example": "빵을 먹어요 – Non yeyapti"
    },
    {
        "grammar": "18. -이/가",
        "meaning": "Yangi ma’lumot / kim? nima?",
        "example": "누가 왔어요? – Kim keldi?"
    },
    {
        "grammar": "19. -은/는",
        "meaning": "Mavzu belgisi (topic particle)",
        "example": "저는 학생이에요 – Men talabaman"
    },
    {
        "grammar": "20. -하고 / -(이)랑",
        "meaning": "... bilan (birga)",
        "example": "친구하고 갔어요 – Do‘stim bilan bordim"
    },
    {
        "grammar": "21. -에 / -에서",
        "meaning": "Joyga / joyda (harakat yo‘nalishi)",
        "example": "학교에 가요 – Maktabga boradi / 집에서 자요 – Uyda uxlaydi"
    },
    {
        "grammar": "22. -도",
        "meaning": "... ham",
        "example": "저도 학생이에요 – Men ham talabaman"
    },
    {
        "grammar": "23. -만",
        "meaning": "Faqat",
        "example": "물만 마셨어요 – Faqat suv ichdim"
    },
    {
        "grammar": "24. -보다",
        "meaning": "... dan (solishtirish)",
        "example": "나보다 키가 커요 – Mendan bo‘yli"
    },
    {
        "grammar": "25. -때문에",
        "meaning": "... sababli",
        "example": "비 때문에 못 갔어요 – Yomg‘ir sababli bora olmadim"
    },
    {
        "grammar": "26. -지만",
        "meaning": "... lekin",
        "example": "바쁘지만 갈게요 – Bandman, lekin boraman"
    },
    {
        "grammar": "27. -거나",
        "meaning": "... yoki ...",
        "example": "먹거나 마셔요 – Yeydi yoki ichadi"
    },
    {
        "grammar": "28. -으러 가다/오다",
        "meaning": "... uchun borish / kelish",
        "example": "공부하러 학교에 가요 – O‘qish uchun maktabga boradi"
    },
    {
        "grammar": "29. -은 후에 / -기 전에",
        "meaning": "... dan keyin / ... dan oldin",
        "example": "먹은 후에 공부해요 – Yegandan so‘ng o‘qiydi"
    },
    {
        "grammar": "30. -아/어야 해요",
        "meaning": "... kerak / ... lozim",
        "example": "공부해야 해요 – O‘qish kerak"
    }
]
topik_questions_grammar_kor9 = [
    {
        "question": "1. '-도록' grammatikasi nimani anglatadi?",
        "options": [
            "A) ...dan keyin",
            "B) ... uchun / ... bo‘lishi uchun",
            "C) ... bo‘lsa edi",
            "D) ... yoki"
        ],
        "answer": "B) ... uchun / ... bo‘lishi uchun"
    },
    {
        "question": "2. '맛있기는 하지만 비싸요' jumlasida '-기는 하지만' nimani bildiradi?",
        "options": [
            "A) ... sababli",
            "B) ... yoki",
            "C) ... lekin / bo‘lsa ham",
            "D) ... uchun"
        ],
        "answer": "C) ... lekin / bo‘lsa ham"
    },
    {
        "question": "3. '-았/었으면 좋겠다' grammatikasi qanday ma'no beradi?",
        "options": [
            "A) Iloji yo‘q",
            "B) Xohish bildirish",
            "C) Tasodifiy holat",
            "D) Iltimos, shunday bo‘lsa edi / umid"
        ],
        "answer": "D) Iltimos, shunday bo‘lsa edi / umid"
    },
    {
        "question": "4. '-고 싶어요' grammatikasi qanday vazifani bajaradi?",
        "options": [
            "A) Bo‘lishsiz gap",
            "B) Xohish bildirish",
            "C) Solishtirish",
            "D) Ruxsat so‘rash"
        ],
        "answer": "B) Xohish bildirish"
    },
    {
        "question": "5. '공부하느라고 늦었어요' deganda '-느라고' qanday ma’no beradi?",
        "options": [
            "A) ... qilish uchun",
            "B) ... sababi bilan (salbiy)",
            "C) ... bo‘lishi mumkin",
            "D) ... bilan birga"
        ],
        "answer": "B) ... sababi bilan (salbiy)"
    },
{
        "question": "6. '공부하고 있어요' jumlasida '-고 있어요' qanday ma’no beradi?",
        "options": [
            "A) O‘tgan zamon",
            "B) Kelajak",
            "C) Hozirgi davomiy harakat",
            "D) Buyruq"
        ],
        "answer": "C) Hozirgi davomiy harakat"
    },
    {
        "question": "7. '-지 마세요' grammatikasi nimani bildiradi?",
        "options": [
            "A) So‘rov",
            "B) Taklif",
            "C) Buyruq",
            "D) Ta’qiqlash"
        ],
        "answer": "D) Ta’qiqlash"
    },
    {
        "question": "8. '친구하고 갔어요' jumlasidagi '-하고' qanday ma’no beradi?",
        "options": [
            "A) Haqida",
            "B) Bilan (birga)",
            "C) O‘rniga",
            "D) Kelajak"
        ],
        "answer": "B) Bilan (birga)"
    },
    {
        "question": "9. '-아/어야 해요' grammatikasi nimani anglatadi?",
        "options": [
            "A) Ruxsat",
            "B) Majburiyat / keraklik",
            "C) Ilmiy fikr",
            "D) Taxmin"
        ],
        "answer": "B) Majburiyat / keraklik"
    },
    {
        "question": "10. '비가 왔지만 갔어요' jumlasidagi '-지만' qanday ma’no beradi?",
        "options": [
            "A) Shuning uchun",
            "B) Agar",
            "C) Bo‘lsa ham / lekin",
            "D) Balki"
        ],
        "answer": "C) Bo‘lsa ham / lekin"
    },
    {
        "question": "11. '-기 전에' degan qo‘shimcha nimani anglatadi?",
        "options": [
            "A) ... dan so‘ng",
            "B) ... dan oldin",
            "C) ... bilan birga",
            "D) ... sababli"
        ],
        "answer": "B) ... dan oldin"
    },
    {
        "question": "12. '저는 학생이에요' jumlasidagi '-은/는' nimani bildiradi?",
        "options": [
            "A) Mavzu belgisi",
            "B) Joy holati",
            "C) Qarama-qarshi",
            "D) Narsa ko‘rsatkichi"
        ],
        "answer": "A) Mavzu belgisi"
    },
    {
        "question": "13. '-았/었어요' grammatikasi qaysi zamonni bildiradi?",
        "options": [
            "A) Hozirgi",
            "B) O‘tgan",
            "C) Kelajak",
            "D) Doimiy"
        ],
        "answer": "B) O‘tgan"
    },
    {
        "question": "14. '돈이 많다면 여행을 가고 싶어요' jumlasidagi '-ㄴ/는다면' nimani bildiradi?",
        "options": [
            "A) Aniqlik",
            "B) Shart / faraz",
            "C) Kelajak",
            "D) O‘tmish"
        ],
        "answer": "B) Shart / faraz"
    },
    {
        "question": "15. '-ㄹ/을 뿐만 아니라' grammatikasi qanday ma’noni beradi?",
        "options": [
            "A) Balki",
            "B) Yana ham",
            "C) Nafaqat ... balki ... ham",
            "D) Taxmin"
        ],
        "answer": "C) Nafaqat ... balki ... ham"
    },
    {
        "question": "16. '계속 연습하다 보니까 실력이 늘었어요' jumlasidagi '-다 보니(까)' nimani bildiradi?",
        "options": [
            "A) Hozirgi holat",
            "B) Orzu",
            "C) Harakat natijasi",
            "D) Taxmin"
        ],
        "answer": "C) Harakat natijasi"
    },
    {
        "question": "17. '비 때문에 못 갔어요' jumlasida '-때문에' nimani bildiradi?",
        "options": [
            "A) Joy",
            "B) Sabab",
            "C) Ob'ekt",
            "D) Oraliq"
        ],
        "answer": "B) Sabab"
    },
    {
        "question": "18. '학교에 가요' jumlasida '-에' qanday rol o‘ynaydi?",
        "options": [
            "A) Harakat manzili (qayerga)",
            "B) Mavzu belgisi",
            "C) Narsani ko‘rsatish",
            "D) Solishtirish"
        ],
        "answer": "A) Harakat manzili (qayerga)"
    },
    {
        "question": "19. '-보다' grammatikasi qaysi vazifani bajaradi?",
        "options": [
            "A) Ruxsat",
            "B) Solishtirish ('... dan')",
            "C) Taxmin",
            "D) Emotsiya"
        ],
        "answer": "B) Solishtirish ('... dan')"
    },
    {
        "question": "20. '-도록 하다' nimani bildiradi?",
        "options": [
            "A) Harakat maqsadi / tavsiya",
            "B) Ta’qiqlash",
            "C) O‘tmish holati",
            "D) Holat solishtiruv"
        ],
        "answer": "A) Harakat maqsadi / tavsiya"
    }
]

# Foydalanuvchi holatlari
user_progress = {}
user_tests = {}
user_scores = {}
grammar_list = {}

# Test nomiga qarab savollarni olish
def get_questions(test_key):
    return {
        'test1': questions_eng1,
        'test2': questions_eng2,
        'test3': questions_eng3,
        'test4': questions_eng4,
        'test5': topik_questions_kor5,
        'test6': topik_questions_kor6,
        'test7': topik_questions_kor7,
        'test8': topik_questions_grammar_kor8,
        'test9': topik_questions_grammar_kor9
    }.get(test_key, [])

# Asosiy menyu
async def show_main_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("🇬🇧 English Tests", callback_data='menu_english')],
        [InlineKeyboardButton("🇰🇷 Korean Tests", callback_data='menu_korean')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("Please select a category:\n카테고리를 선택해 주세요:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Please select a category:\n카테고리를 선택해 주세요:", reply_markup=reply_markup)

# Ingliz testlari menyusi
async def show_english_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("📝 English Test 1", callback_data='test1')],
        [InlineKeyboardButton("📝 English Test 2", callback_data='test2')],
        [InlineKeyboardButton("📝 English Test 3", callback_data='test3')],
        [InlineKeyboardButton("📝 English Test 4", callback_data='test4')],
        [InlineKeyboardButton("⬅️ Orqaga", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text("🇬🇧 Select an English test:", reply_markup=reply_markup)

# Koreys testlari menyusi
async def show_korean_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("🇰🇷 Korean Test 5", callback_data='test5')],
        [InlineKeyboardButton("🇰🇷 Korean Test 6", callback_data='test6')],
        [InlineKeyboardButton("🇰🇷 Korean Test 7", callback_data='test7')],
        [InlineKeyboardButton("🇰🇷 Topik Grammar", callback_data='test8')],
        [InlineKeyboardButton("🇰🇷 Topik Grammar Test ", callback_data='Test9')],
        [InlineKeyboardButton("⬅️ Orqaga", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text("🇰🇷 Select a Korean test:", reply_markup=reply_markup)

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_main_menu(update, context)


# 🆕 Grammatikani ko‘rsatish funksiyasi
async def show_grammar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "📘 <b>Koreys grammatikalari:</b>\n\n"
    for item in grammar_list:
        message += f"🔹 <b>{item['grammar']}</b>\n🧠 Ma’nosi: {item['meaning']}\n📌 Misol: {item['example']}\n\n"

    await update.message.reply_text(message, parse_mode='HTML')

# Savol yuborish
async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, review_mode=False):
    user_id = update.effective_user.id
    index = user_progress.get(user_id, 0)
    test_key = user_tests.get(user_id)
    questions = get_questions(test_key)

    if index >= len(questions):
        score = user_scores.get(user_id, {"correct": 0, "wrong": 0})
        result = f"✅ Test tugadi!\n\nTo‘g‘ri: {score['correct']}\nNoto‘g‘ri: {score['wrong']}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
        await show_main_menu(update, context)
        return

    q = questions[index]

    buttons = [[InlineKeyboardButton(opt, callback_data=opt[0])] for opt in q["options"]] ### shuyerga ham (opt[0])

    # 🔁 Qo‘shimcha tugmalar (orqaga va qaytadan)
    navigation_buttons = []
    if index > 0:
        navigation_buttons.append(InlineKeyboardButton("⬅️ Orqaga", callback_data='back_question'))
    navigation_buttons.append(InlineKeyboardButton("🔄 Qaytadan", callback_data='restart_test'))
    navigation_buttons.append(InlineKeyboardButton("🏠 Bosh menyu", callback_data='main_menu'))
    buttons.append(navigation_buttons)

    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=q["question"], reply_markup=reply_markup)

# Tugmalarni qayta ishlash
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    # Til tanlash menyulari
    if data == 'menu_english':
        await show_english_menu(update, context)
        return
    if data == 'menu_korean':
        await show_korean_menu(update, context)
        return

    # Test tanlovi
    if data.startswith('test'):
        user_tests[user_id] = data
        user_progress[user_id] = 0
        user_scores[user_id] = {"correct": 0, "wrong": 0}
        await send_question(update, context)
        return

    # Orqaga qaytish (oldingi savolga)
    if data == 'back_question':
        if user_progress.get(user_id, 0) > 0:
            user_progress[user_id] -= 1
        await send_question(update, context, review_mode=True)
        return

    # Testni qaytadan boshlash
    if data == 'restart_test':
        user_progress[user_id] = 0
        user_scores[user_id] = {"correct": 0, "wrong": 0}
        await send_question(update, context)
        return

    # Bosh menyuga qaytish
    if query.data == 'main_menu':
        await show_main_menu(update, context)
        return

    # Javobni tekshirish
    test_key = user_tests.get(user_id)
    questions = get_questions(test_key)
    index = user_progress.get(user_id, 0)

    # Indeksni tekshiramiz
    if index >= len(questions):
        await query.edit_message_text("⚠️ Xatolik: Savol topilmadi.")
        await show_main_menu(update, context)
        return

    selected = data
    correct = questions[index[0]]["answer"]### shuyerga [0] qoyiladii javobda korinmaslik uchun

    if selected == correct:
        reply = "✅ To‘g‘ri javob!"
        user_scores[user_id]["correct"] += 1
    else:
        reply = f"❌ Noto‘g‘ri. To‘g‘ri javob: {correct}"
        user_scores[user_id]["wrong"] += 1

    await query.edit_message_text(
        text=f"{questions[index]['question']}\n\nSiz tanladingiz: {selected}\n{reply}"
    )

    user_progress[user_id] = index + 1
    await send_question(update, context)

# Botni ishga tushurish
def main():
    app = ApplicationBuilder().token("8061266773:AAEKneALpb18B01bKlwqhbCFKSv7x38mGt8").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("grammar", show_grammar))
    app.add_handler(CallbackQueryHandler(handle_answer))
    print("✅ Bot ishga tushdi")
    app.run_polling()

if __name__ == "__main__":
    main()
