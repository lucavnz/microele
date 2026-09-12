Ran command: `python3 -c "
import pypdf
print('pypdf installed')
" 2>/dev/null || python3 -c "
import fitz
print('PyMuPDF installed')
" 2>/dev/null || python3 -c "
import pdfplumber
print('pdfplumber installed')
" 2>/dev/null || echo "No direct python pdf lib"
`
Ran command: `python3 -c "
from pypdf import PdfReader
reader = PdfReader('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
print(f'Total pages: {len(reader.pages)}')
for idx in range(min(30, len(reader.pages))):
    text = reader.pages[idx].extract_text()
    first_lines = '\n'.join([line for line in text.splitlines() if line.strip()][:3])
    print(f'--- PAGE {idx+1} ---')
    print(first_lines)
"`
Ran command: `python3 -c "
from pypdf import PdfReader
reader = PdfReader('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
for p in range(14, 22):
    print(f'=================== SLIDE {p+1} ===================')
    print(reader.pages[p].extract_text())
"`
Ran command: `which pdftoppm`
Ran command: `python3 -c "
for mod in ['pypdfium2', 'fitz', 'pdf2image', 'ghostscript', 'sckit-image', 'matplotlib', 'PIL']:
    try:
        __import__(mod)
        print(f'{mod}: available')
    except ImportError:
        print(f'{mod}: NOT available')
"`
Ran command: `python3 -c "
import pypdfium2 as pdfium
import os

pdf = pdfium.PdfDocument('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
out_dir = '/Users/matteoluca/.gemini/antigravity-ide/brain/d7c9ed11-0bf8-488e-8a69-eff19a0ba908/scratch/slides'
os.makedirs(out_dir, exist_ok=True)

# Slides 15 to 22 (0-indexed: 14 to 21)
for i in range(14, 22):
    page = pdf[i]
    image = page.render(scale=2).to_pil()
    image.save(f'{out_dir}/slide_{i+1}.png')
    print(f'Saved slide_{i+1}.png')
"`
Viewed slide_15.png:1-800
Viewed slide_16.png:1-800
Viewed slide_17.png:1-800
Viewed slide_18.png:1-800
Viewed slide_19.png:1-800
Viewed slide_20.png:1-800
Viewed slide_21.png:1-800
Viewed slide_22.png:1-800

Le slide da **15 a 21** della lezione **LEZ7-b** introducono la teoria fondamentale alla base dei **riferimenti di tensione integrati indipendenti dalla temperatura**, che culminano nella celebre architettura del **riferimento a Bandgap**.

Di seguito trovi la spiegazione dettagliata, slide per slide, con il significato fisico, i passaggi matematici (anche quelli che sulle slide sono condensati) e i valori numerici.

---

### Mappa concettuale rapida
1. **Slide 15 & 16**: L'idea ingegneristica $\rightarrow$ sommare due tensioni con pendenze termiche opposte per ottenere pendenza zero.
2. **Slide 17**: Da dove prendiamo queste due tensioni nei circuiti integrati $\rightarrow$ da giunzioni bipolari (BJT).
3. **Slide 18, 19, 20, 21**: Studio approfondito del **coefficiente negativo** (CTAT) fornito dalla tensione base-emettitore $V_{BE}$ del BJT.

---

### Slide 15 – Riferimenti di tensione: Obiettivo e Concetto di Bandgap

* **Il problema pratico**: Nei circuiti integrati (convertitori A/D, D/A, memorie, regolatori LDO, polarizzazioni) serve una tensione fissa $V_{ref}$ che non cambi al variare della temperatura $T$, dell'alimentazione $V_{DD}$ e dei parametri di processo (PVT).
* **La strategia**: Nessun dispositivo elementare ha una tensione naturalmente costante con la temperatura. L'idea è quindi sommare due tensioni con comportamento opposto:
  * Una tensione con coefficiente di temperatura **negativo** (detta **CTAT**: *Complementary To Absolute Temperature*), che scende all'aumentare di $T$.
  * Una tensione con coefficiente di temperatura **positivo** (detta **PTAT**: *Proportional To Absolute Temperature*), che sale all'aumentare di $T$.
* **Perché si chiama "a Bandgap"?**: Perché combinando opportunamente queste due tensioni, il valore di $V_{ref}$ ottenuto (estrapolato allo zero assoluto $0\text{ K}$) converge esattamente al valore dell'**energy gap (bandgap) del silicio** diviso per la carica dell'elettrone:
  $$V_{ref} \approx \frac{E_g}{q} \approx 1.2\text{ V}$$
* **Metrica di prestazione (ppm/°C)**: La bontà del riferimento si misura tramite la **deriva termica** (TC, *Temperature Coefficient*):
  $$TC = \frac{1}{V_{ref}} \frac{\partial V_{ref}}{\partial T} \times 10^6 \quad [\text{ppm/}^\circ\text{C}]$$
  Un buon bandgap integrato ha derive nell'ordine di $10 \div 50\text{ ppm/}^\circ\text{C}$ (o inferiori se compensato).

---

### Slide 16 – Il Principio Matematico di Compensazione

La slide formalizza l'idea intuitiva:
1. Definiamo la tensione di riferimento come combinazione lineare pesata di due tensioni $V_1$ e $V_2$:
   $$V_{ref} = c_1 V_1 + c_2 V_2$$
   dove $c_1$ e $c_2$ sono fattori di proporzionalità (nella pratica circuitale saranno rapporti di resistenze, specchi di corrente o guadagni di amplificatori operazionali).
2. Per rendere $V_{ref}$ indipendente dalla temperatura a una data temperatura nominale $T_0$ (tipicamente ambiente, $300\text{ K} \approx 27^\circ\text{C}$), imponiamo la derivata prima nulla:
   $$\frac{\partial V_{ref}}{\partial T} = c_1 \frac{\partial V_1}{\partial T} + c_2 \frac{\partial V_2}{\partial T} = 0$$
3. Se $V_1$ ha coefficiente negativo ($\frac{\partial V_1}{\partial T} < 0$) e $V_2$ positivo ($\frac{\partial V_2}{\partial T} > 0$), basta scegliere i pesi $c_1$ e $c_2$ in modo che:
   $$c_2 \frac{\partial V_2}{\partial T} = - c_1 \frac{\partial V_1}{\partial T}$$

---

### Slide 17 – Come si ottengono $V_1$ e $V_2$?

La professoressa chiarisce quali blocchi fisici forniscono $V_1$ e $V_2$:
* **$V_1$ (Coefficiente Negativo / CTAT)**: Si ricava direttamente dalla **$V_{BE}$ di un BJT polarizzato in RND** (*Regione Normale Diretta*).
  *(Nota: anche nei processi CMOS puri, si usano BJT parassiti verticali o laterali pnp/npn formati dalle diffusioni e dal substrato o dalle n-well).*
* **$V_2$ (Coefficiente Positivo / PTAT)**: Si ricava dalla **differenza** tra le tensioni base-emettitore di due BJT ($\Delta V_{BE} = V_{BE1} - V_{BE2}$) polarizzati con densità di corrente diverse (agendo sul rapporto delle correnti $n$ e sul rapporto delle aree di emettitore $m$).

---

### Slide 18 – Tensione con coefficiente negativo (1): Il "Paradosso" della $V_{BE}$

Dall'equazione del BJT in conduzione diretta:
$$I_C = I_S \exp\left(\frac{V_{BE}}{V_T}\right) \implies V_{BE} = V_T \ln\left(\frac{I_C}{I_S}\right)$$
dove $V_T = \frac{kT}{q}$ è la tensione termica.

