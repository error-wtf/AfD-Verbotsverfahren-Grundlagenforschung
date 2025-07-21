# AfD-Verbotsverfahren-Grundlagenforschung

Dieses Repository sammelt die zentralen Dokumente, Textfragmente und Forschungsergebnisse zur Vorbereitung einer Klageschrift gegen die Partei „Alternative für Deutschland“ (AfD) beim Bundesverfassungsgericht.

## Projektübersicht

- **Sachverhalt & Grundlagen:** Ausformulierte Entwürfe (PDFs) zum erweiterten Sachverhalt und den rechtlichen Grundlagen.
- **Geheimgutachten:** Vollständige Textfragmentsätze aus den Verfassungsschutz-Gutachten (Teil A & B) in .txt-Dateien.
- **15 Verbotsgründe:** Detaillierte Begründungen und Stichpunktlisten zu den 15 juristischen Verbotsargumenten.
- **Quellenverzeichnis:** Sammlung aller primären und sekundären Quellen (BKA-Berichte, parlamentarische Protokolle, Presseartikel).

## Repository-Struktur

```
├── PUBLIC_SOURCES.md
├── leicht zugängliche Quellen.txt
├── afd-verbot-deepresearch-ausgangspunkt.txt
├── quellen.pdf
├── ENTWURF KLAGESCHRIFT - ERWEITERTER SACHVERHALT - GRUNDLAGEN.pdf
├── ENTWURF KLAGESCHRIFT.pdf
├── WISSENSTAND MAI 2025 AfD.pdf
├── "Im Folgenden werden die zuvor genannten 15 Gründe…".pdf
├── Gründe für ein Afd-Verbots-Verfahren - KI generiert - PDF.pdf
├── schlimmsten zitate der afd.pdf
├── warum die afd verboten gehört.pdf
├── Warum die Alternative für Deutschland verboten gehört.pdf
├── gruende für ein afd verbotsverfahren.pdf
├── gruende_fuer_afd_verbot.txt
├── zusammenfassung_vfs_gutachten_afd.txt
├── Geheimgutachten_Teil A_pages_1_to_100.txt
├── Geheimgutachten_Teil A_pages_101_to_200.txt
├── … (Teil A bis Seite 508)
├── Geheimgutachten_Teil B_pages_1_to_100.txt
├── Geheimgutachten_Teil B_pages_101_to_200.txt
├── … (reparierte Fragmente bis Seite 609)
└── README.md (diese Datei)

```

## Nutzung

1. **Repository klonen**
   ```bash
   git clone https://github.com/LinoCasu/AfD-Verbotsverfahren-Grundlagenforschung.git
   cd AfD-Verbotsverfahren-Grundlagenforschung
   ```

2. **Recherche & Konsolidierung**
   - Suche in den `.txt`-Fragmenten nach spezifischen Begriffen (z. B. "paramilitär", "Verschwörung").
   - Vergleiche die Entwurfsklauseln in den PDFs für Sachverhalts- und Rechtsbegründungskapitel.

3. Nutze Deepresearch um die Quellen zu prüfen

4. Wenn wirklich ein Verbotsverfahren anfangen sollte und Sie Staatsanwalt sind, finden sie Möglichkeiten, die noch nicht zugänglichen Quellen in quellen.pdf, dem Gericht zugänglich zu machen

   
## Mitwirkung

Beiträge sind willkommen! Bitte Issues eröffnen oder Pull Requests einreichen, wenn:
- Du inhaltliche Ergänzungen zu den 15 Verbotsgründen hast.
- Du fehlerhafte Zitate oder Inkonsistenzen in den Fragmente-Dateien findest.
- Du Vorschläge zur Struktur oder zum Aufbau der Klageschrift hast.

---
## KI-gestützte Analyse und Automatisierung

Dieses Repository ist bewusst so aufgebaut, dass es sowohl Jurist:innen als auch Data-Science-Teams effizient unterstützt. Die wichtigsten KI-relevanten Features auf einen Blick:

1. **Durchsuchbare Rohtexte**  
   Die VS-Geheimgutachten liegen als plain-text-Fragmente (*.txt*) vor. Dadurch entfällt aufwändiges OCR- und PDF-Parsing, und KI-Modelle können direkt Named-Entity-Recognition, semantische Suche oder Topic-Modeling auf den Dokumenten ausführen.

2. **Template-basierte Entwurfs-PDFs**  
   Die Klageschrift-Entwürfe (*.pdf*) sind in klar strukturierten Abschnitten (A–D) gegliedert und enthalten Platzhalter für Fußnoten und Seitennachweise. Mit gezielten Prompts lassen sich mit Legal-LMs automatisch alle Quellenangaben vervollständigen und Prüffragen validieren.

