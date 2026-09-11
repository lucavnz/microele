Ran command: `python -c "import pypdf; print('pypdf installed')" 2>$null || python -c "import fitz; print('fitz installed')" 2>$null || python -c "print('python works')"`
Ran command: `python -c "
import sys
for mod in ['pypdf', 'fitz', 'pdfplumber', 'pypdf2']:
    try:
        __import__(mod)
        print(f'{mod}: available')
    except ImportError:
        pass
"`
Ran command: `python -c "
import fitz
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
print('Total pages:', len(doc))
for i in range(len(doc)):
    text = doc[i].get_text()
    first_line = text.strip().split('\n')[0] if text.strip() else 'EMPTY'
    print(f'Page {i+1}: {first_line[:80]}')
"`
Ran command: `python -c "
import fitz
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
for p in range(12, 21):
    print(f'=== PAGE {p+1} ===')
    print(doc[p].get_text())
"`
Ran command: `python -c "
import fitz
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
for p in range(13, 21):
    page = doc[p]
    print(f'Page {p+1}: images={len(page.get_images())}, text_len={len(page.get_text())}')
    for img in page.get_images():
        print('  image:', img)
"`
Ran command: `python -c "
import fitz, os
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
out_dir = r'C:\Users\Accetazione\.gemini\antigravity-ide\brain\96a8c49b-5fd0-46b2-9999-3b43fd59b44b\scratch'
os.makedirs(out_dir, exist_ok=True)
for p in range(13, 21):
    pix = doc[p].get_pixmap(dpi=150)
    out_path = os.path.join(out_dir, f'page_{p+1}.png')
    pix.save(out_path)
    print(f'Saved {out_path}')
"`
Viewed page_14.png:1-800
Viewed page_15.png:1-800
Viewed page_16.png:1-800
Viewed page_17.png:1-800
Viewed page_18.png:1-800
Viewed page_19.png:1-800
Viewed page_20.png:1-800
Viewed page_21.png:1-800
Ran command: `python -c "
import fitz
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
for i in range(13):
    t = doc[i].get_text().strip()
    print(f'Page {i+1}: {t[:100]}...')
"`
Ran command: `python -c "
import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
for i in range(13):
    t = doc[i].get_text().strip().replace('\n', ' ')
    print(f'Page {i+1}: {t[:120]}')
"`
Ran command: `python -c "
import fitz
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
# Let's inspect page 14 high res
pix = doc[13].get_pixmap(dpi=300)
pix.save(r'C:\Users\Accetazione\.gemini\antigravity-ide\brain\96a8c49b-5fd0-46b2-9999-3b43fd59b44b\scratch\page_14_high.png')
"`
Ran command: `python -c "
import fitz
doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\richelli_ampl_4.pdf')
for p in range(13, 21):
    pix = doc[p].get_pixmap(dpi=300)
    pix.save(rf'C:\Users\Accetazione\.gemini\antigravity-ide\brain\96a8c49b-5fd0-46b2-9999-3b43fd59b44b\scratch\page_{p+1}_high.png')
print('All high-res images saved.')
"`
Used tool: manage_task

Hai colto **esattamente** il punto! Quello che vedi da pagina 14 a 21 è il classico **amplificatore operazionale a due stadi** con **compensazione di Miller** (con tecniche di *pole splitting* e *zero-nulling resistor*), dove:
- Il **1° stadio** è un amplificatore cascode differenziale (ad altissimo guadagno).
- Il **2° stadio** è proprio un **Source Comune** (il PMOS $M_{10}$ con carico attivo $M_{12}$).

Andiamo a chiarire subito i tuoi dubbi *"wtf"* sul circuito di pagina 16 e poi analizziamo **pagina per pagina, formula per formula e passaggio per passaggio** tutto il documento.

---

### Risposta rapida ai tuoi dubbi: *"Cos'è quel circuito con $V_\sim, R_S$ e quelle due capacità?"*

