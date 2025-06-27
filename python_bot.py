from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

topik_questions_kor1 = [
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

topik_questions_kor2 = [
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
topik_questions_kor3 = [
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
topik_questions_grammar_kor4 = [
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
topik_questions_grammar_kor5 = [
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
        # 'test1': questions_eng1,
        # 'test2': questions_eng2,
        # 'test3': questions_eng3,
        # 'test4': questions_eng4,
        'test1': topik_questions_kor1,
        'test2': topik_questions_kor2,
        'test3': topik_questions_kor3,
        'test4': topik_questions_grammar_kor4,
        'test5': topik_questions_grammar_kor5
    }.get(test_key, [])

# Asosiy menyu
async def show_main_menu(update, context):
    keyboard = [
        # [InlineKeyboardButton("🇬🇧 English Tests", callback_data='menu_english')],
        [InlineKeyboardButton("🇰🇷 Korean Tests", callback_data='menu_korean')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("카테고리를 선택해 주세요:", reply_markup=reply_markup)

# Ingliz testlari menyusi
# async def show_english_menu(update, context):
#     keyboard = [
#         [InlineKeyboardButton("📝 English Test 1", callback_data='test1')],
#         [InlineKeyboardButton("📝 English Test 2", callback_data='test2')],
#         [InlineKeyboardButton("📝 English Test 3", callback_data='test3')],
#         [InlineKeyboardButton("📝 English Test 4", callback_data='test4')],
#         [InlineKeyboardButton("⬅️ Orqaga", callback_data='main_menu')],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.callback_query.edit_message_text("🇬🇧 Select an English test:", reply_markup=reply_markup)

# Koreys testlari menyusi
async def show_korean_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("🇰🇷 Korean Test 1", callback_data='test1')],
        [InlineKeyboardButton("🇰🇷 Korean Test 2", callback_data='test2')],
        [InlineKeyboardButton("🇰🇷 Korean Test 3", callback_data='test3')],
        [InlineKeyboardButton("🇰🇷 Topik Grammar", callback_data='test')],
        [InlineKeyboardButton("🇰🇷 Topik Grammar Test ", callback_data='Test')],
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

    # Til tanlash menyulari
    # if data == 'menu_english':
    #     # await show_english_menu(update, context)
    #     # return
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
    correct = questions[index]["answer"] ### shuyerga [0] oxiriga qoyiladii javobda korinmaslik uchun

    # Avval progress'ni yangilaymiz
    user_progress[user_id] = index + 1

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
