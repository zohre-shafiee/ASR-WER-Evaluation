# Automatic Speech Recognition (ASR) Evaluation — Word Error Rate

**University group project · NLP / Speech Technology · Python · JiWER**

## Project overview

This project examines the quality of **automatic speech recognition (ASR)** by comparing machine-generated transcripts with manually produced reference transcripts.

The university experiment used the **TADDDAM** transcription system to investigate whether speech from non-native French speakers would produce higher transcription error rates than native speech. This public repository provides a **privacy-safe reproduction of the evaluation workflow**: a reusable WER calculator and entirely fictional sample transcripts. It does not contain original recordings or participant transcripts.

## Research question and protocol

How accurately does an ASR system transcribe spoken French under a controlled description task?

For the course experiment:
- **Four participants** took part: two native and two non-native speakers of French.
- Each observed the same image for **30 seconds**, then described it naturally for about **2–2.5 minutes**.
- Speech was recorded in a **sound-treated room**, using a stationary microphone positioned approximately **30–40 cm** from the speaker.
- Participants provided informed consent before recording; the original files were reserved for the educational research project.
- Recordings were transcribed automatically with **TADDDAM** and compared with manually created orthographic reference transcripts.
- Word-level errors were quantified with the **Word Error Rate (WER)**, followed by a qualitative examination of error types.

The original manual references preserved repetitions and incomplete utterances but omitted most hesitation fillers; TADDDAM outputs often normalized punctuation, repetitions and certain grammatical forms. This difference in transcription conventions is itself a limitation of the comparison.

The small sample supports **exploratory observations only**: it cannot establish a general effect of accent or native-language background.

## Evaluation workflow

```text
Spoken description of an image
              |
              v
        ASR transcription
              |
              +--------------------+
              |                    |
              v                    v
      ASR hypothesis        Manual reference
              |                    |
              +---------+----------+
                        |
                        v
          Text normalization
       lowercase / punctuation /
         whitespace cleanup
                        |
                        v
           Word-level alignment
                  JiWER
                        |
                        v
       Substitutions · Deletions
             · Insertions
                        |
                        v
           Word Error Rate (WER)
```

## Metric

The WER formula is:

```text
WER = (S + D + I) / N
```

Where:

- **S** — substitutions: a reference word is transcribed as a different word;
- **D** — deletions: a reference word is omitted;
- **I** — insertions: a word is added to the hypothesis;
- **N** — number of words in the reference transcript.

For instance, if an invented reference has 17 words and the ASR hypothesis contains one substitution and one deletion, WER is `(1 + 1 + 0) / 17 = 11.76%`.

**A lower WER means fewer word-level recognition errors.** This metric does not on its own capture meaning, downstream usability or all characteristics of fluent speech.

## Implementation

The public `calcul_wer.py` script:

1. Accepts the reference and ASR hypothesis as two UTF-8 text files;
2. Lowercases both transcripts;
3. Replaces punctuation with whitespace and normalizes spaces;
4. Uses JiWER `process_words()` for word-level alignment;
5. Prints WER, substitutions, deletions and insertions.

The script also checks that the normalized reference is not empty.

## Repository structure

```text
.
├── calcul_wer.py
├── requirements.txt
├── test_wer.py
├── examples/
│   ├── reference.txt
│   └── hypothese_asr.txt
├── .github/
│   └── workflows/
│       └── test.yml
└── .gitignore
```

## Reproduce with fictional data

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the public evaluation example:

```bash
python calcul_wer.py examples/reference.txt examples/hypothese_asr.txt
```

The expected example result is:

```text
WER : 11.76 %
Substitutions : 1
Suppressions : 1
Insertions : 0
```

These are **invented example texts**, not student or participant data.

## Automated tests

The repository includes `test_wer.py`, which checks text normalization and expected counts on the fictional example.

```bash
python -m unittest discover -v
```

A GitHub Actions workflow is also configured to install dependencies and run the tests. The presence of the workflow does not guarantee every remote run has passed; check the repository's **Actions** tab for its current status.

## Experimental findings

The university report recorded the following **WER values**. Participant codes, rather than names or individual speech samples, are shown below.

| Participant code | Speech group | WER |
|---|---|---:|
| SA | Native French | 9.96% |
| EL | Native French | 11.46% |
| JI | Non-native French | 12.25% |
| AN | Non-native French | 19.41% |

The two native speakers had lower WERs in this small sample than the two non-native speakers. However, **four recordings are not sufficient to generalize** this finding.

### Error categories and qualitative analysis

The evaluation also examined substitutions, deletions and insertions. The report described more **insertions** in the non-native examples and more **deletions** in the native examples. Possible causes included transcription normalization, hesitation markers, automatically inserted grammatical words and specific audio-processing errors.

The report also documented a **Mann–Whitney U analysis**, with no statistically significant differences for the examined error counts (**p > 0.05**). These findings therefore remain **exploratory**, not evidence of a general native/non-native performance gap.

### What we learned

Word-level error counts reflect more than pronunciation alone. The comparison depends on how manual references and ASR outputs handle disfluencies, repetitions, punctuation and grammatical normalization. This matters when designing a fair evaluation protocol.

## Technologies

- Python 3
- JiWER
- Speech recognition evaluation
- Text normalization and word-level error analysis
- GitHub Actions / `unittest`

## Privacy and ethics

The original recordings and transcriptions were collected for university coursework. This public version deliberately **does not publish**:

- the original audio;
- individual participant identities;
- actual reference or ASR transcripts;
- links between individual results and specific participants.

Only a generic methodology, aggregate range and invented example are made public.

## Limitations and future work

- The study involved **two speakers per group**; future work would need a substantially larger, more diverse sample.
- The non-native speakers had different first languages, so accent-related effects cannot be isolated reliably.
- WER depends on transcription and preprocessing conventions.
- Punctuation is stripped; this evaluation does not separately score punctuation quality.
- The sample of four speakers is too small for broad population conclusions.
- The public repository reproduces the **evaluation metric**, not the original TADDDAM speech recognition model or the entire experimental setup.
- A larger study would need more consistent transcription guidelines and an appropriately reviewed protocol for collecting and storing participant recordings.

## Credits

This project was completed during the **2025–2026 academic year** as part of *Méthodes expérimentales en TAL*, Master's programme in *Sciences du langage — Industrie de la langue*, at **Université Grenoble Alpes**.

**Four-person project team:**
- Camille Benoit-Guyod
- Ombeline Ulbrich-Cloppet
- Jiahong Zhang
- Zohré Shafiee

The experimental design, data collection and analysis were carried out as collaborative coursework. The public code illustrates the WER evaluation process and does not claim that any one member solely authored the entire project.

**Privacy note:** The original report includes signed consent forms and participant information. Those documents, and the original recordings and transcripts, are intentionally **not uploaded** to this public repository.