1. **Cos'è il generatore $V_\sim$ con resistenza $R_S$?**
   È l'**equivalente di Thévenin del primo stadio**! 
   Invece di portarsi dietro tutti gli 8 transistor del primo stadio cascode nei conti di piccolo segnale, il primo stadio viene modellato come un generatore di tensione $V_\sim$ con in serie la sua enorme resistenza di uscita cascode:
   $$R_S = R_{out,cascode} \approx g_m^2 \frac{r_o^2}{2}$$
2. **Perché c'è una capacità $C_A$ a $V_{DD}$ e una $C_c$ al drain?**
   - **$C_A$ collegata a $V_{DD}$**: Il nodo A (il gate di $M_{10}$) ha delle capacità parassite intrinseche (la $C_{gs}$ di $M_{10}$ che va al suo source collegato a $V_{DD}$, le capacità parassite di drain dei transistor cascode $M_4$ e $M_6$, ecc.). Poiché $V_{DD}$ per il segnale (AC) è una **massa virtuale** (la tensione di alimentazione è costante nel tempo, quindi $\Delta V_{DD} = 0$), collegare una capacità a $V_{DD}$ o a massa è **elettricamente identico in piccolo segnale**. $C_A$ è quindi la capacità parassita totale vista sul nodo A.
   - **$C_c$ collegata al drain**: È la **capacità di Miller** introdotta intenzionalmente! Collega l'ingresso del secondo stadio (gate di $M_{10}$, nodo A) con l'uscita del secondo stadio (drain di $M_{10}$, nodo B). Serve a fare il *pole splitting* (separare i poli per rendere il circuito stabile in retroazione).
3. **È un source comune posto in uscita?**
   **Sì, al 100%!** $M_{10}$ è un PMOS a Source Comune (source a $V_{DD}$, ingresso sul gate, uscita sul drain), polarizzato dal generatore di corrente NMOS $M_{12}$ che funge da carico attivo.

---

## Analisi Pagina per Pagina (da Pagina 14 a 21)

---

### Pagina 14: Lo schema completo e il problema di stabilità

La slide mostra lo schema completo dell'amplificatore a due stadi:
- **1° Stadio (Telescopic Cascode)**:
  - Coppia differenziale NMOS $M_1, M_2$ con generatore di coda $I_0$.
  - Cascode NMOS $M_3, M_4$.
  - Specchio/carico cascode PMOS $M_5, M_6, M_7, M_8$.
- **2° Stadio**:
  - Transistor di guadagno $M_{10}$ (PMOS source comune).
  - Carico attivo $M_{12}$ (NMOS a corrente costante).
  - Capacità di carico $C_L$ sull'uscita.

#### I nodi critici individuati:
- **Nodo A (uscita 1° stadio / gate di $M_{10}$)**: È un nodo cascode, quindi ad altissima impedenza:
  $$R_A = R_{out1} \approx g_m \frac{r_o^2}{2} \quad (\text{molto grande})$$
  Dà origine a un polo $\omega_{pA} = \frac{1}{R_A C_A}$.
- **Nodo B (uscita 2° stadio / drain di $M_{10}$)**: Anche questo è un nodo ad alta impedenza:
  $$R_B = r_{o10} \parallel r_{o12} \approx \frac{r_o}{2}$$
  Poiché c'è una capacità di carico $C_L$ tipicamente rilevante, il polo $\omega_{pB} = \frac{1}{R_B C_L}$ cade a frequenze basse.
- **Nodo C (source del cascode $M_4$)**:
  La resistenza vista guardando nel source di un cascode è molto bassa:
  $$R_C \approx \frac{1}{g_{m4}}$$
  Quindi il polo associato al nodo C cade ad altissima frequenza:
  $$\omega_{pC} \approx \frac{g_{m4}}{C_C} \gg \omega_{pA}, \omega_{pB}$$
  Per questo motivo, **C è un polo non dominante**.

#### Il problema:
I poli **A e B sono entrambi a bassa frequenza** e si trovano molto vicini tra loro ($\omega_{pA} \approx \omega_{pB}$). A seconda del dimensionamento, può capitare $\omega_{pA} < \omega_{pB}$ oppure $\omega_{pB} < \omega_{pA}$.
Avere due poli dominanti vicini prima della frequenza di taglio a 0 dB distrugge il margine di fase ($\approx 0^\circ$ o negativo), rendendo l'amplificatore **instabile se richiuso in retroazione**.
> **Obiettivo della compensazione**: allontanare drasticamente i due poli (*pole splitting*), spostando $\omega_{pA}$ a frequenze bassissime (polo super-dominante) e spingendo $\omega_{pB}$ a frequenze molto elevate.

