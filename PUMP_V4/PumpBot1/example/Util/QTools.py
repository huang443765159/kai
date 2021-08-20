from platform import system
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QAbstractItemView, QHeaderView, QTableWidgetItem
from PyQt5.QtGui import QPalette, QColor


LED_COLORS = {

    'DARK_GREEN': (0, 100, 0),
    'GREEN': (0, 255, 0),
    'YELLOW': (255, 255, 0),
    'RED': (255, 0, 0),
    'GRAY': (100, 100, 100),
}


def font_size_auto_adapt(qt_ui):  # 字号自适应:保证Mac和Linux端一致
    def refresh_font_size(widget, offset):
        if 'font' in dir(widget):
            font = widget.font()
            size = font.pointSizeF()
            if size > 0:
                font.setPixelSize(size + offset)
                widget.setFont(font)
        for sub_widget in widget.children():
            refresh_font_size(sub_widget, offset)
    refresh_font_size(widget=qt_ui.centralwidget, offset=0 if system() == 'Darwin' else 0.9)


def get_default_palette():
    palette = QPalette()
    # BASE
    # palette.setColor(QPalette.Background, QColor(255, 255, 255))
    palette.setColor(QPalette.WindowText, QColor(180, 180, 180))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.Light, QColor(180, 180, 180))
    palette.setColor(QPalette.Midlight, QColor(90, 90, 90))
    palette.setColor(QPalette.Dark, QColor(35, 35, 35))
    palette.setColor(QPalette.Text, QColor(180, 180, 180))
    palette.setColor(QPalette.BrightText, QColor(180, 180, 180))
    palette.setColor(QPalette.ButtonText, QColor(180, 180, 180))
    palette.setColor(QPalette.Base, QColor(42, 42, 42))
    # palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.Window, QColor(53, 53, 53, 90))
    palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    palette.setColor(QPalette.Highlight, QColor(90, 90, 90))  # 表格选中背景颜色
    palette.setColor(QPalette.HighlightedText, QColor(180, 180, 180))  # 表格选中字体颜色
    palette.setColor(QPalette.Link, QColor(56, 252, 196))
    palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    palette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipText, QColor(180, 180, 180))
    # DISABLED
    palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
    palette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
    palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
    palette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
    palette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
    return palette


def table_init(table, column_width_list=(), select_as_columns=False, no_edit=False):
    class AlignDelegate(QStyledItemDelegate):
        def initStyleOption(self, option, index):
            super(AlignDelegate, self).initStyleOption(option, index)
            option.displayAlignment = Qt.AlignCenter
    delegate = AlignDelegate(table)
    # COLUMN_WIDTH
    if column_width_list:
        for i in range(len(column_width_list)):
            table.setColumnWidth(i, column_width_list[i])
            table.setItemDelegateForColumn(i, delegate)
    else:
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应高度
        for i in range(table.columnCount()):
            table.setItemDelegateForColumn(i, delegate)  # 居中
    # SELECT_TYPE
    if select_as_columns:  # 整列选中
        table.setSelectionBehavior(QAbstractItemView.SelectColumns)
    # EDITABLE
    if no_edit:
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止修改表格
    # ITEM
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item is None:
                item = QTableWidgetItem()
                item.setText('')
                table.setItem(row, col, item)


def set_led_style(ui_btn, color: str, text_color='black', alpha=0.5):
    rgb = LED_COLORS[color.upper()]
    rgba = 'rgba({:.0f}, {:.0f}, {:.0f}, {:.0%})'.format(rgb[0], rgb[1], rgb[2], alpha)
    color_sheet = 'QToolButton {background-color: ' + rgba + '; border: none; color: ' + text_color + ';}'
    ui_btn.setStyleSheet(color_sheet)
