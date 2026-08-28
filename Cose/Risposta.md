Il succo fondamentale di quelle slide (Slide 83, 84 e 85, pagine PDF 79-81) è questo:

> **In alta frequenza l'induttanza non dipende solo dal singolo filo, ma da *DOVE e COME* torna indietro la corrente (percorso di ritorno) e da cosa fanno i fili vicini (accoppiamento magnetico / crosstalk).**

Nel silicio non puoi considerare una pista metallica isolata: ogni corrente che va da qualche parte deve richiudersi a terra (o su un altro filo). A seconda di dove scorre il ritorno e di come commutano i fili adiacenti, **il campo magnetico cambia radicalmente forma, confinando o sparando rumore in tutto il chip**.

Vediamo i tre casi messi a confronto dal professore:

---

### Caso 1: "2 CONDUTTORI" (Slide 83) – Andata su pista, Ritorno sul piano
* **La situazione:** C'è la pista **B** in alto che porta la corrente di andata ($+1\text{ A}$) e il piano conduttivo **A** sotto (il piano di massa o il substrato) che porta il ritorno ($-1\text{ A}$).
* **Cosa vedi nella simulazione:**  
  Il campo magnetico (le linee di flusso colorate) si sviluppa **tra la pista e il piano sottostante**.
* **Il succo:**  
  L'induttanza parassita è proporzionale all'**area del loop** tra andata e ritorno. Più la pista è vicina al piano di massa (distanza $h$ piccola), più il loop è stretto, minore è l'induttanza parassita $L$ e minore è il campo disperso.

---

### Caso 2: "3 CONDUTTORI" con correnti concordi (Slide 84) – Modo Comune / Bus Dati
* **La situazione:** Immagina due piste metalliche vicine (**B** e **C**, come due linee di un bus dati) che commutano insieme nello stesso verso: entrambe portano corrente di andata ($+0.5\text{ A}$ e $+0.5\text{ A}$). Il ritorno comune ($-1\text{ A}$) scorre tutto sul piano inferiore **A**.
* **Cosa vedi nella simulazione:**  
  I campi magnetici generati da B e C girano nello stesso verso e si **fondono/sommano insieme**, creando una "bolla" magnetica gigante che abbraccia entrambi i conduttori.
* **Il succo:**
  * Si crea una **mutua induttanza positiva ($+M$)**: il campo di una pista entra dentro l'altra creando **crosstalk induttivo** (rumore e interferenza tra segnali vicini).
  * L'induttanza totale vista da ciascuna linea **aumenta** ($L_{eff} = L + M$), rallentando la propagazione dei segnali.

---

### Caso 3: "3 CONDUTTORI" con correnti opposte (Slide 85) – Coppia Differenziale
* **La situazione:** Le due piste vicine portano correnti uguali ma **OPPOSTE**: la pista **B** porta l'andata ($+1\text{ A}$) e la pista adiacente **C** porta il ritorno ($-1\text{ A}$). Il piano sottostante **A** ha corrente nulla ($0\text{ A}$).
* **Cosa vedi nella simulazione:**  
  Il campo magnetico si richiude **strettissimo ad anello solo tra B e C**! A destra e a sinistra i due campi magnetici (essendo generati da correnti contrarie a brevissima distanza) **si cancellano a vicenda**. Il piano sotto A non vede quasi campo magnetico.
* **Il succo:**
  * È il principio della **linea differenziale (differential pair)** o del doppino intrecciato.
  * Il campo magnetico è ultra-confinato: **zero rumore iniettato nel substrato** e **zero interferenze verso l'esterno**.
  * L'induttanza equivalente del loop crolla ($L_{diff} \approx 2(L - M)$), permettendo di andare a frequenze altissime.

---

### Perché il professore lo spiega subito prima dell'Induttore a Spirale (Slide 86)?

Per due motivi pratici:
1. **Per capire come funziona l'induttore a spirale:** Un induttore a spirale è fatto proprio da tante piste affiancate (le spire). Poiché la corrente gira nello stesso verso in tutte le spire adiacenti (come nel **Caso 2**), i campi magnetici di ogni spira si sommano costruttivamente facendo crescere l'induttanza con il quadrato del numero di spire ($L \propto n^2$).
2. **Per capire la "sfiga" dell'induttore:** Quella bolla magnetica gigante penetra dritto nel silicio sottostante (come nel Caso 2 verso il piano A), inducendo correnti parassite dissipative (*eddy currents*) nel substrato conduttivo.