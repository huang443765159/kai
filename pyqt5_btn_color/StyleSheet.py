
# LED
def set_led_style(ui_btn, color: list, text_color='black', alpha=0.5):
    rgba = 'rgba({:.0f}, {:.0f}, {:.0f}, {:.0%})'.format(color[0], color[1], color[2], alpha)
    color_sheet = 'QToolButton {background-color: ' + rgba + '; border: none; color: ' + text_color + ';}'
    ui_btn.setStyleSheet(color_sheet)
