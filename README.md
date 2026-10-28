# Évaluation d'un système de reconnaissance automatique de la parole (ASR)

Projet universitaire réalisé en équipe dans le cadre du cours *Méthodes d’expérimentation en TAL* (Université Grenoble Alpes).

## Objectif

Évaluer les transcriptions produites par le système ASR **Tadddam**, en les comparant à des transcriptions manuelles de référence, à l'aide du **Word Error Rate (WER)**.

## Méthode

Quatre personnes ont réalisé une même tâche de description orale d'une image en français, dans des conditions d'enregistrement comparables. Le protocole comprenait des personnes francophones natives et non natives. Pour chaque production, les transcriptions automatiques ont été comparées aux références manuelles après la mise en minuscules, la suppression de la ponctuation et la normalisation des espaces.

La mesure WER correspond à `(substitutions + suppressions + insertions) / nombre de mots de la référence`.

## Résultats du projet universitaire

Les résultats récapitulés dans le document de projet se situent entre **9,96 % et 19,41 % de WER** sur les quatre productions analysées. L'échantillon est réduit ; les différences observées ne permettent pas de conclure à un effet général du statut natif/non natif ou de l'accent.

## Reproduction avec des données fictives

**Important : les deux exemples fournis ici sont inventés.** Ils servent uniquement à démontrer le calcul ; ce ne sont pas des données recueillies auprès des participantes.

```bash
python -m pip install -r requirements.txt
python calcul_wer.py examples/reference.txt examples/hypothese_asr.txt
```

Le script affiche le WER et le nombre de substitutions, suppressions et insertions.

## Technologies

Python, [JiWER](https://github.com/jitsi/jiwer), reconnaissance automatique de la parole, évaluation des transcriptions.

## Éthique et confidentialité

La collecte initiale était destinée à un usage pédagogique. **Les enregistrements, les transcriptions réelles, les noms, les pseudonymes des participantes et la correspondance avec leurs résultats individuels ne sont pas publiés.** Le script public reprend la méthode de calcul du WER et les fichiers d'entrée sont fictifs.

## Limites

Échantillon de quatre productions, contexte expérimental limité, influence possible du débit, des hésitations ou des caractéristiques du système ASR. Les résultats sont exploratoires.

## Crédits

Travail de groupe réalisé dans un cadre universitaire. Cette version publique présente uniquement la méthode de calcul du WER, sans prétendre représenter l'intégralité des contributions individuelles du groupe.