---

### Pagina 15: Il modello a blocchi e l'effetto Miller a bassa frequenza

La professoressa modella il circuito come due amplificatori invertenti in cascata:
- **Stadio 1**: guadagno $A_1 = -g_m^2 \frac{r_o^2}{2}$ (guadagno del cascode).
- **Stadio 2**: guadagno $A_2 = -g_m \frac{r_o}{2}$ (guadagno del source comune).
- Tra ingresso e uscita di $A_2$ viene posta la capacità $C_c$.

Applicando il classico **Teorema di Miller**:
La capacità $C_c$ vista all'ingresso del 2° stadio appare moltiplicata per $(1 - A_2)$:
$$C_{eq} = C_c (1 + |A_2|) = C_c \left(1 + g_m \frac{r_o}{2}\right)$$
Poiché il guadagno $|A_2|$ è dell'ordine di diverse decine o centinaia, $C_{eq}$ diventa gigantesca!
Questa enorme capacità sul nodo A abbassa enormemente la frequenza del polo A:
$$\omega_{pA}' \approx \frac{1}{R_S C_{eq}} \ll \omega_{pA}$$
*Tuttavia, il semplice Teorema di Miller non dice che fine fa il secondo polo $\omega_{pB}$ e ignora lo zero di trasmissione.* Per questo motivo nelle pagine successive si passa all'analisi rigorosa di piccolo segnale.

---

### Pagina 16: Il circuito equivalente completo del 2° stadio

Qui viene disegnato il circuito che ti ha insospettito:
- **$V_\sim$ e $R_S$**: Equivalente di Thévenin dello stadio 1 visto dal nodo A.
- **$M_{10}$**: PMOS pilotato sul gate (nodo A) con source a $+V_{DD}$.
- **$C_A$ tra gate e $+V_{DD}$**: Rappresenta la somma delle capacità parassite verso massa/alimentazione sul nodo A ($C_{gs10} + C_{gd6} + C_{db6} + C_{gd4} + C_{db4}$).
- **$C_c$ tra gate e drain**: La capacità di compensazione di Miller.
- **$M_{12}$**: NMOS con gate a tensione fissa di polarizzazione, funge da carico attivo.
- **$C_L$**: Capacità di carico sul nodo di uscita B verso massa.

---

### Pagina 17: Circuito equivalente per piccoli segnali (AC)

Nel passaggio al modello a parametri concentrati di piccolo segnale:
1. Le tensioni DC vanno a zero: **$+V_{DD}$ diventa massa AC** (ground). Per questo $C_A$ ora è disegnata tra il nodo A e massa!
2. La tensione al gate rispetto a source/massa è definita come $V_x$.
3. Tra nodo A e nodo B c'è la capacità complessiva di feedback:
   $$C_f = C_c + C_{GD}$$
   *(la professoressa tiene conto anche della parassita intrinseca gate-drain $C_{GD}$ del transistor $M_{10}$ in parallelo a $C_c$)*.
4. Il transistor PMOS $M_{10}$ genera una corrente di piccolo segnale:
   $$i_d = g_{m10} V_x$$
   rappresentata dal generatore di corrente controllato che va dal nodo B a massa.
5. La resistenza vista verso massa dal nodo B è la combinazione parallelo delle resistenze di uscita dei due transistor:
   $$R_L = r_{o10} \parallel r_{o12}$$
6. La capacità verso massa sul nodo B è $C_L$.

---

### Pagina 18: Le equazioni nodali (KCL) e la funzione di trasferimento

Scriviamo le leggi di Kirchhoff delle correnti (KCL) ai due nodi:

#### 1. KCL al Nodo A (tensione $V_x$):
La somma delle correnti uscenti dal nodo A deve essere zero:
$$\frac{V_x - V_\sim}{R_S} + V_x C_A s + (V_x - V_{out})(C_c + C_{GD}) s = 0$$

