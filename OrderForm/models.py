from django.db import models

class Order(models.Model):
    WINDOW_TYPE_CHOICES = [
        ('none', '-- none --'),
        ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'),
        ('xox', 'XOX - 3 Lite Slider X is Active'),
        ('csmt', 'CSMT - Casement'),
        ('sh', 'SH - Single Hung'),
        ('pd', 'PD - Patio Door'),
        ('dh', 'DH - Double Hung'),
        ('xx', 'XX - 2 Lite (X Active)'),
        ('pw', 'PW - Picture Window'),
        ('awn', 'AWN - Awning'),
        ('fr', 'FR - Swing Door'),
        ('bf', 'BF - Bifold Window'),
        ('tt', 'TT - Tilt and Turn'),
        ('bw', 'BW - Bay Window'),
    ]
    COLOR_CHOICES = [
        ('MB', 'Matt Black'),
        ('MC', 'Matt Chocolate'),
        ('MDG', 'Matt Dark Grey'),
        ('MLG', 'Matt Light Grey'),
        ('CG', 'Champagne'),
        ('PW', 'Pure White'),
        ('YW', 'Yellow Wood'),
        ('GO', 'Golden Oak'),
        ('YR', 'Yellow Rosewood'),
        ('RS', 'Red Sandalwood'),
        ('C', 'Custom'),
    ]
    SIZE_OPTIONS = [
        ('NES', 'Net/Exact Size'),
        ('RO', 'Rough Opening'),
    ]
    FRAME_OPTIONS = [
        ('NF', 'Nail Fin'),
        ('SR', 'Stucco/Retro'),
        ('B', 'Block'),
    ]
    GRILLE_OPTIONS = [
        ('no', 'NA'),
        ('yes', 'YES'),
    ]
    QO = [
        ('quote', 'Quote'),
        ('order', 'Order'),
    ]

    HAND_OPTIONS = [
        ('lh', 'Left Hand'),
        ('rh', 'Right Hand'),
    ]
    name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField()
    job_name = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    ordered_by = models.CharField(max_length=100, blank=True)
    ship_to = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    QO = models.CharField(max_length=50, null=True, choices=QO, default='none')
    signature = models.CharField(max_length=100, blank=True, null=True)
    items = models.JSONField(default=list)  # JSONField to store all items
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    extra_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    vat_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    # Field definitions for -1-
    quantity1 = models.IntegerField(null=True, blank=True)
    width1 = models.FloatField(null=True, blank=True)
    height1 = models.FloatField(null=True, blank=True)
    unit_price1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    area1 = models.FloatField(null=True, blank=True)
    total_price1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tempgl1 = models.BooleanField(default=False)
    window_type1 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, null=True, blank=True, default='none')
    h1 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb1 = models.BooleanField(default=False)
    notes1 = models.CharField(max_length=100, blank=True, default="")
    Size_Options1 = models.CharField(max_length=50, choices=SIZE_OPTIONS, null=True, blank=True)
    color1 = models.CharField(max_length=50, choices=COLOR_CHOICES, null=True, blank=True)
    Frame_Options1 = models.CharField(max_length=50, choices=FRAME_OPTIONS, null=True, blank=True)
    Grille_Options1 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, null=True, blank=True)
    LE1 = models.BooleanField(default=False)
    GT1 = models.BooleanField(default=False)
    GR1 = models.BooleanField(default=False)
    B1 = models.BooleanField(default=False)

    #-2-
    quantity2 = models.FloatField(null=True, blank=True)
    width2 = models.FloatField(null=True, blank=True)
    height2 = models.FloatField(null=True, blank=True)
    tempgl2 = models.BooleanField(default=False)
    unit_price2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type2 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h2 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb2 = models.BooleanField(default=False)
    notes2 = models.CharField(max_length=100, default="")
    Size_Options2 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color2 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options2 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options2 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE2 = models.BooleanField(default=False)
    GT2 = models.BooleanField(default=False)
    GR2 = models.BooleanField(default=False)
    B2 = models.BooleanField(default=False)

    #-3-

    quantity3 = models.FloatField(null=True, blank=True)
    width3 = models.FloatField(null=True, blank=True)
    height3 = models.FloatField(null=True, blank=True)
    tempgl3 = models.BooleanField(default=False)
    unit_price3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type3 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h3 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb3 = models.BooleanField(default=False)
    notes3 = models.CharField(max_length=100, default="")
    Size_Options3 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color3 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options3 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options3 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE3 = models.BooleanField(default=False)
    GT3 = models.BooleanField(default=False)
    GR3 = models.BooleanField(default=False)
    B3 = models.BooleanField(default=False)

    #-4-

    quantity4 = models.FloatField(null=True, blank=True)
    width4 = models.FloatField(null=True, blank=True)
    height4 = models.FloatField(null=True, blank=True)
    tempgl4 = models.BooleanField(default=False)
    window_type4 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    unit_price4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    h4 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb4 = models.BooleanField(default=False)
    notes4 = models.CharField(max_length=100, default="")
    Size_Options4 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color4 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options4 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options4 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE4 = models.BooleanField(default=False)
    GT4 = models.BooleanField(default=False)
    GR4 = models.BooleanField(default=False)
    B4 = models.BooleanField(default=False)

    #-5-

    quantity5 = models.FloatField(null=True, blank=True)
    width5 = models.FloatField(null=True, blank=True)
    height5 = models.FloatField(null=True, blank=True)
    tempgl5 = models.BooleanField(default=False)
    window_type5 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    unit_price5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    h5 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb5 = models.BooleanField(default=False)
    notes5 = models.CharField(max_length=100, default="")
    Size_Options5 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color5 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options5 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options5 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE5 = models.BooleanField(default=False)
    GT5 = models.BooleanField(default=False)
    GR5 = models.BooleanField(default=False)
    B5 = models.BooleanField(default=False)

    #-6-

    quantity6 = models.FloatField(null=True, blank=True)
    width6 = models.FloatField(null=True, blank=True)
    height6 = models.FloatField(null=True, blank=True)
    tempgl6 = models.BooleanField(default=False)
    window_type6 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    unit_price6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount6 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    h6 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb6 = models.BooleanField(default=False)
    notes6 = models.CharField(max_length=100, default="")
    Size_Options6 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color6 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options6 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options6 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE6 = models.BooleanField(default=False)
    GT6 = models.BooleanField(default=False)
    GR6 = models.BooleanField(default=False)
    B6 = models.BooleanField(default=False)

    #-7-

    quantity7 = models.FloatField(null=True, blank=True)
    width7 = models.FloatField(null=True, blank=True)
    height7 = models.FloatField(null=True, blank=True)
    tempgl7 = models.BooleanField(default=False)
    unit_price7 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount7 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type7 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h7 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)   
    bnb7 = models.BooleanField(default=False)
    notes7 = models.CharField(max_length=100, default="")
    Size_Options7 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color7 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options7 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options7 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE7 = models.BooleanField(default=False)
    GT7 = models.BooleanField(default=False)
    GR7 = models.BooleanField(default=False)
    B7 = models.BooleanField(default=False)

    #-8-

    quantity8 = models.FloatField(null=True, blank=True)
    width8 = models.FloatField(null=True, blank=True)
    height8 = models.FloatField(null=True, blank=True)
    tempgl8 = models.BooleanField(default=False)
    unit_price8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount8 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type8 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h8 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb8 = models.BooleanField(default=False)
    notes8 = models.CharField(max_length=100, default="")
    Size_Options8 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color8 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options8 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options8 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE8 = models.BooleanField(default=False)
    GT8 = models.BooleanField(default=False)
    GR8 = models.BooleanField(default=False)
    B8 = models.BooleanField(default=False)

    #-9-

    quantity9 = models.FloatField(null=True, blank=True)
    width9 = models.FloatField(null=True, blank=True)
    height9 = models.FloatField(null=True, blank=True)
    tempgl9 = models.BooleanField(default=False)
    unit_price9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount9 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type9 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h9 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb9 = models.BooleanField(default=False)
    notes9 = models.CharField(max_length=100, default="")
    Size_Options9 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color9 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options9 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options9 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE9 = models.BooleanField(default=False)
    GT9 = models.BooleanField(default=False)
    GR9 = models.BooleanField(default=False)
    B9 = models.BooleanField(default=False)

    #-10-

    quantity10 = models.FloatField(null=True, blank=True)
    width10 = models.FloatField(null=True, blank=True)
    height10 = models.FloatField(null=True, blank=True)
    tempgl10 = models.BooleanField(default=False)
    unit_price10 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount10 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type10 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h10 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb10 = models.BooleanField(default=False)
    notes10 = models.CharField(max_length=100, default="")
    Size_Options10 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color10 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options10 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options10 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE10 = models.BooleanField(default=False)
    GT10 = models.BooleanField(default=False)
    GR10 = models.BooleanField(default=False)
    B10 = models.BooleanField(default=False)

    #-11-

    quantity11 = models.FloatField(null=True, blank=True)
    width11 = models.FloatField(null=True, blank=True)
    height11 = models.FloatField(null=True, blank=True)
    tempgl11 = models.BooleanField(default=False)
    unit_price11 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount11 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type11 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h11 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb11 = models.BooleanField(default=False)
    notes11 = models.CharField(max_length=100, default="")
    Size_Options11 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color11 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options11 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options11 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE11 = models.BooleanField(default=False)
    GT11 = models.BooleanField(default=False)
    GR11 = models.BooleanField(default=False)
    B11 = models.BooleanField(default=False)

    #-12-

    quantity12 = models.FloatField(null=True, blank=True)
    width12 = models.FloatField(null=True, blank=True)
    height12 = models.FloatField(null=True, blank=True)
    tempgl12 = models.BooleanField(default=False)
    unit_price12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount12 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    window_type12 = models.CharField(max_length=50, choices=WINDOW_TYPE_CHOICES, default='none')
    h12 = models.CharField(max_length=50, choices=HAND_OPTIONS, null=True, blank=True)
    bnb12 = models.BooleanField(default=False)
    notes12 = models.CharField(max_length=100, default="")
    Size_Options12 = models.CharField(max_length=50, choices=SIZE_OPTIONS, blank=True, null=True)
    color12 = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    Frame_Options12 = models.CharField(max_length=50, choices=FRAME_OPTIONS, blank=True, null=True)
    Grille_Options12 = models.CharField(max_length=50, choices=GRILLE_OPTIONS, blank=True, null=True)
    LE12 = models.BooleanField(default=False)
    GT12 = models.BooleanField(default=False)
    GR12 = models.BooleanField(default=False)
    B12 = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
