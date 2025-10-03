# AI/ML Dizainas „Idėjų Katalizatoriaus“ programėlei

Šis dokumentas aprašo dirbtinio intelekto ir mašininio mokymosi (AI/ML) komponentų dizainą „Idėjų Katalizatoriaus“ programėlei, atsižvelgiant į pateiktus reikalavimus ir kontekstą.

## 1. OCR pipeline

OCR (Optical Character Recognition) apdorojimo grandinė yra atsakinga už teksto išgavimą iš vizualinių šaltinių (ekrano nuotraukų) ir jo paruošimą tolesnei analizei.

**Eilės tvarka:**

1.  **Import:**
    *   **Aprašymas:** Vartotojas įkelia ekrano nuotrauką arba pasidalina teksto citata. Sistema priima įvairius paveikslėlių formatus (PNG, JPEG) ir tekstinius duomenis.
    *   **Prielaidos:** Paveikslėliai yra pakankamai geros kokybės (rezoliucija, apšvietimas) teksto atpažinimui. Teksto citatos yra tiesiogiai perduodamos į kitą etapą.
    *   **Pseudo-kodas:**
        ```python
        def import_data(input_data):
            if is_image(input_data):
                return {"type": "image", "content": input_data}
            elif is_text(input_data):
                return {"type": "text", "content": input_data}
            else:
                raise ValueError("Unsupported input data type")
        ```

2.  **Dedup (Deduplication):**
    *   **Aprašymas:** Siekiant išvengti pasikartojančio turinio apdorojimo ir saugojimo, naujai įkeltas turinys lyginamas su esamu. Tai gali būti atliekama naudojant hešavimo funkcijas paveikslėliams (pvz., perceptual hashing) ir teksto palyginimą.
    *   **Prielaidos:** Dedup tikslumas yra svarbus, bet ne kritinis, nes vartotojas gali sąmoningai įkelti panašų turinį.
    *   **Pseudo-kodas:**
        ```python
        def deduplicate(processed_data, existing_hashes):
            if processed_data["type"] == "image":
                image_hash = calculate_perceptual_hash(processed_data["content"])
                if image_hash in existing_hashes:
                    return {"status": "duplicate", "hash": image_hash}
                return {"status": "new", "hash": image_hash}
            elif processed_data["type"] == "text":
                text_hash = calculate_text_hash(processed_data["content"])
                if text_hash in existing_hashes:
                    return {"status": "duplicate", "hash": text_hash}
                return {"status": "new", "hash": text_hash}
        ```

3.  **OCR (Optical Character Recognition):**
    *   **Aprašymas:** Iš paveikslėlių išgaunamas tekstas. Naudojami pažangūs OCR varikliai (pvz., Google Cloud Vision API, Tesseract su patobulinimais), užtikrinantys aukštą tikslumą (NFR.2.1: >90%).
    *   **Prielaidos:** OCR variklis palaiko lietuvių kalbą ir yra optimizuotas ekrano nuotraukoms.
    *   **Pseudo-kodas:**
        ```python
        def perform_ocr(image_content):
            # Example using a hypothetical OCR service
            ocr_result = OCRService.recognize_text(image_content, lang="lt")
            return ocr_result.full_text, ocr_result.blocks # blocks for layout detection
        ```

4.  **Layout/Region Detection:**
    *   **Aprašymas:** Nustatomi teksto blokai, antraštės, pastraipos ir kitos struktūrinės dalys paveikslėlyje. Tai padeda geriau suprasti dokumento struktūrą ir atskirti citatas nuo bendro teksto.
    *   **Prielaudos:** OCR variklis pateikia informaciją apie teksto blokus ir jų koordinates.
    *   **Pseudo-kodas:**
        ```python
        def detect_layout(ocr_blocks):
            regions = []
            for block in ocr_blocks:
                # Simple heuristic: large text blocks might be paragraphs, smaller ones titles
                if block.is_paragraph:
                    regions.append({"type": "paragraph", "text": block.text, "coords": block.coords})
                elif block.is_title:
                    regions.append({"type": "title", "text": block.text, "coords": block.coords})
                else:
                    regions.append({"type": "text_line", "text": block.text, "coords": block.coords})
            return regions
        ```

