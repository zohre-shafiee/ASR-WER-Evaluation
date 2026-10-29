# Automatic Speech Recognition (ASR) Evaluation — Word Error Rate

**University group project · NLP / Speech Technology · Python · JiWER**

## Project overview

This project examines the quality of **automatic speech recognition (ASR)** by comparing machine-generated transcripts with manually produced reference transcripts.

The university experiment used the **Tadddam** transcription system. This public repository provides a **privacy-safe reproduction of the evaluation workflow**: a reusable WER calculator and entirely fictional sample transcripts. It does not contain original recordings or participant transcripts.

## Research question and protocol

How accurately does an ASR system transcribe spoken French under a controlled description task?

For the course experiment:
- Four speakers described the same picture in French.
- The group included both native and non-native speakers of French.
- The recording task and conditions were designed to be comparable.
- Automatic transcripts were compared against manual reference transcripts.
- Word-level recognition errors were quantified with the **Word Error Rate (WER)**.

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

## Experiment results

In the original course project, the WERs of the four analyzed productions ranged from **9.96% to 19.41%**.

These aggregate figures are included only as a summary of the university report. With four productions, differences should not be interpreted as statistically representative.

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

## Limitations

- WER depends on transcription and preprocessing conventions.
- Punctuation is stripped; this evaluation does not separately score punctuation quality.
- The sample of four speakers is too small for broad population conclusions.
- The public repository reproduces the **evaluation metric**, not the original Tadddam speech recognition model or the entire experimental setup.

## Credits

This was a **group university project** in *Méthodes d’expérimentation en TAL* at Université Grenoble Alpes. The public code illustrates the WER calculation without claiming sole authorship of the overall experiment.