Raggruppiamo rispetto a $V_x$ e $V_{out}$:
$$V_x \left[ \frac{1}{R_S} + s(C_A + C_c + C_{GD}) \right] - V_{out} s (C_c + C_{GD}) = \frac{V_\sim}{R_S}$$
Moltiplicando tutto per $R_S$:
$$V_x [1 + s R_S (C_A + C_c + C_{GD})] - V_{out} s R_S (C_c + C_{GD}) = V_\sim \quad \mathbf{(1)}$$

#### 2. KCL al Nodo B (tensione $V_{out}$):
La somma delle correnti uscenti dal nodo B deve essere zero:
$$(V_{out} - V_x)(C_c + C_{GD}) s + g_{m10} V_x + V_{out} \left( \frac{1}{R_L} + C_L s \right) = 0$$

Raggruppiamo i termini con $V_x$ e $V_{out}$:
$$V_x [g_{m10} - s(C_c + C_{GD})] + V_{out} \left[ \frac{1}{R_L} + s(C_L + C_c + C_{GD}) \right] = 0$$
Da cui possiamo ricavare $V_x$ in funzione di $V_{out}$:
$$V_x = - V_{out} \frac{\frac{1}{R_L} + s(C_L + C_c + C_{GD})}{g_{m10} - s(C_c + C_{GD})}$$

#### 3. Risoluzione del sistema:
Sostituendo $V_x$ nella prima equazione e facendo il denominatore comune, dopo i passaggi algebrici si ottiene la formula scritta a pagina 18:
$$\frac{V_{out}(s)}{V_\sim} = \frac{[(C_c + C_{GD})s - g_m] R_L}{a_2 s^2 + a_1 s + 1}$$

dove:
- **Numeratore**: presenta un termine $[(C_c + C_{GD}) s - g_m] R_L$.
- **Coefficiente di $s$ ($a_1$)**:
  $$a_1 = R_S (1 + g_m R_L)(C_c + C_{GD}) + R_S C_A + R_L (C_c + C_{GD} + C_L)$$
- **Coefficiente di $s^2$ ($a_2$)**:
  $$a_2 = R_S R_L [C_A(C_c + C_{GD}) + C_A C_L + C_L(C_c + C_{GD})]$$

---

### Pagina 19: L'ipotesi dei poli separati

Il denominatore è del secondo ordine: $D(s) = a_2 s^2 + a_1 s + 1$.
Se i due poli $\omega_{pA}$ e $\omega_{pB}$ sono reali e **ben distanziati** in frequenza (ipotesi di compensazione: $\omega_{pA} \ll \omega_{pB}$):

$$D(s) = \left( 1 + \frac{s}{\omega_{pA}} \right) \left( 1 + \frac{s}{\omega_{pB}} \right) = 1 + \left( \frac{1}{\omega_{pA}} + \frac{1}{\omega_{pB}} \right) s + \frac{s^2}{\omega_{pA} \omega_{pB}}$$

Dato che $\omega_{pA} \ll \omega_{pB}$, allora $\frac{1}{\omega_{pA}} \gg \frac{1}{\omega_{pB}}$.
Possiamo quindi trascurare $\frac{1}{\omega_{pB}}$ nella somma lineare:
$$\frac{1}{\omega_{pA}} + \frac{1}{\omega_{pB}} \approx \frac{1}{\omega_{pA}}$$
*(nella slide la professoressa tira una riga su $\frac{1}{\omega_{pB}}$ e scrive "per l'ipotesi")*.

Pertanto:
$$a_1 \approx \frac{1}{\omega_{pA}} \quad \implies \quad \omega_{pA} \approx \frac{1}{a_1}$$
$$a_2 = \frac{1}{\omega_{pA} \omega_{pB}} \quad \implies \quad \omega_{pB} = \frac{1}{a_2 \omega_{pA}} \approx \frac{a_1}{a_2}$$

---

### Pagina 20: Espressione dei due poli e intuizione fisica

Sostituendo i valori di $a_1$ e $a_2$:

