# 🔑 Переменные для Railway

## ✅ Добавьте эти переменные в Railway

В вашем Railway проекте → **Variables** добавьте:

```bash
TELEGRAM_BOT_TOKEN=<ваш Telegram токен>
OPENAI_API_KEY=<ваш OpenAI ключ>
MONGO_URL=<скопируйте из MongoDB сервиса>
DB_NAME=tarot_bot
```

**Правильные значения:**
- TELEGRAM_BOT_TOKEN: `8551518470:AAG6AbFJwSwqphvIu_xIDHQ4N0v2eO3mEkg`
- OPENAI_API_KEY: `sk-proj--eyR_B...` (ваш полный ключ)
- DB_NAME: `tarot_bot`

---

## 📋 Как добавить MONGO_URL:

1. В Railway проекте добавьте MongoDB:
   - Нажмите **"+ New"** → **"Database"** → **"Add MongoDB"**
   
2. Откройте MongoDB сервис → вкладка **Variables**

3. Найдите переменную `MONGO_URL` (или `MONGO_PRIVATE_URL`)

4. Скопируйте её значение (будет выглядеть как: `mongodb://...`)

5. Добавьте в Variables основного сервиса:
   ```
   MONGO_URL=mongodb://...
   ```

---

## ✅ Проверьте Settings:

### Source:
- ✅ Repository: `AndriiNaidenko/tarot-bot`
- ✅ Branch: `main`
- ✅ Root Directory: **ПУСТОЕ** (важно!)

### Deploy:
- ✅ Start Command: `python main.py`

---

## 🚀 После добавления переменных:

Railway автоматически сделает redeploy.

**В логах должно быть:**
```
✅ MongoDB connected: tarot_bot
✅ 🔮 Tarot Bot starting...
✅ Run polling for bot @taro208_bot
```

---

## 📝 Для второго сервиса (Channel Poster):

Создайте второй сервис:
1. **"+ New"** → **"GitHub Repo"** → `tarot-bot`
2. **Start Command:** `python channel_poster.py`
3. Добавьте **те же 4 переменные**

---

**Готово! После добавления переменных бот заработает! 🎉**
