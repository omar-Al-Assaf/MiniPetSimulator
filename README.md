## MiniPetSimulator

في البداية أنشأنا الكود بملفين:
- pet.py
- main.py

بعدها أنشأنا الفروع:
- main
- development
- production

ثم أضفنا ميزتين في فرعين مختلفين:
- feature/feed-pet
- feature/play-with-pet

المشكلة التي ظهرت كانت merge conflict لأننا عدلنا نفس الملفات في الفرعين وهي:
- pet.py
- main.py

قمنا بحل المشكلة يدويًا، ودمجنا التعديلين مع بعض حتى يبقى البرنامج يعمل بشكل صحيح.


في النهاية دمجنا النسخة النهائية في production

لتشغيل المشروع:
في bash اكتب
py main.py