#### 1. Il nuovo polo dominante $\omega_{pA}$:
$$\omega_{pA} = \frac{1}{R_S [(1 + g_{m10} R_L)(C_c + C_{GD}) + C_A] + R_L(C_c + C_L + C_{GD})}$$
Il termine dominante a denominatore è $R_S \cdot (g_{m10} R_L) \cdot (C_c + C_{GD})$, cioè la capacità di Miller moltiplicata per l'enorme guadagno del secondo stadio e vista attraverso l'enorme resistenza $R_S$.
Il polo $\omega_{pA}$ è stato **spinto a frequenza bassissima**!

#### 2. Il nuovo polo non dominante $\omega_{pB}$:
$$\omega_{pB} \approx \frac{a_1}{a_2} \approx \frac{R_S (g_{m10} R_L)(C_c + C_{GD})}{R_S R_L [C_A(C_c + C_{GD}) + C_A C_L + C_L(C_c + C_{GD})]}$$
Semplificando $R_S R_L$ e assumendo $C_c \gg C_{GD}$ e $C_c \gg C_A$:
$$\omega_{pB} \approx \frac{g_{m10}}{C_A + C_L} \quad \left( \text{o circa } \frac{g_{m10}}{C_L} \right)$$

#### L'intuizione fisica della prof (in fondo a pag. 20):
Prima della compensazione il polo di uscita era $\omega_{pB,prima} \approx \frac{1}{R_L C_L}$, dominato dalla grande resistenza $R_L = r_{o10} \parallel r_{o12}$.
**Cosa è successo con $C_c$ ad alte frequenze?**
Ad alta frequenza, la capacità $C_c$ diventa un **corto-circuito** tra il gate e il drain di $M_{10}$!
- Cortocircuitare gate e drain trasforma il transistor $M_{10}$ in una **connessione a diodo**!
- La resistenza vista al nodo di uscita non è più $R_L$, ma diventa la resistenza della connessione a diodo:
  $$R_{eq} \approx \frac{1}{g_{m10}} \ll R_L$$
- Inoltre, il cortocircuito mette la capacità di gate $C_A$ in parallelo alla capacità di carico $C_L$.
Quindi il nuovo polo è semplicemente:
$$\omega_{pB} \approx \frac{1}{R_{eq} C_{tot}} = \frac{1}{\frac{1}{g_{m10}} (C_A + C_L)} = \frac{g_{m10}}{C_A + C_L}$$
È proprio per questo che $\omega_{pB}$ è stato spinto a frequenze molto più alte: la resistenza associata è crollata da $R_L$ a $1/g_{m10}$!

---

### Pagina 21: Lo Zero nel semipiano destro (RHP Zero) e il resistore $R_z$

Guardando il numeratore trovato a pagina 18:
$$N(s) = [(C_c + C_{GD}) s - g_{m10}]$$
Se poniamo $N(s) = 0$, troviamo uno zero alla frequenza:
$$s_z = +\frac{g_{m10}}{C_c + C_{GD}} > 0$$

#### Perché questo zero è una catastrofe?
È uno **Zero a Parte Reale Positiva (Right Half Plane - RHP Zero)**:
- Come ogni zero, il suo modulo aumenta il guadagno di $+20 \text{ dB/decade}$ (spinge la frequenza di cross-over 0 dB più in alto).
- **MA** per la fase si comporta come un polo: introduce uno **sfasamento negativo di $-90^\circ$**!
- Risultato: distrugge completamente il margine di fase, portando il circuito all'oscillazione.

#### La soluzione: Resistenza di Nulling $R_z$ in serie a $C_c$
Inserendo una resistenza $R_z$ in serie al condensatore $C_c$, la corrente diretta attraverso il ramo di Miller viene limitata, e la posizione dello zero diventa:
$$s_z = \frac{1}{C_c \left( \frac{1}{g_{m10}} - R_z \right)}$$

- Se scegliamo **$R_z = \frac{1}{g_{m10}}$**:
  Il denominatore va a zero, quindi $s_z \to \infty$ (**lo zero viene completamente eliminato**).
- Se scegliamo **$R_z > \frac{1}{g_{m10}}$**:
  Il denominatore diventa negativo, quindi lo zero si sposta nel **Semipiano Sinistro (LHP)** ($s_z < 0$). In questo caso, lo zero fornisce un **anticipo di fase di $+90^\circ$**, aiutando ad aumentare ulteriormente il margine di fase!

