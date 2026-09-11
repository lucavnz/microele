Viewed page_12_Im11.png:1-800
Ran command: `python3 -c "
from PIL import Image

img = Image.open('/Users/matteoluca/.gemini/antigravity-ide/brain/a4ca2f00-ca5a-433b-8ecd-2b325a4ebb0f/scratch/page_10_Im10.png')
w, h = img.size
print('Size:', w, h)
# crop bottom left, middle, bottom right
img.crop((0, int(h*0.4), int(w*0.6), h)).save('/Users/matteoluca/.gemini/antigravity-ide/brain/a4ca2f00-ca5a-433b-8ecd-2b325a4ebb0f/scratch/p10_bottom_left.png')
img.crop((int(w*0.5), int(h*0.4), w, h)).save('/Users/matteoluca/.gemini/antigravity-ide/brain/a4ca2f00-ca5a-433b-8ecd-2b325a4ebb0f/scratch/p10_bottom_right.png')
print('Cropped successfully')
"`
Viewed p10_bottom_left.png:1-800
Viewed p10_bottom_right.png:1-800

Il **Recycling Folded Cascode (RFC)** (presentato nelle slide 9, 10 e 11) è un'evoluzione brillante del Folded Cascode classico. 

Nasce da una domanda molto pragmatica che i progettisti si sono posti:
> *"Nel Folded Cascode classico usiamo due generatori di corrente verso massa che ci costano tantissima corrente statica e rumore, ma per il segnale AC non fanno assolutamente nulla (sono spenti). Possiamo **riciclare** quei transistor e la loro corrente per farli partecipare all'amplificazione?"*

Vediamo nel dettaglio **perché si fa**, **qual è l'idea chiave**, **come funziona** e **quali sono i vantaggi e compromessi**.

---

### 1. Il problema del Folded Cascode Classico (Slide 9)

Nel Folded Cascode standard (Slide 9 a sinistra):
* I due generatori di corrente in basso verso massa ($I_{sink}$) hanno il gate a una tensione DC fissa.
* Hanno il solo scopo di assorbire corrente di polarizzazione per i nodi di folding.
* **Per il segnale AC sono rami "morti"**: non amplificano nulla, ma consumano corrente statica e iniettano il loro rumore termico/flicker all'uscita.

L'idea del *Recycling*: **sostituire quei generatori passivi con specchi di corrente attivi**, creando un **secondo percorso di segnale** che va a sommarsi a quello principale.

---

### 2. Come funziona lo schema (Slide 10)

Per far partecipare quei generatori all'amplificazione, il circuito viene modificato in due punti cruciali:

#### A) La coppia differenziale d'ingresso viene sdoppiata in 4 transistor
Nel classico avevi solo $M_1$ e $M_2$ (con corrente totale di coda $2I_B$, cioè $I_B$ per ciascuno).  
Nel Recycling, ogni ramo d'ingresso viene diviso a metà:
* L'ingresso $V_{IN}^+$ pilota **$M_1$** e **$M_3$** (ciascuno porta $I_B/2$).
* L'ingresso $V_{IN}^-$ pilota **$M_2$** e **$M_4$** (ciascuno porta $I_B/2$).

#### B) I generatori in basso diventano specchi di corrente con guadagno $1 : K$
* I transistor $M_1$ e $M_2$ scaricano direttamente sui nodi di folding principali (come nel folded normale).
* I transistor $M_3$ e $M_4$, invece, scaricano la loro corrente sui rami a diodo di due specchi di corrente NMOS posti in basso.
* Questi specchi hanno un rapporto d'area **$1 : K$** (in genere $K = 3$):
  - Il ramo a diodo (dimensione $1$) riceve la corrente di segnale di $M_3$ o $M_4$.
  - Il ramo d'uscita dello specchio (dimensione $K$) **moltiplica la corrente di segnale per $K$** e la inietta nel nodo di folding opposto (connessione incrociata).

---

### 3. I due percorsi di segnale che si sommano (Slide 12)

Quando applichi un segnale differenziale $v_{in}$, adesso all'uscita arrivano **due percorsi in parallelo**:
1. **Percorso Diretto**: il segnale passa attraverso la coppia d'ingresso principale ($M_1, M_2$) e viene ripiegato nel cascode.
2. **Percorso Riciclato**: il segnale passa attraverso l'altra metà della coppia ($M_3, M_4$), entra nello specchio in basso, viene **amplificato di un fattore $K$**, e viene iniettato nel cascode.

Poiché le connessioni sono incrociate, le correnti dei due percorsi **si sommano in fase**.

La transconduttanza totale equivalente ($G_m$) diventa:
$$G_{m,RFC} \approx \frac{g_m}{2} + K \frac{g_m}{2} = g_m \left(\frac{1 + K}{2}\right)$$

---

### 4. Vantaggi: Cosa si ottiene con $K = 3$? (Slide 11)

La slide 11 dice una cosa fondamentale:
> *"Con $K = 3$ il consumo di corrente resta lo stesso del folded cascode classico, ma guadagno, banda e Slew Rate migliorano."*

Facciamo i conti con $K = 3$:
1. **Transconduttanza raddoppiata ($G_m \approx 2 \cdot g_m$):**
   $$G_{m,RFC} = g_m \left(\frac{1 + 3}{2}\right) = 2 \cdot g_m$$
2. **Guadagno in tensione raddoppiato ($+6\text{ dB}$):**
   $$A_v = G_m \cdot R_{out} \approx 2 \times A_{v,classico}$$
   Ottieni il doppio del guadagno a parità di resistenza di uscita e senza spendere $1\ \mu\text{A}$ in più di corrente totale!
3. **Banda a guadagno unitario raddoppiata ($GBW$):**
   $$GBW = \frac{G_m}{2\pi C_L}$$
   Raddoppiando $G_m$, la frequenza di taglio a guadagno unitario raddoppia.
4. **Slew Rate molto più alto:**
   A grande segnale, lo specchio moltiplica la corrente di scarica della capacità di carico per un fattore $K$, velocizzando enormemente le transizioni rapide.

---

### 5. Perché non scegliere un $K$ enorme (es. $K = 10$)? I compromessi (Slide 11)

Slide 11 sottolinea:
> *"Il valore di K influenza il guadagno (...) ma anche il margine di fase (maggiore è K, minore è il PM), quindi viene scelto come compromesso tra 2 e 4."*

* **Peggioramento del Margine di Fase (PM):**  
  Lo specchio di corrente $1 : K$ aggiunge un nodo interno (il drain del transistor a diodo). Più aumenti $K$, più grande diventa il transistor dello specchio $\to$ aumenta la sua capacità parassita di gate $C_{gs}$ $\to$ il polo parassita associato a quel nodo scende a frequenze più basse, erodendo il margine di fase e rischiando instabilità/oscillazioni.
* **Compromesso ottimale ($K = 3$):**  
  Scegliere $K = 3$ rappresenta lo "sweet spot" perfetto dove ottieni il **raddoppio di guadagno e banda a pari consumo**, mantenendo un margine di fase ampiamente stabile ($\ge 60^\circ$).