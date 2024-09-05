from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'contact_phone', 'job_name', 'email', 'date',
            'ordered_by', 'ship_to', 'address',
            'quantity1', 'width1', 'height1', 'unit_price1', 'discount1',
            'area1', 'total_price1', 'notes1', 'Size_Options1', 'color1',
            'Frame_Options1', 'Grille_Options1', 
            'tempgl1', 'window_type1', 'bnb1','QO','signature',
            'quantity2','width2','height2','tempgl2','window_type2',
            'bnb2','notes2','Size_Options2','color2','Frame_Options2','Grille_Options2',
            'quantity3','width3','height3','tempgl3','window_type3',
            'bnb3','notes3','Size_Options3','color3','Frame_Options3','Grille_Options3',
            'quantity4','width4','height4','tempgl4','window_type4',
            'bnb4','notes4','Size_Options4','color4','Frame_Options4','Grille_Options4',
            'quantity5','width5','height5','tempgl5','window_type5',
            'bnb5','notes5','Size_Options5','color5','Frame_Options5','Grille_Options5',
            'quantity6','width6','height6','tempgl6','window_type6',
            'bnb6','notes6','Size_Options6','color6','Frame_Options6','Grille_Options6',
            'quantity7','width7','height7','tempgl7','window_type7',
            'bnb7','notes7','Size_Options7','color7','Frame_Options7','Grille_Options7',
            'quantity8','width8','height8','tempgl8','window_type8',
            'bnb8','notes8','Size_Options8','color8','Frame_Options8','Grille_Options8',
            'quantity9','width9','height9','tempgl9','window_type9',
            'bnb9','notes9','Size_Options9','color9','Frame_Options9','Grille_Options9',
            'quantity10','width10','height10','tempgl10','window_type10',
            'bnb10','notes10','Size_Options10','color10','Frame_Options10','Grille_Options10',
            'quantity11','width11','height11','tempgl11','window_type11',
            'bnb11','notes11','Size_Options11','color11','Frame_Options11','Grille_Options11',
            'quantity12','width12','height12','tempgl12','window_type12',
            'bnb12','notes12','Size_Options12','color12','Frame_Options12','Grille_Options12'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Change the label of 'contact_phone'
        self.fields['contact_phone'].label = 'Contact Phone Number'
        self.fields['QO'].label = 'Order or Quote'
        self.fields['quantity1'].label = 'Quantity'
        self.fields['width1'].label = 'Width'
        self.fields['height1'].label = 'Height'
        self.fields['tempgl1'].label = 'Temp GL'
        self.fields['window_type1'].label = 'Window Type'
        self.fields['bnb1'].label = 'Build-IN Blinds'
        self.fields['notes1'].label = 'Note'
        self.fields['Size_Options1'].label = 'Size Options'
        self.fields['color1'].label = 'Color'
        self.fields['Frame_Options1'].label = 'Frame Option'
        self.fields['Grille_Options1'].label = 'Grille Option'
        self.fields['LE1'].label = 'Low-E'
        self.fields['GT1'].label = 'Grey Tinted'
        self.fields['GR1'].label = 'Grey Reflective'
        self.fields['B1'].label = 'Blue'
        self.fields['signature'].label = 'Signature'

        self.fields['quantity2'].label = 'Quantity'
        self.fields['width2'].label = 'Width'
        self.fields['height2'].label = 'Height'
        self.fields['tempgl2'].label = 'Temp GL'
        self.fields['window_type2'].label = 'Window Type'
        self.fields['bnb2'].label = 'Build-IN Blinds'
        self.fields['notes2'].label = 'Note'
        self.fields['Size_Options2'].label = 'Size Options'
        self.fields['color2'].label = 'Color'
        self.fields['Frame_Options2'].label = 'Frame Option'
        self.fields['Grille_Options2'].label = 'Grille Option'
        self.fields['LE2'].label = 'Low-E'
        self.fields['GT2'].label = 'Grey Tinted'
        self.fields['GR2'].label = 'Grey Reflective'
        self.fields['B2'].label = 'Blue'

        self.fields['quantity3'].label = 'Quantity'
        self.fields['width3'].label = 'Width'
        self.fields['height3'].label = 'Height'
        self.fields['tempgl3'].label = 'Temp GL'
        self.fields['window_type3'].label = 'Window Type'
        self.fields['bnb3'].label = 'Build-IN Blinds'
        self.fields['notes3'].label = 'Note'
        self.fields['Size_Options3'].label = 'Size Options'
        self.fields['color3'].label = 'Color'
        self.fields['Frame_Options3'].label = 'Frame Option'
        self.fields['Grille_Options3'].label = 'Grille Option'
        self.fields['LE3'].label = 'Low-E'
        self.fields['GT3'].label = 'Grey Tinted'
        self.fields['GR3'].label = 'Grey Reflective'
        self.fields['B3'].label = 'Blue'

        self.fields['quantity4'].label = 'Quantity'
        self.fields['width4'].label = 'Width'
        self.fields['height4'].label = 'Height'
        self.fields['tempgl4'].label = 'Temp GL'
        self.fields['window_type4'].label = 'Window Type'
        self.fields['bnb4'].label = 'Build-IN Blinds'
        self.fields['notes4'].label = 'Note'
        self.fields['Size_Options4'].label = 'Size Options'
        self.fields['color4'].label = 'Color'
        self.fields['Frame_Options4'].label = 'Frame Option'
        self.fields['Grille_Options4'].label = 'Grille Option'
        self.fields['LE4'].label = 'Low-E'
        self.fields['GT4'].label = 'Grey Tinted'
        self.fields['GR4'].label = 'Grey Reflective'
        self.fields['B4'].label = 'Blue'

        self.fields['quantity5'].label = 'Quantity'
        self.fields['width5'].label = 'Width'
        self.fields['height5'].label = 'Height'
        self.fields['tempgl5'].label = 'Temp GL'
        self.fields['window_type5'].label = 'Window Type'
        self.fields['bnb5'].label = 'Build-IN Blinds'
        self.fields['notes5'].label = 'Note'
        self.fields['Size_Options5'].label = 'Size Options'
        self.fields['color5'].label = 'Color'
        self.fields['Frame_Options5'].label = 'Frame Option'
        self.fields['Grille_Options5'].label = 'Grille Option'
        self.fields['LE5'].label = 'Low-E'
        self.fields['GT5'].label = 'Grey Tinted'
        self.fields['GR5'].label = 'Grey Reflective'
        self.fields['B5'].label = 'Blue'

        self.fields['quantity6'].label = 'Quantity'
        self.fields['width6'].label = 'Width'
        self.fields['height6'].label = 'Height'
        self.fields['tempgl6'].label = 'Temp GL'
        self.fields['window_type6'].label = 'Window Type'
        self.fields['bnb6'].label = 'Build-IN Blinds'
        self.fields['notes6'].label = 'Note'
        self.fields['Size_Options6'].label = 'Size Options'
        self.fields['color6'].label = 'Color'
        self.fields['Frame_Options6'].label = 'Frame Option'
        self.fields['Grille_Options6'].label = 'Grille Option'
        self.fields['LE6'].label = 'Low-E'
        self.fields['GT6'].label = 'Grey Tinted'
        self.fields['GR6'].label = 'Grey Reflective'
        self.fields['B6'].label = 'Blue'

        self.fields['quantity7'].label = 'Quantity'
        self.fields['width7'].label = 'Width'
        self.fields['height7'].label = 'Height'
        self.fields['tempgl7'].label = 'Temp GL'
        self.fields['window_type7'].label = 'Window Type'
        self.fields['bnb7'].label = 'Build-IN Blinds'
        self.fields['notes7'].label = 'Note'
        self.fields['Size_Options7'].label = 'Size Options'
        self.fields['color7'].label = 'Color'
        self.fields['Frame_Options7'].label = 'Frame Option'
        self.fields['Grille_Options7'].label = 'Grille Option'
        self.fields['LE7'].label = 'Low-E'
        self.fields['GT7'].label = 'Grey Tinted'
        self.fields['GR7'].label = 'Grey Reflective'
        self.fields['B7'].label = 'Blue'

        self.fields['quantity8'].label = 'Quantity'
        self.fields['width8'].label = 'Width'
        self.fields['height8'].label = 'Height'
        self.fields['tempgl8'].label = 'Temp GL'
        self.fields['window_type8'].label = 'Window Type'
        self.fields['bnb8'].label = 'Build-IN Blinds'
        self.fields['notes8'].label = 'Note'
        self.fields['Size_Options8'].label = 'Size Options'
        self.fields['color8'].label = 'Color'
        self.fields['Frame_Options8'].label = 'Frame Option'
        self.fields['Grille_Options8'].label = 'Grille Option'
        self.fields['LE8'].label = 'Low-E'
        self.fields['GT8'].label = 'Grey Tinted'
        self.fields['GR8'].label = 'Grey Reflective'
        self.fields['B8'].label = 'Blue'

        self.fields['quantity9'].label = 'Quantity'
        self.fields['width9'].label = 'Width'
        self.fields['height9'].label = 'Height'
        self.fields['tempgl9'].label = 'Temp GL'
        self.fields['window_type9'].label = 'Window Type'
        self.fields['bnb9'].label = 'Build-IN Blinds'
        self.fields['notes9'].label = 'Note'
        self.fields['Size_Options9'].label = 'Size Options'
        self.fields['color9'].label = 'Color'
        self.fields['Frame_Options9'].label = 'Frame Option'
        self.fields['Grille_Options9'].label = 'Grille Option'
        self.fields['LE9'].label = 'Low-E'
        self.fields['GT9'].label = 'Grey Tinted'
        self.fields['GR9'].label = 'Grey Reflective'
        self.fields['B9'].label = 'Blue'

        self.fields['quantity10'].label = 'Quantity'
        self.fields['width10'].label = 'Width'
        self.fields['height10'].label = 'Height'
        self.fields['tempgl10'].label = 'Temp GL'
        self.fields['window_type10'].label = 'Window Type'
        self.fields['bnb10'].label = 'Build-IN Blinds'
        self.fields['notes10'].label = 'Note'
        self.fields['Size_Options10'].label = 'Size Options'
        self.fields['color10'].label = 'Color'
        self.fields['Frame_Options10'].label = 'Frame Option'
        self.fields['Grille_Options10'].label = 'Grille Option'
        self.fields['LE10'].label = 'Low-E'
        self.fields['GT10'].label = 'Grey Tinted'
        self.fields['GR10'].label = 'Grey Reflective'
        self.fields['B10'].label = 'Blue'

        self.fields['quantity11'].label = 'Quantity'
        self.fields['width11'].label = 'Width'
        self.fields['height11'].label = 'Height'
        self.fields['tempgl11'].label = 'Temp GL'
        self.fields['window_type11'].label = 'Window Type'
        self.fields['bnb11'].label = 'Build-IN Blinds'
        self.fields['notes11'].label = 'Note'
        self.fields['Size_Options11'].label = 'Size Options'
        self.fields['color11'].label = 'Color'
        self.fields['Frame_Options11'].label = 'Frame Option'
        self.fields['Grille_Options11'].label = 'Grille Option'
        self.fields['LE11'].label = 'Low-E'
        self.fields['GT11'].label = 'Grey Tinted'
        self.fields['GR11'].label = 'Grey Reflective'
        self.fields['B11'].label = 'Blue'

        self.fields['quantity12'].label = 'Quantity'
        self.fields['width12'].label = 'Width'
        self.fields['height12'].label = 'Height'
        self.fields['tempgl12'].label = 'Temp GL'
        self.fields['window_type12'].label = 'Window Type'
        self.fields['bnb12'].label = 'Build-IN Blinds'
        self.fields['notes12'].label = 'Note'
        self.fields['Size_Options12'].label = 'Size Options'
        self.fields['color12'].label = 'Color'
        self.fields['Frame_Options12'].label = 'Frame Option'
        self.fields['Grille_Options12'].label = 'Grille Option'
        self.fields['LE12'].label = 'Low-E'
        self.fields['GT12'].label = 'Grey Tinted'
        self.fields['GR12'].label = 'Grey Reflective'
        self.fields['B12'].label = 'Blue'