#### La condizione finale su $C_c$ (in fondo a pag. 21):
$$C_c^2 \gg \frac{g_{m1}}{g_{m10}} (C_{GS10} C_c + C_L C_c + C_{GS10} C_L)$$
Da dove salta fuori questa disuguaglianza?
La larghezza di banda a guadagno unitario dell'amplificatore compensato è:
$$\omega_{GBW} \approx \frac{g_{m1}}{C_c}$$
Per avere un margine di fase stabile (es. $> 60^\circ$), il secondo polo $\omega_{pB} \approx \frac{g_{m10}}{C_L + C_A (1 + C_L / C_c)}$ deve trovarsi ben oltre la frequenza di taglio a guadagno unitario:
$$\omega_{GBW} \ll \omega_{pB} \iff \frac{g_{m1}}{C_c} \ll \frac{g_{m10}}{C_L + C_A + \frac{C_A C_L}{C_c}}$$
Moltiplicando a croce per $C_c$ e ponendo $C_A \approx C_{GS10}$:
$$g_{m1} (C_L C_c + C_{GS10} C_c + C_{GS10} C_L) \ll g_{m10} C_c^2$$
Dividendo per $g_{m10}$:
$$C_c^2 \gg \frac{g_{m1}}{g_{m10}} (C_{GS10} C_c + C_L C_c + C_{GS10} C_L)$$
Ciò dimostra che:
- Più $g_{m10}$ del 2° stadio è grande rispetto a $g_{m1}$ del 1° stadio, più $C_c$ può essere scelta **piccola** (risparmiando area di silicio e migliorando lo slew rate).
- Viceversa, se il secondo stadio ha una $g_m$ modesta, servirà una $C_c$ molto più grande per garantire la stabilità.

---

### Riepilogo concettuale delle 8 pagine

```
Pag. 14: Due poli dominanti vicini (A e B) -> Rischio instabilità
   │
Pag. 15: Idea di Miller a blocchi -> Cc crea una Ceq enorme al nodo A
   │
Pag. 16: Modellazione del circuito: Stadio 1 = Thévenin (V~, Rs), Stadio 2 = Source Comune PMOS
   │
Pag. 17: Circuito di piccolo segnale AC (Vdd va a massa, parallelo Cc + CGD)
   │
Pag. 18: Risoluzione nodale esatta (KCL) -> Funzione di trasferimento del 2° ordine
   │
Pag. 19: Ipotesi poli ben spaziati (wpA << wpB) -> Semplificazione del denominatore
   │
Pag. 20: Pole Splitting:
         - wpA crolla a bassa frequenza (effetto Miller x Rs)
         - wpB schizza ad alta frequenza (grazie a Req = 1/gm10 per diodo-connection di Cc)
   │
Pag. 21: Eliminazione dello zero dannoso (RHP) tramite Rz = 1/gm10 e dimensionamento di Cc
```

Edited Risposta.md
Viewed Risposta.md:236-245
Viewed Risposta.md:328-332

La tua domanda è **fondamentale** ed è esattamente il dubbio più intelligente che possa venire: tocca il cosiddetto **"Paradosso di Miller"** e il motivo per cui **il semplice Teorema di Miller "scolastico" fallisce** quando si vuole capire cosa succede al polo di uscita!

Andiamo a sviscerare punto per punto la questione:
1. Hai ragione sul Teorema di Miller e sulla capacità al drain?
2. Aggiungiamo un polo al circuito?
3. **Il vero paradosso**: se metto una capacità in parallelo all'uscita, la capacità aumenta... perché diavolo il polo si sposta a frequenze **più alte** invece che più basse?

---

### 1. Hai ragione tu? Cosa dice il Teorema di Miller "classico"

Nel Teorema di Miller classico, se hai un'impedenza (la capacità $C_c$) collegata tra ingresso (nodo A, gate) e uscita (nodo B, drain) di un blocco con guadagno di tensione $A_v$:
- **All'ingresso** vedi una capacità verso massa:
  $$C_{in} = C_c (1 - A_v)$$
  Poiché lo stadio è invertente ($A_v = -|A_v|$), si ha:
  $$C_{in} = C_c (1 + |A_v|)$$
  *(questa è la famosa moltiplicazione di Miller che abbiamo visto a pagina 15)*.

