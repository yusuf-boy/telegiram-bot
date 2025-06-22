from deep_translator import GoogleTranslator

def translate(text):
    # Avtomatik tilni aniqlashga harakat qilamiz
    # Agar matn o‘zbekcha bo‘lsa → inglizchaga, aks holda o‘zbekchaga
    try:
        uzbek_harf = any(c in text.lower() for c in 'қўғҳўўҳҳ')
        target_lang = 'en' if uzbek_harf else 'uz'
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"❌ Xatolik yuz berdi: {e}"