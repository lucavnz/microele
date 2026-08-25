# Regole di Scrittura e Riorganizzazione Appunti Markdown (.md)

Quando l'utente richiede di riscrivere, sistemare, riorganizzare o formattare un blocco di testo o una nota `.md`:

---

### 1. Nessun Contenuto Extra Non Richiesto (Non "allungare il brodo")
* **Attenersi strettamente a ciò che l'utente ha scritto:** non inventare o aggiungere blocchi teorici non menzionati o non richiesti.
* **Legare solo il filo logico:** fare solo le minime modifiche necessarie per collegare i concetti e rendere la spiegazione chiara, scorrevole e comprensibile al 100%.

---

### 2. Mantenere lo Stile Autentico da Appunti Informali
* Preservare il tono diretto, sintetico e informale dell'utente (frasi brevi, analogie intuitive, linguaggio schietto; evitare lo stile accademico prolisso da libro di testo).
* Correggere refusi di battitura (*typo*), grammatica e punteggiatura.

---

### 3. Formattazione Formule in $\LaTeX$
* Formattare sempre tutte le variabili, simboli fisici, unità ed equazioni in $\LaTeX$:
  * Inline: `$V_{th}$`, `$I_D$`, `$g_m$`, `$r_o$`, `$R_{th}$`, `$\lambda$`, ecc.
  * In blocco: `$$\Delta T = R_{th} \cdot P_d$$`

---

### 4. Esplorazione Repository, Link Contestuali e Backlinking (Obsidian & Preview)
* **Esplorazione attiva della repository (Prendersi il tempo di indagare):**
  * Prima di finalizzare una nota o aggiungere link, **esplora l'intera repository e ispeziona gli altri file `.md`** presenti nelle varie cartelle (`Introduzione/`, `Tecnologie/`, `Effetti di canale corto/`, ecc.).
  * Comprendi la mappa concettuale complessiva per capire esattamente *chi deve essere collegato a chi*.
* **Link nel corpo del testo:** inserire i link direttamente **nel punto esatto in cui viene citato il concetto** (es. inline nella frase o con richiamo `👉 Approfondimento: [Nome](./percorso/file.md)`), oltre alla sezione `*Pagine correlate:*` a fondo pagina.
* **Aggiornamento Bidirezionale delle Pagine Collegate (Backlinking Attivo):**
  * Quando crei o modifichi una pagina $A$ e aggiungi un link verso una pagina esistente $B$, **controlla anche la pagina $B$**: se nel testo di $B$ c'è un passaggio in cui si parla dell'argomento di $A$, inserisci il link contestuale verso $A$ nel testo di $B$ e aggiorna le sue `*Pagine correlate:*`.
* **Solo file ESISTENTI e strettamente PERTINENTI:**
  * **ZERO allucinazioni:** collegare **solo ed esclusivamente** file che esistono realmente nel workspace.
  * **ZERO link a caso:** collegare solo note che hanno un'effettiva correlazione logica/tecnica con il tema trattato.
* **Sintassi Relativa Obbligatoria:**
  * Utilizzare **esclusivamente link relativi standard Markdown**:
    * Es. `./Effetti%20di%20canale%20corto/DIBL.md` oppure `../Introduzione/Integrati%20protetti%20da%20interferenze.md`
    * Sostituire gli spazi nei nomi file con `%20`.
    * **MAI** usare percorsi assoluti come `file:///...`.

---

### 5. Esempi di Riferimento nel Repository
Prima di formattare una nota, prendere a modello la struttura, i titoli (`###`) e la pulizia dei file già consolidati:
* `Microelettronica/Introduzione/Integrati protetti da interferenze.md`
* `Microelettronica/Introduzione/Resistenza termica.md`
* `Microelettronica/Tecnologie/Difficoltà nel fare un componente ideale.md`
* `Microelettronica/Tecnologie/Resistore.md`
* `Microelettronica/Introduzione/Analogico non si scende di dimensioni.md`