- **All'uscita** vedi una capacità verso massa:
  $$C_{out} = C_c \left(1 - \frac{1}{A_v}\right) = C_c \left(1 + \frac{1}{|A_v|}\right)$$
  Poiché il guadagno in modulo $|A_v| = g_m R_L \gg 1$, il termine $\frac{1}{|A_v|} \approx 0$, quindi:
  $$C_{out} \approx C_c$$

Quindi **hai perfettamente ragione**: secondo Miller, sull'uscita si troverebbe una capacità pari a $C_c$ che va a sommarsi in parallelo a $C_L$, portando la capacità totale di uscita a:
$$C_{out,tot} = C_L + C_c$$

---

### 2. Aggiunge un polo al circuito?

**No.**
Nel circuito fisico c'erano già **due nodi ad alta impedenza**:
- Nodo A (il gate di $M_{10}$) $\rightarrow$ aveva già il suo polo $\omega_{pA}$.
- Nodo B (il drain di $M_{10}$, uscita) $\rightarrow$ aveva già il suo polo $\omega_{pB}$.

Quando colleghi una capacità $C_c$ tra il nodo A e il nodo B, non hai aggiunto un terzo nodo a massa: la capacità $C_c$ connette semplicemente due nodi già esistenti. L'ordine del circuito rimane **2** (due capacità indipendenti, quindi due poli nel denominatore).

---

### 3. Il Paradosso: perché l'uscita viene spinta ad ALTA frequenza?

Arriviamo al nocciolo del tuo dubbio, che è geniale:

> *"Se all'uscita ci metto $C_c$ in parallelo a $C_L$, la capacità totale aumenta ($C_L + C_c$). La frequenza del polo è $\omega = \frac{1}{R \cdot C}$. Se $C$ aumenta, $\omega$ dovrebbe diminuire! Perché invece $\omega_{pB}$ va a frequenze molto più alte?!"*

Ecco svelato il "trucco" della fisica: **perché il Teorema di Miller classico qui non è applicabile!**

#### Il limite del Teorema di Miller:
Il Teorema di Miller assume che il guadagno di tensione sia un **numero reale costante e indipendente dalla frequenza**: $V_{out} = A_v \cdot V_{in}$.
Ma ad alta frequenza (in prossimità del secondo polo $\omega_{pB}$), questa assunzione è **completamente falsa**:
1. Il guadagno dello stadio crolla e subisce uno sfasamento.
2. La capacità $C_c$ non è un carico passivo isolato: è una **linea di trasmissione bidirezionale** che crea una **retroazione negativa locale fortissima** attorno al transistor $M_{10}$!

#### Cosa succede fisicamente ad alta frequenza? (La spiegazione della prof a pag. 20)

Ricorda la formula del polo:
$$\omega_{polo} = \frac{1}{R_{eq} \cdot C_{eq}}$$
Per spostare un polo ad alta frequenza hai due possibilità: diminuire $C$, oppure **diminuire drasticamente $R$**.

Guarda cosa succede alle due quantità:

1. **La Capacità ($C_{eq}$):**
   A frequenze elevate, l'impedenza del condensatore $Z_{Cc} = \frac{1}{j\omega C_c}$ diventa piccolissima: **$C_c$ si comporta come un corto-circuito** tra Gate e Drain!
   Essendo Gate e Drain cortocircuitati, la capacità di gate ($C_A$) e quella di drain ($C_L$) si trovano in parallelo:
   $$C_{eq} \approx C_L + C_A$$
   La capacità è cambiata di poco rispetto a prima (è leggermente aumentata).