5.  **Language Detection:**
    *   **Aprašymas:** Nustatoma atpažinto teksto kalba. Tai svarbu tolesniam turinio supratimui ir teksto normalizavimui.
    *   **Prielaidos:** Sistema palaiko kelias kalbas, ypač lietuvių ir anglų.
    *   **Pseudo-kodas:**
        ```python
        def detect_language(text):
            # Example using a hypothetical language detection library
            lang_code = LanguageDetector.detect(text)
            return lang_code # e.g., "lt", "en"
        ```

6.  **Text Normalization:**
    *   **Aprašymas:** Išgautas tekstas valomas ir normalizuojamas: pašalinami nereikalingi simboliai, koreguojamos dažnos OCR klaidos, konvertuojama į vieningą formatą (pvz., mažosios raidės, pašalinami dvigubi tarpai).
    *   **Prielaidos:** Normalizavimo taisyklės yra apibrėžtos ir atnaujinamos.
    *   **Pseudo-kodas:**
        ```python
        def normalize_text(text, language):
            text = text.lower() # Convert to lowercase
            text = remove_punctuation(text) # Remove punctuation
            text = remove_extra_spaces(text) # Remove extra spaces
            # Apply language-specific normalization if needed
            if language == "lt":
                text = apply_lithuanian_normalization(text)
            return text
        ```

## 2. Turinio supratimas

Šiame etape apdorotas tekstas analizuojamas, siekiant išgauti semantinę informaciją.

### 2.1. Teksto klasifikacija

*   **Aprašymas:** Nustatoma bendra teksto kategorija ar tema (pvz., "verslas", "technologijos", "asmeninis tobulėjimas", "naujienos"). Tai padeda priskirti PARA sritis ir generuoti aukšto lygio žymes.
*   **Modelis:** Naudojamas iš anksto apmokytas teksto klasifikavimo modelis (pvz., BERT, RoBERTa arba specializuotas FastText modelis), apmokytas ant didelio įvairaus teksto duomenų rinkinio su atitinkamomis kategorijomis. Modelis bus nuolat tobulinamas su vartotojų atsiliepimais.
*   **Pavyzdys:** Tekstas apie "lyderystės principus" gali būti klasifikuojamas kaip "asmeninis tobulėjimas" ir "verslas".
*   **Pseudo-kodas:**
    ```python
    def classify_text(normalized_text):
        # Load pre-trained classification model
        model = load_ml_model("text_classifier")
        probabilities = model.predict(normalized_text)
        # Return top N categories with their confidence scores
        return get_top_categories(probabilities, n=3)
    ```

### 2.2. Citatos atpažinimas

*   **Aprašymas:** Identifikuojamos konkrečios citatos tekste. Tai gali būti atliekama naudojant taisykles (kabutės, autoriaus paminėjimas) ir/arba mašininio mokymosi modelius (pvz., seka-į-seką modeliai, apmokyti atpažinti citatų struktūras).
*   **Modelis/Taisyklės:** Hibridinis metodas:
    *   **Taisyklės:** Ieškoma teksto, apgaubto kabutėmis ("...", '...'), arba teksto, po kurio seka autoriaus paminėjimas (pvz., "- Autorius").
    *   **ML modelis:** Jei taisyklės nepakankamos, gali būti naudojamas smulkiai sureguliuotas (fine-tuned) Named Entity Recognition (NER) modelis, apmokytas atpažinti citatų pradžią ir pabaigą.
*   **Pavyzdys:** "Vienintelis būdas atlikti puikų darbą – mylėti tai, ką darai." - Steve Jobs.
*   **Pseudo-kodas:**
    ```python
    def extract_quotes(text, layout_regions):
        quotes = []
        # Rule-based detection
        for sentence in split_into_sentences(text):
            if '"' in sentence or "'" in sentence: # Simple check for quotes
                quotes.append({"text": sentence, "method": "rule_based"})
        
        # ML-based detection (if rules are insufficient or for higher accuracy)
        # ner_model = load_ml_model("quote_ner")
        # ml_quotes = ner_model.predict(text)
        # quotes.extend(ml_quotes)
        
        return quotes
    ```

### 2.3. Temų išgryninimas

