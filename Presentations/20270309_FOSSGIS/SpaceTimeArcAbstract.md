# Abstract für FOSSGIS Konferenz 2027

**SpaceTime Arc: Eine offene Infrastruktur für spatio-temporale Human-Environment-Interaktion**

*Christian Willmes (Universität zu Köln), Florian Thiery (Research Squirrel Engineers Network), Volker Mische (IPFS Foundation)*

## Das Projekt

SpaceTime Arc ist ein neu entwickeltes Open-Source-Projekt, das eine innovative Infrastruktur für spatio-temporale Daten des menschlichen Raumes über Vergangenheit, Gegenwart und Zukunft hinweg bietet. Im Zentrum steht ein virtueller Globus mit Zeitschieber, der es ermöglicht, Landschaften der Erdgeschichte zu erkunden, aktuelle Geodaten zu visualisieren und zukünftige Szenarien zu simulieren.

## Vision und Innovationspotenzial

Die zentrale Innovation des SpaceTime Arc liegt in der Integration heterogener geospatialer Daten über verschiedene Zeitebenen und Fachdisziplinen hinweg. Das System ermöglicht die Erstellung integrierter 4D-Landschaften (3D-Raum + 1D-Zeit), die als Grundlage für Human-Environment-Interaction-Modellierung dienen können.

**Kernkomponenten:**

- **Virtueller Globus mit Zeitschieber**: Ermöglicht "Zeitreisen" durch historische Landschaften
- **Dateninfrastruktur**: Integriert archäologische, paläoökologische und zukunftsorientierte Daten
- **Open-Source-Prinzipien**: Volle Transparenz und Nachnutzbarkeit
- **Dezentrale Architektur**: Kombination aus Cloud-Native-Geodatenformaten (CNG) und Linked Open Data-Technologien

## Technische Architektur

Die Systemarchitektur von SpaceTime Arc basiert auf einem dreistufigen Ansatz:

1. **Datenbereitstellung & Publikation**: Entwicklung von Datenmodellen, -formaten und Publikationsworkflows
2. **Datenspeicherung & -verteilung**: Nutzung von S3, IPFS und semantischem Web (Matadisco, Linked Open Data)
3. **Client-Anwendungen**: WebApp, QGIS-Plugin und API für verschiedene Nutzergruppen

**Technologische Basis:**

- Cloud-Native Geodatenformate (Vektor, Raster, Mesh, 3D Tiles)
- Semantische Integration via CIDOC CRM, GeoSPARQL, SOSA/SSN und OWL-Time
- Distribuierte Datenspeicherung und -suche (Matadisco-Protokoll)
- 3D-Geodatenintegration via OGC 3D Tiles Standard

## Anwendungsbereiche

Das SpaceTime Arc-System bietet vielfältige Einsatzmöglichkeiten:

- **Forschung**: Integration und Visualisierung von Paläoumweltdaten, archäologischen 3D-Rekonstruktionen und zukünftigen Klimaszenarien
- **Bildung**: Interaktives Lernen über Erdgeschichte und menschliche Zivilisationen
- **Stadt- und Landschaftsplanung**: Analyse von Landschaftsentwicklungen über lange Zeiträume
- **Katastrophenschutz**: Simulation von Küstenveränderungen und Landschaftsentwicklungen

## Wissenschaftliche Relevanz

SpaceTime Arc adressiert aktuelle Herausforderungen im Bereich der geospatialen Datenintegration:

1. **Heterogenität von Paläodaten**: Entwicklung von Workflows zur Integration qualitativer und quantitativer Umweltrekonstruktionen
2. **FAIR-Datenprinzipien**: Volle Umsetzung der FAIR-Prinzipien (Findable, Accessible, Interoperable, Reusable)
3. **Semantische Interoperabilität**: Nutzung etablierter Ontologien für die Integration unterschiedlicher Datendomänen
4. **Open Science**: Publikation wissenschaftlicher Daten in peer-reviewten Journalen und Repositorien

Das Projekt steht in der Tradition etablierter Arbeiten wie PaleoMaps (Willmes 2016) und stützt sich auf bewährte Technologien wie CIDOC CRM, GeoSPARQL und die OGC 3D Tiles Spezifikation.

## Beitritt zum Projekt

SpaceTime Arc ist ein kollaboratives Open-Source-Projekt. Wir laden interessierte Forscher:innen, Entwickler:innen und Institutionen ein, sich an der Weiterentwicklung zu beteiligen. Dazu gehören:

- Mitwirkung bei der Entwicklung von Datenmodellen und -workflows
- Bereitstellung und Annotation von Daten
- Entwicklung von Client-Anwendungen
- Durchführung von Fallstudien zur Validierung des Systems

Das Projekt wird über die GitHub-Organisation [SpaceTimeArc](https://github.com/orgs/SpaceTimeArc/) koordiniert. Für die FOSSGIS-Konferenz 2027 stellen wir unsere Entwicklungen und Konzepte zur Diskussion und suchen nach weiteren Kooperationspartnern in der FOSSGIS-Community.

## Warum FOSSGIS?

Die FOSSGIS-Konferenz ist die ideale Plattform für unser Projekt, da sie sich auf freie und offene Geodateninfrastrukturen konzentriert. SpaceTime Arc passt perfekt zur Konferenzagenda, die sich mit folgenden Themen beschäftigt:

- Open-Source-Geodatenprozesse
- Geodateninfrastrukturen und -werkzeuge
- Semantische Technologien in der Geoinformatik
- 3D-Geodaten und virtuelle Globen
- Nachhaltige Datenpublikation und -archivierung

## Fazit

SpaceTime Arc bietet eine innovative und dringend benötigte Infrastruktur für spatio-temporale Human-Environment-Interaction-Forschung. Durch die Kombination von bewährten Open-Source-Technologien, Linked Open Data-Prinzipien und Cloud-Native Geodatenformaten setzt das Projekt neue Maßstäbe für die Integration und Analyse von Umweltdaten über Zeit und Raum hinweg.

Wir präsentieren unsere Systemarchitektur, erste Implementierungen und Ausblicke auf zukünftige Entwicklungen und laden die FOSSGIS-Community zur Diskussion und Collaboration ein.

**Schlüsselwörter:** Spatio-temporale GIS, Open-Source-Geodateninfrastruktur, Linked Open Data, Cloud-Native Geodaten, 4D-Visualisierung, Human-Environment-Interaction, FAIR-Datenmanagement, 3D Tiles, IPFS, QGIS-Plugin