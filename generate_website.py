#!/usr/bin/env python3
"""
Script to generate website content for MGdBI Python scripts
"""
import os
import ast
import re
from pathlib import Path

def extract_docstring(filepath):
    """Extract the first docstring from a Python file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        if ast.get_docstring(tree):
            return ast.get_docstring(tree)
        
        # If no module docstring, look for first function docstring
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                if docstring:
                    return f"Function {node.name}: {docstring}"
        
        return None
    except Exception:
        return None

def extract_description_from_comments(filepath):
    """Extract description from comments in the first few lines."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        description_lines = []
        for line in lines[:10]:  # Check first 10 lines
            line = line.strip()
            if line.startswith('#') and not line.startswith('#!/'):
                # Clean up comment
                comment = line.lstrip('#').strip()
                if comment and not comment.startswith('...'):
                    description_lines.append(comment)
        
        return ' '.join(description_lines) if description_lines else None
    except Exception:
        return None

def infer_description_from_filename(filename):
    """Infer description from filename."""
    name_without_ext = filename.replace('.py', '').replace('-', ' ').replace('_', ' ')
    
    descriptions = {
        'sum': 'Berechnung der Summe von natürlichen Zahlen',
        'sum squares': 'Berechnung der Summe von Quadratzahlen',
        'sum even numbers': 'Berechnung der Summe von geraden Zahlen',
        'sum odd numbers': 'Berechnung der Summe von ungeraden Zahlen',
        'sum powers of 2': 'Berechnung der Summe von Zweierpotenzen',
        'prod': 'Berechnung des Produkts von natürlichen Zahlen (Fakultät)',
        'binomial coefficient': 'Berechnung des Binomialkoeffizienten',
        'pascals triangle': 'Erzeugung des Pascalschen Dreiecks',
        'number theory': 'Zahlentheoretische Operationen (ggT, kgV)',
        'number value': 'Umrechnung von Binärzahlen ins Dezimalsystem',
        'prime factorization': 'Primfaktorzerlegung von Zahlen',
        'isbn validator': 'Validierung von ISBN-10 Nummern',
        'isbn13 validator': 'Validierung von ISBN-13 Nummern',
        'truth table': 'Erzeugung von Wahrheitstabellen für logische Ausdrücke',
        'simplify logic formula': 'Vereinfachung logischer Formeln',
        'logic2sets': 'Übersetzung zwischen Aussagenlogik und Mengenoperationen'
    }
    
    return descriptions.get(name_without_ext, f'Python-Script: {name_without_ext}')

def categorize_script(filename, description):
    """Categorize script based on filename and description."""
    filename_lower = filename.lower()
    desc_lower = description.lower() if description else ''
    
    if any(word in filename_lower or word in desc_lower for word in ['sum', 'prod', 'binomial', 'pascal']):
        return 'Mathematische Berechnungen'
    elif any(word in filename_lower or word in desc_lower for word in ['logic', 'truth', 'sets']):
        return 'Logik und Mengentheorie'
    elif any(word in filename_lower or word in desc_lower for word in ['isbn']):
        return 'ISBN-Validierung'
    elif any(word in filename_lower or word in desc_lower for word in ['prime', 'number', 'gcd', 'lcm']):
        return 'Zahlentheorie'
    else:
        return 'Sonstige'

def get_python_files():
    """Get all Python files in the current directory."""
    current_dir = Path('.')
    python_files = []
    
    for file in current_dir.glob('*.py'):
        if file.name != 'generate_website.py':  # Exclude this script
            python_files.append(file.name)
    
    return sorted(python_files)

def generate_script_info():
    """Generate information about all Python scripts."""
    scripts = []
    
    for filename in get_python_files():
        filepath = Path(filename)
        
        # Try to extract description
        description = (
            extract_docstring(filepath) or 
            extract_description_from_comments(filepath) or 
            infer_description_from_filename(filename)
        )
        
        # Get file size and line count
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            line_count = len(lines)
            file_size = filepath.stat().st_size
        except Exception:
            line_count = 0
            file_size = 0
        
        category = categorize_script(filename, description)
        
        scripts.append({
            'filename': filename,
            'description': description,
            'category': category,
            'line_count': line_count,
            'file_size': file_size
        })
    
    return scripts