*   **Aprašymas:** Išskiriamos pagrindinės teksto temos ir sub-temos. Tai gilesnė analizė nei teksto klasifikacija, leidžianti generuoti detalesnes žymes.
*   **Modelis:** Naudojamas temų modeliavimo algoritmas (pvz., LDA, NMF) arba pažangesni neuroniniai tinklai (pvz., Top2Vec, BERTopic), kurie gali išgauti temas iš teksto korpuso. Modelis apmokomas ant didelio duomenų rinkinio, kad atpažintų įvairias temas.
*   **Pavyzdys:** Tekstas apie "dirbtinio intelekto etiką" gali išgryninti temas "AI", "etika", "technologijos", "filosofija".
*   **Pseudo-kodas:**
    ```python
    def extract_topics(normalized_text, language):
        # Load pre-trained topic model
        topic_model = load_ml_model("topic_extractor")
        topics = topic_model.get_topics(normalized_text, language=language)
        return topics # e.g., [{"topic": "lyderystė", "score": 0.85}, {"topic": "inovacijos", "score": 0.6}]
    ```

## 3. Žymėjimas

Žymėjimo procesas apima automatinių žymių generavimą ir jų valdymą.

### 3.1. Ontologija (auto-tags)

*   **Aprašymas:** Automatinės žymės generuojamos remiantis teksto klasifikacija, temų išgryninimu ir iš anksto apibrėžta ontologija. Ontologija yra hierarchinė žinių struktūra, apibrėžianti sąvokas ir jų ryšius programėlės domene.
*   **Ontologijos struktūra:**
    *   Aukšto lygio kategorijos (pvz., "Asmeninis Augimas", "Profesinis Tobulėjimas", "Kūryba").
    *   Sub-kategorijos (pvz., "Lyderystė", "Produktyvumas", "Finansai" po "Asmeninis Augimas").
    *   Specifinės žymės (pvz., "#mindfulness", "#OKR", "#citata").
*   **Generavimo procesas:**
    1.  Teksto klasifikacija nustato aukšto lygio kategorijas.
    2.  Temų išgryninimas identifikuoja sub-kategorijas ir specifines žymes.
    3.  Citatos atpažinimas prideda žymę "#citata".
    4.  Naudojamas žodynas (angl. lexicon) su raktažodžiais, susietais su ontologijos žymėmis.
*   **Pavyzdys:** Jei tekstas klasifikuojamas kaip "Asmeninis Augimas" ir išgryninamos temos "lyderystė", "motyvacija", o taip pat aptinkama citata, gali būti sugeneruotos žymės: `#asmeninisaugimas`, `#lyderystė`, `#motyvacija`, `#citata`.
*   **Pseudo-kodas:**
    ```python
    def generate_auto_tags(text_classifications, topics, quotes_detected, ontology):
        tags = set()
        # Add tags based on classifications
        for category in text_classifications:
            tags.add(ontology.get_tag_for_category(category["name"]))
        
        # Add tags based on topics
        for topic in topics:
            tags.add(ontology.get_tag_for_topic(topic["topic"]))
            
        if quotes_detected:
            tags.add("#citata")
            
        # Further refine tags using keyword matching against a lexicon
        # For example, if "OKR" is in text, add "#OKR"
        
        return list(tags)
    ```

### 3.2. „Confidence“ slenksčiai

*   **Aprašymas:** Kiekvienai sugeneruotai žymei priskiriamas pasitikėjimo balas (confidence score). Žymės, kurių balas viršija nustatytą slenkstį, yra automatiškai priskiriamos. Žymės, kurių balas yra žemiau aukšto slenksčio, bet viršija žemesnį slenkstį, gali būti pasiūlytos vartotojui peržiūrėti.
*   **Slenksčiai:**
    *   **Aukštas slenkstis (pvz., 0.8):** Žymės priskiriamos automatiškai.
    *   **Žemas slenkstis (pvz., 0.5):** Žymės siūlomos vartotojui kaip rekomendacijos.
