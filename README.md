# 🐟 Stormo

**Forecasts with AI agent swarms, right from your phone · Previsioni con sciami di agenti IA dal telefono · Прогнозы с помощью роя ИИ-агентов прямо с телефона**

**▶ Live: https://bossartemii.github.io/Stormo/**

[English](#english) · [Italiano](#italiano) · [Русский](#русский)

---

## English

Stormo is a lightweight, mobile-first alternative to [MiroFish](https://github.com/666ghj/MiroFish). Paste a news story, press release, post or product description. The app creates a group of simulated people (AI agents), each with their own age, job, character and opinion. The agents discuss it round after round: they post, reply, like and change their minds. At the end an AI analyst writes a **forecast report**.

MiroFish needs Python, Docker, a graph database and a powerful computer. Stormo is **a single web page**. The UI is available in **English, Italian and Russian** (IT/EN/RU switch at the top).

### Features
- 📝 Scenario: paste text or load a `.txt`, pick the question, the platform, 4–40 agents and 1–8 rounds
- 🌊 Live simulation: social-style feed with threaded replies, opinion-over-time chart, for / undecided / against split
- ⚡ Event injection: add a new fact mid-simulation and watch how agents react
- 👥 Agents: profile, opinion shift, posts, and a chat **interview**
- 📊 Report: summary, forecast with probability, turning points, factions, risks, recommendations. Export `.md` / `.json` or share
- 🌍 Simulation language can differ from the UI language (IT, EN, RU, RO, ES, FR, DE)
- 💾 Last 10 simulations saved on the device · 📱 installable PWA · 🧪 Demo mode with no key

### Ways to run it
| Where | How |
|---|---|
| **Any browser, online** | GitHub Pages (see below) |
| **Android with Termux** | `pkg install python git` → `git clone https://github.com/bossartemii/Stormo` → `cd stormo` → `sh start.sh` → opens `http://localhost:8080` |
| **PC (macOS / Linux)** | `sh start.sh` or `python3 server.py` |
| **PC (Windows)** | double-click `start.bat` |
| **Offline, no server** | just open `index.html` (no install-as-app and no proxy) |

`server.py` uses only the Python standard library. Options: `--port 9000`, `--lan` (reach it from other devices on your Wi-Fi), `--no-open`.
When Stormo is opened through `server.py`, the **local proxy** turns on automatically (Settings → "Use the local server as a proxy"). It forwards AI requests from the server instead of the browser, which avoids CORS blocks from some providers.

**Termux tips:** keep Termux running in the background (`termux-wake-lock`). To run a local model, install Ollama in Termux and choose *Custom* → `http://localhost:11434/v1`.

### AI engines
Groq (free tier) · Google Gemini (free tier) · OpenAI · Anthropic Claude · OpenRouter · DeepSeek · Custom (any OpenAI-compatible API, e.g. Ollama). Model names can be edited in Settings. Your key stays on your device.
Approximate number of AI calls: `agents/15 + rounds × agents/6 + 1` (12 agents × 4 rounds ≈ 10 calls).

### Publish on GitHub Pages (works from a phone too)
1. Create a new public repository, e.g. `stormo`
2. **Add file → Upload files** and upload every file in this folder
3. **Settings → Pages → Deploy from a branch → `main` / root → Save**
4. After a minute: `https://YOURNAME.github.io/stormo/` → browser menu → **Add to Home screen**

---

## Italiano

Stormo è un'alternativa leggera e pensata per il telefono a [MiroFish](https://github.com/666ghj/MiroFish). Incolli una notizia, un comunicato, un post o la descrizione di un prodotto. L'app crea un gruppo di persone simulate (agenti IA), ognuna con età, lavoro, carattere e opinione propri. Gli agenti ne discutono round dopo round: postano, rispondono, mettono like e cambiano idea. Alla fine un analista IA scrive un **report di previsione**.

L'interfaccia è in **italiano, inglese e russo** (selettore IT/EN/RU in alto).

### Come avviarla
| Dove | Come |
|---|---|
| **Qualsiasi browser, online** | GitHub Pages (vedi sotto) |
| **Android con Termux** | `pkg install python git` → `git clone https://github.com/bossartemii/Stormo` → `cd stormo` → `sh start.sh` → si apre `http://localhost:8080` |
| **PC (macOS / Linux)** | `sh start.sh` oppure `python3 server.py` |
| **PC (Windows)** | doppio clic su `start.bat` |
| **Offline, senza server** | apri direttamente `index.html` (senza installazione come app e senza proxy) |

`server.py` usa solo la libreria standard di Python. Opzioni: `--port 9000`, `--lan` (raggiungibile da altri dispositivi sul tuo Wi-Fi), `--no-open`.
Quando apri Stormo tramite `server.py`, il **proxy locale** si attiva da solo (Impostazioni → "Usa il server locale come proxy"). Le richieste all'IA partono dal server invece che dal browser, così si evitano i blocchi CORS di alcuni fornitori.

**Consigli per Termux:** tieni Termux attivo in background (`termux-wake-lock`). Per un modello locale installa Ollama in Termux e scegli *Personalizzato* → `http://localhost:11434/v1`.

### Pubblicarla su GitHub Pages (anche dal telefono)
1. Crea un nuovo repository pubblico, es. `stormo`
2. **Add file → Upload files** e carica tutti i file di questa cartella
3. **Settings → Pages → Deploy from a branch → `main` / root → Save**
4. Dopo un minuto: `https://TUONOME.github.io/stormo/` → menu del browser → **Aggiungi a schermata Home**

Motori IA, funzioni e costi: vedi la sezione inglese qui sopra.

---

## Русский

Stormo — лёгкая альтернатива [MiroFish](https://github.com/666ghj/MiroFish), созданная для телефона. Вставьте новость, пресс-релиз, пост или описание продукта. Приложение создаёт группу симулированных людей (ИИ-агентов), у каждого свой возраст, профессия, характер и мнение. Агенты обсуждают тему раунд за раундом: пишут посты, отвечают, ставят лайки и меняют мнение. В конце ИИ-аналитик пишет **отчёт-прогноз**.

Интерфейс на **русском, английском и итальянском** (переключатель IT/EN/RU вверху).

### Как запустить
| Где | Как |
|---|---|
| **Любой браузер, онлайн** | GitHub Pages (см. ниже) |
| **Android с Termux** | `pkg install python git` → `git clone https://github.com/bossartemii/Stormo` → `cd stormo` → `sh start.sh` → откроется `http://localhost:8080` |
| **ПК (macOS / Linux)** | `sh start.sh` или `python3 server.py` |
| **ПК (Windows)** | двойной клик по `start.bat` |
| **Офлайн, без сервера** | просто откройте `index.html` (без установки как приложения и без прокси) |

`server.py` использует только стандартную библиотеку Python. Параметры: `--port 9000`, `--lan` (доступ с других устройств в вашей сети Wi-Fi), `--no-open`.
Если Stormo открыт через `server.py`, **локальный прокси** включается автоматически (Настройки → «Использовать локальный сервер как прокси»). Запросы к ИИ идут с сервера, а не из браузера, поэтому CORS-блокировки некоторых провайдеров не мешают.

**Советы для Termux:** держите Termux активным в фоне (`termux-wake-lock`). Для локальной модели установите Ollama в Termux и выберите *Свой* → `http://localhost:11434/v1`.

### Публикация на GitHub Pages (можно с телефона)
1. Создайте новый публичный репозиторий, например `stormo`
2. **Add file → Upload files** и загрузите все файлы из этой папки
3. **Settings → Pages → Deploy from a branch → `main` / root → Save**
4. Через минуту: `https://ВАШНИК.github.io/stormo/` → меню браузера → **Добавить на главный экран**

ИИ-движки, функции и стоимость — см. английский раздел выше.

---

Stormo is written from scratch and contains no MiroFish code. · License: MIT