* **Il dubbio tipico dello studente**: Se $V_T = \frac{kT}{q}$ cresce linearmente con la temperatura $T$, perché mai la $V_{BE}$ diminuisce?
* **La risposta fisica**: All'interno del logaritmo c'è la corrente di saturazione inversa $I_S$. **$I_S$ cresce in maniera mostruosamente rapida (esponenziale) con la temperatura**, sovrastando di gran lunga la crescita lineare di $V_T$. Di conseguenza, per mantenere costante la corrente $I_C$, la $V_{BE}$ **deve diminuire**.
* **Problema della curvatura**: La derivata $\frac{\partial V_{BE}}{\partial T}$ non è una costante fissa, ma dipende a sua volta da $T$. Perciò:
  * L'annullamento della derivata $\frac{\partial V_{ref}}{\partial T} = 0$ è perfetto solo ad **una specifica temperatura** di progetto.
  * Se si plotta $V_{ref}$ in funzione di $T$, si ottiene una curva con andamento a campana/parabolico (detta **curvatura del bandgap**). Per applicazioni ultra-precise servono tecniche di compensazione della curvatura (*curvature correction*).

---

### Slide 19 – Origine Fisica della dipendenza termica di $I_S$

Questa slide risponde alla domanda: *perché $I_S$ cresce così tanto con la temperatura?*

Dalla fisica dei semiconduttori, la corrente di saturazione inversa di un diodo/BJT è legata alla diffusione e concentrazione dei portatori:
$$I_S \propto \mu \cdot KT \cdot n_i^2$$
La slide analizza i due contributi fondamentali:
1. **La mobilità $\mu$**:
   All'aumentare di $T$, le oscillazioni del reticolo cristallino (fononi) aumentano, ostacolando il moto degli elettroni/lacune (scattering reticolare). La mobilità decresce come:
   $$\mu \propto \mu_0 T^{-3/2}$$
2. **La concentrazione intrinseca al quadrato $n_i^2$**:
   Governata dalla statistica di Fermi-Dirac / Boltzmann e dalle densità di stati ($N_C, N_V \propto T^{3/2}$):
   $$n_i^2 = N_C N_V \exp\left(-\frac{E_g}{KT}\right) \propto T^3 \exp\left(-\frac{E_g}{KT}\right)$$

Moltiplicando i fattori:
$$I_S \propto (\mu) \cdot (T) \cdot (n_i^2) \propto T^{-3/2} \cdot T^1 \cdot T^3 \exp\left[-\frac{E_g}{KT}\right] = T^{2.5} \exp\left[-\frac{E_g}{KT}\right]$$

La slide adotta la notazione classica compatta della letteratura (es. Gray-Meyer/Razavi):
$$I_S \propto T^{4+m} \exp\left[-\frac{E_g}{KT}\right] \quad \text{con } m \approx -3/2$$
Infatti: $4 + m = 4 - 1.5 = 2.5$.

---

### Slide 20 – Derivazione Matematica di $\frac{\partial V_{BE}}{\partial T}$

Sulla slide ci sono due formule collegate da una freccia arancione. Ecco tutti i passaggi algebrici passo per passo.

#### Passaggio 1: Derivata iniziale del prodotto
Partiamo da $V_{BE} = V_T \ln(I_C / I_S) = V_T [\ln(I_C) - \ln(I_S)]$.
Ipotizzando $I_C$ costante rispetto a $T$ ($\frac{\partial I_C}{\partial T} \approx 0$), applichiamo la derivata del prodotto:
$$\frac{\partial V_{BE}}{\partial T} = \frac{\partial V_T}{\partial T} \ln\left(\frac{I_C}{I_S}\right) + V_T \frac{\partial}{\partial T}\left(-\ln I_S\right) = \frac{\partial V_T}{\partial T} \ln\left(\frac{I_C}{I_S}\right) - \frac{V_T}{I_S} \frac{\partial I_S}{\partial T}$$
*(Questa è esattamente la prima equazione in alto nella slide 20)*.

#### Passaggio 2: Sviluppo del primo termine
Poiché $V_T = \frac{kT}{q}$, la sua derivata è:
$$\frac{\partial V_T}{\partial T} = \frac{k}{q} = \frac{V_T}{T}$$
Inoltre, dalla definizione di $V_{BE}$, abbiamo che $\ln(I_C/I_S) = \frac{V_{BE}}{V_T}$. Sostituendo:
$$\frac{\partial V_T}{\partial T} \ln\left(\frac{I_C}{I_S}\right) = \frac{V_T}{T} \cdot \frac{V_{BE}}{V_T} = \frac{V_{BE}}{T}$$

#### Passaggio 3: Sviluppo del secondo termine tramite $\ln(I_S)$
Dalla Slide 19, scriviamo $I_S = C \cdot T^{4+m} \exp\left(-\frac{E_g}{KT}\right)$ (con $C$ costante).
Prendiamo il logaritmo naturale:
$$\ln(I_S) = \ln(C) + (4+m)\ln(T) - \frac{E_g}{KT}$$
Deriviamo rispetto a $T$:
$$\frac{1}{I_S} \frac{\partial I_S}{\partial T} = \frac{\partial \ln(I_S)}{\partial T} = \frac{4+m}{T} - \left(-\frac{E_g}{K T^2}\right) = \frac{4+m}{T} + \frac{E_g}{K T^2}$$
Ora moltiplichiamo per $V_T = \frac{KT}{q}$:
$$\frac{V_T}{I_S}\frac{\partial I_S}{\partial T} = \frac{KT}{q}\left[ \frac{4+m}{T} + \frac{E_g}{KT^2} \right] = \frac{(4+m)V_T}{T} + \frac{E_g / q}{T}$$

#### Passaggio 4: Risultato finale
Sostituendo i due termini nella derivata di $V_{BE}$:
$$\frac{\partial V_{BE}}{\partial T} = \frac{V_{BE}}{T} - \left[ \frac{(4+m)V_T}{T} + \frac{E_g / q}{T} \right]$$
Raccogliendo $T$ a denominatore comune si ottiene la formula finale nel riquadro della slide:
$$\frac{\partial V_{BE}}{\partial T} = \frac{V_{BE} - (4+m)V_T - E_g / q}{T}$$

---

### Slide 21 – Esempio Numerico Reale

La slide applica la formula appena ricavata per calcolare quanto vale numericamente questo coefficiente a temperatura ambiente:
* **Dati tipici di funzionamento**:
  * Temperatura ambiente: $T = 300\text{ K}$ ($27^\circ\text{C}$).
  * Tensione di polarizzazione della giunzione: $V_{BE} \approx 750\text{ mV} = 0.75\text{ V}$.
  * Tensione termica: $V_T = \frac{kT}{q} \approx 26\text{ mV} = 0.026\text{ V}$.
  * Bandgap del silicio: $\frac{E_g}{q} \approx 1.12\text{ V} \div 1.2\text{ V}$.
  * Esponente: $4+m = 4 - 1.5 = 2.5$.

* **Calcolo del numeratore**:
  $$\text{Num} = 0.75\text{ V} - 2.5 \cdot (0.026\text{ V}) - 1.12\text{ V}$$
  $$\text{Num} = 0.75 - 0.065 - 1.12 = -0.435\text{ V} = -435\text{ mV}$$

* **Calcolo della pendenza**:
  $$\frac{\partial V_{BE}}{\partial T} = \frac{-435\text{ mV}}{300\text{ K}} \approx -1.45 \div -1.5\text{ mV/K}$$