*   **Tikslas:** Balansuoti tarp automatizavimo ir vartotojo kontrolės, užtikrinant aukštą žymių relevanciją (NFR.2.2).
*   **Pseudo-kodas:**
    ```python
    def filter_tags_by_confidence(generated_tags_with_scores, high_threshold=0.8, low_threshold=0.5):
        auto_assigned_tags = []
        suggested_tags = []
        for tag, score in generated_tags_with_scores:
            if score >= high_threshold:
                auto_assigned_tags.append(tag)
            elif score >= low_threshold:
                suggested_tags.append(tag)
        return auto_assigned_tags, suggested_tags
    ```

### 3.3. Redaguojamumas

*   **Aprašymas:** Vartotojas turi galimybę peržiūrėti, redaguoti, pridėti ar pašalinti automatiškai sugeneruotas žymes. Tai užtikrina vartotojo kontrolę ir leidžia tobulinti AI modelius per vartotojo atsiliepimus.
*   **Mechanizmas:** Programėlės sąsajoje pateikiamas žymių sąrašas, kurį vartotojas gali interaktyviai keisti. Vartotojo atlikti pakeitimai gali būti naudojami modelio tobulinimui (pvz., per aktyvų mokymąsi).

## 4. PARA priskyrimas

PARA (Projects, Areas, Resources, Archives) priskyrimas yra hibridinis metodas, derinantis taisykles ir mašininio mokymosi modelius.

### 4.1. Taisyklių + modelio hibridas

*   **Aprašymas:** Kiekviena užfiksuota idėja bandoma priskirti prie vienos iš PARA kategorijų (Project, Area, Resource, Archive) ir konkrečios vartotojo sukurtos PARA srities (pvz., "Asmeninis Augimas", "Darbas", "Hobiai").
*   **Hibridinis metodas:**
    1.  **Taisyklės (pirmenybė):**
        *   **Raktai žodžiai/frazės:** Jei tekste aptinkami konkretūs raktažodžiai ar frazės, susijusios su esamais vartotojo projektais ar sritimis, idėja priskiriama atitinkamai. Pvz., jei tekstas mini "naujo produkto paleidimą" ir vartotojas turi projektą "Produkto X paleidimas", idėja priskiriama tam projektui.
        *   **Vartotojo nustatymai:** Vartotojas gali nustatyti numatytąsias PARA sritis tam tikroms žymėms ar šaltiniams.
        *   **Kontekstas:** Jei idėja yra susijusi su aktyvia užduotimi ar projektu, prie kurio vartotojas dirba, ji gali būti priskirta tam pačiam kontekstui.
    2.  **ML modelis (fallback):**
        *   **Modelis:** Teksto klasifikavimo modelis (pvz., smulkiai sureguliuotas BERT modelis), apmokytas ant vartotojo duomenų (esami projektai, sritys, resursai ir jų turinys). Modelis mokosi susieti teksto turinį su PARA kategorijomis ir konkrečiomis sritimis.
        *   **Mokymas:** Modelis mokomas naudojant vartotojo istorinius duomenis: kaip vartotojas anksčiau priskyrė idėjas prie PARA sričių. Tai yra personalizuotas modelis.
        *   **Išvestis:** Modelis pateikia tikimybę kiekvienai PARA kategorijai ir konkrečiai sričiai.
*   **Pavyzdys:**
    *   Tekstas: "Susitikimas su komanda dėl naujos rinkodaros strategijos."
    *   Taisyklė: "rinkodaros strategija" atitinka projektą "Rinkodaros kampanija Q4". Priskiriama: Project: "Rinkodaros kampanija Q4".
    *   Jei taisyklių nėra: ML modelis nustato, kad didžiausia tikimybė yra Area: "Darbas" su 0.92 pasitikėjimu.
*   **Pseudo-kodas:**
    ```python
    def assign_para(normalized_text, user_projects, user_areas, user_resources, user_archives, user_settings):
        # 1. Rule-based assignment (priority)
        for project in user_projects:
            if any(keyword in normalized_text for keyword in project.keywords):
                return {"type": "Project", "name": project.name, "method": "rule_based"}
        
        for area in user_areas:
            if any(keyword in normalized_text for keyword in area.keywords):
                return {"type": "Area", "name": area.name, "method": "rule_based"}
        
        # Check user-defined default settings
        if user_settings.has_default_para_for_tags(current_tags):
            return user_settings.get_default_para(current_tags)

        # 2. ML Model-based assignment (fallback)
        para_model = load_ml_model("para_assigner_personal") # Personal model for each user
        probabilities = para_model.predict(normalized_text, user_projects, user_areas, user_resources, user_archives)
        
        # Select the PARA with the highest confidence
        best_para = get_highest_confidence_para(probabilities)
        
        return {"type": best_para.type, "name": best_para.name, "method": "ml_based", "confidence": best_para.confidence}
    ```

