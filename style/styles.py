BACKGROUND = "#463353"
LIGHT_BACKGROUND = '#6c4068'
BUTTON = "#a75f84"
HOVER_BUTTON = "#f289a7"
HIGHLIGHT = '#f8babe'

BOTON = {"height" : 80,
         "anchor": "center",
         "compound" : "left",
         "background" : BUTTON,
         "foreground" : "WHITE",
         "activebackground" : HOVER_BUTTON,
         "activeforeground" : "WHITE",
         "highlightbackground" : HOVER_BUTTON,
         "highlightcolor" : "WHITE",
         "highlightthickness" : 2,
         "border" : 0,
         "font" : ("Abhadi", 18),
         "cursor" : "hand1"
}

LABEL = {
      'font' : ('Abhadi', 12),
      'background' : '#500400',
      'foreground' : "WHITE"
}

def on_enter(e):
  e.widget['background'] = HOVER_BUTTON

def on_leave(e):
  e.widget['background'] = BUTTON