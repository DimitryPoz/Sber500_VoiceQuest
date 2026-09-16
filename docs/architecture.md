# Architecture

## Mobile

Flutter is responsible for the game UI, character selection, scene playback, microphone recording and progress screens.

## API

FastAPI handles authentication, scenes, attempts, scoring, XP, achievements and progress.

## AI pipeline

Audio → Speech-to-Text → pronunciation / speech analysis → structured result → LLM feedback → mobile response.

The LLM should generate child-friendly feedback, but pronunciation scoring should rely on a dedicated speech/phonetic signal rather than an LLM alone.

## Data

PostgreSQL stores users, scenes, dialogue lines, attempts, scores, XP and achievements.

S3-compatible storage keeps audio assets.

## Analytics

Track scene starts, completed lines, recording attempts, retries, session duration and voluntary speaking time.
