import os

def update_navbar_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_btn = '<a href=\"careers.html\" class=\"btn\">Get Started</a>'
    new_btn = '''<div style=\"display:flex; gap:1rem; align-items:center;\">
      <button class=\"theme-toggle btn btn-secondary\" style=\"padding: 0.5rem 1rem; border:1px solid var(--border-color); background:transparent; color:var(--text-color);\">??</button>
      <a href=\"careers.html\" class=\"btn\">Get Started</a>
    </div>'''
    
    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)

def update_navbar_others(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_nav = '<nav class=\"navbar\">\n    <a href=\"index.html\" class=\"logo\">SkillBridge</a>\n  </nav>'
    new_nav = '''<nav class=\"navbar\" style=\"border-bottom: 1px solid var(--border-color); background: var(--nav-bg); padding: 1rem 4rem;\">
    <a href=\"index.html\" class=\"logo\" style=\"color: var(--text-heading); font-weight: 800; font-size: 1.5rem; text-decoration: none;\">SkillBridge</a>
    <button class=\"theme-toggle btn btn-secondary\" style=\"padding: 0.5rem 1rem; border:1px solid var(--border-color); background:transparent; color:var(--text-color);\">??</button>
  </nav>'''
    
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

update_navbar_index()
update_navbar_others('careers.html')
update_navbar_others('assess.html')
update_navbar_others('dashboard.html')

# Update app.js
with open('js/app.js', 'a', encoding='utf-8') as f:
    f.write('''
// Theme Toggle Logic
document.addEventListener('DOMContentLoaded', () => {
  const currentTheme = localStorage.getItem('sb_theme') || 'light';
  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  }
  
  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.textContent = currentTheme === 'dark' ? '??' : '??';
    btn.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('sb_theme', 'light');
        document.querySelectorAll('.theme-toggle').forEach(b => b.textContent = '??');
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('sb_theme', 'dark');
        document.querySelectorAll('.theme-toggle').forEach(b => b.textContent = '??');
      }
    });
  });
});
''')

