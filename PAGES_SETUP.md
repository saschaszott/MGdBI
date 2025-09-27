# GitHub Pages Setup für MGdBI

Diese Anleitung erklärt, wie Sie GitHub Pages für dieses Repository aktivieren.

## Automatische Aktivierung

1. Gehen Sie zu den **Settings** Ihres GitHub Repositories
2. Scrollen Sie zum Abschnitt **Pages** (linke Seitenleiste)
3. Unter **Source** wählen Sie **GitHub Actions**
4. Die Workflow-Datei `.github/workflows/pages.yml` wird automatisch erkannt

## Nach der Aktivierung

- Die Website wird automatisch bei jedem Push zum `main` Branch neu erstellt
- Die Website ist erreichbar unter: `https://saschaszott.github.io/MGdBI/`
- Der Build-Status ist in der **Actions**-Registerkarte sichtbar

## Manuelle Aktualisierung

Falls neue Python-Scripte hinzugefügt werden, wird die Website automatisch aktualisiert. Sie können auch manuell eine Aktualisierung auslösen:

1. Gehen Sie zur **Actions**-Registerkarte
2. Klicken Sie auf "Deploy to GitHub Pages"
3. Klicken Sie auf **Run workflow**

## Lokale Entwicklung

Um die Website lokal zu testen:

```bash
# Website generieren
python generate_website.py

# Lokalen Server starten
python -m http.server 8000

# Website öffnen: http://localhost:8000
```

Die Website wird automatisch mit aktuellen Informationen über alle Python-Scripte im Repository generiert.