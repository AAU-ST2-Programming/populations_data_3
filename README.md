# Supervised learning: klassifikation

- **Lecture specific files**: files/* - `En mappe som indeholder filer I skal bruge i forbindelse med forlæsningen.`

---

## Forberedelse til lektionen

Følg denne guide nøje for at være klar til undervisningen:

### 1. Literatur

**Primær litteratur:**
- Python-basics (fx lister, funktioner, løkker og simple datastrukturer) forudsættes kendt.
- [Data Wrangling with Python af Jacek Gołębiewski (PDF)](https://datawranglingpy.gagolewski.com/datawranglingpy.pdf)
  - 12.3 Classification tasks 

**Supplerende litteratur:**
- [GeeksforGeeks: K-Nearest Neighbors (KNN) Algorithm](https://www.geeksforgeeks.org/k-nearest-neighbours/)
- [TutorialsPoint: Machine Learning - KNN](https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_knn_algorithm_finding_nearest_neighbors.htm)
- [scikit-learn: model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [scikit-learn: KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

**Undervisningsmateriale i repo:**
- [Notebook: populations_data_3.ipynb](./populations_data_3.ipynb)
  - Bruges som forelæsningsnoter og in-class gennemgang

**Formål:** Forstå hvordan klassifikationsmodeller trænes, evalueres og fortolkes på populationsdata.

---

### 2. Installationer og opsætning
- Følg denne guide for at installere Python:  
  [Install Python Guide](https://github.com/AAU-Python-Guides/install_python_guide)
- Følg denne guide for at sætte VS Code op til Python:  
  [VS Code for Python Guide](https://github.com/AAU-Python-Guides/visual_studio_code_for_python)
- Installer følgende extensions i Visual Studio Code:
  - `Python`
  - `jupyter`

### 3. Download materialet
> ```zsh
> cd ~
> git clone https://github.com/AAU-ST2-Programming/populations_data_3.git
> cd populations_data_3
> git pull
> ```

---

## Lektionens fokus

- Supervised learning til klassifikation
- k-NN og betydningen af valg af k
- Feature-skalering og dens effekt på afstandsbaserede modeller
- Beslutningsgrænser og visuel fortolkning af modeller
- Modelevaluering og krydsvalidering

---

## Forventninger til forberedelse og undervisning

- **Før/efter kursusgang:**
  - Gennemgå tidligere kursusgange (vi bygger videre hver gang)
  - Læs nyt materiale som beskrevet ovenfor
- **Tidsforbrug:**
  - 4 timers forberedelse (hjemme, før undervisning)
  - 4 timers undervisning og gruppeopgaver
  - 4 timers individuel opgaveregning (hjemme, efter undervisning)

---

## Spørgsmål og opgaver

- Til hver opgave i undervisningen vil der være:
  - En opgavebeskrivelse
  - En guide til hvordan opgaven løses
  - Svar på opgaven
- Opgaverne bliver gradvist sværere og bygger på tidligere lektioner.
- Til eksamen vil der kun være en opgavebeskrivelse – du skal selv kunne vurdere, hvordan opgaven løses.
