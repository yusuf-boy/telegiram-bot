from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

topik_questions_kor1 = [
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
topik_questions_kor2 = []
topik_questions_kor3 = []

# Foydalanuvchi holatlari
user_progress = {}
user_tests = {}
user_scores = {}
grammar_list = {}

# Test nomiga qarab savollarni olish
def get_questions(test_key):
    return {
        'test1': topik_questions_kor1,
        'test2': topik_questions_kor2,
        'test3': topik_questions_kor3,
    }.get(test_key, [])

# Asosiy menyu
async def show_main_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("🇰🇷 Korean Test 1", callback_data='test1')],
        [InlineKeyboardButton("🇰🇷 Korean Test 2", callback_data='test2')],
        [InlineKeyboardButton("🇰🇷 Korean Test 3", callback_data='test3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("카테고리를 선택해 주세요:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("카테고리를 선택해 주세요:", reply_markup=reply_markup)

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
    app.add_handler(CommandHandler("grammar", show_grammar))
    app.add_handler(CallbackQueryHandler(handle_answer))
    print("✅ Bot ishga tushdi")
    app.run_polling()

if __name__ == "__main__":
    main()
