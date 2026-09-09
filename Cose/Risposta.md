Ran command: `python3 -c '
import pypdf

reader = pypdf.PdfReader("/Users/matteoluca/Downloads/microele/combin.pdf")
print("Total pages:", len(reader.pages))
for p in range(71, len(reader.pages)):
    print("="*30 + f" PDF PAGE {p+1} " + "="*30)
    print(reader.pages[p].extract_text())
'
`
Ran command: `gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -r150 -dFirstPage=75 -dLastPage=78 -sOutputFile=/Users/matteoluca/.gemini/antigravity-ide/brain/a5712e0d-342a-4896-9e4a-3373ee63245c/scratch/dyn_cascade_%02d.png /Users/matteoluca/Downloads/microele/combin.pdf`
Viewed dyn_cascade_01.png:1-800
Viewed dyn_cascade_02.png:1-800
Viewed dyn_cascade_03.png:1-800
Viewed dyn_cascade_04.png:1-800

Le **slide da 75 a 78** (le ultime del capitolo) affrontano la domanda definitiva sulla logica dinamica:  
**Possiamo collegare più porte dinamiche in cascata una dopo l'altra per formare un circuito complesso?**

La risposta immediata è: **NO, non direttamente!**  
La slide 75 ti mostra il perché (il disastroso problema del *cascading*), mentre le slide 76, 77 e 78 presentano le **tre storiche soluzioni architetturali** inventate per risolvere il problema:
1. **Domino Logic (Slide 76)** — La soluzione regina, usatissima nell'industria;
2. **np-CMOS (Slide 77)** — L'alternanza n-tree / p-tree;
3. **NORA Logic (Slide 78)** — L'estensione *No-Race* per sistemi sequenziali e pipeline.

---

## Slide 75: Cascading Dynamic Gates (Il Problema della Cascata)

![Slide 75 - Cascading Dynamic Gates](/Users/matteoluca/.gemini/antigravity-ide/brain/a5712e0d-342a-4896-9e4a-3373ee63245c/scratch/dyn_cascade_01.png)

### Il Circuito:
Colleghiamo direttamente l'uscita della prima porta dinamica ($Out1$) all'ingresso della seconda porta dinamica ($Out2$).  
Entrambe le porte condividono lo **stesso segnale di clock $Clk$**.

---

### Cosa succede nel ciclo di funzionamento?

1. **Fase di Precarica ($Clk = 0$):**
   * Sia $Out1$ che $Out2$ vengono caricate al valore alto: **$Out1 = 1$ ($2.5\text{ V}$)** e **$Out2 = 1$ ($2.5\text{ V}$)**.

2. **Fase di Valutazione ($Clk = 1$):**
   * Supponiamo che l'ingresso $In$ valga $1$.
   * **Cosa DOVREBBE succedere teoricamente:**
     * La prima porta si deve scaricare: $Out1$ passa da $1 \to 0$.
     * Poiché $Out1$ alla fine vale $0$, l'nMOS della seconda porta deve rimanere spento $\implies$ **$Out2$ DOVREBBE RIMANERE A 1**.

3. **Cosa succede REALMENTE (Guarda il grafico dei tempi a destra!):**
   * All'inizio della valutazione ($t = 0$), $Out1$ **è ancora a $1$** (ci mette un tempo finito di scarica $t_{pHL}$ per scendere a zero).
   * L'nMOS della seconda porta vede sul suo gate $Out1 = 1$, che è ampiamente superiore a $V_{Tn}$!
   * **L'nMOS della seconda porta SI ACCENDE SUBITO e comincia a scaricare verso terra il condensatore $Out2$!**
   * Quando finalmente la prima porta finisce di scaricarsi e porta $Out1$ sotto $V_{Tn}$, l'nMOS della seconda porta si spegne... **MA È TROPPO TARDI!**
   * $Out2$ ha già perso una consistente quantità di carica, subendo una caduta $\mathbf{\Delta V}$ (freccia rossa). Se la prima porta è un po' lenta, **$Out2$ si scarica completamente a $0\text{ V}$**!

### La Regola Fondamentale in Rosso:
> **"Only $0 \to 1$ transitions allowed at inputs!"**  
> *(Agli ingressi di una rete dinamica ad nMOS sono ammesse SOLO transizioni $0 \to 1$!)*