3. **Maschinenlesbare Linklisten**  
   Dateien wie `PUBLIC_SOURCES.md` und `leicht zugängliche Quellen.txt` liefern strukturierte Metadaten und URLs. Sie können direkt in Crawler-Skripte oder ETL-Pipelines eingespeist werden, um neue Verfassungsschutzberichte, Bundestagsdokumente oder Gerichtsurteile fortlaufend zu überwachen und zu archivieren.

4. **Graph- und Relationsextraktion**  
   Die Zuordnung von juristischen Argumenten zu Quellen im `quellen.pdf` ermöglicht es, automatisch einen Fakten-Graphen zu generieren (z. B. mit Neo4j), in dem Knoten (Argumente) und Kanten (Belege) visualisiert und Lücken identifiziert werden können.

5. **Nahtlose Integration in ML-Workflows**  
   Standardisierte Dateinamen und Ordnerstrukturen machen es einfach, die Daten in Jupyter-Notebooks, Colab-Environments oder Produktionspipelines einzubinden. So lassen sich schnell Trainingsdatensätze für Legal-LMs erstellen, Feeds für Dokumenten-Updates konfigurieren und Automatisierungen implementieren.

Dank dieser durchdachten Basis können sowohl rechtliche als auch technische Expert:innen ihre jeweiligen Teilaufgaben – von der juristischen Quellensuche bis zum maschinellen Text-Clustering – parallel und effizient abarbeiten.```

---
## 📚 Zugriff auf Dokumente und Ressourcen

Dieses Repository enthält eine umfassende Sammlung an Quellen und Vorarbeiten zum Verbotsverfahren gegen die AfD. Um alle Materialien zu nutzen, gehen Sie bitte wie folgt vor:

### 1. Öffentlich zugängliche Dokumente  
In der Datei [`leicht zugängliche Quellen.txt`](./leicht%20zug%C3%A4ngliche%20Quellen.txt) sind alle frei abrufbaren PDF-Links und Webseiten gelistet:

- **Verfassungsschutzberichte (BfV 2023 & 2024)**
- **Bundestags-Plenarprotokolle** (86. und 203. Sitzung)
- **Drucksache 20/010** (Sicherheitspaket-Anhörung)
- **NPD-Verbotsurteil** (BVerfG 2017, BVerfGE 123, 267 ff.)
- **BMI-Pressemitteilungen** zum VSB

Einfach die Datei öffnen und die Links anklicken oder kopieren.

### 2. Geheime und interne Unterlagen  
Einige der zentralen Beweismittel (z. B. „Ethnokultur-Papier“, Geheimgutachten, Whistleblower-Protokolle, interne E-Mails) sind aus Geheimschutz- oder Datenschutzgründen nicht im öffentlichen Netz verfügbar. Um diese Dokumente zu erhalten, nutzen Sie bitte:

- **Akteneinsicht beim Bundesverfassungsgericht**  
  Formulargemäßer Antrag nach § 43 BVerfGG  
- **Parlamentarische Auskünfte**  
  Schriftliche Bitten an den Innen- oder Geheimdienstausschuss des Deutschen Bundestags (§ 44 GG, Geschäftsordnung BT)  
- **Direktanfragen an Behörden**  
  BMI-Pressestelle oder zuständiges Landesamt für Verfassungsschutz (BfV/LfV)

> **Tipp:** Formulieren Sie in Ihren Anträgen stets klar den Zweck („Verbotsverfahren AfD – Vorlage im Aktenverfügungsverfahren“) und fügen Sie eine Liste der benötigten Unterlagen bei.

### 3. Externe Gutachten & wissenschaftliche Studien  
Für zusätzliche Sachverständigengutachten und Datenauswertungen (z. B. Jenaer Institut für Demokratieforschung, Humboldt-Institut) kontaktieren Sie bitte direkt:

- **Unabhängige Fachinstitute** per E-Mail oder Fernleihe  
- **Universitätsbibliotheken** (Digitalisate via Fernleihe oder Open Access Portale)  

### 4. Social-Media-Daten  
Um den kompletten Datensatz (Tweets, Telegram-Channels) zu exportieren, empfehlen wir:

1. **Twitter Developer API** (Academic Access)  
2. **Telegram-Tools** (Channelscraper, Telethon)  
3. **Beweissicherung:** Unmittelbare Generierung von SHA-256-Hashes für alle Exporte  

---
Ich habe mal das Leak für eine KI aufbereitet. Der Verfassungsschutzbericht ist ja nur nach alter Antifa-Manier, Antifa ist Handarbeit, nur eingescannt worden. Das bereitet KI dadurch Probleme es zu in Gänze zu lesen. Deshalb habe ich ein Python-Script mit Tesseract und OCR drüber laufen lassen und die Bilder als Text-Form gespeichert. Die Textform hat trotz spezieller Tricks zur besseren Verarbeitung kleine Typo-Fehler. Aber mit den originalen PDF (in gesplitteter Form - wegen der Ausgabenbegrenzung von KI) kann die KI den Inhalt zu 96% erfassen. Da ein Verbotsverfahren realistisch bis zu 3 Jahren dauert, können Anwaltskanzleien, oder Interessierte nun KI's damit füttern. Ich habe gleich mal einen Anfang einer Klageschrift, mögliche noch unter Verschluss liegende Quellen die nötig sind, eine Presseschau und Gründe für ein Verbot beigefügt. Da das Ganze bis zu 3 Jahren dauern würde und dann die nächsten Bundestagswahlen sind, und vorraussichtlich die AfD dann sehr viele Stimmen bekommt, sollte man JETZT damit anfangen. Auch wenn gerade der Mantel des Schweigens drüber gelegt ist und Dobrindt mit seiner Konservativen Revolution (man googel mal den Ursprung dieses Begriffes auf Wikipedia) alles andere als aktiv wird, sollte man eigentlich nun (auch wenn der Leak aus ner blöden Ecke kommt) eigentlich dieses Thema vorranbringen. Denn wenn die Afd erstmal an der Macht ist, bleibt wahrscheinlich nicht mehr viel, um deren Faschismus noch zu stoppen.

---

Hier alle 15 Verbotsgründe:

1. Verfassungswidrige Zielsetzung
– Die AfD strebt eine ethnisch‑kulturell homogene „Volksgemeinschaft“ statt Pluralismus an.

2. Systematische Hetze und Menschenfeindlichkeit
– Regelmäßige Diffamierung von Migrant\:innen, Muslim\:innen, Schwarzen und Queers als „Fremdkörper“ oder „Invasion“.

3. Antisemitische Codes und Verschwörungsmythen
– Nutzung historischer Chiffren („Systemmedien“, „Wölfe“) und antisemitischer Motive zur Delegitimierung pluralistischer Institutionen.

4. Beziehungen zu rechtsextremen Netzwerken
– Personelle und organisatorische Verzahnung mit dem „Flügel“ um Höcke, der Identitären Bewegung und paramilitärischen Gruppierungen.

5. Paramilitärisches Potenzial
– Aufbau inoffizieller „Verteidigungsformationen“ und Kooperation mit rechtsextremen Kampfsportgruppen.

6. Gefährdung der öffentlichen Sicherheit und Ordnung
– Aufrufe zu bewaffneten Bürgerwehren und Missachtung polizeilicher sowie gerichtlicher Anweisungen.

7. Angriff auf Rechtsstaat und Gewaltenteilung
– Systematisches Infragestellen von Gerichten, Verfassungsorganen (z. B. Rundfunkrat) und öffentlich‑rechtlichen Medien.

8. Untergrabung demokratischer Prozesse
– Einsatz von Bot‑Netzen und Microtargeting auf Social Media zur Manipulation öffentlicher Debatten.

9. Verletzung von Minderheitenrechten
– Forderungen nach Aberkennung der Staatsbürgerschaft, Abschiebungen und Einschränkung kultureller Freiheiten.

10. Delegitimierung und Spaltung der Gesellschaft
– Diffamierung von NGOs und zivilgesellschaftlichen Akteuren als „Regierungswerkzeuge“.

11. Verletzung der Menschenrechtsprinzipien
– Missachtung von Asylrecht, Glaubens‑ und Meinungsfreiheit zugunsten eines exklusiven Volksbegriffs.

12. Unfähigkeit zur innerparteilichen Abgrenzung
– Keine wirksamen Disziplinarmaßnahmen gegen verfassungsfeindliche Flügel oder Mitglieder.

13. Gerichtliche Einstufung als Verdachts‑ bzw. Beobachtungsfall
– Einstufung durch BfV und Verwaltungsgerichte bestätigt rechtsextremistische Grundausrichtung.

14. Präzedenzfälle und Verfassungsschutzkriterien
– Erfüllen aller Voraussetzungen des BVerfG‑Dreistufentests gemäß Art. 21 GG.

15. Keine marginale Gruppierung
– Anders als bei der NPD verfügt die AfD über substantielle Organisations‑ und Mobilisierungskraft.

---

Alle Quellenangaben sind in den Dateien enthalten.


https://afd-verbot.de