### 4.2. Fallback į „Inbox“

*   **Aprašymas:** Jei nei taisyklės, nei ML modelis negali priskirti idėjos su pakankamu pasitikėjimu (pvz., žemiau nustatyto slenksčio), idėja automatiškai patenka į „Idėjų Pašto dėžutę“ (Inbox).
*   **Tikslas:** Užtikrinti, kad nė viena idėja nebūtų prarasta ir vartotojas galėtų rankiniu būdu ją peržiūrėti ir priskirti vėliau.
*   **Pseudo-kodas:**
    ```python
    def handle_para_assignment_result(para_assignment_result, min_confidence_threshold=0.6):
        if para_assignment_result["confidence"] >= min_confidence_threshold:
            return para_assignment_result
        else:
            return {"type": "Inbox", "name": "Idėjų Pašto dėžutė", "method": "fallback"}
    ```

## 5. Relevantiškumo scoring veiksmų pasiūlymams (task vs project vs save)

Po to, kai idėja yra apdorota ir jai priskirti metaduomenys (OCR tekstas, žymės, PARA), sistema pasiūlo tris veiksmus: sukurti užduotį, pridėti prie projekto, tiesiog išsaugoti. Šių veiksmų relevantiškumas įvertinamas naudojant mašininio mokymosi modelį.

### 5.1. Modelis ir požymiai

*   **Modelis:** Daugiaklasis klasifikavimo modelis (pvz., logistinė regresija, Random Forest, arba smulkiai sureguliuotas BERT modelis), apmokytas nustatyti labiausiai tinkamą veiksmą.
*   **Mokymas:** Modelis mokomas naudojant istorinius vartotojo duomenis: kokius veiksmus vartotojas pasirinko anksčiau, atsižvelgiant į idėjos turinį, žymes, PARA priskyrimą ir vartotojo kontekstą.
*   **Požymiai (Features):**
    *   **Idėjos turinys:** Normalizuotas OCR tekstas, teksto įterpimai (embeddings).
    *   **Metaduomenys:** Sugeneruotos žymės, PARA priskyrimas (kategorija ir sritis).
    *   **Vartotojo kontekstas:**
        *   **Aktyvūs projektai/užduotys:** Ar idėja yra susijusi su šiuo metu aktyviais vartotojo projektais ar užduotimis?
        *   **Vartotojo elgesio istorija:** Kokie veiksmai buvo dažniausiai pasirenkami panašioms idėjoms praeityje?
        *   **Laikas:** Paros metas, savaitės diena (gali įtakoti vartotojo produktyvumą ir norą imtis veiksmų).
        *   **Idėjos sudėtingumas/veiksmingumas:** Ar tekstas rodo, kad idėja yra veiksminga (pvz., "įgyvendinti", "pradėti", "sukurti") ar labiau informacinė (pvz., "sužinoti", "perskaityti")?
    *   **Citatos buvimas:** Jei idėja yra citata, ji gali būti labiau linkusi būti "tiesiog išsaugota" arba "pridėta prie resursų".
*   **Išvestis:** Modelis pateikia tikimybę kiekvienam veiksmui (Task, Project, Save).
*   **Pseudo-kodas:**
    ```python
    def score_action_relevance(idea_content, tags, para_assignment, user_context):
        action_model = load_ml_model("action_relevance_scorer")
        
        features = {
            "text_embedding": get_text_embedding(idea_content),
            "tags": tags,
            "para_type": para_assignment["type"],
            "para_name": para_assignment["name"],
            "is_related_to_active_project": check_active_project_relevance(idea_content, user_context),
            "user_action_history_features": get_user_action_history_features(user_context),
            "time_of_day": get_current_time_features(),
            "contains_action_verbs": contains_action_verbs(idea_content),
            "is_quote": "citata" in tags # Simplified check
        }
        
        probabilities = action_model.predict(features)
        return {
            "create_task": probabilities["task"],
            "add_to_project": probabilities["project"],
            "just_save": probabilities["save"]
        }
    ```