* **Conclusione fisica fondamentale**:
  $$\frac{\partial V_{BE}}{\partial T} \approx -1.5\text{ mV/}^\circ\text{C}$$
  Ogni grado Celsius di aumento della temperatura fa scendere la $V_{BE}$ di circa **$1.5\text{ mV}$** (valore tipico tra $-1.5$ e $-2\text{ mV/}^\circ\text{C}$). 
  Abbiamo quindi trovato in modo rigoroso il nostro segnale **CTAT**.

---

### Verso le slide successive (Slide 22+)
Nelle slide che seguono (22-25), vedrai come ricavare la tensione a **coefficiente positivo**:
$$\Delta V_{BE} = V_T \ln(m \cdot n) \implies \frac{\partial \Delta V_{BE}}{\partial T} = \frac{k}{q}\ln(m \cdot n) \approx +0.087\text{ mV/K} \cdot \ln(m \cdot n)$$
e come sommarla a $V_{BE}$ con un guadagno opportuno per annullare perfettamente i $-1.5\text{ mV/}^\circ\text{C}$ ottenuti qui alla Slide 21.

Ran command: `python3 -c "
import pypdfium2 as pdfium
import os

pdf = pdfium.PdfDocument('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
out_dir = '/Users/matteoluca/.gemini/antigravity-ide/brain/d7c9ed11-0bf8-488e-8a69-eff19a0ba908/scratch/slides'
os.makedirs(out_dir, exist_ok=True)

for i in range(21, 29): # slides 22 to 29 (0-indexed 21 to 28)
    page = pdf[i]
    image = page.render(scale=2).to_pil()
    image.save(f'{out_dir}/slide_{i+1}.png')
    print(f'Saved slide_{i+1}.png')
"`
Viewed slide_22.png:1-800
Viewed slide_23.png:1-800
Viewed slide_24.png:1-800
Viewed slide_25.png:1-800
Viewed slide_26.png:1-800
Viewed slide_27.png:1-800
Viewed slide_28.png:1-800

Ecco la spiegazione dettagliata, passo dopo passo e con tutti i passaggi matematici, delle **slide da 22 a 28** della lezione sui riferimenti di tensione.

---

### Mappa del percorso (Slide 22–28)
Nelle slide 15–21 abbiamo analizzato il termine a **coefficiente negativo** (CTAT):
$$\frac{\partial V_{BE}}{\partial T} \approx -1.5\text{ mV/}^\circ\text{C}$$
Ora l'obiettivo delle slide 22–28 è:
1. **Slide 22, 23, 24:** Trovare il termine a **coefficiente positivo** (PTAT) $\rightarrow$ la differenza $\Delta V_{BE}$.
2. **Slide 25, 26, 27:** Mettere insieme i due pezzi ($V_{ref} = c_1 V_{BE} + c_2 \Delta V_{BE}$), trovare il fattore di proporzionalità e dimostrare perché il risultato converge a **$\approx 1.25\text{ V}$** (Bandgap del silicio).
3. **Slide 28:** Costruire il primo schema circuitale per sommare le tensioni e far emergere il limite pratico che porterà al circuito completo.

---

### Slide 22 – Tensione con coefficiente positivo (I)

* **L'idea fisica:** Sappiamo che la tensione termica $V_T = \frac{kT}{q}$ ha un coefficiente di temperatura **positivo** ed è perfettamente lineare con $T$:
  $$\frac{\partial V_T}{\partial T} = \frac{k}{q} \approx \frac{1.38 \times 10^{-23}\text{ J/K}}{1.6 \times 10^{-19}\text{ C}} \approx +0.087\text{ mV/}^\circ\text{C}$$
* **Il problema:** $V_T$ è una costante fisica legata all'energia termica dei portatori nel semiconduttore; non esiste un "morsetto" fisico da cui prelevare direttamente $V_T$.
* **La genialità circuitale:** Possiamo estrarre una tensione proporzionale a $V_T$ facendo la **differenza tra le $V_{BE}$ di due transistor bipolari polarizzati a densità di corrente diversa**:
  $$\Delta V_{BE} = V_{BE1} - V_{BE2}$$
* **Perché la differenza elimina il problema di $I_S$?**
  Sottraendo le due tensioni, il termine logaritmico della corrente di saturazione inversa $I_S(T)$ (che creava la complicata dipendenza non lineare a slide 19-20) **si elide completamente**!
* Come si sbilanciano le due $V_{BE}$? In due modi:
  1. Alimentandoli con **correnti diverse** (rapporto $n$).
  2. Costruendoli con **aree di emettitore diverse** (rapporto $m$).

---

### Slide 23 – Coefficiente positivo di T (II): Sbilanciamento in Corrente ($n$)

La slide analizza il primo caso: due transistor identici ($Q_1$ e $Q_2$) con la stessa area (quindi $I_{S1} = I_{S2} = I_S$).
* $Q_1$ è polarizzato con una corrente $n I_C$ ($n > 1$).
* $Q_2$ è polarizzato con una corrente $I_C$.

Scriviamo le due tensioni base-emettitore:
$$V_{BE1} = V_T \ln\left(\frac{n I_C}{I_S}\right)$$
$$V_{BE2} = V_T \ln\left(\frac{I_C}{I_S}\right)$$

Calcoliamo la differenza tra le due $V_{BE}$ (sfruttando la proprietà dei logaritmi $\ln A - \ln B = \ln(A/B)$):
$$\Delta V_{BE} = V_{BE1} - V_{BE2} = V_T \left[ \ln\left(\frac{n I_C}{I_S}\right) - \ln\left(\frac{I_C}{I_S}\right) \right] = V_T \ln\left(\frac{\frac{n I_C}{I_S}}{\frac{I_C}{I_S}}\right)$$

$$\mathbf{\Delta V_{BE} = V_T \ln(n)}$$

Deriviamo rispetto alla temperatura $T$:
$$\frac{\partial \Delta V_{BE}}{\partial T} = \frac{\partial}{\partial T}\left( \frac{kT}{q} \ln n \right) = \frac{\mathbf{k}}{\mathbf{q}} \ln(n)$$

* **Osservazione fondamentale:**  
  Essendo $n > 1$, si ha $\ln(n) > 0$. Poiché $k/q > 0$, la derivata è **rigorosamente positiva**!  
  Abbiamo ottenuto una tensione **PTAT pura**: varia in modo perfettamente lineare con la temperatura, senza alcuna distorsione legata a $I_S$.

---

### Slide 24 – Coefficiente positivo di T (III): Sbilanciamento in Area ($m$) e Combinato

