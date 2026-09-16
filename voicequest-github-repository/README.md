# VoiceQuest

AI-powered language learning through character voice acting.

## Idea

VoiceQuest turns language practice into a game. A child chooses a character and a scene, listens to a line, records their voice, and receives friendly AI feedback on pronunciation, fluency and delivery.

## Core loop

Choose character → choose scene → listen → record → AI analysis → friendly feedback → repeat → reward → continue.

## MVP

- Flutter mobile app
- Python + FastAPI backend
- PostgreSQL
- S3-compatible media storage
- Speech-to-Text
- Pronunciation analysis
- LLM-generated child-friendly feedback
- XP, achievements and progress
- Parent progress screen
- Basic analytics

## Team

**Пожаров Дмитрий**  
Product Manager, AI / Backend Developer

**Шабаев Кирилл**  
Mobile / Frontend Developer, UX/UI

## Repository structure

```text
voicequest/
├── apps/
│   └── mobile/              # Flutter application
├── services/
│   └── api/                 # FastAPI backend
├── docs/                    # Product and technical documentation
├── content/                 # Characters, scenes and dialogue
├── infra/                   # Local/dev infrastructure
├── .github/
│   └── workflows/           # CI
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Local development

### Backend

```bash
cd services/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Mobile

```bash
cd apps/mobile
flutter pub get
flutter run
```

### Infrastructure

```bash
docker compose up -d
```

## 4-week MVP plan

### Week 1
Product, UX/UI, architecture, Flutter/FastAPI setup, characters and scenes.

### Week 2
Character and scene selection, audio playback, voice recording, STT and first speech-analysis loop.

### Week 3
AI feedback, retries, XP, achievements, progress and basic adaptation.

### Week 4
Testing, bug fixing, analytics, content polishing and Sber 500 demo preparation.

## Product principle

The main metric is not screen time. It is how much language the child voluntarily speaks.
