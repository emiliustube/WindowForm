from django.shortcuts import render
from .models import Order
from django.http import HttpResponseRedirect

def order_view(request):
    if request.method == "POST":
        # Capture form data from request.POST
        name = request.POST.get('name')
        contact_phone = request.POST.get('contact_phone')
        email = request.POST.get('email')
        job_name = request.POST.get('job_name')
        date = request.POST.get('date')
        ordered_by = request.POST.get('ordered_by')
        ship_to = request.POST.get('ship_to')
        address = request.POST.get('address')
        qo = request.POST.get('QO')
        signature = request.POST.get('signature')

        shipping_price = request.POST.get('shipping_price', 0)
        extra_discount = request.POST.get('extra_discount', 0)
        vat_percentage = request.POST.get('vat_percentage', 0)

        # Mapping dictionaries for labels
        color_labels = {
            'MB': 'Matt Black',
            'MC': 'Matt Chocolate',
            'MDG': 'Matt Dark Grey',
            'MLG': 'Matt Light Grey',
            'CG': 'Champagne',
            'PW': 'Pure White',
            'YW': 'Yellow Wood',
            'GO': 'Golden Oak',
            'YR': 'Yellow Rosewood',
            'RS': 'Red Sandalwood',
            'C': 'Custom',
        }

        frame_options_labels = {
            'NF': 'Nail Fin',
            'SR': 'Stucco/Retro',
            'B': 'Block',
        }

        size_options_labels = {
            'NES': 'Net/Exact Size',
            'RO': 'Rough Opening',
        }

        grille_options_labels = {
            'no': 'NA',
            'yes': 'YES',
        }

        window_types_labels = {
            'none': '',  # Ensure 'none' maps to an empty string
            'xo_ox': 'XO/OX - 2 Lite Slider (X is Active)',
            'xox': 'XOX - 3 Lite Slider (X is Active)',
            'csmt': 'CSMT - Casement',
            'sh': 'SH - Single Hung',
            'pd': 'PD - Patio Door',
            'dh': 'DH - Double Hung',
            'xx': 'XX - 2 Lite (X Active)',
            'pw': 'PW - Picture Window',
            'awn': 'AWN - Awning',
            'fr': 'FR - Swing Door',
            'bf': 'BF - Bifold Window',
            'tt': 'TT - Tilt and Turn',
            'bw': 'BW - Bay Window',
            'fw': 'FW - Folding Window',
        }

        hand_options = {
            'lh': 'Left Hand',
            'rh': 'Right Hand',
        }

        # Capture fields for multiple items (up to 12 items)
        items = []
        for i in range(1, 13):
            quantity = request.POST.get(f'quantity{i}', '0')
            width = request.POST.get(f'width{i}', '0')
            height = request.POST.get(f'height{i}', '0')
            unit_price = request.POST.get(f'unit_price{i}', '0')
            discount = request.POST.get(f'discount{i}', '0')

            # Capture checkbox and notes fields
            tempgl = request.POST.get(f'tempgl{i}', 'off') == 'on'  # Converts to True if checked
            window_type = request.POST.get(f'window_type{i}', '')
            h = request.POST.get(f'h{i}', '')
            bnb = request.POST.get(f'bnb{i}', 'off') == 'on'
            notes = request.POST.get(f'notes{i}', '')
            Size_Options = request.POST.get(f'Size_Options{i}', '')
            color = request.POST.get(f'color{i}', '')
            Frame_Options = request.POST.get(f'Frame_Options{i}', '')
            Grille_Options = request.POST.get(f'Grille_Options{i}', '')
            LE = request.POST.get(f'LE{i}', 'off') == 'on'
            GT = request.POST.get(f'GT{i}', 'off') == 'on'
            GR = request.POST.get(f'GR{i}', 'off') == 'on'
            B = request.POST.get(f'B{i}', 'off') == 'on'

            # Convert to float and provide defaults for empty fields
            try:
                quantity = float(quantity) if quantity else 0
                width = float(width) if width else 0
                height = float(height) if height else 0
                unit_price = float(unit_price) if unit_price else 0
                discount = float(discount) if discount else 0
            except ValueError:
                quantity = width = height = unit_price = discount = 0

            total_price = quantity * width * height * unit_price * (1 - discount / 100)

            # Prepare description from checkboxes, notes, and selected options
            description_parts = []
            if tempgl: description_parts.append('Temp GL')
            if h: description_parts.append(hand_options.get(h,h))
            if bnb: description_parts.append('Build-N Blinds')
            if Size_Options: description_parts.append(size_options_labels.get(Size_Options, Size_Options))
            if color: description_parts.append(color_labels.get(color, color))
            if Frame_Options: description_parts.append(frame_options_labels.get(Frame_Options, Frame_Options))
            if Grille_Options: description_parts.append(grille_options_labels.get(Grille_Options, Grille_Options))
            if LE: description_parts.append('Low-E')
            if GT: description_parts.append('Grey Tinted')
            if GR: description_parts.append('Grey Reflective')
            if B: description_parts.append('Blue')
            if window_type and window_type != 'none':
                description_parts.append(window_types_labels.get(window_type, window_type))
            if notes: description_parts.append(notes)

            description = ', '.join(description_parts) if description_parts else f"Item {i}"

            item = {
                'quantity': quantity,
                'width': width,
                'height': height,
                'unit_price': unit_price,
                'discount': discount,
                'total_price': total_price,
                'description': description,
                'tempgl': tempgl,
                'h' : h,
                'bnb': bnb,
                'notes': notes,
                'LE': LE,
                'GT': GT,
                'GR': GR,
                'B': B,
            }
            items.append(item)

        # Create and save a new Order instance
        order = Order(
            name=name,
            contact_phone=contact_phone,
            email=email,
            job_name=job_name,
            date=date,
            ordered_by=ordered_by,
            ship_to=ship_to,
            address=address,
            QO=qo,
            signature=signature,
            items=items,
            shipping_price=shipping_price,
            extra_discount=extra_discount,
            vat_percentage=vat_percentage,  
            # Assign the fields for the items to the Order instance dynamically
            **{f'quantity{i+1}': item['quantity'] for i, item in enumerate(items)},
            **{f'width{i+1}': item['width'] for i, item in enumerate(items)},
            **{f'height{i+1}': item['height'] for i, item in enumerate(items)},
            **{f'unit_price{i+1}': item['unit_price'] for i, item in enumerate(items)},
            **{f'discount{i+1}': item['discount'] for i, item in enumerate(items)},
            **{f'tempgl{i+1}': item['tempgl'] for i, item in enumerate(items)},
            **{f'bnb{i+1}': item['bnb'] for i, item in enumerate(items)},
            **{f'notes{i+1}': item['notes'] for i, item in enumerate(items)},
            **{f'LE{i+1}': item['LE'] for i, item in enumerate(items)},
            **{f'GT{i+1}': item['GT'] for i, item in enumerate(items)},
            **{f'GR{i+1}': item['GR'] for i, item in enumerate(items)},
            **{f'B{i+1}': item['B'] for i, item in enumerate(items)},
        )
        order.save()

        # Pass item details to the template
        return render(request, 'order_confirmation.html', {'order': order, 'items': items})
    else:
        return render(request, 'index.html')
