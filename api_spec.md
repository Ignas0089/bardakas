openapi: 3.0.0
info:
  title: Idėjų Katalizatoriaus API
  version: 1.0.0
  description: API specifikacija „Idėjų Katalizatoriaus“ programėlei, skirtai idėjų fiksavimui, apdorojimui ir pavertimui veiksmais.

servers:
  - url: https://api.idejukatalizatorius.lt/v1
    description: Pagrindinis serveris

tags:
  - name: Ideas
    description: Idėjų valdymas
  - name: Actions
    description: Veiksmų pasiūlymai
  - name: Tasks
    description: Užduočių valdymas
  - name: Projects
    description: Projektų valdymas
  - name: Search
    description: Paieška
  - name: Events
    description: Įvykių pranešimai

paths:
  /ideas:
    post:
      summary: Įkelti naują idėją
      description: Įkelia naują idėją (ekrano nuotrauką ar URL) apdorojimui.
      tags:
        - Ideas
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/IdeaInput'
      responses:
        '202':
          description: Idėja sėkmingai priimta apdorojimui.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    format: uuid
                    description: Unikalus idėjos identifikatorius.
                  status:
                    type: string
                    description: Idėjos apdorojimo būsena (pvz., "received", "processing").
        '400':
          description: Neteisinga užklausa.
        '500':
          description: Vidinė serverio klaida.

  /ideas/{id}:
    get:
      summary: Gauti idėjos detales
      description: Grąžina konkrečios idėjos metaduomenis, OCR turinį, žymes ir PARA priskyrimą.
      tags:
        - Ideas
      parameters:
        - in: path
          name: id
          schema:
            type: string
            format: uuid
          required: true
          description: Unikalus idėjos identifikatorius.
      responses:
        '200':
          description: Idėjos detalės sėkmingai gautos.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Idea'
        '404':
          description: Idėja nerasta.
        '500':
          description: Vidinė serverio klaida.

  /actions/suggest:
    post:
      summary: Pasiūlyti veiksmus idėjai
      description: Grąžina rekomenduojamus veiksmus (sukurti užduotį, pridėti prie projekto, išsaugoti) su pasitikėjimo balais konkrečiai idėjai.
      tags:
        - Actions
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                ideaId:
                  type: string
                  format: uuid
                  description: Idėjos, kuriai siūlomi veiksmai, identifikatorius.
              required:
                - ideaId
      responses:
        '200':
          description: Veiksmų pasiūlymai sėkmingai gauti.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionSuggestion'
        '404':
          description: Idėja nerasta.
        '500':
          description: Vidinė serverio klaida.

  /tasks:
    post:
      summary: Sukurti naują užduotį
      description: Sukuria naują užduotį, prie kurios gali būti pridedama idėja ir jos metaduomenys.
      tags:
        - Tasks
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TaskInput'
      responses:
        '201':
          description: Užduotis sėkmingai sukurta.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    format: uuid
                    description: Unikalus užduoties identifikatorius.
                  title:
                    type: string
                    description: Užduoties pavadinimas.
                  description:
                    type: string
                    nullable: true
                    description: Užduoties aprašymas.
                  attachedIdeaId:
                    type: string
                    format: uuid
                    nullable: true
                    description: Prisegtos idėjos identifikatorius.
        '400':
          description: Neteisinga užklausa.
        '500':
          description: Vidinė serverio klaida.

  /projects/{id}/attach:
    post:
      summary: Pridėti idėją prie projekto
      description: Prideda idėją ir jos metaduomenis prie esamo projekto.
      tags:
        - Projects
      parameters:
        - in: path
          name: id
          schema:
            type: string
            format: uuid
          required: true
          description: Unikalus projekto identifikatorius.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProjectAttachInput'
      responses:
        '200':
          description: Idėja sėkmingai pridėta prie projekto.
        '400':
          description: Neteisinga užklausa.
        '440':
          description: Projektas nerastas.
        '500':
          description: Vidinė serverio klaida.

  /search:
    get:
      summary: Išmanioji paieška
      description: Atlieka išmaniąją paiešką pagal OCR turinį, žymes, projektus ir užduotis.
      tags:
        - Search
      parameters:
        - in: query
          name: q
          schema:
            type: string
          required: true
          description: Paieškos užklausa.
        - in: query
          name: tags
          schema:
            type: array
            items:
              type: string
          description: Filtruoti pagal žymes (pvz., #lyderystė).
        - in: query
          name: projects
          schema:
            type: array
            items:
              type: string
          description: Filtruoti pagal projektų pavadinimus.
        - in: query
          name: tasks
          schema:
            type: array
            items:
              type: string
          description: Filtruoti pagal užduočių pavadinimus.
        - in: query
          name: paraArea
          schema:
            type: string
          description: Filtruoti pagal PARA sritį (pvz., "Asmeninis Augimas").
      responses:
        '200':
          description: Paieškos rezultatai sėkmingai gauti.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SearchResult'
        '400':
          description: Neteisinga užklausa.
        '500':
          description: Vidinė serverio klaida.

webhooks:
  ideaProcessed:
    post:
      summary: Idėjos apdorojimo įvykis
      description: Išsiunčiamas, kai idėja yra sėkmingai apdorota AI ir paruošta veiksmams.
      tags:
        - Events
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/IdeaProcessedEvent'
      responses:
        '200':
          description: Įvykis sėkmingai gautas.
        '400':
          description: Neteisinga užklausa.

components:
  schemas:
    IdeaInput:
      type: object
      properties:
        file:
          type: string
          format: binary
          description: Įkeliamas failas (ekrano nuotrauka).
        url:
          type: string
          format: uri
          nullable: true
          description: URL, jei idėja yra iš interneto.
        source:
          type: string
          enum: [share, drag]
          description: Kaip idėja buvo įkelta (pasidalinta ar nutempta).
        device:
          type: string
          nullable: true
          description: Įrenginys, iš kurio įkelta idėja.
      required:
        - source

    Idea:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unikalus idėjos identifikatorius.
        originalContentUrl:
          type: string
          format: uri
          description: Originalaus įkelto failo/URL nuoroda.
        ocrText:
          type: string
          description: Išgautas tekstas iš originalaus turinio.
        tags:
          type: array
          items:
            type: string
          description: Automatiškai sugeneruotos žymės (pvz., #lyderystė, #citata).
        paraAssignment:
          type: object
          properties:
            type:
              type: string
              enum: [Project, Area, Resource, Archive, Inbox]
              description: PARA kategorija.
            name:
              type: string
              description: Konkrečios PARA srities pavadinimas (pvz., "Asmeninis Augimas").
          required:
            - type
            - name
        metadata:
          type: object
          additionalProperties: true
          description: Papildomi AI sugeneruoti metaduomenys (pvz., temos, citatos).
        createdAt:
          type: string
          format: date-time
          description: Idėjos sukūrimo data ir laikas.
      required:
        - id
        - originalContentUrl
        - ocrText
        - tags
        - paraAssignment
        - createdAt

    ActionSuggestion:
      type: object
      properties:
        ideaId:
          type: string
          format: uuid
          description: Idėjos, kuriai siūlomi veiksmai, identifikatorius.
        suggestions:
          type: array
          items:
            type: object
            properties:
              action:
                type: string
                enum: [create_task, add_to_project, just_save]
                description: Siūlomas veiksmas.
              score:
                type: number
                format: float
                description: Veiksmo relevantiškumo balas (0-1).
              label:
                type: string
                description: Veiksmo etiketė (pvz., "[+] sukurti užduotį").
            required:
              - action
              - score
              - label
      required:
        - ideaId
        - suggestions

    TaskInput:
      type: object
      properties:
        title:
          type: string
          description: Užduoties pavadinimas.
        description:
          type: string
          nullable: true
          description: Užduoties aprašymas.
        ideaId:
          type: string
          format: uuid
          nullable: true
          description: Idėjos, kurią reikia prisegti prie užduoties, identifikatorius.
      required:
        - title

    ProjectAttachInput:
      type: object
      properties:
        ideaId:
          type: string
          format: uuid
          description: Idėjos, kurią reikia pridėti prie projekto, identifikatorius.
      required:
        - ideaId

    SearchResult:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Rasto elemento identifikatorius (idėja, užduotis, projektas).
        type:
          type: string
          enum: [idea, task, project]
          description: Rasto elemento tipas.
        title:
          type: string
          description: Rasto elemento pavadinimas/antraštė.
        excerpt:
          type: string
          nullable: true
          description: Trumpas turinio fragmentas su paieškos užklausos atitikmenimis.
        tags:
          type: array
          items:
            type: string
          description: Susijusios žymės.
        paraAssignment:
          type: object
          properties:
            type:
              type: string
              enum: [Project, Area, Resource, Archive, Inbox]
            name:
              type: string
          required:
            - type
            - name
      required:
        - id
        - type
        - title

    IdeaProcessedEvent:
      type: object
      properties:
        ideaId:
          type: string
          format: uuid
          description: Apdorotos idėjos identifikatorius.
        status:
          type: string
          enum: [processed, failed]
          description: Apdorojimo būsena.
        details:
          type: object
          nullable: true
          additionalProperties: true
          description: Papildoma informacija apie apdorojimą (pvz., klaidos pranešimas).
      required:
        - ideaId
        - status