* Se un ingresso parte da $0$, l'nMOS parte **spento**: non può fare danni. Se poi deve accendersi, commuta $0 \to 1$ al momento giusto.
* Se invece un ingresso parte da $1$ e deve fare una transizione $1 \to 0$ (come fa l'uscita di una porta dinamica), l'nMOS parte **acceso per sbaglio**, scarica l'uscita a valle e causa un errore irreversibile!

---

## Slide 76: Domino Logic (La Soluzione N°1)

![Slide 76 - Domino Logic](/Users/matteoluca/.gemini/antigravity-ide/brain/a5712e0d-342a-4896-9e4a-3373ee63245c/scratch/dyn_cascade_02.png)

Come trasformiamo una transizione vietata $1 \to 0$ in una transizione permessa $0 \to 1$?  
**Inserendo un normale INVERTER STATICO CMOS all'uscita di ogni stadio dinamico!**

Questa combinazione (**Porta Dinamica + Inverter CMOS**) prende il nome di **Domino Gate**.

---

### Come funziona la logica Domino:

1. **In Precarica ($Clk = 0$):**
   * Il nodo dinamico interno si precarica a **$1$**.
   * L'inverter inverte il segnale $\implies$ l'uscita effettiva della porta ($Out1$) va a **$0\text{ V}$**!
   * La seconda porta dinamica vede all'ingresso uno **$0$ pulito**: il suo nMOS è rigorosamente spento. Nessuna scarica accidentale!

2. **In Valutazione ($Clk = 1$):**
   * **Se la PDN non conduce:** il nodo interno resta a $1 \implies$ l'uscita $Out1$ resta a **$0$** ($0 \to 0$).
   * **Se la PDN conduce:** il nodo interno si scarica a $0 \implies$ l'inverter fa commutare l'uscita **$0 \to 1$**!
   * Questa transizione $0 \to 1$ è **perfettamente lecita** per la porta successiva: accende il transistor a valle solo ed esclusivamente quando il dato è pronto e valido!

### Perché si chiama "Domino"?
Immagina una fila di tessere del domino:
* Durante la precarica, tutte le tessere vengono messe in piedi ($Out = 0$ per tutti gli stadi).
* Durante la valutazione, se il primo stadio commuta ($0 \to 1$), fa cadere la seconda tessera ($0 \to 1$), che fa cadere la terza ($0 \to 1$), e così via a catena!  
  Si propaga una rapida onda di transizioni monotonically crescenti ($0 \to 1$).

### Proprietà e Limiti della Logica Domino (Domande d'esame!):
* **È una logica non-invertente:** La porta dinamica fa un'inversione (PDN), ma l'inverter ne fa un'altra $\implies$ NOT + NOT = buffer non-invertente! Una porta Domino può realizzare solo funzioni **AND, OR** (non può fare direttamente NAND o NOR). Per fare funzioni invertenti serve la logica a doppia rotaia (*Dual-Rail Domino*).
* **Robustezza:** L'inverter disaccoppia il nodo dinamico flottante dal mondo esterno e permette di aggiungere facilmente un **Keeper ($M_{kp}$)** (visibile sul secondo stadio).

---

## Slide 77: np-CMOS (Detta anche Zipper Logic)

![Slide 77 - np-CMOS](/Users/matteoluca/.gemini/antigravity-ide/brain/a5712e0d-342a-4896-9e4a-3373ee63245c/scratch/dyn_cascade_03.png)

Nella logica Domino siamo stati costretti a inserire un inverter tra ogni stadio. E se volessimo eliminare anche quell'inverter per risparmiare transistor e ritardo?  
La soluzione è la logica **np-CMOS**: **alternare uno stadio a soli nMOS con uno stadio a soli pMOS**.

---

### La Struttura Alternata:

1. **Stadio 1: Blocco $n$-tree (a sinistra)**
   * Ha una **PDN ad nMOS**.
   * Pilotato da $Clk$.
   * Si precarica in alto a **$1$** e durante la valutazione può solo fare: **$1 \to 1$** oppure **$1 \to 0$**.

2. **Stadio 2: Blocco $p$-tree (a destra)**
   * È il "duale specchiato": la logica è fatta da una **PUN a pMOS**!
   * Il transistor di precarica è un nMOS in basso (pilotato da $\overline{Clk}$): pre-scarica l'uscita $Out2$ a **$0\text{ V}$**!
   * Il transistor di valutazione è un pMOS in alto (pilotato da $\overline{Clk}$).

---

### Perché funziona senza errori?
Guarda le due regole in rosso in basso:
* **"Only $0 \to 1$ transitions allowed at inputs of PDN"** (Gli nMOS vogliono ingressi che salgono).
* **"Only $1 \to 0$ transitions allowed at inputs of PUN"** (I pMOS vogliono ingressi che scendono!).

Verifichiamo la cascata:
* In precarica lo stadio $n$ mette $Out1 = 1$.
* L'ingresso dello stadio $p$ riceve $1 \implies$ **i suoi pMOS sono rigorosamente SPENTI**!
* Quando inizia la valutazione, lo stadio $p$ non può scaricarsi né caricarsi per errore. Se e solo se lo stadio $n$ commuta ($1 \to 0$), i pMOS dello stadio $p$ si accendono e portano $Out2$ a $1$ ($0 \to 1$).
* E l'uscita dello stadio $p$ ($0 \to 1$) può pilotare direttamente un successivo stadio $n$!

**Svantaggio dell'np-CMOS:** Gli stadi $p$-tree usano pMOS nella rete logica, che sono intrinsecamente più lenti degli nMOS a causa della minore mobilità delle lacune.

---

## Slide 78: NORA Logic (NO-RAce CMOS)

![Slide 78 - NORA Logic](/Users/matteoluca/.gemini/antigravity-ide/brain/a5712e0d-342a-4896-9e4a-3373ee63245c/scratch/dyn_cascade_04.png)

La logica **NORA** (*NO-RAce CMOS*) è il coronamento e l'estensione dell'np-CMOS per la progettazione di sistemi complessi con registri e pipeline sincrone:

### Caratteristiche Principali:
1. **Flessibilità di interconnessione:**
   * Puoi collegare direttamente uno stadio $n$ a uno stadio $p$ (come in np-CMOS);
   * **OPPURE** puoi mettere un inverter statico all'uscita dello stadio $n$ per pilotare **altri stadi $n$** (come nella logica Domino)!
   * Nello schema della slide vedi entrambi:
     * $Out1$ va direttamente alla PUN dello stadio $p$;
     * Attraverso l'inverter va *"to other PDN's"*.
2. **"No-Race" (Immunità alle corse critiche di clock):**
   * NORA definisce regole matematiche precise per interporre latch $C^2\text{MOS}$ tra blocchi logici combinatori dinamici, garantendo che le transizioni di valutazione non entrino mai in "corsa critica" (*race condition*) con i fronti di precarica del clock, anche in presenza di clock skew tra $Clk$ e $\overline{Clk}$.

### L'Avvertenza Finale in Blu (WARNING):
> **"WARNING: Very sensitive to noise!"**  
> *(ATTENZIONE: Estremamente sensibile al rumore!)*

Perché NORA e np-CMOS sono quasi scomparse dai progetti moderni a favore della logica Domino?
* Avere sia nodi $n$ flottanti precaricati a $V_{DD}$ che nodi $p$ flottanti precaricati a massa raddoppia i problemi di accoppiamento capacitivo;
* La presenza di clock complementari ($Clk$ e $\overline{Clk}$) crea sfasamenti temporali (*clock skew*) ad altissima frequenza;
* I margini di rumore sono ridottissimi sia verso l'alto che verso il basso.

---

### Mappa Concettuale Finale delle 4 Slide (75–78)

```
                            PROBLEMA (Slide 75)
              La cascata diretta dinamica non funziona:
             transizioni 1 -> 0 causano false scariche!
                                  │
      ┌───────────────────────────┼───────────────────────────┐
      ▼                           ▼                           ▼
 DOMINO LOGIC (Slide 76)      np-CMOS (Slide 77)       NORA LOGIC (Slide 78)
 ───────────────────────      ──────────────────       ─────────────────────
 Inserisce un INVERTER        Alterna blocchi n-tree   Combina np-CMOS con
 CMOS statico tra gli stadi.  e blocchi p-tree.        inverter e registri C²MOS.
 Ingressi sempre 0 -> 1.      Evita gli inverter.      Elimina le corse critiche.
 Re della tecnologia reale!   Più lento (pMOS PUN).    Molto sensibile al rumore.
```