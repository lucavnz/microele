La **PVD** (*Physical Vapor Deposition*, Deposizione Fisica da Fase Vapore) è una tecnica di microfabbricazione in cui un materiale solido viene trasferito su un substrato mediante processi puramente fisici, **senza reazioni chimiche**.

---

### 1. Principio di Funzionamento: Lo Sputtering

Il metodo PVD più comune in microelettronica è lo **sputtering**:
1. Si inserisce il wafer in una camera ad alto vuoto contenente un gas inerte (tipicamente Argon, $\text{Ar}$).
2. Si applica un forte campo elettrico che ionizza il gas creando un plasma di ioni $\text{Ar}^+$.
3. Gli ioni positivi vengono accelerati contro un bersaglio solido (*target*) del metallo che si vuole depositare (es. Alluminio, Titanio, Rame).
4. L'impatto degli ioni scalza via meccanicamente gli atomi del bersaglio, che viaggiano in linea retta nella camera a vuoto e si depositano sulla superficie del wafer formando un film sottile uniforme.

---

### 2. Vantaggi e Limiti: L'Effetto Ombra nei Fori Profondi

* **Vantaggi:**
  * Ottimo controllo dello spessore su superfici piane e orizzontali.
  * Elevata purezza del film depositato.
  * Ideale per depositare i livelli orizzontali di metallizzazione ($\text{Metal 1}$, $\text{Metal 2}$, ecc.).
* **Limiti (La Traiettoria Balistica in Linea Retta):**
  * Gli atomi viaggiano in linea retta come vernice spruzzata da una bomboletta (*line-of-sight*).
  * Se la superficie presenta fori stretti e profondi ad alto rapporto d'aspetto (come i [Vias](./Vias.md)), gli atomi si accumulano sui bordi superiori creando un "effetto ombra": il fondo e le pareti verticali non vengono rivestiti a sufficienza, lasciando cavità vuote (*poor step coverage*).

Per riempire canali e fori verticali complessi si deve quindi ricorrere alla deposizione chimica:
👉 Vedi: [CVD](./CVD.md) e [Vias](./Vias.md)

---

*Pagine correlate:*
- [CVD](./CVD.md)
- [Vias](./Vias.md)
- [Elettromigrazione e tossicità dei metalli](./Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [Siliciuro](./Siliciuro.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