def generate_html():
    """Generate the complete HTML website."""
    scripts = generate_script_info()
    
    # Convert to JavaScript format
    js_scripts = []
    for script in scripts:
        # Escape both quotes and newlines for JavaScript
        description = script['description'].replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n').replace('\r', '')
        js_scripts.append(f"""            {{
                filename: '{script['filename']}',
                description: '{description}',
                category: '{script['category']}',
                line_count: {script['line_count']},
                file_size: {script['file_size']}
            }}""")
    
    js_scripts_string = ',\n'.join(js_scripts)
    
    html_template = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MGdBI - Python-Scripte</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}

        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 0;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-align: center;
        }}

        header p {{
            font-size: 1.1rem;
            text-align: center;
            opacity: 0.9;
        }}

        .stats {{
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            text-align: center;
        }}

        .stat-item {{
            margin: 0.5rem;
        }}

        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
            display: block;
        }}

        .stat-label {{
            font-size: 0.9rem;
            color: #666;
        }}

        .category {{
            background: white;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}

        .category-header {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 1rem 1.5rem;
            font-size: 1.3rem;
            font-weight: bold;
        }}

        .scripts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
            padding: 1.5rem;
        }}

        .script-card {{
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 1.5rem;
            transition: all 0.3s ease;
            cursor: pointer;
        }}

        .script-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            border-color: #667eea;
        }}

        .script-filename {{
            font-size: 1.2rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 0.5rem;
            font-family: 'Courier New', monospace;
        }}

        .script-description {{
            color: #666;
            margin-bottom: 1rem;
            font-size: 0.95rem;
        }}

        .script-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            color: #999;
            border-top: 1px solid #e9ecef;
            padding-top: 0.5rem;
        }}

        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
        }}

        .modal-content {{
            background-color: white;
            margin: 5% auto;
            padding: 2rem;
            border-radius: 10px;
            width: 90%;
            max-width: 800px;
            max-height: 80vh;
            overflow-y: auto;
        }}

        .close {{
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }}

        .close:hover {{
            color: #000;
        }}

        pre {{
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 1rem;
            overflow-x: auto;
            font-size: 0.9rem;
            white-space: pre-wrap;
        }}

        .search-container {{
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .search-box {{
            width: 100%;
            padding: 0.8rem;
            border: 2px solid #e9ecef;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }}

        .search-box:focus {{
            outline: none;
            border-color: #667eea;
        }}

        .github-link {{
            text-align: center;
            margin-top: 2rem;
        }}

        .github-link a {{
            color: #667eea;
            text-decoration: none;
            font-size: 1.1rem;
        }}

        .github-link a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2rem;
            }}
            
            .scripts-grid {{
                grid-template-columns: 1fr;
            }}
            
            .stats {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>MGdBI – Python-Scripte</h1>
            <p>Mathematische Grundlagen der Bibliotheksinformatik</p>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">Autor: Sascha Szott</p>
        </header>

        <div class="stats" id="stats">
            <!-- Stats will be populated by JavaScript -->
        </div>

        <div class="search-container">
            <input type="text" class="search-box" id="searchBox" placeholder="Nach Python-Scripten suchen...">
        </div>

        <div id="categories">
            <!-- Categories will be populated by JavaScript -->
        </div>

        <div class="github-link">
            <a href="https://github.com/saschaszott/MGdBI" target="_blank">🔗 GitHub Repository</a>
        </div>
    </div>

    <!-- Modal for displaying code -->
    <div id="codeModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h3 id="modalTitle"></h3>
            <pre id="modalCode"></pre>
        </div>
    </div>

    <script>
        // Python scripts data
        const pythonScripts = [
{js_scripts_string}
        ];

        // Generate statistics
        function generateStats() {{
            const totalScripts = pythonScripts.length;
            const totalLines = pythonScripts.reduce((sum, script) => sum + script.line_count, 0);
            const categories = [...new Set(pythonScripts.map(script => script.category))];
            const totalSize = pythonScripts.reduce((sum, script) => sum + script.file_size, 0);

            const statsHtml = `
                <div class="stat-item">
                    <span class="stat-number">${{totalScripts}}</span>
                    <span class="stat-label">Python-Scripte</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">${{categories.length}}</span>
                    <span class="stat-label">Kategorien</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">${{totalLines}}</span>
                    <span class="stat-label">Zeilen Code</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">${{Math.round(totalSize / 1024 * 10) / 10}}</span>
                    <span class="stat-label">KB Gesamtgröße</span>
                </div>
            `;

            document.getElementById('stats').innerHTML = statsHtml;
        }}

        // Generate categories and scripts
        function generateCategories(scriptsToShow = pythonScripts) {{
            const categories = {{}};
            
            scriptsToShow.forEach(script => {{
                if (!categories[script.category]) {{
                    categories[script.category] = [];
                }}
                categories[script.category].push(script);
            }});

            const categoriesHtml = Object.entries(categories).map(([category, scripts]) => {{
                const scriptsHtml = scripts.map(script => `
                    <div class="script-card" onclick="showCode('${{script.filename}}')">
                        <div class="script-filename">${{script.filename}}</div>
                        <div class="script-description">${{script.description}}</div>
                        <div class="script-meta">
                            <span>${{script.line_count}} Zeilen</span>
                            <span>${{script.file_size}} Bytes</span>
                        </div>
                    </div>
                `).join('');

                return `
                    <div class="category">
                        <div class="category-header">
                            ${{category}} (${{scripts.length}} ${{scripts.length === 1 ? 'Script' : 'Scripte'}})
                        </div>
                        <div class="scripts-grid">
                            ${{scriptsHtml}}
                        </div>
                    </div>
                `;
            }}).join('');

            document.getElementById('categories').innerHTML = categoriesHtml;
        }}

        // Show code in modal
        async function showCode(filename) {{
            const modal = document.getElementById('codeModal');
            const modalTitle = document.getElementById('modalTitle');
            const modalCode = document.getElementById('modalCode');

            modalTitle.textContent = filename;
            modalCode.textContent = 'Lädt...';
            modal.style.display = 'block';

            try {{
                const response = await fetch(filename);
                if (response.ok) {{
                    const code = await response.text();
                    modalCode.textContent = code;
                }} else {{
                    modalCode.textContent = 'Fehler beim Laden der Datei.';
                }}
            }} catch (error) {{
                modalCode.textContent = 'Fehler beim Laden der Datei: ' + error.message;
            }}
        }}

        // Search functionality
        function setupSearch() {{
            const searchBox = document.getElementById('searchBox');
            searchBox.addEventListener('input', (e) => {{
                const query = e.target.value.toLowerCase();
                const filteredScripts = pythonScripts.filter(script => 
                    script.filename.toLowerCase().includes(query) ||
                    script.description.toLowerCase().includes(query) ||
                    script.category.toLowerCase().includes(query)
                );
                generateCategories(filteredScripts);
            }});
        }}

        // Setup modal
        function setupModal() {{
            const modal = document.getElementById('codeModal');
            const closeBtn = document.querySelector('.close');

            closeBtn.onclick = function() {{
                modal.style.display = 'none';
            }}

            window.onclick = function(event) {{
                if (event.target === modal) {{
                    modal.style.display = 'none';
                }}
            }}
        }}

        // Initialize the page
        document.addEventListener('DOMContentLoaded', function() {{
            generateStats();
            generateCategories();
            setupSearch();
            setupModal();
        }});
    </script>
</body>
</html>'''
    
    return html_template

if __name__ == '__main__':
    scripts = generate_script_info()
    
    # Group by category
    categories = {}
    for script in scripts:
        cat = script['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(script)
    
    # Print summary
    print(f"Found {len(scripts)} Python scripts in {len(categories)} categories:")
    for cat, cat_scripts in categories.items():
        print(f"  {cat}: {len(cat_scripts)} scripts")
    
    # Generate HTML
    html_content = generate_html()
    
    # Write to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Generated index.html successfully!")