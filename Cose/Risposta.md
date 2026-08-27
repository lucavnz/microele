Ran command: `python -c "
import fitz

doc = fitz.open('modelli.pdf')
# PDF pages 69 to 76 (0-indexed 68 to 75)
for pno in range(68, 76):
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    out_path = f'C:/Users/Accetazione/.gemini/antigravity-ide/brain/7d4aa0ac-2f49-44d3-94b2-08f701aea9de/salita_p{pno+1}.png'
    pix.save(out_path)
    text = page.get_text()
    first_line = text.strip().split('\n')[0] if text.strip() else ''
    last_line = text.strip().split('\n')[-1] if text.strip() else ''
    print(f'PDF p.{pno+1} (Slide {last_line}) -> {first_line} -> {out_path}')
"`
Ran command: `python -c "
import fitz

doc = fitz.open('modelli.pdf')
for pno in range(68, 75):
    print(f'==========================================')
    print(f'PDF PAGE {pno+1} (Slide footer: {doc[pno].get_text().strip().split()[-1]})')
    print(f'==========================================')
    print(doc[pno].get_text().encode('ascii', errors='replace').decode('ascii'))
"`
Viewed salita_p70.png:1-800
Viewed salita_p71.png:1-800
Viewed salita_p72.png:1-800
Viewed salita_p73.png:1-800

Nelle slide da 74 a 78 (pagine PDF da 70 a 74), il professore analizza il fenomeno opposto: **il transitorio di salita**, cioè **l'accensione del diodo**.

### Lo scenario
* **Circuito:** Il solito generatore $V_g$ con la resistenza $R = 10\text{ k}\Omega$ in serie al diodo.
* **Stato iniziale ($t < 0$):** $V_g = -V_2$ (tensione negativa, es. $-20\text{ V}$ o $-5\text{ V}$). Il diodo è **spento (inversa)**, la corrente è quasi nulla ($I \approx -I_S \approx 0$), quindi ai suoi capi c'è tutta la tensione negativa: $V(0) = -V_2$.
* **All'istante $t = 0$:** Il generatore commuta bruscamente a **$+V_1$** (tensione positiva, es. $+20\text{ V}$ o $+5\text{ V}$).
* **L'obiettivo:** Calcolare come la tensione $V(t)$ ai capi del diodo sale da $-V_2$ fino al valore di conduzione diretta $+V_{ON} \approx 0.7\text{ V}$.

Anche qui il professore divide il transitorio in **DUE FASI**:
1. **Fase 1 ($V < 0$, da $0$ a $t_0$):** La tensione sale da $-V_2$ fino a $0\text{ V}$ (Slide 74-75).
2. **Fase 2 ($V > 0$, per $t > t_0$):** La tensione sale da $0\text{ V}$ fino a $\approx 0.7\text{ V}$ (Slide 76-77).
3. **Confronto globale (Slide 78):** Il transitorio completo.

---

### FASE 1: Slide 74 e 75 – Transitorio di Salita con $V < 0$ ($0 \le t \le t_0$)

#### 1. Cosa fa la fisica qui? Cosa si trascura? (Slide 74)
* Finché la tensione ai capi del diodo è negativa ($V \le 0$), il diodo è ancora interdetto: non ci sono portatori minoritari iniettati nella base.
* Quindi: **la carica di diffusione è ZERO ($Q_d = 0$) e la capacità di diffusione è ZERO ($C_d = 0$)!**
* Chi comanda in questa fase è **SOLO la capacità di svuotamento/giunzione $C_j$**.
* Il generatore $+V_1$ deve "restringere" la zona di svuotamento caricando la capacità $C_j$ attraverso la resistenza $R$. È a tutti gli effetti una **carica esponenziale di un circuito RC**!

#### 2. Il calcolo con $C_{eq}$
Poiché $C_j(V)$ è non-lineare, per fare il calcolo a mano si usa di nuovo la **capacità equivalente $C_{eq} = K_{eq} C_{j0}$** tra $V_a = -V_2$ e $V_b = 0\text{ V}$:
* Valore iniziale: $V(0) = -V_2$
* Valore a cui tenderebbe l'asintoto: $V(\infty) = +V_1$
* Soluzione classica:
  $$V(t) = V_1 - (V_1 + V_2) e^{-\frac{t}{R C_{eq}}}$$
