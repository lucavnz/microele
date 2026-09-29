# Approfondimento: Teorema e Capacità di Miller negli Amplificatori a Due Stadi

Hai toccato esattamente il punto in cui il 90% degli studenti si confonde! Mettiamo subito ordine tra il **Teorema di Miller**, **quale capacità diventa grande**, e **dove diavolo si mette** negli amplificatori delle slide della prof. Richelli ([richelli_ampl_4.pdf](file:///Users/matteoluca/Downloads/microele/richelli_ampl_4.pdf)).

---

### 1. Cosa significa "smontare" la capacità (Teorema di Miller)

Immagina di avere un amplificatore con guadagno di tensione $A_v = \frac{V_2}{V_1}$.  
Tra il nodo d'ingresso (1) e il nodo d'uscita (2) c'è un condensatore $C$.

Se inietti una tensione $V_1$ all'ingresso, all'uscita hai $V_2 = A_v V_1$.  
La corrente che l'ingresso deve fornire al condensatore è:
$$I_1 = (V_1 - V_2) \cdot sC = V_1(1 - A_v) \cdot sC$$

L'ammettenza equivalente vista dal nodo d'ingresso verso massa è quindi:
$$Y_{in} = \frac{I_1}{V_1} = s \cdot [C(1 - A_v)] \implies \mathbf{C_{in} = C(1 - A_v)}$$

Facendo lo stesso calcolo dal nodo d'uscita:
$$I_2 = (V_2 - V_1) \cdot sC = V_2\left(1 - \frac{1}{A_v}\right) \cdot sC \implies \mathbf{C_{out} = C\left(1 - \frac{1}{A_v}\right)}$$

---

### 2. "Quella rilevante in un invertente è quella in uscita?" $\rightarrow$ **NO, è l'opposto!**

Se lo stadio è **invertente**, il guadagno è negativo: $A_v = -|A_v|$ (con $|A_v| \gg 1$, per esempio $|A_v| = 50$ o $100$).

Guarda cosa succede alle due capacità:

* **All'INGRESSO:**
  $$C_{in} = C(1 - (-|A_v|)) = \mathbf{C \cdot (1 + |A_v|)}$$
  **È questa quella rilevante ed enorme!** Se metti una $C = 2\text{ pF}$ e lo stadio guadagna $-50$, dall'ingresso vedi $2 \times 51 \approx \mathbf{102\text{ pF}}$ verso massa!  
  *Intuizione fisica:* se il terminale di sinistra sale di $+1\text{ V}$ e quello di destra scende di $-50\text{ V}$, ai capi del condensatore cadono $51\text{ V}$. L'ingresso deve pompare 51 volte più carica di quanta ne servirebbe se l'altro capo fosse a massa fissa. Sembra un condensatore 51 volte più grande!
* **All'USCITA:**
  $$C_{out} = C\left(1 - \left(-\frac{1}{|A_v|}\right)\right) = C\left(1 + \frac{1}{|A_v|}\right) \approx \mathbf{C}$$
  Poiché $\frac{1}{|A_v|} \approx \frac{1}{50} = 0.02$, all'uscita la capacità resta praticamente identica a $C$, **non esplode per niente**.

---

### 3. "Ma negli amplificatori non invertenti o differenziali cosa si fa?"

Ecco il grandissimo malinteso: **la capacità di compensazione $C_c$ NON è collegata a cavallo della coppia differenziale!**

Guarda lo schema dell'amplificatore a due stadi nelle slide:
* **Slide 2** (schema a blocchi/transistor) e **Slide 14-16**:
  * **$1^\circ$ Stadio ($A_1$):** È la coppia differenziale (M1-M2 con carico attivo). Prende in ingresso la tensione differenziale e produce una tensione al **nodo intermedio A**.
  * **$2^\circ$ Stadio ($A_2$):** È un transistor a **Source Comune** (M6 a slide 2, oppure M10 a slide 14-16).
  * **E il Source Comune è INVERTENTE!** Infatti nella slide 15 trovi scritto proprio:
    $$A_2 = -g_m \frac{r_o}{2}$$
  * **Dove è collegata la capacità $C_c$?**  
    È collegata tra il **gate del secondo stadio (nodo A)** e il **drain del secondo stadio (uscita B / $V_o$)**!
  * Essa scavalca solo ed esclusivamente il secondo stadio, che è un source comune invertente!

Quindi il Teorema di Miller si applica **solo al $2^\circ$ stadio** (come mostrato a **Slide 15**):
$$C_{eq} = C_c (1 - A_2) = C_c \left(1 + g_m \frac{r_o}{2}\right)$$
Questa capacità equivalente $C_{eq}$ finisce appesa al **nodo intermedio A** verso massa.

---

### 4. A cosa serve tutto questo? (Il *Pole Splitting*, Slide 14-20)

Perché facciamo questa cosa invece di lasciare l'amplificatore com'era?

1. **Senza compensazione (Slide 14):**
   * Al nodo intermedio A hai una resistenza altissima ($R_A = R_{out,1}$) e una capacità parassita $C_A \implies$ polo $\omega_{pA}$.
   * Al nodo di uscita B hai una resistenza $R_L$ e una capacità di carico $C_L \implies$ polo $\omega_{pB}$.
   * I due poli sono entrambi a frequenze intermedie/simili. Se chiudi l'amplificatore in retroazione, due poli vicini introducono uno sfasamento di $180^\circ$ prima che il guadagno scenda sotto $0\text{ dB} \implies$ **il circuito oscilla ed è instabile**.

2. **Con la capacità di Miller $C_c$ (Slide 15, 18, 20):**
   * **Polo dominante $\omega_{pA}$:** Il nodo A ora vede la capacità enorme di Miller $C_{eq} \approx C_c \cdot |A_2|$.  
     Il polo del primo stadio viene trascinato a **frequenza bassissima**:
     $$\omega_{pA} \approx \frac{1}{R_{out,1} \cdot C_c |A_2|} = \frac{1}{R_{out,1} \cdot g_{m2} R_{out,2} C_c}$$
   * **Polo non dominante $\omega_{pB}$:** Alle frequenze elevate, $C_c$ diventa un cortocircuito locale tra drain e gate del secondo stadio, trasformando il transistor M10 in una connessione a diodo con resistenza $1/g_{m10}$. Il polo di uscita viene spinto a **frequenza altissima**:
     $$\omega_{pB} \approx \frac{g_{m10}}{C_L + C_A}$$
   * **Risultato:** I due poli si allontanano drasticamente (**separazione dei poli** o *pole splitting*). L'amplificatore adesso si comporta come un sistema a singolo polo dominante, garantendo un ottimo margine di fase ($PM \ge 60^\circ$).

---

### 5. Gli ultimi due dettagli importanti delle slide

* **Perché a Slide 21 si mette la resistenza $R_z$ (o $R_c$) in serie a $C_c$?**  
  Poiché $C_c$ è un percorso fisico bidirezionale, ad altissima frequenza il segnale passa dritto dall'ingresso all'uscita scavalcando il transistor. Questo introduce uno **zero a parte reale positiva (RHP Zero)** a $\omega_z = + \frac{g_m}{C_c}$, che degrada la fase (-90°). Mettendo una resistenza in serie $R_z \approx \frac{1}{g_m}$, lo zero viene cancellato o spostato a parte reale negativa.
* **Perché a Slide 4 il Cascode "non risente dell'effetto Miller"?**  
  Nel cascode (Source Comune + Gate Comune), il transistor di ingresso (Source Comune) ha sul drain la sorgente del Gate Comune, che ha resistenza bassissima $R_{in2} \approx \frac{1}{g_m}$.  
  Quindi il guadagno del primo transistor è solo $A_{v1} \approx -g_m \cdot \frac{1}{g_m} = -1$.  
  La capacità parassita $C_{gd1}$ vede un effetto Miller di appena $(1 - (-1)) = 2$, anziché 50 o 100! Ecco perché il cascode elimina l'effetto Miller parassita.

Hai centrato le tre domande più cruciali (e quelle su cui molti libri fanno confusione). Rispondiamo con precisione a ciascuna:

---

### 1. "Ma quindi anche l'uscita aumenta di $C$?"

**SÌ, esattamente!**  
Applicando Miller al nodo di uscita:
$$C_{out} = C_c \left(1 - \frac{1}{A_v}\right) = C_c \left(1 + \frac{1}{|A_v|}\right)$$
Poiché il guadagno $|A_v|$ è grande (es. $50$ o $100$), il termine $\frac{1}{|A_v|} \approx 0.01 \ll 1$.  
Quindi:
$$C_{out} \approx C_c$$
Se sul nodo di uscita c'era già la capacità di carico $C_L$, la capacità totale verso massa all'uscita diventa:
$$C_{\text{uscita, totale}} \approx C_L + C_c$$

* **La differenza fondamentale tra ingresso e uscita:**
  * All'**ingresso** $C_c$ viene moltiplicata per il guadagno: $+ C_c \cdot (1 + |A_v|)$ $\implies$ **esplode** (da $2\text{ pF}$ diventa $100\text{ pF}$).
  * All'**uscita** si somma semplicemente $+ C_c$ $\implies$ **aumenta di pochissimo** (da $10\text{ pF}$ di carico diventa $12\text{ pF}$).

---

### 2. "Son due poli, da uno diventa due? Perché?"

**No, i poli erano già DUE fin dall'inizio!**  
Non è che da uno ne compaiono due: c'erano già due nodi ad alta impedenza nel circuito.

Guarda cosa c'era **prima** di mettere la capacità $C_c$ ([Slide 14](file:///Users/matteoluca/Downloads/microele/richelli_ampl_4.pdf)):
1. **Nodo A (uscita del $1^\circ$ stadio):** resistenza altissima $R_A = R_{out,1}$ e parassita $C_A$ $\implies$ **$1^\circ$ Polo:** $\omega_A \approx \frac{1}{R_A C_A}$.
2. **Nodo B (uscita del $2^\circ$ stadio):** resistenza altissima $R_L = R_{out,2}$ e carico $C_L$ $\implies$ **$2^\circ$ Polo:** $\omega_B \approx \frac{1}{R_L C_L}$.

Entrambi i nodi vedono resistenze dell'ordine dei Megaohm. Di conseguenza, i due poli $\omega_A$ e $\omega_B$ si trovavano a **frequenze vicine** (entrambi a frequenza medio-bassa).  
*Il disastro:* due poli vicini sfasano il segnale di $180^\circ$ prima che il guadagno sia sceso sotto $0\text{ dB}$. Se chiudi l'amplificatore in retroazione, **oscilla come un matto**.

#### Cosa fa $C_c$? Fa il *Pole Splitting* (separazione dei poli):
Non crea poli nuovi: prende i due poli che già avevi e li **allontana a forza**:
* **$\omega_{p1}$ (il dominante):** viene spinto verso l'origine a frequenza **bassissima** (kHz o Hz).
* **$\omega_{p2}$ (il non dominante):** viene calciato via a frequenza **altissima** (decine/centinaia di MHz).

---

### 3. "Assume guadagno costante? Cioè cosa significa?"

Questa è la domanda più intelligente in assoluto, ed è il motivo per cui **il Teorema di Miller classico fallisce sul secondo polo** e la professoressa nelle slide deve fare il calcolo con le matrici/KCL a Slide 17-20!

#### Il limite del Teorema di Miller classico:
Nel Teorema di Miller si scrive:
$$C_{in} = C_c(1 - A_v)$$
assumendo implicitamente che il guadagno $A_v$ sia **un numero fisso costante** ($A_v = -g_m R_L$).  
* Questo va benissimo per trovare il **primo polo** $\omega_{p1}$, perché quel polo si trova a frequenze bassissime, dove il guadagno è ancora al suo valore continuo DC ($A_{v0}$).
* **Ma per il secondo polo $\omega_{p2}$ NON FUNZIONA PIÙ!**  
  A frequenze elevate il guadagno $A_v(s)$ non è affatto costante: è già crollato per colpa del primo polo! Se usassi Miller assumendo $A_v$ costante, troveresti per l'uscita:
  $$\omega_{p2, \text{ingenuo}} \approx \frac{1}{R_L (C_L + C_c)} \quad \text{--- SBAGLIATO!}$$
  Questo polo errato sarebbe ancora a frequenza bassa perché $R_L$ è grandissima!

#### Cosa succede REALMENTE ad alta frequenza? (L'intuizione di Slide 20)
Guarda l'annotazione manoscritta della prof a fondo di **Slide 20**:
> *"La $C_c$ alle alte frequenze cortocircuita M10 portando ad avere $C_A$ in parallelo a $C_L$ e la $R_{eq}$ vista adesso è $1/g_{m10}$."*

Cosa significa fisicamente?
1. Ad alta frequenza l'impedenza del condensatore crolla: $Z_{Cc} = \frac{1}{s C_c} \to 0$ (diventa un filo!).
2. Se $C_c$ diventa un filo, **collega il Gate di M10 direttamente al suo Drain**.
3. Un MOSFET con Gate e Drain cortocircuitati è un **MOSFET a diodo**!
4. E quale resistenza offre un MOSFET connesso a diodo? Non offre più la gigantesca resistenza $R_L = r_o$, ma offre:
   $$R_{eq} \approx \frac{1}{g_m}$$
5. La resistenza vista dal nodo di uscita crolla da Megaohm a poche centinaia di Ohm ($1/g_m$)!  
   Di conseguenza, il vero secondo polo calcolato correttamente (Slide 18-20) è:
   $$\mathbf{\omega_{p2} \approx \frac{g_{m10}}{C_L + C_A}}$$

### Ricapitolando la "magia" del Pole Splitting:
```text
Senza Cc:
Nodo A:  [RA = ro]   e  [CA]  ──►  Polo a 1/(ro · CA)         (medio) ──┐ Poli vicini:
Nodo B:  [RL = ro]   e  [CL]  ──►  Polo a 1/(ro · CL)         (medio) ──┘ INSTABILE!

Con Cc (Miller):
Nodo A:  [RA = ro]   e  [Cc · gm ro]  ──► Polo 1 ≈ 1/(gm ro² Cc)  (BASSISSIMO, dominante)
Nodo B:  [Req = 1/gm] e  [CL + CA]     ──► Polo 2 ≈ gm/(CL + CA)    (ALTISSIMO, innocuo)
                                                                 STABILE!
```


Ecco la spiegazione passo-passo di **tutto ciò che fa la prof nelle slide da 16 a 21** ([richelli_ampl_4.pdf](file:///Users/matteoluca/Downloads/microele/richelli_ampl_4.pdf)).  
È la classica dimostrazione formale del **Pole Splitting** (separazione dei poli) e dell'effetto della capacità di compensazione $C_c$.

---

### Il punto di partenza (Slide 16 e 17)
Abbiamo il circuito a due stadi:
* **$1^\circ$ Stadio:** telescopico/cascode. Nel circuito equivalente viene modellato semplicemente con la sua resistenza di uscita **$R_s$** (che è gigantesca, dell'ordine di $g_m r_o^2$).
* **Nodo A:** nodo intermedio (tra $1^\circ$ e $2^\circ$ stadio), con tensione $V_x$ e capacità parassita verso massa **$C_A$**.
* **$2^\circ$ Stadio ($M_{10}$):** stadio a source comune invertente. Ha transconduttanza $g_{m10}$, resistenza di carico $R_L = r_{o10} \parallel r_{o12}$, e carico capacitivo **$C_L$** al nodo di uscita B ($V_{out}$).
* **La capacità di compensazione:** tra il nodo A e il nodo B è inserita **$C_c$**, che si trova in parallelo alla capacità intrinseca del MOS **$C_{GD}$** (quindi la capacità totale di feedback è $C_c + C_{GD}$).

---

### Passo 1: Le equazioni nodali di Kirchhoff (Slide 18)
Per non fare approssimazioni campate per aria, la prof scrive la legge di Kirchhoff delle correnti (KCL) ai due nodi A e B nel dominio di Laplace ($s$):

1. **Al nodo A (tensione $V_x$):**
   $$\frac{V_x - V_{in}}{R_s} + V_x C_A s + (V_x - V_{out})(C_c + C_{GD}) s = 0$$
   *(corrente che arriva dal generatore attraverso $R_s$ = corrente che va a terra in $C_A$ + corrente che scavalca verso l'uscita attraverso $C_c + C_{GD}$)*

2. **Al nodo B (uscita $V_{out}$):**
   $$(V_{out} - V_x)(C_c + C_{GD}) s + g_{m10} V_x + V_{out}\left(\frac{1}{R_L} + C_L s\right) = 0$$
   *(corrente che arriva da $C_c$ + corrente erogata dal canale del MOS $g_m V_x$ + corrente che scende in $R_L$ e $C_L$ = 0)*

Risolvendo questo sistema lineare di due equazioni, si ottiene la funzione di trasferimento completa $\frac{V_{out}(s)}{V_{in}(s)}$:

$$\frac{V_{out}(s)}{V_{in}(s)} = \frac{[(C_c + C_{GD})s - g_m] R_L}{a \cdot s^2 + b \cdot s + 1}$$

dove i coefficienti del denominatore $D(s) = a s^2 + b s + 1$ valgono:
* **$a$ (termine di $s^2$):**
  $$a = R_s R_L [C_A (C_c + C_{GD}) + C_A C_L + C_L (C_c + C_{GD})]$$
* **$b$ (termine di $s$):**
  $$b = R_s [(1 + g_m R_L)(C_c + C_{GD}) + C_A] + R_L (C_c + C_{GD} + C_L)$$

---

### Passo 2: Il trucco dei "Poli ben separati" (Slide 19)
Ora abbiamo un polinomio di secondo grado al denominatore:
$$D(s) = a s^2 + b s + 1$$
In generale, un sistema con due poli reali si scrive come:
$$D(s) = \left(1 + \frac{s}{\omega_{pA}}\right)\left(1 + \frac{s}{\omega_{pB}}\right) = 1 + \left(\frac{1}{\omega_{pA}} + \frac{1}{\omega_{pB}}\right)s + \left(\frac{1}{\omega_{pA}\omega_{pB}}\right)s^2$$

Qui la prof fa l'**ipotesi di poli dominanti/ben separati** ($\omega_{pA} \ll \omega_{pB}$):  
Se il primo polo è a frequenza bassissima e il secondo a frequenza altissima, allora $\frac{1}{\omega_{pA}}$ è infinitamente più grande di $\frac{1}{\omega_{pB}}$!
$$\frac{1}{\omega_{pA}} + \frac{1}{\omega_{pB}} \approx \frac{1}{\omega_{pA}}$$
*(ecco perché nella slide 19 vedi barrato il termine $\frac{1}{\omega_{pB}}$ con la freccia "per l'ipotesi")*.

Questo trucco matematico è fantastico perché ci permette di dire subito che:
* **Il coefficiente di $s$ è semplicemente:**  
  $$b \approx \frac{1}{\omega_{pA}}$$
* **Il coefficiente di $s^2$ è:**  
  $$a = \frac{1}{\omega_{pA} \cdot \omega_{pB}}$$

---

### Passo 3: Ricavare i due poli (Slide 20)

#### 1. Il Polo Dominante $\omega_{pA}$:
Dato che $b \approx \frac{1}{\omega_{pA}}$, basta invertire $b$:
$$\omega_{pA} = \frac{1}{b} = \frac{1}{R_s [(1 + g_{m10} R_L)(C_c + C_{GD}) + C_A] + R_L(C_c + C_L + C_{GD})}$$

Guarda dentro la parentesi quadra: c'è **$R_s \cdot (1 + g_m R_L)(C_c + C_{GD})$**!  
È **esattamente l'effetto Miller**: la capacità $(C_c + C_{GD})$ vista dal nodo d'ingresso viene moltiplicata per il guadagno dello stadio $(1 + g_m R_L)$.  
Poiché $R_s$ è enorme e la capacità è moltiplicata per il guadagno, questo denominatore è mostruoso $\implies \mathbf{\omega_{pA}}$ **crolla a frequenza bassissima**.

#### 2. Il Secondo Polo $\omega_{pB}$:
Come si ricava $\omega_{pB}$ conoscendo $a$ e $b$?  
Facendo il rapporto:
$$\frac{b}{a} = \frac{\frac{1}{\omega_{pA}}}{\frac{1}{\omega_{pA}\omega_{pB}}} = \mathbf{\omega_{pB}}$$
Facendo $\frac{b}{a}$, il termine gigante $R_s R_L (1 + g_m R_L)(C_c + C_{GD})$ al numeratore si semplifica con i fattori $R_s R_L$ del denominatore, e dopo qualche semplificazione algebrica rimane:
$$\omega_{pB} \approx \frac{g_{m10}}{C_A + C_L}$$

**Il significato fisico (la nota manoscritta in basso a Slide 20):**  
Prima di mettere $C_c$, il polo al nodo B valeva $\omega_{pB} \approx \frac{1}{R_L C_L}$ (lento, perché $R_L$ è enorme).  
Ora con $C_c$, alle alte frequenze $C_c$ diventa un cortocircuito locale tra Drain e Gate del MOS:
* Il MOS si comporta da **diodo**, quindi la resistenza vista verso massa non è più $R_L$ ma crolla a **$1/g_{m10}$** (poche centinaia di ohm)!
* Le capacità $C_A$ e $C_L$ si trovano in parallelo.  
* Il polo diventa $\omega_{pB} \approx \frac{1}{(1/g_{m10})(C_A + C_L)} = \frac{g_{m10}}{C_A + C_L}$, che è a **frequenza altissima**!

---

### Passo 4: Il numeratore e lo zero a parte reale positiva (Slide 18 e 21)
Guarda il numeratore trovato a Slide 18:
$$N(s) = [(C_c + C_{GD})s - g_m] R_L$$
Se lo poniamo uguale a zero per trovare lo zero della funzione di trasferimento:
$$(C_c + C_{GD})s - g_m = 0 \implies \mathbf{s_z = + \frac{g_m}{C_c + C_{GD}}}$$

Questo zero ha **segno positivo** (si trova nel semipiano destro, **RHP Zero**)!
* **Perché c'è?** Perché ad alta frequenza la corrente può attraversare direttamente $C_c$ scavalcando il transistor (feedforward path).
* **Perché è pericoloso?** Perché uno zero aumenta il modulo del guadagno (+20 dB/dec), ma se è a destra **sfasa negativamente di $-90^\circ$** (esattamente come un polo!). Quindi mangia margine di fase e rischia di far oscillare l'amplificatore.

#### La soluzione (Slide 21):
Nelle slide 2 e 21 si vede che in serie a $C_c$ viene inserita una **resistenza $R_z$** (chiamata anche $R_c$):
* Con la resistenza in serie, lo zero si sposta a:
  $$s_z = \frac{1}{C_c \left(\frac{1}{g_{m10}} - R_z\right)}$$
* Se scegli **$R_z \approx \frac{1}{g_{m10}}$**, il denominatore va a zero e lo zero viene sparato all'infinito (eliminato!).
* Se scegli **$R_z > \frac{1}{g_{m10}}$**, lo zero passa nel semipiano sinistro (LHP), dove invece di togliere fase regala **$+90^\circ$ di fase benefica**, aumentando la stabilità!
* La faccenda dello **zero** è fondamentale. Vediamola in modo super intuitivo: **da dove nasce fisicamente**, **perché è una disgrazia**, e **come la resistenza $R_z$ lo elimina**.

---

### 1. Da dove salta fuori fisicamente lo zero? (I "due percorsi")

Guarda il transistor del secondo stadio $M_{10}$ con la capacità $C_c$ montata tra Gate e Drain.  
Un segnale di tensione $V_x$ presente sul Gate (nodo A) ha **DUE modi diversi** per arrivare all'uscita (nodo B):

```text
                  ┌────── Cc ──────┐  (Percorso 2: NON invertente, salta sopra)
                  │                │
                  ▼                ▼
   Vin ──[ Rs ]──( A )───────────( B )──► Vout
                  │                │
                  │   M10 (MOS)    │
                  └───[ G    D ]───┘  (Percorso 1: INVERTENTE, passa dal canale)
```

1. **Percorso 1 (attraverso il transistor):**  
   Il segnale $V_x$ pilota il gate $\implies$ il canale genera una corrente $I_{MOS} = g_m V_x$.  
   Poiché è un amplificatore a source comune, questo percorso è **invertente** (se $V_x$ sale, il transistor si accende e tira il nodo di uscita **verso il basso**).
2. **Percorso 2 (attraverso il condensatore $C_c$):**  
   Il condensatore è un filo aperto a bassa frequenza, ma ad alta frequenza fa passare corrente diretta: $I_{Cc} \approx s C_c V_x$.  
   Questo percorso è **diretto (feedforward) e NON invertente** (se $V_x$ sale, spinge carica dentro $C_c$ e tira il nodo di uscita **verso l'alto**).

---

### 2. Perché questo crea uno ZERO?

Che cos'è uno **zero** in una funzione di trasferimento?  
È una frequenza speciale in cui **l'uscita $V_{out}$ vale ZERO anche se l'ingresso si muove** ($V_x \neq 0$).

Immagina di metterti alla frequenza in cui l'uscita è ferma a zero ($V_{out} = 0$):
* Dal condensatore arriva una corrente verso l'uscita pari a:  
  $$I_{Cc} = (V_x - 0) \cdot s C_c = s C_c V_x \quad \text{(spinge in su)}$$
* Il transistor invece scarica una corrente pari a:  
  $$I_{MOS} = g_m V_x \quad \text{(tira in giù)}$$

Per fare in modo che il nodo di uscita non si muova affatto ($V_{out} = 0$), le due correnti devono **annullarsi a vicenda**:
$$I_{Cc} = I_{MOS} \implies s C_c V_x = g_m V_x$$
Semplificando $V_x$:
$$\mathbf{s_z = + \frac{g_m}{C_c}}$$

Ecco lo zero! È la frequenza in cui la corrente che "scavalca" attraverso il condensatore **pareggia ed elide esattamente** la corrente generata dal transistor.

---

### 3. Perché questo zero ha il segno PIÙ ed è una "bestia nera"?

Nota bene: lo zero è venuto con il **segno POSITIVO**:
$$s_z = \mathbf{+} \frac{g_m}{C_c}$$
In geometria dei controlli automatici, si trova nel semipiano destro del piano complesso ($s > 0$), per questo si chiama **RHP Zero** (*Right-Half Plane Zero*).

Perché è la cosa peggiore che possa capitare a un amplificatore?
* Uno **zero normale a sinistra (LHP, con segno meno)**:
  * Fa salire il modulo di $+20\text{ dB/dec}$.
  * **Regala $+90^\circ$ di fase positiva** (aiuta tantissimo la stabilità!).
* Un **polo (a sinistra)**:
  * Fa scendere il modulo di $-20\text{ dB/dec}$.
  * **Ritarda la fase di $-90^\circ$**.

Ma il nostro **RHP Zero (a destra, con segno più)** fa un mix disastroso:
1. Come tutti gli zeri, **fa salire il modulo (+20 dB/dec)** $\implies$ ritarda la discesa del guadagno, allargando la banda e spingendo la frequenza di cross-over più in alto.
2. Ma per via del segno $+$, **RITARDA LA FASE DI $-90^\circ$ (come se fosse un polo!)**:
   $$\text{Fase di } \left(1 - \frac{s}{\omega_z}\right) \xrightarrow{s=j\omega} -\arctan\left(\frac{\omega}{\omega_z}\right) \implies \mathbf{-90^\circ}$$

Ti ritrovi con un elemento che tiene alto il guadagno ma ti ammazza la fase:
* Polo dominante $\implies -90^\circ$
* Secondo polo $\implies -45^\circ / -90^\circ$
* RHP Zero $\implies$ altri $-90^\circ$!
La fase crolla ben oltre $-180^\circ$ mentre il guadagno è ancora $> 0\text{ dB} \implies$ **l'amplificatore oscilla e diventa instabile**.

---

### 4. Come risolve il problema la resistenza $R_z$ (Slide 21)?

Per impedire che il percorso capacitivo "vinca" sul transistor creando questo zero a destra, si mette una **resistenza $R_z$ in serie a $C_c$**:

```text
                  ┌───[ Rz ]───[ Cc ]───┐
                  │                     │
                  ▼                     ▼
   Vin ──[ Rs ]──( A )────────────────( B )──► Vout
                  │                     │
                  │        M10          │
                  └──────[ G   D ]──────┘
```

Ora l'impedenza del ramo superiore non è più solo $\frac{1}{s C_c}$, ma è:
$$Z = R_z + \frac{1}{s C_c} = \frac{1 + s C_c R_z}{s C_c}$$

Rifacciamo lo stesso bilancio di correnti con $V_{out} = 0$:
$$I_{\text{ramo sup}} = \frac{V_x}{Z} = \frac{s C_c V_x}{1 + s C_c R_z}$$
Uguagliamola alla corrente del transistor $g_m V_x$:
$$\frac{s C_c V_x}{1 + s C_c R_z} = g_m V_x$$
Semplificando $V_x$:
$$s C_c = g_m (1 + s C_c R_z) = g_m + s C_c g_m R_z$$
Portiamo $s$ a sinistra:
$$s C_c (1 - g_m R_z) = g_m$$
Ricaviamo la nuova posizione dello zero:
$$\mathbf{s_z = \frac{g_m}{C_c (1 - g_m R_z)} = \frac{1}{C_c \left(\frac{1}{g_m} - R_z\right)}}$$

Guarda cosa succede al variare di $R_z$ (è proprio quello che vedi scritto a mano nella **Slide 21**):

1. **Se scegli $R_z = \frac{1}{g_m}$:**  
   Al denominatore hai $\frac{1}{g_m} - \frac{1}{g_m} = 0 \implies \mathbf{s_z \to \infty}$!  
   Lo zero viene **sparato a frequenza infinita**, cioè **scompare del tutto dal circuito**!
2. **Se scegli $R_z > \frac{1}{g_m}$:**  
   Il termine $\left(\frac{1}{g_m} - R_z\right)$ diventa **negativo**!  
   Quindi lo zero **cambia segno** e si sposta nel **semipiano sinistro (LHP Zero)**:
   $$\mathbf{s_z < 0}$$
   Ora non è più dannoso, anzi fa il miracolo: essendo a sinistra, **regala $+90^\circ$ di fase positiva**, che va a cancellare il ritardo introdotto dal secondo polo $\omega_{pB}$, rendendo l'amplificatore stabilissimo!