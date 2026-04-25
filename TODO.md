# Header Mobile Fix — DONE

## Goal
Make "Cytti" stay big, stack "Fashions" below it smaller, and show nav links on mobile screens.

## Files updated
- [x] index.html
- [x] collections.html
- [x] contact.html
- [x] about.html
- [x] visit.html
- [x] visit (1).html
- [x] home.html

## Changes made
1. HTML: `<em>Fashions</em>` → `<em class="brand-sub">Fashions</em>` in all files
2. CSS: Added mobile-specific styles (`@media(max-width:767px)`) so:
   - Brand stacks vertically with "Fashions" smaller below "Cytti"
   - Nav links are visible, compact, centered and wrap on small screens
   - WhatsApp button shrinks to fit
3. Desktop layout (`@media(min-width:768px)`) stays exactly the same

