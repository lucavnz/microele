Il tuo dubbio è legittimo ed è uno dei concetti più affascinanti della fisica dei circuiti.

La risposta breve è: **quel 50% si perde per forza per la conservazione dell'energia, e non dipende dal valore della resistenza (che infatti si cancella nei conti)!**

Vediamo passo dopo passo perché succede matematicamente e fisicamente.

---

### 1. Il confronto diretto tra i due integrali (Senza tirare in ballo resistenze)

Mettiamo a confronto l'integrale dell'**alimentatore** e l'integrale del **condensatore**:

#### A) Quanta energia ha speso l'alimentatore?
L'alimentatore sta a tensione **fissa** $V_{DD}$. Per spostare una carica totale $Q = C \cdot V_{DD}$ a potenziale costante $V_{DD}$, l'alimentatore compie un lavoro pari a:
$$E_{\text{alim}} = \int_0^\infty V_{DD} \cdot i(t) \, dt = V_{DD} \int_0^Q dq = V_{DD} \cdot Q = V_{DD} \cdot (C \cdot V_{DD}) = \mathbf{C V_{DD}^2}$$

#### B) Quanta energia ha assorbito il condensatore?
Mentre il condensatore si carica, la sua tensione $v_C(t)$ **non è fissa a $V_{DD}$**, ma parte da $0\text{ V}$ e sale pian piano fino a $V_{DD}$. 
Quindi le prime cariche entrano a $0\text{ V}$, le seconde a $0.5\text{ V}$, le ultime a $V_{DD}$.

L'energia immagazzinata nel campo elettrico del condensatore è l'integrale della potenza **sul condensatore**:
$$E_C = \int_0^\infty v_C(t) \cdot i(t) \, dt = \int_0^\infty v_C(t) \cdot \left( C \frac{dv_C}{dt} \right) dt = C \int_0^{V_{DD}} v_C \, dv_C$$

Risolvendo l'integrale:
$$E_C = C \left[ \frac{v_C^2}{2} \right]_0^{V_{DD}} = \mathbf{\frac{1}{2} C V_{DD}^2}$$

---

### 2. Dov'è finita la differenza? ($\Delta E = E_{\text{alim}} - E_C$)

Facendo la sottrazione:
$$E_{\text{persa}} = E_{\text{alim}} - E_C = C V_{DD}^2 - \frac{1}{2} C V_{DD}^2 = \mathbf{\frac{1}{2} C V_{DD}^2}$$

Per il principio di conservazione dell'energia (Primo Principio della Termodinamica), quell'energia mancante **deve essere stata dissipata nel percorso** che collega l'alimentatore al condensatore (cioè attraverso il canale conduttivo del transistor PMOS e i fili metallici).

---

### 3. La "Magia": Perché la Resistenza non compare nella formula finale?

Potresti chiederti: *"Ma se c'è una resistenza $R$ nel transistor, perché l'energia dissipata non dipende da $R$?"*

Facciamo il calcolo esplicito dell'energia dissipata su una generica resistenza $R$ per effetto Joule ($P = R \cdot i^2$):

1. In un circuito $RC$, la corrente di carica vale: 
   $$i(t) = \frac{V_{DD}}{R} e^{-\frac{t}{RC}}$$
2. L'energia dissipata in calore sulla resistenza è:
   $$E_R = \int_0^\infty R \cdot [i(t)]^2 \, dt = R \int_0^\infty \left( \frac{V_{DD}}{R} e^{-\frac{t}{RC}} \right)^2 dt = \frac{V_{DD}^2}{R} \int_0^\infty e^{-\frac{2t}{RC}} dt$$
3. Risolvendo l'integrale esponenziale:
   $$\int_0^\infty e^{-\frac{2t}{RC}} dt = \left[ -\frac{RC}{2} e^{-\frac{2t}{RC}} \right]_0^\infty = 0 - \left( -\frac{RC}{2} \right) = \frac{RC}{2}$$
4. Moltiplichiamo per il termine fuori dall'integrale:
   $$E_R = \frac{V_{DD}^2}{\cancel{R}} \cdot \frac{\cancel{R} C}{2} = \mathbf{\frac{1}{2} C V_{DD}^2}$$

> **Il risultato straordinario:**
> **La resistenza $R$ al denominatore si cancella esattamente con la $R$ al numeratore!**

* **Se $R$ è piccolissima (transistor grandissimo e conduttivo):** la corrente iniziale $I$ è enorme ($I^2$ gigantesco), ma il tempo di carica è brevissimo $\implies$ l'energia dissipata è comunque $\frac{1}{2} C V_{DD}^2$.
* **Se $R$ è grandissima (transistor piccolo e resistivo):** la corrente $I$ è minuscola ($I^2$ piccolo), ma il tempo di carica dura tantissimo $\implies$ l'energia dissipata è sempre $\frac{1}{2} C V_{DD}^2$.

---

### 4. L'Intuizione Fisica (L'analogia del serbatoio)

Immagina di dover riempire d'acqua un secchio alto $V_{DD}$ prendendo l'acqua da una cascata che si trova a quota fissa $V_{DD}$:
* L'acqua parte sempre con energia potenziale $m g V_{DD}$ (fornita dall'alimentatore).
* All'inizio il secchio è vuoto: l'acqua precipita dall'altezza $V_{DD}$ fino al fondo ($0\text{ metri}$) e sbatte sul fondo dissipando tutta la sua energia cinetica in schizzi e calore.
* Man mano che il secchio si riempie, il dislivello tra la cascata e la superficie dell'acqua diminuisce.
* In media, l'acqua è caduta da un dislivello medio pari a **metà altezza ($\frac{V_{DD}}{2}$)**.
* Quindi, **esattamente metà dell'energia potenziale è andata persa nell'urto/turbolenza**, mentre solo l'altra metà resta immagazzinata come energia potenziale del fluido nel secchio.