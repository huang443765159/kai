from typing import Union
from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QCheckBox, QRadioButton, QLabel
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QStyledItemDelegate, QHeaderView, QAbstractItemView
from PyQt5.QtCore import Qt


def list_to_str(_list: list) -> str:
    result = str([float('%.4f' % num) for num in _list])
    return result


def set_item_without_sign(
        ui_item: Union[QSpinBox, QDoubleSpinBox, QCheckBox, QRadioButton],
        val: Union[float, bool],
        ena: bool = True):

    ui_item.blockSignals(True)
    if ui_item.__class__ in [QSpinBox, QDoubleSpinBox]:
        ui_item.setValue(val)
    elif ui_item.__class__ in [QCheckBox]:
        ui_item: QCheckBox
        ui_item.setChecked(2 if val else 0)
    elif ui_item.__class__ in [QRadioButton]:
        ui_item: QRadioButton
        ui_item.setChecked(2 if val else 0)
    else:
        pass
        # msg(level=LEVEL.ERROR, info=f'NOT_SUPPORT_CLASS={ui_item.__class__}')
    ui_item.setEnabled(ena)
    ui_item.blockSignals(False)


def set_label_light(ui_item: QLabel, switch: bool):
    color = [0, 255, 0] if switch else [200, 200, 200]
    sheet = f"""
                QLabel
                {{
                    color: rgb({color[0]}, {color[1]}, {color[2]});
                 }} """
    ui_item.setStyleSheet(sheet)


# LED
def set_led_style(ui_btn, color: list, text_color='black', alpha=0.5):
    rgba = 'rgba({:.0f}, {:.0f}, {:.0f}, {:.0%})'.format(color[0], color[1], color[2], alpha)
    color_sheet = 'QToolButton {background-color: ' + rgba + '; border: none; color: ' + text_color + ';}'
    ui_btn.setStyleSheet(color_sheet)


def table_init(table: QTableWidget, column_width_list=(), no_edit=False):
    class AlignDelegate(QStyledItemDelegate):
        def initStyleOption(self, option, index):
            super(AlignDelegate, self).initStyleOption(option, index)
            option.displayAlignment = Qt.AlignCenter
    delegate = AlignDelegate(table)
    if column_width_list:
        for i in range(len(column_width_list)):
            table.setColumnWidth(i, column_width_list[i])
    for i in range(table.columnCount()):
        table.setItemDelegateForColumn(i, delegate)  # 居中
    table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应高度
    if no_edit:
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止修改表格
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item is None:
                item = QTableWidgetItem()
                table.setItem(row, col, item)
            item.setText('-')
