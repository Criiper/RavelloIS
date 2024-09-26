BACKGROUND = "#463353"
LIGHT_BACKGROUND = '#6c4068'
COMPONENT = "#a75f84"
HOVER = "#f289a7"
HIGHLIGHT = '#f8babe'

BUTTON = {"height" : 80,
         "anchor": "center",
         "compound" : "left",
         "background" : COMPONENT,
         "foreground" : "WHITE",
         "activebackground" : HOVER,
         "activeforeground" : "WHITE",
         "highlightbackground" : HOVER,
         "highlightcolor" : "WHITE",
         "highlightthickness" : 2,
         "border" : 0,
         "font" : ("Abhadi", 18),
         "cursor" : "hand1"
}

BUTTON_H = {"height" : 1,
         "anchor": "center",
         "compound" : "left",
         "background" : COMPONENT,
         "foreground" : "WHITE",
         "activebackground" : HOVER,
         "activeforeground" : "WHITE",
         "highlightbackground" : HOVER,
         "highlightcolor" : "WHITE",
         "highlightthickness" : 2,
         "border" : 0,
         "font" : ("Abhadi", 12),
         "cursor" : "hand1"
}

LABEL = {
      'font' : ('Abhadi', 12),
      'background' : '#a75f84',
      'foreground' : "WHITE"
}

def on_enter(e):
  e.widget['background'] = HOVER

def on_leave(e):
  e.widget['background'] = COMPONENT