Nella pratica integrata, usare solo il rapporto di corrente $n$ ha un limite: per avere un $\ln(n)$ grande servirebbero correnti enormemente sbilanciate (es. 100 volte più corrente in un ramo rispetto all'altro), con grande spreco di potenza.

Possiamo allora sbilanciare anche l'**area di giunzione** dei due transistor:
* $Q_1$ ha area unitaria $A_1 = A \implies I_{S1} = I_S$.
* $Q_2$ è costituito da $m$ transistor identici in parallelo, quindi ha area $A_2 = m \cdot A \implies I_{S2} = m \cdot I_S$.

Se alimentiamo $Q_1$ con corrente $n I_C$ e $Q_2$ con corrente $I_C$:
$$V_{BE1} = V_T \ln\left(\frac{n I_C}{I_S}\right)$$
$$V_{BE2} = V_T \ln\left(\frac{I_C}{m I_S}\right)$$

Sottraendo:
$$\Delta V_{BE} = V_{BE1} - V_{BE2} = V_T \ln\left(\frac{\frac{n I_C}{I_S}}{\frac{I_C}{m I_S}}\right) = \mathbf{V_T \ln(n \cdot m)}$$

E la derivata termica vale:
$$\frac{\partial \Delta V_{BE}}{\partial T} = \frac{k}{q} \ln(n \cdot m)$$

> **Vantaggio pratico:** Giocando sia sulle correnti ($n$) sia sul layout delle aree ($m$), l'argomento del logaritmo diventa il prodotto $n \cdot m$. Ad esempio, con $n = 2$ e $m = 8$, l'argomento è $16$, ottenuto senza correnti elevate e con un layout compatto a matrice (common-centroid).

---

### Slide 25 – Riferimento a Bandgap (I): Mettiamo insieme le cose...

Ora abbiamo a disposizione entrambi i blocchi:
1. **Termine CTAT (negativo):** $V_{BE}$, con pendenza $\frac{\partial V_{BE}}{\partial T} \approx -1.5\text{ mV/}^\circ\text{C}$.
2. **Termine PTAT (positivo):** $V_T \ln(nm)$, dove la tensione termica elementare ha pendenza $\frac{\partial V_T}{\partial T} = \frac{k}{q} \approx +0.087\text{ mV/}^\circ\text{C}$.

Scriviamo la tensione di riferimento complessiva:
$$V_{ref} = c_1 V_{BE} + c_2 V_T \ln(nm)$$

* **Il confronto numerico immediato:**
  * Il coefficiente negativo è di circa **$-1.5\text{ mV/K}$**.
  * La pendenza intrinseca di $V_T$ è di appena **$+0.087\text{ mV/K}$**.
  * Si vede subito che il termine positivo è circa **17 volte più piccolo** del termine negativo! Per cancellare i $-1.5\text{ mV/K}$, il blocco PTAT dovrà essere opportunamente amplificato.

---

### Slide 26 – Riferimento a Bandgap (II): Dimostrazione Analitica

La slide analizza il caso teorico semplificato ponendo i pesi $c_1 = c_2 = 1$ (assorbendo l'eventuale moltiplicatore dentro l'argomento del logaritmo $n$):
$$V_{REF} = V_{BE} + V_T \ln(n)$$

Imponiamo la condizione di derivata nulla rispetto a $T$:
$$\frac{\partial V_{REF}}{\partial T} = \frac{\partial V_{BE}}{\partial T} + \frac{\partial V_T}{\partial T} \ln(n) = 0$$

Poiché $\frac{\partial V_T}{\partial T} = \frac{k}{q} = \frac{V_T}{T}$, possiamo riscrivere:
$$\frac{\partial V_{BE}}{\partial T} + \frac{V_T}{T} \ln(n) = 0 \implies \frac{\partial V_{BE}}{\partial T} = - \frac{V_T}{T} \ln(n)$$

Ora sostituiamo al posto di $\frac{\partial V_{BE}}{\partial T}$ l'espressione dimostrata alla **Slide 20**:
$$\frac{V_{BE} - (4+m)V_T - E_g/q}{T} = - \frac{V_T}{T}\ln(n)$$

Moltiplichiamo entrambi i membri per $T$:
$$V_{BE} - (4+m)V_T - \frac{E_g}{q} = - V_T \ln(n)$$

Isoliamo $V_{BE}$ (formula nel riquadro di Slide 26):
$$\mathbf{V_{BE} = \frac{E_g}{q} + \big(4+m - \ln(n)\big) V_T}$$

#### Cosa succede se risostituiamo questa $V_{BE}$ in $V_{REF}$?
$$V_{REF} = V_{BE} + V_T \ln(n) = \left[ \frac{E_g}{q} + \big(4+m - \ln(n)\big)V_T \right] + V_T \ln(n)$$
I termini con $\ln(n)$ si cancellano esattamente:
$$V_{REF} = \frac{E_g}{q} + (4+m)V_T$$

Se consideriamo la temperatura allo zero assoluto ($T \to 0\text{ K}$, dove $V_T \to 0$):
$$V_{REF}(0\text{ K}) = \frac{\mathbf{E_g}}{\mathbf{q}} \approx \mathbf{1.205\text{ V}}$$
**Ecco svelato il mistero del nome "Bandgap"**: la tensione a derivata nulla converge esattamente al valore del salto di banda proibita del silicio!

---

### Slide 27 – Esempio Numerico: Come scegliamo $n$?

Se impostiamo $c_1 = 1$, quant'è il fattore moltiplicativo necessario sul termine PTAT per annullare la deriva termica a temperatura ambiente ($T = 300\text{ K}$)?

Dobbiamo uguagliare le pendenze in valore assoluto:
$$0.087 \cdot c_2 \ln(n) = 1.5\text{ mV/K}$$
$$c_2 \ln(n) = \frac{1.5}{0.087} \approx \mathbf{17.2}$$

Sostituiamo questo fattore nella formula di $V_{ref}$:
$$V_{ref} = V_{BE} + 17.2 \cdot V_T$$

Mettiamo i numeri a $300\text{ K}$ ($V_{BE} \approx 0.75\text{ V}$, $V_T \approx 0.026\text{ V}$):
$$17.2 \cdot V_T = 17.2 \times 0.0259\text{ V} \approx 0.445\text{ V} \div 0.45\text{ V}$$
$$V_{ref} \approx 0.75\text{ V} + 0.45\text{ V} \approx \mathbf{1.20 \div 1.25\text{ V}}$$

Indipendentemente dalla tecnologia CMOS usata, **qualsiasi riferimento a bandgap ben progettato fornirà sempre una tensione di circa $1.25\text{ V}$**.

---

### Slide 28 – Facciamo la Somma... (Implementazione Circuitale)

Come si realizza circuitalmente la somma $V_{BE} + \text{termine PTAT}$?  
Slide 28 mostra la topologia classica a due rami:

```
          Vdd                     Vdd
           |                       |
        [Ic (gen)]              [Ic (gen)]
           |                       |
           +-----> Vo1             +-----> Vo2
           |                       |
          _|_                     [ R ]
          / \ Q1                   |
         /___\ (Area A)           _|_
           |                      / \ Q2
          GND                    /___\ (Area n*A)
                                   |
                                  GND
```

* **Ramo 1 (sinistra):**
  Un generatore di corrente $I_C$ alimenta il transistor $Q_1$ (con area di emettitore unitaria $A$).  
  Il potenziale al nodo $V_{o1}$ è semplicemente:
  $$V_{o1} = V_{BE1}$$

* **Ramo 2 (destra):**
  Un generatore con la stessa corrente $I_C$ alimenta il transistor $Q_2$, che ha un'area $n$ volte maggiore ($n A$), **con una resistenza $R$ posta in serie al suo emettitore**.  
  Il potenziale al nodo $V_{o2}$ è:
  $$V_{o2} = V_{BE2} + R \cdot I_C$$

#### Il ruolo dell'uguaglianza $V_{o1} = V_{o2}$:
Se un anello di retroazione (come un amplificatore operazionale) impone che i due nodi siano allo stesso potenziale ($V_{o1} = V_{o2}$):
$$V_{BE1} = V_{BE2} + R \cdot I_C \implies R \cdot I_C = V_{BE1} - V_{BE2} = \Delta V_{BE}$$

Poiché le correnti di collettore sono uguali ($I_C$), la differenza $\Delta V_{BE}$ dipende unicamente dal rapporto di area $n$:
$$\Delta V_{BE} = V_T \ln(n)$$
Da cui si ricava la corrente che scorre nel circuito:
$$R \cdot I_C = V_T \ln(n) \implies \mathbf{I_C = \frac{V_T \ln(n)}{R}}$$
*(Nota: questa è proprio una corrente PTAT, proporzionale a $T$!)*

Sostituendo $R \cdot I_C$ nell'espressione di $V_{o2}$:
$$\mathbf{V_{o2} = V_{BE2} + V_T \ln(n)}$$
Abbiamo ottenuto esattamente la somma cercata: una $V_{BE}$ (CTAT) più un termine proporzionale a $V_T$ (PTAT)!

---

### Il "Colpo di Scena" verso Slide 29–30 (Perché non finisce qui?)
Guarda cosa richiede l'esempio di Slide 27:
Se volessimo ottenere il fattore $17.2$ direttamente con il solo termine $\ln(n)$ (cioè senza $c_2$), dovremmo avere:
$$\ln(n) = 17.2 \implies n = e^{17.2} \approx 29.500.000$$
Dovremmo costruire $Q_2$ grande **30 milioni di volte** rispetto a $Q_1$! È palesemente irrealizzabile su silicio.

Ed è proprio qui che entra in gioco l'architettura completa di **Slide 30** (la cella Brokaw con amplificatore operazionale), dove si userà un partitore di resistenze $\left(1 + \frac{R_2}{R_3}\right)$ per moltiplicare il piccolo termine $\Delta V_{BE}$ e raggiungere il valore $17.2$ con un rapporto di aree $n$ piccolo e realistico (es. $n = 8$).

Ran command: `python3 -c "
import pypdfium2 as pdfium
import os

pdf = pdfium.PdfDocument('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
out_dir = '/Users/matteoluca/.gemini/antigravity-ide/brain/d7c9ed11-0bf8-488e-8a69-eff19a0ba908/scratch/slides'
os.makedirs(out_dir, exist_ok=True)

for i in range(28, 35): # slides 29 to 35 (0-indexed 28 to 34)
    page = pdf[i]
    image = page.render(scale=2).to_pil()
    image.save(f'{out_dir}/slide_{i+1}.png')
    print(f'Saved slide_{i+1}.png')
"`
Viewed slide_29.png:1-800
Viewed slide_30.png:1-800
Viewed slide_31.png:1-800
Viewed slide_32.png:1-800
Viewed slide_33.png:1-800
Viewed slide_34.png:1-800
Viewed slide_35.png:1-800

Capisco benissimo il tuo dubbio! A prima vista, guardando solo la Slide 28, sembra che quei due nodi $V_{o1}$ e $V_{o2}$ siano "appesi nel vuoto". 

Ecco esattamente **cosa c'è sotto**, come funziona la **retroazione con l'amplificatore operazionale** e l'analisi dettagliata di tutte le slide **da 29 a 34**.

---

### La risposta al tuo dubbio: Cosa c'entra l'Op-Amp?

Guarda lo schema concettuale di ciò che accade:

```
                  +----------------- Vo (Uscita del Bandgap = Vref)
                  |        |
                 [R1]     [R2]
                  |        |
         Vo1 ----(*)      (*)---- Vo2
                  |        |
                  |       [R3]
                  |        |
                 Q1       Q2 (Area n*A)
                 _|_      _|_
                 ///      ///
                  |        |
                  +---(+)  +---(-)
                        \  /
                        [OP-AMP]
                           |
                           +--------> Comanda la linea superiore Vo!
```

1. **Chi comanda la linea in alto?** L'uscita stessa dell'operazionale ($V_o$)! Non è un generatore esterno: è l'operazionale che alimenta dall'alto i due rami attraverso le resistenze $R_1$ e $R_2$. Quindi **$V_o$ è la tensione di riferimento $V_{REF}$ che vogliamo ottenere**.
2. **Cosa colleghiamo agli ingressi dell'Op-Amp?**
   * L'ingresso non-invertente $(+)$ si collega al nodo $V_{o1}$ (sopra $Q_1$).
   * L'ingresso invertente $(-)$ si collega al nodo $V_{o2}$ (tra $R_2$ e $R_3$).
3. **Come funziona la retroazione?**
   L'op-amp ha un guadagno ad anello aperto altissimo ($A_v \to \infty$).
   * Se per qualche motivo $V_{o1} > V_{o2}$, la tensione differenziale d'ingresso $(V^+ - V^-)$ è positiva.
   * L'op-amp alza la sua tensione di uscita $V_o$.
   * Alzando $V_o$, inietta più corrente in entrambi i rami.
   * La maggiore corrente che scorre nel ramo destro attraversa $R_3$, creando una caduta di potenziale maggiore che **fa salire $V_{o2}$ finché non eguaglia esattamente $V_{o1}$**.
   * A regime, grazie al **cortocircuito virtuale**, l'op-amp impone rigorosamente:
     $$V^+ = V^- \iff \mathbf{V_{o1} = V_{o2}}$$

---

### Slide 29 – Aspetti Pratici (I): Le due condizioni difficili

La slide evidenzia due problemi pratici nati dalla teoria precedente:
1. **$V_{o1} = V_{o2}$ ("Bisogna索引garantirlo!"):**  
   Come abbiamo appena visto, non possiamo "sperare" che siano uguali. Serve un circuito attivo di retroazione (l'operazionale) che forzi attivamente l'uguaglianza.
2. **$R I_C = V_T \ln(n)$ ("Difficile per $\ln(n) = 17.2$!"):**  
   Se volessimo ottenere il fattore $17.2$ solo tramite il logaritmo del rapporto di area $n$ (come ipotizzato a Slide 27), servirebbe:
   $$n = e^{17.2} \approx 29.500.000$$
   Dovremmo costruire un transistor $Q_2$ con un'area **30 milioni di volte più grande** di $Q_1$! Sul silicio è pura fantascienza.

---

### Slide 30 – Aspetti Pratici (II): Il Circuito Completo a Bandgap

La Slide 30 presenta la soluzione classica (architettura di tipo *Brokaw/Kuijk* con amplificatore operazionale).

#### Analisi circuitale del funzionamento:
* Scegliamo le due resistenze di carico superiori identiche: **$R_1 = R_2$**.
* Poiché l'op-amp impone $V^+ = V^-$, la caduta di potenziale ai capi di $R_1$ è identica a quella su $R_2$:
  $$V_o - V^+ = V_o - V^- \implies I_1 = I_2 = I$$
  L'operazionale costringe i due rami a condurre la **stessa identica corrente $I$**!
* Guardiamo il ramo sinistro:
  $$V^+ = V_{BE1}$$
* Guardiamo il ramo destro:
  $$V^- = V_{BE2} + R_3 \cdot I$$
* Poiché $V^+ = V^-$:
  $$V_{BE1} = V_{BE2} + R_3 \cdot I \implies \mathbf{R_3 \cdot I = V_{BE1} - V_{BE2} = \Delta V_{BE}}$$
  Quindi la corrente nei rami è data da:
  $$I = \frac{\Delta V_{BE}}{R_3} = \frac{V_T \ln(n)}{R_3}$$
* Ora calcoliamo la tensione di uscita $V_o$ (partendo da massa e risalendo il ramo destro):
  $$V_o = V_{BE2} + R_3 \cdot I + R_2 \cdot I = V_{BE2} + (R_2 + R_3) \cdot I$$
  Sostituendo $I = \frac{V_T \ln(n)}{R_3}$:
  $$V_o = V_{BE2} + \frac{V_T \ln(n)}{R_3} (R_2 + R_3)$$
  Raccogliendo $R_3$:
  $$\mathbf{V_o = V_{BE2} + \left(1 + \frac{R_2}{R_3}\right) V_T \ln(n)}$$

#### Perché questo risolve il problema di $\ln(n) = 17.2$?
Guardiamo la formula finale nel riquadro in basso a destra:
$$\mathbf{\left(1 + \frac{R_2}{R_3}\right) \ln(n) \approx 17.2}$$
Ora abbiamo **due gradi di libertà**:
* Non serve un'area $n$ mostruosa! Possiamo scegliere un normalissimo **$n = 8$** (facile da realizzare con una matrice $3 \times 3$ dove il transistor centrale è $Q_1$ e gli 8 intorno in parallelo formano $Q_2$).
  Poiché $\ln(8) \approx 2.08$:
  $$1 + \frac{R_2}{R_3} = \frac{17.2}{2.08} \approx 8.27 \implies \frac{R_2}{R_3} \approx 7.27$$
* Realizzare un rapporto tra resistenze di circa $7.3$ in tecnologia integrata è facilissimo, compatto ed estremamente preciso (il rapporto tra resistenze su silicio ha tolleranze inferiori allo $0.1\%$).

---

### Slide 31 – Il Circuito a Bandgap (1): La Trascrizione dei Passaggi

Questa slide riporta gli appunti manoscritti della professoressa, che confermano punto per punto la dimostrazione appena vista:
1. *"AO si trova in alto guadagno dato che $V^+ = V^-$"* $\rightarrow$ cortocircuito virtuale.
2. *"Inoltre $R_1 = R_2$, quindi su $R_3$ cade $\Delta V_{BE}$"* $\rightarrow$ poiché le correnti nei due rami sono uguali, la differenza di tensione tra le basi-emettitori deve cadere interamente su $R_3$.
3. Legge di Kirchhoff alle maglie (KVL):
   * Ramo destro: $V_{REF} - R_2 I - \Delta V_{BE} - V_{BE2} = 0 \implies V_{OUT} = V_{BE2} + (R_2 + R_3) I$
   * Corrente: $I = \frac{\Delta V_{BE}}{R_3} = \frac{V_T \ln(n)}{R_3}$
   * Uscita: $V_{REF} = V_{BE2} + (R_2 + R_3) \frac{V_T \ln(n)}{R_3}$
4. Nota a piè di pagina: *"Se $R_1 = \frac{R_2}{m}$ allora $\ln(m \cdot n)$"*:  
   Se invece di fare $R_1 = R_2$ scegliamo le resistenze sbilanciate di un fattore $m$, allora anche le correnti nei rami avranno rapporto $m$, e l'argomento del logaritmo diventerà $(m \cdot n)$ come visto a Slide 24.

---

### Slide 32 – Aspetti Pratici (III): Il Problema dell'Offset ($V_{os}$)

Nel mondo reale l'operazionale non è ideale. A causa delle asimmetrie di fabbricazione della coppia differenziale d'ingresso (mismatch di $V_{th}$ e dimensioni), compare una **tensione di offset d'ingresso $V_{os}$**.

Nello schema di Slide 32, l'offset è modellato come un generatore di tensione $V_{os}$ in serie al morsetto non-invertente $(+)$:
$$V^+ = V^- + V_{os}$$

Ricalcoliamo cosa succede alla caduta su $R_3$:
* $V^+ = V_{BE1}$
* $V^- = V_{BE2} + R_3 I$
* Sostituendo la relazione con l'offset:
  $$V_{BE1} = (V_{BE2} + R_3 I) + V_{os} \implies \mathbf{R_3 I = (V_{BE1} - V_{BE2}) - V_{os} = V_T \ln(n) - V_{os}}$$
* La corrente che scorre nel circuito diventa "inquinata" dall'offset:
  $$I = \frac{V_T \ln(n) - V_{os}}{R_3}$$
* Ricalcoliamo la tensione di uscita $V_o$:
  $$\mathbf{V_o = V_{BE2} + \big(V_T \ln(n) - V_{os}\big) \left(1 + \frac{R_2}{R_3}\right)}$$

#### Perché l'offset è disastroso qui?
Il termine moltiplicativo $\left(1 + \frac{R_2}{R_3}\right)$ vale circa **$8 \div 10$**.
* Se l'operazionale ha un modesto offset di soli $5\text{ mV}$, all'uscita questo viene moltiplicato:
  $$\Delta V_o \approx -5\text{ mV} \times 8.3 \approx \mathbf{-41.5\text{ mV}}$$
  Un errore enorme su una tensione di $1.25\text{ V}$!
* Peggio ancora: **l'offset $V_{os}$ varia con la temperatura** (drift termico dell'offset $\frac{\partial V_{os}}{\partial T}$), distruggendo la cancellazione termica del Bandgap.

---

### Slide 33 – Strategie per minimizzare il problema dell'offset

La slide elenca 3 soluzioni ingegneristiche:
1. **Buon disegno dell'operazionale:**  
   Usare transistor d'ingresso con canali molto lunghi e larghi ($W, L$ grandi) e layout simmetrici a baricentro comune (common-centroid) per ridurre il mismatch intrinseco.
2. **Dare più peso a $\Delta V_{BE}$ ($I_{C1} = m I_{C2} \implies \Delta V_{BE} = V_T \ln(nm)$):**  
   Aumentando il valore nominale di $\Delta V_{BE}$, l'errore percentuale dovuto a $V_{os}$ (che vale $\frac{V_{os}}{\Delta V_{BE}}$) diventa proporzionalmente più piccolo.
3. **Usare due BJT per raddoppiare $\Delta V_{BE}$:**  
   Mettere due BJT in serie su ciascun ramo.

---

### Slide 34 – Soluzione possibile (?): I BJT Impilati (Stacked)

La slide mostra l'implementazione pratica del 3° punto di Slide 33:
* Sul ramo sinistro mettiamo **due BJT in serie**: $Q_1$ e $Q_2$ (ciascuno con area unitaria $A$).  
  La tensione totale sul ramo sinistro diventa: $2 V_{BE}$.
* Sul ramo destro mettiamo **due BJT in serie**: $Q_3$ e $Q_4$ (ciascuno con area $n A$) in serie a $R_3$.  
  La differenza di potenziale prodotta dai BJT raddoppia a **$2 \Delta V_{BE}$**!

La caduta su $R_3$ diventa:
$$R_3 I = 2 \Delta V_{BE} - V_{os} = 2 V_T \ln(nm) - V_{os}$$
E la tensione di uscita risulta:
$$\mathbf{V_o = 2 V_{BE} + \big(2 V_T \ln(nm) - V_{os}\big) \left(1 + \frac{R_2}{R_3}\right)}$$

* **Perché l'uscita è meno sensibile a $V_{os}$?**  
  Il segnale utile PTAT è raddoppiato ($2 V_T \ln(nm)$), quindi il peso relativo dell'offset $V_{os}$ è **dimezzato**.
* **Perché il titolo ha un punto di domanda "(?)"?**  
  Perché questa soluzione ha due grossi svantaggi pratici:
  1. **Tensione di alimentazione richiesta più alta:** Con due BJT in serie, l'uscita sale a $V_o \approx 2 \times 1.25\text{ V} \approx \mathbf{2.5\text{ V}}$. Nelle moderne tecnologie CMOS che funzionano a $1.2\text{ V}$ o $1.8\text{ V}$, questo circuito semplicemente non può essere alimentato!
  2. **Problema tecnologico del collettore:** Nelle tecnologie CMOS standard con substrato p comune, tutti i BJT verticali parassiti hanno il collettore fisicamente vincolato al substrato (GND). Non è possibile metterli in serie uno sopra l'altro senza processi speciali più costosi (come deep n-well isolata o BiCMOS).


Ran command: `python3 -c "
from pypdf import PdfReader
reader = PdfReader('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
print(f'Total pages: {len(reader.pages)}')
for p in range(34, len(reader.pages)):
    print(f'=== SLIDE {p+1} ===')
    text = reader.pages[p].extract_text()
    print('\n'.join([l for l in text.splitlines() if l.strip()][:5]))
"`
Ran command: `python3 -c "
import pypdfium2 as pdfium
import os

pdf = pdfium.PdfDocument('/Users/matteoluca/Downloads/microele/LEZ7-b (1).pdf')
out_dir = '/Users/matteoluca/.gemini/antigravity-ide/brain/d7c9ed11-0bf8-488e-8a69-eff19a0ba908/scratch/slides'

for i in range(34, 44): # slides 35 to 44 (0-indexed 34 to 43)
    page = pdf[i]
    image = page.render(scale=2).to_pil()
    image.save(f'{out_dir}/slide_{i+1}.png')
    print(f'Saved slide_{i+1}.png')
"`
Viewed slide_35.png:1-800
Viewed slide_36.png:1-800
Viewed slide_37.png:1-800
Viewed slide_38.png:1-800
Viewed slide_39.png:1-800
Viewed slide_40.png:1-800
Viewed slide_41.png:1-800
Viewed slide_42.png:1-800
Viewed slide_43.png:1-800
Viewed slide_44.png:1-800

Ecco la spiegazione dettagliata, chiara e completa delle **slide da 35 a 44** (fino all'ultima pagina della lezione). 

Qui la professoressa affronta le **sfide tecnologiche reali nel silicio**, presenta i **circuiti commerciali**, mostra come eliminare l'operazionale e infine spiega i **limiti moderni del Bandgap**.

---

### Mappa Concettuale (Slide 35–44)

1. **Slide 35, 36, 37:** Come si fanno i BJT in un processo CMOS? Il vincolo del **collettore a massa** e il trucco per raddoppiare $\Delta V_{BE}$.
2. **Slide 38:** I 3 problemi pratici (collettore, self-heating e circuito di **start-up**).
3. **Slide 39 & 40:** Il **Bandgap Commerciale** con amplificatore differenziale e pesi a resistenze.
4. **Slide 41, 42, 43:** Il **Bandgap SENZA operazionale** (a specchi di corrente).
5. **Slide 44:** I limiti del bandgap classico nelle tecnologie moderne (perché $1.2\text{ V}$ oggi è un problema!).

---

### Slide 35 – BJT e processo CMOS (Il vincolo tecnologico del substrato)

In un normale processo CMOS (a substrato di tipo p), non esistono maschere dedicate per costruire transistor bipolari (a meno di pagare processi BiCMOS molto più costosi).  
Tuttavia, si forma **gratuitamente un BJT parassita verticale di tipo PNP**:

```
        C (p+)           E (p+)      B (n+)
          |                |           |
     +---------+      +---------+ +---------+
     |  p-sub  |      |        N-Well       |
     +---------+      +---------------------+
     ========================================
             SUBSTRATO p (p-sub)
     ========================================
```

* **Emettitore (E):** Diffusione $p^+$ all'interno dell'N-Well.
* **Base (B):** Pozzetto $N$-Well (con contatto $n^+$).
* **Collettore (C):** L'intero substrato di silicio del chip ($p\text{-sub}$).

> ⚠️ **LA REGOLA FONDAMENTALE DEL SILICIO:**  
> Il substrato comune di silicio è il "fondo" di tutto il chip e deve essere tassativamente collegato alla tensione più bassa in assoluto, cioè **a massa (GND)**, per evitare di polarizzare in diretta le giunzioni parassite e causare il latch-up.  
> **Conseguenza:** Il collettore di questo BJT pnp verticale è **inevitabilmente cortocircuitato a massa! Non puoi collegarlo a nessun altro nodo.**

---

### Slide 36 & 37 – Come aumento $\Delta V_{BE}$ con i collettori a massa?

A Slide 34 avevamo ipotizzato di impilare due BJT uno sopra l'altro ($Q_2$ sul collettore di $Q_1$) per ottenere $2 V_{BE}$. Ma ora capisci perché c'era il punto di domanda "(?)": **il transistor superiore avrebbe avuto il collettore staccato da massa, cosa impossibile in CMOS!**

La Slide 36 mostra la soluzione geniale per aggirare il problema:
1. Prendiamo $Q_1$ con base e collettore a massa. Il suo emettitore sale al potenziale $V_{EB1}$.
2. **Colleghiamo la base di $Q_2$ all'emettitore di $Q_1$!**
3. Anche il collettore di $Q_2$ viene collegato **direttamente a massa**!
4. La tensione sull'emettitore di $Q_2$ diventa:
   $$V_{E2} = V_{B2} + V_{EB2} = V_{EB1} + V_{EB2} = \mathbf{2 V_{BE}}$$
   Abbiamo ottenuto $2 V_{BE}$ avendo **tutti i collettori ancorati a massa**!

A **Slide 37** questo blocco a due transistor viene inserito su entrambi i rami del Bandgap:
* Ramo 1: coppia $Q_1, Q_2$ di area unitaria $A$.
* Ramo 2: coppia $Q_3, Q_4$ di area $n A$, con la resistenza $R_1$ in serie.
* In alto: due specchi di corrente PMOS pilotati dall'operazionale.
* La domanda in arancione: *"Cosa non abbiamo ancora considerato?"* porta dritto alla Slide 38.

---

### Slide 38 – Il Circuito a Bandgap (2): Start-Up e Self-Heating

La slide fissa tre considerazioni critiche per l'esame:
1. **PNP con collettore a massa:** come appena dimostrato.
2. **Auto-riscaldamento (Self-Heating):** L'operazionale deve consumare pochissima corrente. Se l'operazionale scalda localmente il silicio circostante, crea gradienti di temperatura interni che sballano la compensazione termica del Bandgap.
3. **Problema dello Start-Up:**  
   Anche questo circuito, essendo un anello chiuso ad autopolarizzazione, ha **due punti di equilibrio**: quello desiderato ($V_o \approx 1.25\text{ V}$) e quello a riposo nullo ($I = 0, V_o = 0\text{ V}$).  
   *Se all'accensione $I = 0$, i morsetti dell'op-amp sono a $0\text{ V}$ e il circuito non si accende mai.*
   * **La modifica circuitale (schema a destra):**  
     L'uscita dell'op-amp pilota il gate di un **transistor PMOS di passaggio** collegato tra $V_{DD}$ e il nodo $V_{REF}$. Si inserisce un ramo ausiliario di start-up che all'accensione forza la conduzione e, una volta a regime, si disattiva da solo.

---

### Slide 39 & 40 – Un Bandgap Commerciale ad Alte Prestazioni

Nelle Slide 39 e 40 viene analizzato uno schema industriale reale, dove l'uscita viene prelevata tramite uno **stadio amplificatore differenziale** con resistenze di retroazione.

Guardiamo la formula finale ricavata dagli appunti manoscritti di Slide 40:
$$\mathbf{V_o = \left(\frac{R_4}{R_6}\right) V_{BE} + 2 \left(\frac{R_5}{R_1}\right) V_T \ln(n)}$$

#### Da dove salta fuori questa formula? (Passaggi di Slide 40):
1. Ai nodi interni $V_X$ e $V_Y$ il circuito impone l'uguaglianza dei potenziali:
   $$V_X = V_Y \implies I_D R_1 + 2 V_{BE1} = 2 V_{BE2} \implies I_D = \frac{2 \Delta V_{BE}}{R_1} = \frac{2 V_T \ln(n)}{R_1}$$
   Questa corrente $I_D$ è una **corrente PTAT pura**.
2. La corrente $I_D$ viene specchiata dallo specchio PMOS superiore ($M_2 - M_{10}$) sul ramo di sinistra dell'amplificatore, attraversando la resistenza $R_5$:
   $$V_o^- = -2 \frac{R_5}{R_1} V_T \ln(n)$$
3. Sul ramo destro, il transistor $M_9$ riceve una tensione legata a $V_{BE}$, iniettando una corrente proporzionale a $V_{BE}/R_6$ che attraversa $R_4$:
   $$V_o^+ = \frac{R_4}{R_6} V_{BE}$$
4. L'uscita differenziale $V_o = V_o^+ - V_o^-$ somma i due termini.

#### Perché questo schema è così importante?
Nei bandgap elementari, la tensione finale era vincolata rigidamente a $1.25\text{ V}$.  
In questa topologia commerciale, **i pesi del termine CTAT e del termine PTAT sono determinati da due rapporti di resistenze indipendenti**:
$$\text{Peso CTAT} = \frac{R_4}{R_6}, \qquad \text{Peso PTAT} = 2 \frac{R_5}{R_1}$$
Modificando opportunamente questi rapporti di resistenze, il progettista può ottenere **qualunque valore di tensione di riferimento desideri**, non necessariamente $1.25\text{ V}$!

---

### Slide 41, 42, 43 – Bandgap SENZA Amplificatore Operazionale

Gli amplificatori operazionali occupano area, consumano corrente e introducono offset. È possibile costruire un riferimento a bandgap **senza usare alcun operazionale**?  
**Sì!** Sfruttando gli specchi di corrente autopolari visti a inizio lezione.

#### Come funziona il circuito (Slide 41 e 42):
* In alto abbiamo uno specchio PMOS a 3 rami ($M_3, M_4, M_5$) che forzano correnti uguali: $I_{D1} = I_{D2} = I_{D3} = I$.
* Sotto ci sono due transistor NMOS ($M_1, M_2$ evidenziati nel riquadro tratteggiato rosso a Slide 42) con i gate collegati insieme.
* Poiché $M_1$ e $M_2$ hanno la stessa corrente e stessa $V_{GS}$, impongono che i loro source siano allo stesso potenziale:
  $$\mathbf{V_{s1} = V_{s2}}$$
* Ma il source di $M_1$ è collegato all'emettitore di $Q_1$, mentre il source di $M_2$ è collegato a $R_1$ in serie a $Q_2$:
  $$V_{BE1} = V_{BE2} + R_1 \cdot I \implies R_1 \cdot I = \Delta V_{BE} = V_T \ln(n)$$
  La corrente autogenerata nei rami è una corrente PTAT:
  $$\mathbf{I_{PTAT} = \frac{V_T \ln(n)}{R_1}}$$
* Questa corrente $I_{PTAT}$ viene specchiata dal transistor $M_5$ nel terzo ramo di uscita, che contiene una resistenza $R_2$ in serie al BJT $Q_3$.
* La tensione di uscita ai capi del terzo ramo vale:
  $$\mathbf{V_o = V_{BE3} + R_2 \cdot I_{PTAT} = V_{BE3} + \left(\frac{R_2}{R_1}\right) V_T \ln(n)}$$

È esattamente la formula del Bandgap! $V_{BE}$ (CTAT) più $V_T \ln(n)$ pesato dal rapporto $\frac{R_2}{R_1}$ (PTAT), **senza usare neanche un amplificatore operazionale!**

* **Il problema residuo (Slide 43):**  
  La modulazione di lunghezza di canale ($\lambda$) dei transistor MOS fa sì che se le tensioni $V_{DS}$ dei tre rami non sono identiche, le correnti specchiate non sono perfettamente uguali. Per risolvere questo limite si usano transistor **cascode** sia sui rami superiori sia su quelli inferiori.

---

### Slide 44 – Bandgap: Aspetti Problematici e Nuove Frontiere

L'ultima slide è una sintesi critica essenziale, spesso materia di domande teoriche o di orale:

| Limite del Bandgap Classico | Perché è un problema oggi? | Soluzione Moderna |
| :--- | :--- | :--- |
| **$V_{ref} \approx 1.2\text{ V}$ troppo alta** | Nelle moderne tecnologie CMOS nanometriche (es. $28\text{ nm}, 16\text{ nm}, 7\text{ nm}$), l'alimentazione $V_{DD}$ è scesa a **$0.9\text{ V} \div 1.0\text{ V}$**. Un circuito che deve erogare $1.2\text{ V}$ **non può funzionare** perché supera $V_{DD}$! | **Sub-1V Bandgap (es. topologia Banba):** Si sommano correnti invece di tensioni ($I_{ref} = I_{CTAT} + I_{PTAT}$) e si fa scorrere la somma su una resistenza verso massa per ottenere $V_{ref} \approx 0.5\text{ V}$. |
| **L'operazionale consuma e ha offset** | Occupa tanta area su silicio, dissipa potenza a riposo e l'offset $V_{os}$ rovina la precisione termica. | Bandgap a specchi cascode senza op-amp o con tecniche di autozero / chopper. |
| **I resistori consumano area e fanno rumore** | Le resistenze integrate ad alto valore occupano tantissimo silicio e iniettano rumore termico Johnson ($4kTR$). | **Resistorless Bandgap:** Bandgap realizzati solo con transistor MOS. |
| **I BJT parassiti hanno basso guadagno** | I BJT parassiti in CMOS hanno $\beta$ scarso ($2 \div 5$) e forte dispersione di processo. | **MOS in sottosoglia (Subthreshold):** Un transistor MOS polarizzato sotto soglia ($V_{GS} < V_{th}$) conduce una corrente puramente diffusiva con caratteristica esponenziale identica al BJT, ma consumando nanoampere e funzionando a tensioni bassissime. |

---

### Mappa mentale finale per l'esame
1. **CTAT:** $V_{BE}$, pendenza $-1.5\text{ mV/}^\circ\text{C}$ (dominata da $I_S(T) \propto T^{4+m}e^{-E_g/kT}$).
2. **PTAT:** $\Delta V_{BE} = V_T \ln(n)$, pendenza $+0.087 \ln(n)\text{ mV/}^\circ\text{C}$.
3. **Condizione di annullamento:** $c_2 \ln(n) \approx 17.2 \implies V_{REF} \approx 1.25\text{ V}$ (pari all'energy gap del silicio diviso $q$).
4. **Implementazione con Op-Amp:** L'op-amp forza $V_{o1} = V_{o2}$ e moltiplica $\Delta V_{BE}$ per $\left(1 + \frac{R_2}{R_3}\right)$, evitando aree giganti.
5. **Tecnologia CMOS:** BJT parassiti verticali PNP con collettore vincolato a massa $\rightarrow$ uso del trucco base-emettitore per raddoppiare $\Delta V_{BE}$.
6. **Alternativa senza Op-Amp:** Specchi di corrente autopolari che generano $I_{PTAT} = \frac{\Delta V_{BE}}{R_1}$ e la specchiano su un terzo ramo con $R_2$ e $V_{BE3}$.