* **Il tempo $t_0$ (quando $V = 0\text{ V}$):**
  Imponendo $V(t_0) = 0$, si ricava il tempo impiegato per arrivare a zero:
  $$t_0 = R C_{eq} \ln\left(1 + \frac{V_2}{V_1}\right)$$
  *(Nota: il prof scrive nel fumetto rosso che il diodo rimane spento fino a circa l'$80\%$ di $V_{ON} \approx 0.55\text{ V}$, ma per semplicità analitica pone il traguardo a $0\text{ V}$)*.

#### 3. Analisi del grafico di Slide 75 (Esempio Numerico)
Guardiamo le due curve nel grafico:
* **Curva verde ("calcolo"):** formula teorica esponenziale con $C_{eq}$ costante ($C_{eq} = 67.9\text{ fF}$ per $20\text{ V}$; $96.4\text{ fF}$ per $5\text{ V}$).
* **Curva arancione ("simulazione"):** simulazione reale con $C_j(V)$ variabile.

**Perché all'inizio la simulazione (arancione) sale più veloce del calcolo (verde)?**
* A $-20\text{ V}$, la giunzione è allargatissima, quindi la capacità reale $C_j$ è piccolissima ($49.1\text{ fF} < C_{eq} = 67.9\text{ fF}$).
* Poiché la costante di tempo reale $\tau = R C_j$ è più piccola, il transitorio reale **parte più ripido**!
* Man mano che la tensione sale verso $0\text{ V}$, la giunzione si restringe, $C_j$ cresce fino a $150\text{ fF}$ ($> C_{eq}$) e la salita rallenta.
* Alla fine, in $t_0$, le due curve si incrociano: il tempo $t_0$ calcolato ($471\text{ ps}$ per $20\text{ V}$, $668\text{ ps}$ per $5\text{ V}$) è incredibilmente accurato!

---

### FASE 2: Slide 76 e 77 – Transitorio con $V > 0$ ($t > t_0$)

Qui arriva il punto concettuale più importante di tutta la lezione.

#### 1. L'impostazione teorica di Slide 76
* A $t = t_0$, la tensione supera $0\text{ V}$. Adesso la giunzione si polarizza in diretta e comincia a iniettare cariche minoritarie (si deve accumulare la carica $Q_d$).
* Condizioni:
  * A $t = t_0$: $Q_d(t_0) = 0$ (non c'erano ancora cariche).
  * A regime ($t \to \infty$): la corrente a regime è $I \approx V_1 / R$, quindi la carica finale sarà $Q_d(\infty) = \tau_T \frac{V_1}{R}$.
* Il professore imposta l'equazione differenziale per la carica $Q_d$:
  $$Q_d(t) = \tau_T \frac{V_1}{R} \left(1 - e^{-\frac{t - t_0}{\tau_T}}\right)$$
  e ricava la tensione: $V(t) = \Phi_T \ln\left(1 + \frac{Q_d(t)}{\tau_T I_S}\right)$.
* **Cosa ha trascurato qui il professore nel fare la formula?**
  Nel formulare questa equazione ha considerato **SOLO la carica di diffusione $Q_d$**, ignorando completamente $C_j$!

#### 2. Il colpo di scena nei grafici di Slide 77!
Guarda il grafico di Slide 77: ci sono tre curve per la tensione $V(t)$:
1. **Curva verde ("calcolo"):** la formula teorica con solo $Q_d$.
2. **Curva rossa ("simulazione con $C_{j0} = 0$"):** la simulazione SPICE in cui $C_j$ è forzata a zero.
   *(Nota: la curva verde e la curva rossa sono identiche e salgono in verticale quasi istantaneamente!)*
3. **Curva azzurra ("simulazione con $C_{j0} = 150\text{ fF}$", cioè il circuito reale):**
   **È LENTISSIMA rispetto alle altre due!** Sale con una pendenza molto più dolce!

Il professore scrive in giallo:
> **"Prevale ancora $C_j$!"**

#### Perché la curva azzurra è così lenta? Perché $C_j$ non si può trascurare qui?
È la differenza chiave rispetto al transitorio di discesa (spegnimento):
* **Nello spegnimento (slide 68):** il diodo era già carico di minoritari ($Q_d$ enorme). $C_j$ era minuscola al confronto, quindi trascurarla non faceva danni.
* **Nell'accensione (slide 77):** all'istante $t = t_0$, **$Q_d$ parte da ZERO!**
* Invece a $V \approx 0\text{ V}$, la capacità di giunzione $C_j$ è al suo **massimo storico** ($C_j \ge C_{j0} = 150\text{ fF}$)!
* Prima che la tensione possa salire verso $0.7\text{ V}$, la corrente fornita dalla resistenza $R$ viene **interamente assorbita da $C_j$ per caricare la zona di svuotamento**!
* Quindi è la capacità di giunzione $C_j$ che frena e rallenta tutta la salita della tensione, specialmente a $V_1 = 5\text{ V}$ dove la corrente disponibile è minore ($0.5\text{ mA}$ contro i $2\text{ mA}$ del caso a $20\text{ V}$).
* **Conclusione fisica:** L'assunzione analitica di trascurare $C_j$ per $t > t_0$ era **sbagliata**: $C_j$ detta legge anche sopra lo zero!

---

### Slide 78 – TRANSITORIO COMPLETO

Slide 78 mette insieme i due pezzi del puzzle (da $-V_2$ fino a $+V_{ON}$) e confronta i due casi:

1. **Caso con tensioni elevate ($V_1 = V_2 = 20\text{ V}$, grafico in alto):**
   * Corrente disponibile grande ($I \approx 2\text{ mA}$).
   * Sotto lo zero domina $C_j$.
   * Sopra lo zero la corrente è sufficiente a caricare in fretta sia $C_j$ che $Q_d$: compare l'effetto di $C_d$ e la curva di calcolo non è troppo lontana dalla simulazione.
2. **Caso con tensioni moderate/basse ($V_1 = V_2 = 5\text{ V}$, grafico in basso):**
   * Corrente disponibile limitata ($I \approx 0.5\text{ mA}$).
   * La capacità di giunzione $C_j$ assorbe gran parte della corrente per tutta la transizione.
   * Il professore mette la freccia con la scritta:
     > **"Prevale ancora $C_j$!"**
     Il calcolo teorico semplificato (che trascurava $C_j$ sopra lo zero) fa un errore visibile, perché la salita reale (curva arancione) è molto più lenta e smussata a causa di $C_j$.

---

### Tabella di riepilogo: Discesa vs Salita

| Fase del Transitorio | Cosa fa la tensione | Chi domina la fisica? | È lecito trascurare $C_j$? |
| :--- | :--- | :--- | :--- |
| **Discesa (Spegnimento) $0 < t < t_S$** | Resta a $+0.7\text{ V}$ | **$C_d$ (Carica $Q_d$)** | **SÌ.** $Q_d$ è talmente grande che $C_j$ non conta quasi nulla. |
| **Discesa (Spegnimento) $t > t_S$** | Crolla da $0$ a $-V_2$ | **$C_j$ (Circuito RC con $C_{eq}$)** | $C_d = 0$, esiste solo $C_j$. |
| **Salita (Accensione) $0 < t < t_0$** | Sale da $-V_2$ a $0\text{ V}$ | **$C_j$ (Circuito RC con $C_{eq}$)** | $C_d = 0$, esiste solo $C_j$. |
| **Salita (Accensione) $t > t_0$** | Sale da $0$ a $+0.7\text{ V}$ | **Ancora $C_j$!** (poi interviene $C_d$) | **NO!** $Q_d$ parte da zero, quindi $C_j$ rallenta pesantemente l'accensione. |