2. **La Resistenza ($R_{eq}$) — ECCO LA CHIAVE:**
   - **PRIMA della compensazione (senza $C_c$):**
     Il transistor $M_{10}$ ha il gate staccato dal drain. La resistenza vista guardando nel drain verso massa è la grande resistenza di uscita del transistor:
     $$R_{prima} = R_L = r_{o10} \parallel r_{o12} \quad (\sim 100\text{ k}\Omega \div 1\text{ M}\Omega)$$
     Quindi il polo prima era a frequenza relativamente bassa:
     $$\omega_{pB,prima} = \frac{1}{R_L \cdot C_L}$$

   - **DOPO la compensazione (con $C_c$), ad alta frequenza:**
     Poiché $C_c$ è un corto-circuito, il **Gate di $M_{10}$ è collegato direttamente al suo Drain**!
     Come si chiama un MOSFET con il Gate collegato al Drain?
     **Transistor connesso a diodo (diode-connected)!**
     E quant'è la resistenza vista al nodo di un transistor connesso a diodo?
     $$R_{diodo} \approx \frac{1}{g_{m10}} \quad (\sim 100\,\Omega \div 1\text{ k}\Omega)$$

#### Facciamo due conti numerici per renderlo evidente:

Supponiamo valori realistici da circuito integrato:
- $R_L = 500\text{ k}\Omega$
- $g_{m10} = 2\text{ mA/V} \implies \frac{1}{g_{m10}} = 500\,\Omega$ (la resistenza è scesa di **1000 volte**!)
- $C_L = 1\text{ pF}$, $C_A = 0.2\text{ pF}$ (la capacità è salita da $1\text{ pF}$ a $1.2\text{ pF}$, cioè solo del $20\%$).

Calcoliamo il polo prima e dopo:
- **Prima della compensazione:**
  $$\omega_{pB,prima} = \frac{1}{500\text{ k}\Omega \times 1\text{ pF}} = \frac{1}{5 \times 10^{-7}} = 2 \times 10^6\text{ rad/s} \quad (\approx 300\text{ kHz})$$
- **Dopo la compensazione:**
  $$\omega_{pB,dopo} \approx \frac{g_{m10}}{C_L + C_A} = \frac{1}{500\,\Omega \times 1.2\text{ pF}} = \frac{1}{6 \times 10^{-10}} = 1.67 \times 10^9\text{ rad/s} \quad (\approx 260\text{ MHz})$$

Il polo è schizzato da **$300\text{ kHz}$** a **$260\text{ MHz}$**!
È andato a frequenze **quasi 1000 volte più alte**!

---

### Interpretazione con la Teoria dei Sistemi e Retroazione

Se preferisci vederla dal punto di vista della teoria della retroazione:
$C_c$ realizza un anello di **retroazione negativa locale di tensione parallelo-parallelo** sul transistor $M_{10}$:
- La retroazione negativa preleva la tensione d'uscita (nodo B) e la riporta all'ingresso (nodo A).
- Una retroazione negativa sulla tensione di uscita **abbatte l'impedenza di uscita** dividendola per il fattore di retroazione $(1 + T)$:
  $$R_{out,chiuso} \approx \frac{R_L}{1 + g_{m10} R_L} \approx \frac{1}{g_{m10}}$$

---

### In sintesi: perché si chiama "Pole Splitting" (Sdoppiamento dei poli)?

La capacità $C_c$ agisce come una leva simmetrica ma opposta sui due nodi:

| Nodo | Effetto di $C_c$ | Risultato sul polo |
| :--- | :--- | :--- |
| **Nodo A (Ingresso)** | La resistenza rimane alta ($R_S$), ma la capacità viene moltiplicata per il guadagno: $C_{in} \approx g_{m10} R_L C_c$ (Effetto Miller). | **$\omega_{pA}$ crolla verso il basso** (diventa il polo dominante a frequenza bassissima). |
| **Nodo B (Uscita)** | La capacità cambia pochissimo ($C_A + C_L$), ma la resistenza crolla da $R_L$ a $\frac{1}{g_{m10}}$ per effetto della connessione a diodo ad alta frequenza. | **$\omega_{pB}$ schizza verso l'alto** (diventa un polo ad altissima frequenza). |

I due poli, che all'inizio erano vicini e "litigavano" tra loro rendendo instabile l'amplificatore, vengono **drasticamente separati** (*split*): ora il circuito ha un singolo polo dominante ben isolato e un margine di fase eccellente!