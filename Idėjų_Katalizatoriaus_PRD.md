# Produkto Reikalavimų Dokumentas (PRD) – „Idėjų Katalizatorius“

## 1. Tikslai, „non-goals“

### 1.1. Tikslai
*   **Efektyvus idėjų fiksavimas:** Suteikti vartotojams galimybę greitai ir lengvai užfiksuoti idėjas, citatas ir svarbią informaciją iš vizualinių šaltinių (pvz., ekrano nuotraukų) ir teksto.
*   **Automatinis informacijos apdorojimas:** Panaudoti dirbtinį intelektą (AI) automatiniam užfiksuotos informacijos apdorojimui, įskaitant optinį simbolių atpažinimą (OCR), temų priskyrimą, žymių generavimą ir PARA (Projects, Areas, Resources, Archives) metodikos taikymą.
*   **Idėjų pavertimas veiksmais:** Supaprastinti idėjų konvertavimą į apčiuopiamus veiksmus, leidžiant vartotojams tiesiogiai kurti užduotis, pridėti prie esamų projektų arba tiesiog išsaugoti informaciją ateičiai.
*   **Centralizuota idėjų ir užduočių saugykla:** Sukurti vieningą platformą, kurioje vartotojai galėtų tvarkyti savo idėjas, užduotis ir projektus, užtikrinant lengvą prieigą ir organizavimą.
*   **Išmani paieška:** Įdiegti galingą paieškos funkcionalumą, leidžiantį vartotojams greitai rasti bet kokią užfiksuotą informaciją, naudojant OCR turinį, žymes, projektus ir užduotis.

### 1.2. „Non-goals“
*   **Išplėstinis užduočių valdymas:** Programėlė nėra skirta pakeisti pilnavertes projektų ar užduočių valdymo sistemas, siūlančias tokias funkcijas kaip Gantt diagramos, komandos bendradarbiavimas, išsamus resursų planavimas.
*   **Dokumentų kūrimas/redagavimas:** Nėra skirta ilgų dokumentų kūrimui, redagavimui ar formatavimui. Pagrindinis dėmesys skiriamas trumpos, fragmentuotos informacijos fiksavimui ir apdorojimui.
*   **Socialinis bendrinimas:** Programėlė nėra socialinio tinklo ar bendrinimo platforma. Ji skirta asmeniniam idėjų ir informacijos valdymui.
*   **Išplėstinė failų saugykla:** Nors failai (ekrano nuotraukos, citatos) yra saugomi, programėlė nėra skirta kaip pagrindinė išplėstinė failų saugykla su versijavimu ar išplėstinėmis failų tvarkymo funkcijomis.

## 2. Pagr. vartotojų segmentai & JTBD (Jobs To Be Done)

### 2.1. Pagrindiniai vartotojų segmentai
*   **Žinių darbuotojai / Specialistai:** Asmenys, kurie nuolat apdoroja didelius kiekius informacijos (straipsniai, ataskaitos, prezentacijos) ir ieško būdų, kaip efektyviai fiksuoti įžvalgas bei paversti jas veiksmais.
*   **Studentai / Besimokantieji:** Asmenys, kurie renka informaciją iš paskaitų, knygų, interneto ir nori ją organizuoti studijoms, projektams ar asmeniniam tobulėjimui.
*   **Kūrybiniai profesionalai / Idėjų generatoriai:** Asmenys, kuriems reikia greitai užfiksuoti įkvėpimą, mintis, eskizus ir susieti juos su konkrečiais projektais ar idėjų bankais.
*   **Asmeninio tobulėjimo entuziastai:** Asmenys, kurie seka citatas, straipsnius, knygas, susijusias su asmeniniu augimu, lyderyste ir nori šią informaciją integruoti į savo kasdienę praktiką.

### 2.2. JTBD (Jobs To Be Done)
*   **Kai aš skaitau ar naršau internete ir randu vertingos informacijos (citata, grafikas, idėja), aš noriu ją greitai užfiksuoti (pvz., ekrano nuotrauka), kad neprarasčiau įžvalgos ir galėčiau prie jos grįžti vėliau.**
    *   *Funkcinis sprendimas:* Vartotojas pasidalina ekrano nuotrauka/citata.
