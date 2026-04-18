import os
import re

source_dir = "source"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False

    # Regex to find _("...") or _('...') containing NVDA
    # This simple regex looks for _( followed by string literal containing NVDA.
    # It might not handle multiline strings perfectly, but it covers 99% of cases.
    
    def replacer(match):
        full_match = match.group(0)
        return full_match.replace("NVDA", "LASR")

    # Match _("...") or _('...') or _("""...""") or _('''...''')
    # Let's match any string literal that contains NVDA and is inside _() or pgettext()
    
    # We will use a simpler approach: 
    # Just find 'NVDA' and replace with 'LASR' if it's inside _("...")
    # Actually, let's just use re.sub on the whole file, but only targeting _(...) blocks
    
    new_content = content
    
    # Pattern to match _( "..." ) or _( '...' )
    pattern = r'_\(\s*([\'"]{1,3})(.*?)\1\s*\)'
    
    def inner_replacer(m):
        quote = m.group(1)
        text = m.group(2)
        if "NVDA" in text:
            text = text.replace("NVDA", "LASR")
        return f"_({quote}{text}{quote})"

    new_content = re.sub(pattern, inner_replacer, new_content, flags=re.DOTALL)

    # Also match kwargs like title=_("...")
    # The previous regex handles that because it just looks for _(...)
    
    # Let's also do pgettext("...", "...")
    pgettext_pattern = r'pgettext\(\s*([\'"]{1,3})(.*?)\1\s*,\s*([\'"]{1,3})(.*?)\3\s*\)'
    def pgettext_replacer(m):
        q1 = m.group(1)
        ctx = m.group(2)
        q2 = m.group(3)
        text = m.group(4)
        if "NVDA" in text:
            text = text.replace("NVDA", "LASR")
        return f"pgettext({q1}{ctx}{q1}, {q2}{text}{q2})"
        
    new_content = re.sub(pgettext_pattern, pgettext_replacer, new_content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
        return True
    return False

updated_count = 0
for root, dirs, files in os.walk(source_dir):
    for f in files:
        if f.endswith('.py') or f.endswith('.pyw'):
            filepath = os.path.join(root, f)
            if process_file(filepath):
                updated_count += 1

print(f"Total files updated: {updated_count}")
