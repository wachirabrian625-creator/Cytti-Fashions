import glob, os

files = glob.glob('*.html')
old_emoji = '💬'

replacements = [
    # CSS additions
    ('.cta-btn:hover{transform:scale(1.05)}', '.cta-btn:hover{transform:scale(1.05)}\n  .cta-btn .wa-icon{height:18px;width:18px;object-fit:contain}'),
    ('.socials a:hover{background:rgba(255,255,255,.1)}', '.socials a:hover{background:rgba(255,255,255,.1)}\n  .socials a img{height:20px;width:20px;object-fit:contain}'),
    ('.wa-float:hover{transform:scale(1.1)}', '.wa-float:hover{transform:scale(1.1)}\n  .wa-float img{height:28px;width:28px;object-fit:contain}'),
    # Header CTA
    ('class="cta-btn">WhatsApp Us</a>', 'class="cta-btn"><img src="photos/whatsApp.png" alt="WhatsApp" class="wa-icon"> WhatsApp Us</a>'),
    # Footer social
    ('aria-label="WhatsApp">' + old_emoji + '</a>', 'aria-label="WhatsApp"><img src="photos/whatsApp.png" alt="WhatsApp"></a>'),
    # Floating button
    ('class="wa-float" aria-label="Chat on WhatsApp">' + old_emoji + '</a>', 'class="wa-float" aria-label="Chat on WhatsApp"><img src="photos/whatsApp.png" alt="WhatsApp"></a>'),
    # Inline inquiries (collections.html style)
    ('>' + old_emoji + ' Inquire on WhatsApp</a>', '><img src="photos/whatsApp.png" alt="WhatsApp" style="height:16px;width:16px;vertical-align:middle;margin-right:4px"> Inquire on WhatsApp</a>'),
    # Inline inquiries (home.html wa-link style)
    ('class="wa-link">' + old_emoji + ' Inquire on WhatsApp</a>', 'class="wa-link"><img src="photos/whatsApp.png" alt="WhatsApp" style="height:16px;width:16px;vertical-align:middle;margin-right:4px"> Inquire on WhatsApp</a>'),
    # WhatsApp Fibbie buttons
    ('class="cta-btn">' + old_emoji + ' WhatsApp Fibbie</a>', 'class="cta-btn"><img src="photos/whatsApp.png" alt="WhatsApp" style="height:16px;width:16px;vertical-align:middle;margin-right:4px"> WhatsApp Fibbie</a>'),
    # Ask About Dress Shoes
    ('class="cta-btn">' + old_emoji + ' Ask About Dress Shoes</a>', 'class="cta-btn"><img src="photos/whatsApp.png" alt="WhatsApp" style="height:16px;width:16px;vertical-align:middle;margin-right:4px"> Ask About Dress Shoes</a>'),
    # Contact page channel card icon
    ('font-size:1.4rem">' + old_emoji + '</div>', '"><img src="photos/whatsApp.png" alt="WhatsApp" style="height:28px;width:28px"></div>'),
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', fname)
    else:
        print('No changes in', fname)

print('Done!')