*   **Kai aš užfiksavau informaciją, aš noriu, kad ji būtų automatiškai apdorota ir suskirstyta pagal temas bei žymes, kad man nereikėtų to daryti rankiniu būdu ir galėčiau lengviau ją rasti ateityje.**
    *   *Funkcinis sprendimas:* AI atlieka OCR, priskiria temas, generuoja žymes (#lyderystė, #citata, #asmeninisaugimas), priskiria PARA (Area: „Asmeninis Augimas“).
*   **Kai aš turiu užfiksuotą idėją ar informaciją, aš noriu ją paversti konkrečiu veiksmu (užduotimi, projekto dalimi) arba tiesiog išsaugoti, kad idėjos neliktų tik idėjomis, o būtų integruotos į mano darbo eigą.**
    *   *Funkcinis sprendimas:* Pasiūlo veiksmus: [+] sukurti užduotį, [->] pridėti prie projekto, [✓] tiesiog išsaugoti.
*   **Kai aš noriu rasti konkrečią idėją, užduotį ar informacijos fragmentą, aš noriu turėti išmanią paieškos sistemą, kuri leistų man ieškoti pagal turinį (įskaitant OCR), žymes, projektus ir užduotis, kad greitai rasčiau tai, ko man reikia.**
    *   *Funkcinis sprendimas:* Išmanioji paieška (apima OCR turinį, žymes, projektus, užduotis).
*   **Kai aš noriu matyti savo svarbiausias užduotis ir aktyvius projektus, aš noriu, kad pagrindiniame ekrane būtų aiškiai pateikta ši informacija, kad galėčiau lengvai sekti savo progresą ir prioritetus.**
    *   *Funkcinis sprendimas:* Pagrindinis ekranas: Šiandienos užduotys, Aktyvūs projektai, Idėjų „Pašto dėžutė“.

## 3. Sėkmės metrikos

Siekiant įvertinti „Idėjų Katalizatoriaus“ programėlės sėkmę, bus stebimos šios metrikos:

### 3.1. Activation (Aktyvacija)
*   **Pirmosios idėjos fiksavimas ir apdorojimas:** Vartotojų, kurie sėkmingai įkėlė ekrano nuotrauką/citatą ir gavo AI apdorotus metaduomenis (OCR, temos, žymės, PARA priskyrimas), procentas per pirmąsias 24 valandas po registracijos.
*   **Pirmasis idėjos konvertavimas į veiksmą:** Vartotojų, kurie per pirmąsias 48 valandas po registracijos sėkmingai sukūrė užduotį arba pridėjo idėją prie projekto, procentas.

### 3.2. Retention (Išlaikymas)
*   **Savaitės/Mėnesio aktyvūs vartotojai (WAU/MAU):** Vartotojų, kurie bent kartą per savaitę/mėnesį prisijungia prie programėlės ir atlieka bent vieną veiksmą (pvz., fiksuoja idėją, peržiūri užduotis, naudoja paiešką), skaičius ir procentas.
*   **Idėjų fiksavimo dažnumas:** Vidutinis idėjų, užfiksuotų vieno aktyvaus vartotojo per savaitę/mėnesį, skaičius.
*   **Užduočių/projektų kūrimo dažnumas:** Vidutinis užduočių/projektų, sukurtų iš idėjų vieno aktyvaus vartotojo per savaitę/mėnesį, skaičius.

### 3.3. Task Conversion (Užduočių konversija)
*   **Idėjų konversijos rodiklis:** Užfiksuotų idėjų, kurios buvo konvertuotos į užduotis arba pridėtos prie projektų, procentas.
*   **Veiksmų pasirinkimo pasiskirstymas:** Procentinis pasiskirstymas tarp pasirinktų veiksmų po idėjos fiksavimo ([+] sukurti užduotį, [->] pridėti prie projekto, [✓] tiesiog išsaugoti).
*   **Laikas iki veiksmo:** Vidutinis laikas nuo idėjos užfiksavimo iki jos konvertavimo į užduotį ar pridėjimo prie projekto.

### 3.4. Search Success (Paieškos sėkmė)
*   **Paieškos naudojimo dažnumas:** Vidutinis paieškos užklausų skaičius per aktyvų vartotoją per savaitę/mėnesį.
*   **Sėkmingų paieškų procentas:** Paieškų, po kurių vartotojas peržiūrėjo bent vieną paieškos rezultatą arba atliko veiksmą su juo, procentas.
*   **Paieškos rezultatų relevancija:** Vartotojų, kurie pasinaudojo paieška ir rado ieškomą informaciją (galima matuoti per tolesnius veiksmus su paieškos rezultatais arba tiesioginiu vartotojo atsiliepimu, jei bus įdiegta).
*   **Paieškos filtrų naudojimas:** Išmaniosios paieškos filtrų (pagal žymes, projektus, PARA sritis) naudojimo dažnumas.

## 4. Reikalavimai (funkciniai, nefunkciniai), apribojimai

### 4.1. Funkciniai reikalavimai (FR)
*   **FR.1 Idėjos fiksavimas:**
    *   FR.1.1 Vartotojas turi galėti pasidalinti ekrano nuotrauka su programėle.
    *   FR.1.2 Vartotojas turi galėti pasidalinti teksto citata su programėle.
*   **FR.2 AI apdorojimas:**
    *   FR.2.1 Programėlė turi atlikti optinį simbolių atpažinimą (OCR) iš įkeltų ekrano nuotraukų.
    *   FR.2.2 AI turi automatiškai priskirti temas užfiksuotai informacijai.
    *   FR.2.3 AI turi automatiškai generuoti žymes (pvz., #lyderystė, #citata, #asmeninisaugimas) užfiksuotai informacijai.
    *   FR.2.4 AI turi automatiškai priskirti užfiksuotą informaciją prie PARA sistemos (pvz., Area: „Asmeninis Augimas“).
*   **FR.3 Veiksmų pasiūlymai:**
    *   FR.3.1 Po informacijos apdorojimo programėlė turi pasiūlyti vartotojui tris veiksmus:
        *   [+] Sukurti užduotį.
        *   [->] Pridėti prie projekto.
        *   [✓] Tiesiog išsaugoti.
*   **FR.4 Užduočių/Projektų valdymas:**
    *   FR.4.1 Pasirinkus „Sukurti užduotį“, originalus failas (ekrano nuotrauka/citata) ir AI sugeneruoti metaduomenys turi būti automatiškai prisegti prie naujai sukurtos užduoties.
    *   FR.4.2 Vartotojas turi galėti peržiūrėti šiandienos užduotis pagrindiniame ekrane.
    *   FR.4.3 Vartotojas turi galėti peržiūrėti aktyvius projektus pagrindiniame ekrane.
    *   FR.4.4 Vartotojas turi turėti „Idėjų Pašto dėžutę“ pagrindiniame ekrane, kurioje būtų saugomos neišspręstos idėjos.
*   **FR.5 Išmanioji paieška:**
    *   FR.5.1 Programėlė turi turėti išmaniąją paieškos funkciją.
    *   FR.5.2 Paieška turi apimti OCR atpažintą turinį.
    *   FR.5.3 Paieška turi apimti sugeneruotas žymes.
    *   FR.5.4 Paieška turi apimti projektų pavadinimus ir turinį.
    *   FR.5.5 Paieška turi apimti užduočių pavadinimus ir turinį.

### 4.2. Nefunkciniai reikalavimai (NFR)
*   **NFR.1 Našumas:**
    *   NFR.1.1 AI apdorojimas (OCR, žymės, PARA) turi būti atliktas per maksimaliai 5 sekundes po failo įkėlimo.
    *   NFR.1.2 Paieškos rezultatai turi būti pateikti per maksimaliai 2 sekundes.
    *   NFR.1.3 Programėlės sąsaja turi veikti sklandžiai ir be vėlavimų.
*   **NFR.2 Patikimumas:**
    *   NFR.2.1 OCR atpažinimo tikslumas turi būti ne mažesnis nei 90% aiškiai matomam tekstui.
    *   NFR.2.2 AI temų priskyrimo ir žymių generavimo relevancija turi būti aukšta (pvz., >80% vartotojų vertina kaip tikslią).
    *   NFR.2.3 Visi užfiksuoti failai ir metaduomenys turi būti patikimai saugomi ir prieinami.
*   **NFR.3 Naudojamumas:**
    *   NFR.3.1 Programėlės sąsaja turi būti intuityvi ir lengvai suprantama naujiems vartotojams.
    *   NFR.3.2 Idėjų fiksavimo ir veiksmų pasirinkimo procesas turi būti kuo paprastesnis ir reikalauti minimalaus vartotojo įsikišimo.
*   **NFR.4 Saugumas:**
    *   NFR.4.1 Vartotojo duomenys (įkelti failai, metaduomenys, užduotys) turi būti saugomi ir apsaugoti nuo neautorizuotos prieigos.
    *   NFR.4.2 Turi būti užtikrintas duomenų perdavimo saugumas (pvz., naudojant šifravimą).
*   **NFR.5 Suderinamumas:**
    *   NFR.5.1 Programėlė turi palaikyti populiarius paveikslėlių formatus (pvz., PNG, JPEG) ekrano nuotraukoms.
    *   NFR.5.2 Programėlė turi būti suderinama su pagrindinėmis mobiliosiomis operacinėmis sistemomis (pvz., iOS, Android).

### 4.3. Apribojimai
*   **AP.1 Konteksto apribojimas:** Visi reikalavimai ir funkcionalumas turi griežtai atitikti pateiktą kontekstą ir „non-goals“ sąrašą.
*   **AP.2 AI priklausomybė:** Programėlės pagrindinis funkcionalumas priklauso nuo AI apdorojimo tikslumo ir našumo.
*   **AP.3 Failų dydis:** Gali būti nustatyti maksimalūs failų dydžio apribojimai įkeliamoms ekrano nuotraukoms/citatoms, siekiant užtikrinti našumą ir saugojimo efektyvumą.