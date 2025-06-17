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
        "options": ["A) Emphasized syllables", "B) Unstressed syllables", "C) Word-final vowels", "D) Consonant clusters"],
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
        "options": ["A) Intonation differences", "B) Contrastive phonemes", "C) Suprasegmental stress", "D) Allophonic variation"],
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
    "options": ["A) Deletion of vowels", "B) Overlapping of speech sounds in production", "C) Changing stress", "D) Syllable division"],
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
        "options": ["A) The nasal cavity", "B) The area behind the tongue", "C) The space between the vocal folds", "D) The alveolar ridge"],
        "answer": "C) The space between the vocal folds"
    },
    {
        "question": "72. Which of the following is a central vowel?",
        "options": ["A) /iː/", "B) /ɜː/", "C) /æ/", "D) /uː/"],
        "answer": "B) /ɜː/"
    },
    {
        "question": "73. The onset of a syllable refers to:",
        "options": ["A) The initial consonant(s) before the vowel", "B) The main vowel", "C) The final consonant", "D) A suprasegmental element"],
        "answer": "A) The initial consonant(s) before the vowel"
    },
    {
        "question": "74. What is the articulatory feature of /h/?",
        "options": ["A) Voiced stop", "B) Nasal plosive", "C) Voiceless glottal fricative", "D) Voiced bilabial fricative"],
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
        "options": ["A) Strengthening a sound", "B) Weakening a sound", "C) Voicing a sound", "D) Aspiration of a sound"],
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
        "options": ["A) Allophonic variation", "B) Sounds that signal a change in meaning", "C) Stress placement", "D) Phonotactics"],
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
        "options": ["A) First syllable stressed", "B) Second syllable stressed", "C) Third syllable stressed", "D) All syllables stressed equally"],
        "answer": "B) Second syllable stressed"
    },
    {
        "question": "93. A phonemic transcription differs from a phonetic transcription in that it:",
        "options": ["A) Uses slashes and omits fine detail", "B) Uses brackets and shows exact pronunciation", "C) Only marks vowels", "D) Uses numbers"],
        "answer": "A) Uses slashes and omits fine detail"
    },
    {
        "question": "94. In syllable structure, what is a coda?",
        "options": ["A) Initial consonant(s)", "B) Final consonant(s)", "C) Vowel nucleus", "D) Suprasegmental element"],
        "answer": "B) Final consonant(s)"
    },
    {
        "question": "95. What feature do all approximants share?",
        "options": ["A) Complete oral closure", "B) Minimal obstruction to airflow", "C) Nasality", "D) Vocal fold vibration"],
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
        "options": ["A) Stress patterns", "B) Rules about permissible sound combinations in a language", "C) Vowel length rules", "D) Nasal assimilation"],
        "answer": "B) Rules about permissible sound combinations in a language"
    }
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
        "options": ["A) 13th century", "B) Early 14th century", "C) Late 15th to early 16th century",
                    "D) 12th century"],
        "answer": "C) Late 15th to early 16th century"
    },
    {
        "question": "42. National English was based on which dialect?",
        "options": ["A) Northern", "B) Southern", "C) East Midland", "D) West Saxon"],
        "answer": "C) East Midland"
    },
    {
        "question": "43. Which of the following developed from Vulgar Latin?",
        "options": ["A) Old English", "B) Old Norse", "C) French", "D) Gothic"],
        "answer": "C) French"
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

questions_eng4 = []

questions_kor5 = []

questions_kor6 = []

# Foydalanuvchi holatlari
user_progress = {}
user_tests = {}
user_scores = {}


# Test nomiga qarab savollarni olish
def get_questions(test_key):
    return {
        'test1': questions_eng1,
        'test2': questions_eng2,
        'test3': questions_eng3,
        'test4': questions_eng4,
        'test5': questions_kor5,
        'test6': questions_kor6,
    }.get(test_key, [])


# Asosiy menyu
async def show_main_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("📝 English Test 1", callback_data='test1')],
        [InlineKeyboardButton("📝 English Test 2", callback_data='test2')],
        [InlineKeyboardButton("📝 English Test 3", callback_data='test3')],
        [InlineKeyboardButton("📝 English Test 4", callback_data='test4')],
        [InlineKeyboardButton("🇰🇷 Korean Test 5", callback_data='test5')],
        [InlineKeyboardButton("🇰🇷 Korean Test 6", callback_data='test6')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("Please select a test:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Please select a test:", reply_markup=reply_markup)


# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_main_menu(update, context)


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

    buttons = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in q["options"]] ### shuyerga ham (opt[0])

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
    correct = questions[index]["answer"]### shuyerga [0] qoyiladii javobda korinmaslik uchun

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
    app.add_handler(CallbackQueryHandler(handle_answer))
    print("✅ Bot ishga tushdi")
    app.run_polling()


if __name__ == "__main__":
    main()