## 6. A/B testuojami „nudges“ (kada siūlyti užduotį vs „tiesiog išsaugoti“)

„Nudges“ yra subtilūs vartotojo sąsajos elementai ar pranešimai, skirti paskatinti vartotoją atlikti tam tikrus veiksmus. Jie bus A/B testuojami, siekiant optimizuoti idėjų konversiją į užduotis ar projektus.

### 6.1. A/B testavimo strategija

*   **Tikslas:** Padidinti idėjų konversijos rodiklį (NFR.3.2, Sėkmės metrika 3.3).
*   **Metodika:** Vartotojai bus atsitiktinai suskirstyti į kontrolinę ir eksperimentines grupes. Kiekvienai grupei bus rodomi skirtingi „nudges“ arba jų nebus visai.
*   **Metrikos:** Stebimas veiksmų pasirinkimo pasiskirstymas (Sėkmės metrika 3.3), idėjų konversijos rodiklis, laikas iki veiksmo.

### 6.2. „Nudges“ tipai ir scenarijai

*   **Scenarijus 1: Aukšta užduoties relevancija, žema projekto/išsaugojimo relevancija.**
    *   **Nudge:** Ryškiau pabrėžti „Sukurti užduotį“ mygtuką (pvz., didesnis, ryškesnė spalva, animacija). Gali būti rodomas trumpas pranešimas: „Ši idėja puikiai tinka užduočiai!“.
    *   **A/B testas:** Kontrolinė grupė mato standartinius mygtukus. Eksperimentinė grupė mato pabrėžtą užduoties mygtuką ir/arba pranešimą.

*   **Scenarijus 2: Aukšta išsaugojimo relevancija (pvz., citata, bendra informacija), žema užduoties/projekto relevancija.**
    *   **Nudge:** Ryškiau pabrėžti „Tiesiog išsaugoti“ mygtuką. Gali būti rodomas pranešimas: „Išsaugokite šią įžvalgą ateičiai!“.
    *   **A/B testas:** Kontrolinė grupė mato standartinius mygtukus. Eksperimentinė grupė mato pabrėžtą išsaugojimo mygtuką ir/arba pranešimą.

*   **Scenarijus 3: Panaši relevancija tarp užduoties ir išsaugojimo.**
    *   **Nudge:** Gali būti rodomas klausimas: „Ar norėtumėte paversti tai veiksmu, ar tiesiog išsaugoti?“. Arba pasiūlyti papildomą kontekstą, kodėl viena parinktis gali būti geresnė.
    *   **A/B testas:** Kontrolinė grupė mato standartinius mygtukus. Eksperimentinė grupė mato klausimą arba papildomą informaciją.

*   **Scenarijus 4: Vartotojo elgesio istorija.**
    *   **Nudge:** Jei vartotojas dažnai konvertuoja panašias idėjas į užduotis, sistema gali automatiškai pasiūlyti „Sukurti užduotį“ kaip numatytąjį veiksmą, bet su galimybe lengvai pakeisti.
    *   **A/B testas:** Kontrolinė grupė visada mato vienodą numatytąjį pasirinkimą. Eksperimentinė grupė mato personalizuotą numatytąjį pasirinkimą.

### 6.3. „Nudge“ valdymo sistema

*   **Aprašymas:** Reikalinga sistema, kuri leistų dinamiškai konfigūruoti ir diegti skirtingus „nudges“, stebėti jų efektyvumą ir automatiškai parinkti geriausiai veikiančius.
*   **Technologijos:** Gali būti naudojamos funkcijos vėliavėlės (feature flags) ir nuotolinė konfigūracija, leidžianti keisti „nudges“ be programėlės atnaujinimo.
*   **ML optimizavimas:** Ilgainiui, ML modelis gali būti apmokytas nustatyti optimalų „nudge“ kiekvienam vartotojui ir idėjai, atsižvelgiant į kontekstą ir istorinį elgesį.