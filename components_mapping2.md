# PySide6 和 PyQt-Fluent-Widgets 组件对照表（包含简化的自定义函数）

## 输入组件
| PySide6 组件名        | PyQt-Fluent-Widgets 组件名                       | 简要描述                       |
|-----------------------|-------------------------------------------------|--------------------------------|
| `QPushButton`         | [PushButton](#pushbutton)                       | 标准按钮组件                   |
| `QPushButton`         | [PrimaryPushButton](#primarypushbutton)         | 主题色按钮组件                 |
| `QPushButton`         | [TransparentPushButton](#transparentpushbutton) | 透明按钮组件                   |
| `QToolButton`         | [ToolButton](#toolbutton)                       | 工具按钮组件，只显示图标       |
| `QToolButton`         | [PrimaryToolButton](#primarytoolbutton)         | 主题色工具按钮组件             |
| `QToolButton`         | [TransparentToolButton](#transparenttoolbutton) | 透明工具按钮组件               |
| `QPushButton`         | [TogglePushButton](#togglepushbutton)           | 切换按钮组件                   |
| `QToolButton`         | [ToggleToolButton](#toggletoolbutton)           | 工具切换按钮组件               |
| `QPushButton`         | [TransparentTogglePushButton](#transparenttogglepushbutton) | 透明切换按钮组件     |
| `QToolButton`         | [TransparentToggleToolButton](#transparenttoggletoolbutton) | 透明工具切换按钮组件 |
| `QPushButton`         | [PillPushButton](#pillpushbutton)               | 圆形标签或过滤器按钮组件       |
| `QToolButton`         | [PillToolButton](#pilltoolbutton)               | 只显示图标的圆形标签或过滤器按钮 |
| `QPushButton`         | [DropDownPushButton](#dropdownpushbutton)       | 下拉菜单按钮组件               |
| `QToolButton`         | [DropDownToolButton](#dropdowntoolbutton)       | 下拉菜单工具按钮组件           |
| `QPushButton`         | [PrimaryDropDownPushButton](#primarydropdownpushbutton) | 主题色下拉菜单按钮组件   |
| `QToolButton`         | [PrimaryDropDownToolButton](#primarydropdowntoolbutton) | 主题色下拉菜单工具按钮组件 |
| `QPushButton`         | [TransparentDropDownPushButton](#transparentdropdownpushbutton) | 透明下拉菜单按钮组件 |
| `QToolButton`         | [TransparentDropDownToolButton](#transparentdropdowntoolbutton) | 透明下拉菜单工具按钮组件 |
| `QPushButton`         | [SplitPushButton](#splitpushbutton)             | 拆分按钮组件                   |
| `QToolButton`         | [SplitToolButton](#splittoolbutton)             | 拆分工具按钮组件               |
| `QPushButton`         | [PrimarySplitPushButton](#primarysplitpushbutton) | 主题色拆分按钮组件           |
| `QToolButton`         | [PrimarySplitToolButton](#primarysplittoolbutton) | 主题色拆分工具按钮组件       |
| `QCheckBox`           | [CheckBox](#checkbox)                   | 多选复选框组件                 |
| `QComboBox`           | [ComboBox](#combobox)                   | 下拉框组件，用于展示和选择内容 |
| `QComboBox`           | [EditableComboBox](#editablecombobox)   | 可编辑的下拉框组件             |
| `QRadioButton`        | [RadioButton](#radiobutton)             | 单选按钮组件                   |
| `QSlider`             | [Slider](#slider)                      | 滑动条组件，用于在固定区间内选择值 |
| `QCheckBox` (Toggle)  | [SwitchButton](#switchbutton)           | 开关按钮组件，用于在两种状态间切换 |
| 无直接替代           | [IconWidget](#iconwidget)               | 图标组件，用于显示图标          |

## 日期时间组件
| PySide6 组件名        | PyQt-Fluent-Widgets 组件名                       | 简要描述                       |
|-----------------------|-----------------------------------------|--------------------------------|
| `QDateEdit`           | [DatePicker](#datepicker)               | 日期选择组件                   |
| `QTimeEdit`           | [TimePicker](#timepicker)               | 时间选择组件（24小时制）        |
| `QDateEdit` + `QCalendarWidget` | [CalendarPicker](#calendarpicker) | 日历日期选择组件              |

## 对话框组件  
| PySide6 组件名        | PyQt-Fluent-Widgets 组件名               | 简要描述                       |
|-----------------------|-----------------------------------------|--------------------------------|
| `QDialog`             | [Dialog](#dialog)                       | 模态无边框对话框                |
| `QMessageBox`         | [MessageBox](#messagebox)               | 模态遮罩对话框                 |
| 自定义实现           | [MessageBoxBase](#messageboxbase)        | 基于 MessageBox 的自定义对话框 |
| `QColorDialog`        | [ColorDialog](#colordialog)             | 颜色选择对话框                 |
| `QDialog` 或自定义  | [Flyout](#flyout)                       | 可关闭的弹出窗口               |
| 自定义实现           | [FlyoutViewBase](#customflyout)          | 自定义弹出窗口内容的基础类     |
| `QDialog` 或自定义  | [TeachingTip](#teachingtip)             | 教学提示气泡弹窗               |

## 布局组件
| PySide6 组件名        | PyQt-Fluent-Widgets 组件名               | 简要描述                       |
|-----------------------|-----------------------------------------|--------------------------------|
| `QVBoxLayout`, `QHBoxLayout` | [FlowLayout](#flowlayout)      | 自适应宽度的流式布局             |
| `QGroupBox`           | [HeaderCardWidget](#headercardwidget)    | 带标题的卡片组件，可替代 QGroupBox  |
| 自定义实现           | [CardWidget](#cardwidget)                | 灵活的卡片组件                   |
| 自定义实现           | [SimpleCardWidget](#simplecardwidget)     | 背景不变的简单卡片组件            |
| 自定义实现           | [ElevatedCardWidget](#elevatedcardwidget) | 带阴影效果的卡片组件              |
| 自定义实现           | [GroupHeaderCardWidget](#groupheadercardwidget) | 带分组功能的卡片组件          |

## 菜单和工具栏组件
| PySide6 组件名        | PyQt-Fluent-Widgets 组件名               | 简要描述                         |
|-----------------------|-----------------------------------------|----------------------------------|
| `QMenu`               | [RoundMenu](#roundmenu)                 | 圆角菜单组件，类似于 QMenu      |
| `QMenu` + `QActionGroup` | [CheckableMenu](#checkablemenu)      | 支持勾选功能的菜单               |
| `QSystemTrayIcon`     | [SystemTrayMenu](#systemtraymenu)       | 系统托盘菜单组件                |
| 自定义实现           | [CommandBar](#commandbar)               | 水平排列的命令栏组件             |
| 自定义实现           | [CommandBarView](#commandbarview)       | 配合 Flyout 使用的命令栏视图组件 |



### 组件描述

---

#### **PushButton**

**PushButton** 是一个标准按钮组件，通常用于触发操作或提交表单。它是 `QPushButton` 的替代组件，并提供类似的接口。

**主要功能**：

- **替代组件**: `QPushButton`
- **主要接口**: `clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于几乎所有需要用户点击触发事件的场合，如提交表单、触发动作等。

**示例代码**：

```python
button = PushButton('Standard push button')
button.clicked.connect(lambda: print("Button clicked"))

# 带图标的按钮示例
button_with_icon = PushButton(FluentIcon.FOLDER, 'Standard push button with icon')
```

------

#### **PrimaryPushButton**

**PrimaryPushButton** 是一个主题色按钮组件，通常用于强调某种操作。它是 `QPushButton` 的增强版本。

**主要功能**：

- **替代组件**: `QPushButton`
- **主要接口**: `clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要用户特别注意或优先操作的按钮，如确认、提交等关键操作。

**示例代码**：

```python
primary_button = PrimaryPushButton('Accent style button')
primary_button.clicked.connect(lambda: print("Primary button clicked"))

# 带图标的主按钮
primary_button_with_icon = PrimaryPushButton(FluentIcon.UPDATE, 'Accent style button')
```

------

#### **TransparentPushButton**

**TransparentPushButton** 是一个透明按钮组件，通常用于不希望按钮背景显眼的场合，但仍需要用户点击。

**主要功能**：

- **替代组件**: `QPushButton`
- **主要接口**: `clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于界面设计中需要按钮背景透明的场合，如图片上的按钮、文本叠加的按钮等。

**示例代码**：

```python
transparent_button = TransparentPushButton('Transparent push button')
transparent_button.clicked.connect(lambda: print("Transparent button clicked"))

# 带图标的透明按钮
transparent_button_with_icon = TransparentPushButton(FluentIcon.BOOK_SHELF, 'Transparent push button')
```

------

#### **ToolButton**

**ToolButton** 只用于显示图标，通常用于工具栏或其他只需要图标表示的场景。它是 `QToolButton` 的替代组件，并提供类似的接口。

**主要功能**：

- **替代组件**: `QToolButton`
- **主要接口**: `clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏、导航栏或任何只需要图标表示的按钮场合。

**示例代码**：

```python
tool_button = ToolButton(FluentIcon.SETTING)
tool_button.clicked.connect(lambda: print("Tool button clicked"))

# 使用自定义图标
tool_button_with_custom_icon = ToolButton(QIcon("/path/to/icon.png"))
```

------

#### **PrimaryToolButton**

**PrimaryToolButton** 只用于显示图标，是 `ToolButton` 的增强版本，适用于需要强调操作的工具栏按钮。

**主要功能**：

- **替代组件**: `QToolButton`
- **主要接口**: `clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要特别强调的工具栏按钮或导航按钮。

**示例代码**：

```python
primary_tool_button = PrimaryToolButton(FluentIcon.FOLDER)
primary_tool_button.clicked.connect(lambda: print("Primary tool button clicked"))

# 使用自定义图标
primary_tool_button_with_custom_icon = PrimaryToolButton(QIcon("/path/to/icon.png"))
```

------

#### **TransparentToolButton**

**TransparentToolButton** 是一个透明的工具按钮组件，通常用于不希望按钮背景显眼的工具栏场合。

**主要功能**：

- **替代组件**: `QToolButton`
- **主要接口**: `clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要背景透明的按钮。

**示例代码**：

```python
transparent_tool_button = TransparentToolButton(FluentIcon.MAIL)
transparent_tool_button.clicked.connect(lambda: print("Transparent tool button clicked"))

# 使用自定义图标
transparent_tool_button_with_custom_icon = TransparentToolButton(QIcon("/path/to/icon.png"))
```

------

#### **TogglePushButton**

**TogglePushButton** 是一个切换按钮组件，通常用于在启用和禁用状态之间进行切换。它是 `QPushButton` 的替代组件。

**主要功能**：

- **替代组件**: `QPushButton`
- **主要接口**: `toggled` 信号用于响应按钮状态改变事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要用户切换某种状态的场合，如启用/禁用功能。

**示例代码**：

```python
toggle_button = TogglePushButton('Toggle push button')
toggle_button.toggled.connect(lambda checked: print(f"Button is checked: {checked}"))

# 带图标的切换按钮
toggle_button_with_icon = TogglePushButton(FluentIcon.SEND, 'Toggle push button')
```

------

#### **ToggleToolButton**

**ToggleToolButton** 是一个工具切换按钮组件，通常用于在工具栏中实现启用和禁用状态之间的切换。它是 `QToolButton` 的替代组件。

**主要功能**：

- **替代组件**: `QToolButton`
- **主要接口**: `toggled` 信号用于响应按钮状态改变事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要切换状态的按钮。

**示例代码**：

```python
toggle_tool_button = ToggleToolButton(FluentIcon.GITHUB)
toggle_tool_button.toggled.connect(lambda checked: print(f"Tool button is checked: {checked}"))

# 使用自定义图标
toggle_tool_button_with_custom_icon = ToggleToolButton(QIcon("/path/to/icon.png"))
```

------

#### **TransparentTogglePushButton**

**TransparentTogglePushButton** 是一个透明的切换按钮组件，通常用于在启用和禁用状态之间进行切换，但不希望按钮背景显眼的场合。

**主要功能**：

- **替代组件**: `TogglePushButton`
- **主要接口**: `toggled` 信号用于响应按钮状态改变事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要背景透明的切换按钮场合。

**示例代码**：

```python
transparent_toggle_button = TransparentTogglePushButton('Transparent toggle button')
transparent_toggle_button.toggled.connect(lambda checked: print(f"Transparent button is checked: {checked}"))

# 带图标的透明切换按钮
transparent_toggle_button_with_icon = TransparentTogglePushButton(FluentIcon.BOOK_SHELF, 'Transparent toggle button')
```

------

#### **TransparentToggleToolButton**

**TransparentToggleToolButton** 是一个透明的工具切换按钮组件，通常用于在工具栏中实现启用和禁用状态之间的切换，同时不希望按钮背景显眼的场合。

**主要功能**：

- **替代组件**: `ToggleToolButton`
- **主要接口**: `toggled` 信号用于响应按钮状态改变事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要背景透明的切换按钮。

**示例代码**：

```python
transparent_toggle_tool_button = TransparentToggleToolButton(FluentIcon.GITHUB)
transparent_toggle_tool_button.toggled.connect(lambda checked: print(f"Transparent tool button is checked: {checked}"))

# 使用自定义图标
transparent_toggle_tool_button_with_custom_icon = TransparentToggleToolButton(QIcon("/path/to/icon.png"))
```

------

#### **PillPushButton**

**PillPushButton** 是一个圆形标签或过滤器按钮组件，通常用于显示文本和图标，类似于 `TogglePushButton`。

**主要功能**：

- **替代组件**: `TogglePushButton`
- **主要接口**: `toggled` 信号用于响应按钮状态改变事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于标签或过滤器功能的按钮，如选项卡或筛选条件。

**示例代码**：

```python
pill_button = PillPushButton('Pill push button')
pill_button.toggled.connect(lambda checked: print(f"Pill button is checked: {checked}"))

# 带图标的圆形标签按钮
pill_button_with_icon = PillPushButton(FluentIcon.CALENDAR, 'Pill push button')
```

------

#### **PillToolButton**

**PillToolButton** 是一个圆形标签或过滤器工具按钮组件，通常只用于显示图标，类似于 `ToggleToolButton`。

**主要功能**：

- **替代组件**: `ToggleToolButton`
- **主要接口**: `toggled` 信号用于响应按钮状态改变事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于标签或过滤器功能的工具按钮。

**示例代码**：

```python
pill_tool_button = PillToolButton(FluentIcon.GITHUB)
pill_tool_button.toggled.connect(lambda checked: print(f"Pill tool button is checked: {checked}"))

# 使用自定义图标
pill_tool_button_with_custom_icon = PillToolButton(QIcon("/path/to/icon.png"))
```

------

#### **DropDownPushButton**

**DropDownPushButton** 是一个下拉菜单按钮组件，点击时可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setMenu()` 设置下拉菜单，`clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要弹出下拉菜单的场合，如选项列表或快捷操作。

**示例代码**：

```python
dropdown_button = DropDownPushButton(FluentIcon.MAIL, 'Email')

# 创建菜单
menu = RoundMenu(parent=dropdown_button)
menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("你干嘛~")))
menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("喜欢唱跳RAP")))
menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("只因你太美")))

# 添加菜单
dropdown_button.setMenu(menu)
```

------

#### **DropDownToolButton**

**DropDownToolButton** 是一个下拉菜单工具按钮组件，点击时可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setMenu()` 设置下拉菜单，`clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要弹出下拉菜单的按钮。

**示例代码**：

```python
dropdown_tool_button = DropDownToolButton(FluentIcon.MAIL)

# 创建菜单
menu = RoundMenu(parent=dropdown_tool_button)
menu.addAction(Action(FluentIcon.SEND_FIL, 'Send', triggered=lambda: print("已发送")))
menu.addAction(Action(FluentIcon.SAVE, 'Save', triggered=lambda: print("已保存")))

# 添加菜单
dropdown_tool_button.setMenu(menu)
```

------

#### **PrimaryDropDownPushButton**

**PrimaryDropDownPushButton** 是一个主题色下拉菜单按钮组件，点击时可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setMenu()` 设置下拉菜单，`clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要特别强调且弹出下拉菜单的场合。

**示例代码**：

```python
primary_dropdown_button = PrimaryDropDownPushButton(FluentIcon.MAIL, 'Email')

# 创建菜单
menu = RoundMenu(parent=primary_dropdown_button)
menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("你干嘛~")))
menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("喜欢唱跳RAP")))
menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("只因你太美")))

# 添加菜单
primary_dropdown_button.setMenu(menu)
```

------

#### **PrimaryDropDownToolButton**

**PrimaryDropDownToolButton** 是一个主题色下拉菜单工具按钮组件，点击时可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setMenu()` 设置下拉菜单，`clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要特别强调且弹出下拉菜单的按钮。

**示例代码**：

```python
primary_dropdown_tool_button = PrimaryDropDownToolButton(FluentIcon.MAIL, 'Email')

# 创建菜单
menu = RoundMenu(parent=primary_dropdown_tool_button)
menu.addAction(Action(FluentIcon.SEND_FIL, 'Send', triggered=lambda: print("已发送")))
menu.addAction(Action(FluentIcon.SAVE, 'Save', triggered=lambda: print("已保存")))

# 添加菜单
primary_dropdown_tool_button.setMenu(menu)
```

------

#### **TransparentDropDownPushButton**

**TransparentDropDownPushButton** 是一个透明下拉菜单按钮组件，点击时可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setMenu()` 设置下拉菜单，`clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要背景透明且弹出下拉菜单的场合。

**示例代码**：

```python
transparent_dropdown_button = TransparentDropDownPushButton(FluentIcon.MAIL, 'Email')

# 创建菜单
menu = RoundMenu(parent=transparent_dropdown_button)
menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("你干嘛~")))
menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("喜欢唱跳RAP")))
menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("只因你太美")))

# 添加菜单
transparent_dropdown_button.setMenu(menu)
```

------

#### **TransparentDropDownToolButton**

**TransparentDropDownToolButton** 是一个透明下拉菜单工具按钮组件，点击时可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setMenu()` 设置下拉菜单，`clicked` 信号用于响应按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要背景透明且弹出下拉菜单的按钮。

**示例代码**：

```python
transparent_dropdown_tool_button = TransparentDropDownToolButton(FluentIcon.MAIL)

# 创建菜单
menu = RoundMenu(parent=transparent_dropdown_tool_button)
menu.addAction(Action(FluentIcon.SEND_FIL, 'Send', triggered=lambda: print("已发送")))
menu.addAction(Action(FluentIcon.SAVE, 'Save', triggered=lambda: print("已保存")))

# 添加菜单
transparent_dropdown_tool_button.setMenu(menu)
```

------

#### **SplitPushButton**

**SplitPushButton** 是一个拆分按钮组件，由两个按钮组成，点击左侧按钮会触发 `clicked` 信号，点击右侧按钮可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setFlyout()` 设置右侧按钮的下拉菜单，`clicked` 信号用于响应左侧按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要同时提供主操作和辅助操作的场合，如常用操作和更多选项。

**示例代码**：

```python
split_button = SplitPushButton(FluentIcon.GITHUB, 'Split push button')
split_button.clicked.connect(lambda: print("点击左侧按钮"))

# 创建菜单
menu = RoundMenu(parent=split_button)
menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("你干嘛~")))
menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("喜欢唱跳RAP")))
menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("只因你太美")))

# 添加菜单
split_button.setFlyout(menu)
```

------

#### **SplitToolButton**

**SplitToolButton** 是一个拆分工具按钮组件，由两个按钮组成，点击左侧按钮会触发 `clicked` 信号，点击右侧按钮可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setFlyout()` 设置右侧按钮的下拉菜单，`clicked` 信号用于响应左侧按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要同时提供主操作和辅助操作的场合。

**示例代码**：

```python
split_tool_button = SplitToolButton(FluentIcon.MAIL)
split_tool_button.clicked.connect(lambda: print("点击左侧按钮"))

# 创建菜单
menu = RoundMenu(parent=split_tool_button)
menu.addAction(Action(FluentIcon.SEND_FIL, 'Send', triggered=lambda: print("已发送")))
menu.addAction(Action(FluentIcon.SAVE, 'Save', triggered=lambda: print("已保存")))

# 添加菜单
split_tool_button.setFlyout(menu)
```

------

#### **PrimarySplitPushButton**

**PrimarySplitPushButton** 是一个主题色拆分按钮组件，由两个按钮组成，点击左侧按钮会触发 `clicked` 信号，点击右侧按钮可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setFlyout()` 设置右侧按钮的下拉菜单，`clicked` 信号用于响应左侧按钮点击事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setIcon()` 用于设置按钮的图标。

**应用场景**：适用于需要特别强调且同时提供主操作和辅助操作的场合。

**示例代码**：

```python
primary_split_button = PrimarySplitPushButton(FluentIcon.GITHUB, 'Split push button')
primary_split_button.clicked.connect(lambda: print("点击左侧按钮"))

# 创建菜单
menu = RoundMenu(parent=primary_split_button)
menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("你干嘛~")))
menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("喜欢唱跳RAP")))
menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("只因你太美")))

# 添加菜单
primary_split_button.setFlyout(menu)
```

------

#### **PrimarySplitToolButton**

**PrimarySplitToolButton** 是一个主题色拆分工具按钮组件，由两个按钮组成，点击左侧按钮会触发 `clicked` 信号，点击右侧按钮可弹出下拉菜单。下拉菜单必须是 `RoundMenu` 及其子类。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setFlyout()` 设置右侧按钮的下拉菜单，`clicked` 信号用于响应左侧按钮点击事件。
- **自定义样式**: `setIcon()` 用于设置按钮的图标。

**应用场景**：适用于工具栏中需要特别强调且同时提供主操作和辅助操作的场合。

**示例代码**：

```python
primary_split_tool_button = PrimarySplitToolButton(FluentIcon.MAIL)
primary_split_tool_button.clicked.connect(lambda: print("点击左侧按钮"))

# 创建菜单
menu = RoundMenu(parent=primary_split_tool_button)
menu.addAction(Action(FluentIcon.SEND_FIL, 'Send', triggered=lambda: print("已发送")))
menu.addAction(Action(FluentIcon.SAVE, 'Save', triggered=lambda: print("已保存")))

# 添加菜单
primary_split_tool_button.setFlyout(menu)
```

------

#### **CheckBox**

**CheckBox** 是一个多选复选框组件，通常用于在一组备选项中进行多选。它是 `QCheckBox` 的替代组件，并提供类似的接口。

**主要功能**：

- **替代组件**: `QCheckBox`
- **主要接口**: `stateChanged` 信号用于响应复选框状态改变事件。
- **自定义样式**: `setText()` 用于设置复选框的文本，`setChecked()` 用于设置复选框的选中状态。

**应用场景**：适用于需要用户在一组选项中进行多选的场合，如表单选项、设置项等。

**支持三态**：CheckBox 同样支持三态模式，通过 `setTristate(True)` 启用三态，并使用 `setCheckState(Qt.PartiallyChecked)` 设置部分选中的状态。

**示例代码**：

```python
checkBox = CheckBox("Text")

# 选中复选框
checkBox.setChecked(True)

# 监听复选框状态改变信号
checkBox.stateChanged.connect(lambda: print(checkBox.isChecked()))

# 启用三态并设置为部分选中
checkBox.setTristate(True)
checkBox.setCheckState(Qt.PartiallyChecked)
```

------

#### **ComboBox**

**ComboBox** 是一个用于展示和选择内容的下拉框组件，通常用于选项过多时使用。它继承自 `PushButton`，重新实现了 `QComboBox` 的大部分接口，但无法在 Designer 中添加选项。

**主要功能**：

- **替代组件**: `QComboBox`
- **主要接口**: `currentIndexChanged` 信号用于响应选项改变事件，`addItems()` 和 `addItem()` 用于添加选项。
- **自定义样式**: `setText()` 用于设置下拉框的提示文本，`setPlaceholderText()` 用于设置未选中状态的提示文本。

**应用场景**：适用于需要用户从大量选项中选择一个的场合，如表单选择、设置选项等。

**支持绑定数据**：每个选项都可以绑定数据，通过 `addItem()` 添加选项时传入 `userData`，然后通过 `itemData()` 获取绑定的数据。

**示例代码**：

```python
comboBox = ComboBox()

# 添加选项
items = ['shoko', '西宫硝子', '宝多六花', '小鸟游六花']
comboBox.addItems(items)

# 当前选项的索引改变信号
comboBox.currentIndexChanged.connect(lambda index: print(comboBox.currentText()))

# 每个选项绑定数据
comboBox.addItem('leetcode', userData="剑指 Offer")
print(comboBox.itemData(4))  # 输出 "剑指 Offer"

# 设置提示文本和取消选中
comboBox.setPlaceholderText("选择一个脑婆")
comboBox.setCurrentIndex(-1)
```

------

#### **EditableComboBox**

**EditableComboBox** 是一个可编辑的下拉框组件，允许用户编辑当前选项，并按下回车时添加新选项。它继承自 `LineEdit`，同样无法在 Designer 中添加选项。

**主要功能**：

- **替代组件**: `QComboBox`
- **主要接口**: `currentIndexChanged` 信号用于响应选项改变事件，`addItems()` 和 `addItem()` 用于添加选项，`setCompleter()` 用于设置补全提示。
- **自定义样式**: `setText()` 用于设置下拉框的提示文本，`setPlaceholderText()` 用于设置未选中状态的提示文本。

**应用场景**：适用于需要用户输入自定义选项或从建议列表中选择的场合，如搜索框、动态表单等。

**支持补全提示**：可以通过设置补全器 (`QCompleter`) 来提供输入时的建议。

**示例代码**：

```python
comboBox = EditableComboBox()

# 添加选项
items = ['shoko', '西宫硝子', '宝多六花', '小鸟游六花']
comboBox.addItems(items)

# 当前选项的索引改变信号
comboBox.currentIndexChanged.connect(lambda index: print(comboBox.currentText()))

# 设置补全提示
completer = QCompleter(items, comboBox)
completer.setMaxVisibleItems(10)
comboBox.setCompleter(completer)
```

------

#### **RadioButton**

**RadioButton** 是一个用于在一组备选项中进行单选的按钮组件，通常与 `QButtonGroup` 组合使用。它是 `QRadioButton` 的替代组件，并提供类似的接口。

**主要功能**：

- **替代组件**: `QRadioButton`
- **主要接口**: `toggled` 信号用于响应按钮选中状态改变事件。
- **自定义样式**: `setText()` 用于设置按钮的文本，`setChecked()` 用于设置按钮的选中状态。

**应用场景**：适用于需要用户在多个选项中进行单选的场合，如表单、选项设置等。

**示例代码**：

```python
w = QWidget()

button1 = RadioButton('Option 1')
button2 = RadioButton('Option 2')
button3 = RadioButton('Option 3')

# 将单选按钮添加到互斥的按钮组
buttonGroup = QButtonGroup(w)
buttonGroup.addButton(button1)
buttonGroup.addButton(button2)
buttonGroup.addButton(button3)

# 当前选中的按钮发生改变
buttonGroup.buttonToggled.connect(lambda button: print(button.text()))

# 选中第一个按钮
button1.setChecked(True)

# 将按钮添加到垂直布局
layout = QVBoxLayout(w)
layout.addWidget(button1, 0, Qt.AlignCenter)
layout.addWidget(button2, 0, Qt.AlignCenter)
layout.addWidget(button3, 0, Qt.AlignCenter)
```

------·

#### **Slider**

**Slider** 是一个滑动条组件，通常用于在一个固定区间内选择值。它是 `QSlider` 的替代组件，并提供类似的接口。

**主要功能**：

- **替代组件**: `QSlider`
- **主要接口**: `valueChanged` 信号用于响应滑动条的数值改变事件。
- **自定义样式**: `setRange()` 用于设置滑动条的取值范围，`setValue()` 用于设置当前值。

**应用场景**：适用于需要用户选择一个范围内数值的场合，如音量控制、进度条等。

**示例代码**：

水平滑动条：

```python
slider = Slider(Qt.Horizontal)
slider.setFixedWidth(200)

# 设置取值范围和当前值
slider.setRange(0, 50)
slider.setValue(20)

# 获取当前值
print(slider.value())
```

垂直滑动条：

```python
python复制代码slider_vertical = Slider(Qt.Vertical)
slider_vertical.setRange(0, 100)
slider_vertical.setValue(40)
```

------

#### **SwitchButton**

**SwitchButton** 是一个开关按钮组件，表示两种相互对立的状态间的切换，通常用于触发「开/关」操作。它是 `QCheckBox` 的替代组件，主要用于切换操作，并提供类似的接口。

**主要功能**：

- **替代组件**: `QCheckBox`（Toggle 模式）
- **主要接口**: `checkedChanged` 信号用于响应开关状态改变事件。
- **自定义样式**: `setChecked()` 用于设置按钮的当前状态，`isChecked()` 用于获取按钮是否处于选中状态，`setOffText()` 和 `setOnText()` 用于设置按钮的关闭和开启文本。

**应用场景**：适用于需要用户在两种状态之间进行切换的场合，如启用/禁用功能的设置开关。

**示例代码**：

```python
button = SwitchButton()

# 监听开关状态改变信号
button.checkedChanged.connect(lambda checked: print("是否选中按钮：", checked))

# 更改按钮状态
button.setChecked(True)

# 获取按钮是否选中
print(button.isChecked())

# 修改开关文本
button.setOffText("关闭")
button.setOnText("开启")
```

------

#### **IconWidget**

**IconWidget** 是一个用于显示图标的组件，支持传入 `FluentIconBase`、`QIcon` 和 `str` 类型的图标。它没有直接对应的 PySide6 组件，是一个独特的图标展示组件。

**主要功能**：

- **替代组件**: 无直接替代
- **主要接口**: `setIcon()` 用于设置图标，支持 `FluentIconBase`、`QIcon` 和 `str` 类型的图标。
- **自定义样式**: `setFixedSize()` 用于调整图标组件的大小。

**应用场景**：适用于需要展示静态或动态图标的场合，如状态显示、导航图标等。

**示例代码**：

```python
# 创建一个图标组件并调整图标大小
w = IconWidget(FluentIcon.AIRPLANE)
w.setFixedSize(20, 20)

# 更换图标
# 类型为 FluentIconBase 子类
w.setIcon(InfoBarIcon.SUCCESS)
w.setIcon(FluentIcon.AIRPLANE.colored(Qt.red, Qt.blue))

# 类型为 QIcon
w.setIcon(QIcon("/path/to/icon"))

# 类型为 str，代表图标路径
w.setIcon("/path/to/icon")
```

------

#### **DatePicker**

**DatePicker** 是一个用于选择日期的组件，当选择的日期发生改变时，会发送 `dateChanged` 信号。它是 `QDateEdit` 的替代组件，提供更丰富的格式自定义功能。

**主要功能**：

- **替代组件**: `QDateEdit`
- **主要接口**: `dateChanged` 信号用于响应日期改变事件，`setDate()` 和 `date()` 用于设置和获取日期。
- **自定义样式**: 通过继承 `PickerColumnFormatter` 可以自定义日期选择器的列格式。

**应用场景**：适用于需要用户选择日期的场合，如表单日期输入、日程安排等。

**示例代码**：

```python
datePicker = DatePicker()

# 设置当前日期
datePicker.setDate(QDate(2024, 2, 26))

# 获取当前日期
print(datePicker.date)

# 日期发生改变
datePicker.dateChanged.connect(lambda date: print(date.toString()))

# 自定义日期选择器的月格式
class MonthFormatter(PickerColumnFormatter):
    """ Month formatter """

    def encode(self, value):
        # 此处 value 的取值范围为 1-12
        return str(value) + "😊"

    def decode(self, value: str):
        return int(value[:-1])

# 使用自定义的月格式（第一列）
datePicker.setColumnFormatter(0, MonthFormatter())
```

------

#### **TimePicker**

**TimePicker** 是一个用于选择24小时制时间的组件，当选择的时间发生改变时，会发送 `timeChanged` 信号。它是 `QTimeEdit` 的替代组件，并提供自定义格式的功能。

**主要功能**：

- **替代组件**: `QTimeEdit`
- **主要接口**: `timeChanged` 信号用于响应时间改变事件，`setTime()` 和 `time()` 用于设置和获取时间。
- **自定义样式**: 通过继承 `PickerColumnFormatter` 可以自定义时间选择器的列格式。

**应用场景**：适用于需要用户选择具体时间的场合，如表单时间输入、时间安排等。

**支持列的显示与隐藏**：可以通过 `setColumnVisible()` 方法显示或隐藏具体的时间列（小时、分钟、秒）。

**示例代码**：

```python
timePicker = TimePicker()

# 设置当前时间
timePicker.setTime(QTime(13, 53, 26))

# 获取当前时间
print(timePicker.time)

# 时间发生改变
timePicker.timeChanged.connect(lambda time: print(time.toString()))

# 自定义时间选择器的秒格式
class SecondsFormatter(PickerColumnFormatter):
    """ Seconds formatter """

    def encode(self, value):
        return str(value) + "秒"

    def decode(self, value: str):
        return int(value[:-1])

# 使用自定义的秒格式（第三列）
timePicker.setColumnFormatter(2, SecondsFormatter())

# 隐藏小时列，只显示分钟和秒
timePicker.setColumnVisible(0, False)
timePicker.setColumnVisible(1, True)
timePicker.setColumnVisible(2, True)
```

------

#### **CalendarPicker**

**CalendarPicker** 是一个日历日期选择组件，提供了更直观的日历界面供用户选择日期。它是 `QDateEdit` 与 `QCalendarWidget` 结合的替代组件，并提供日期格式设置功能。

**主要功能**：

- **替代组件**: `QDateEdit` + `QCalendarWidget`
- **主要接口**: `dateChanged` 信号用于响应日期改变事件，`setDate()` 和 `date()` 用于设置和获取日期。
- **自定义样式**: `setDateFormat()` 用于设置显示的日期格式。

**应用场景**：适用于需要用户通过直观日历选择日期的场合，如日期选择、日程安排等。

**示例代码**：

```python
calendarPicker = CalendarPicker()

# 设置当前日期
calendarPicker.setDate(QDate(2024, 2, 26))

# 获取当前日期
print(calendarPicker.date)

# 日期发生改变
calendarPicker.dateChanged.connect(lambda date: print(date.toString()))

# 设置日期格式
calendarPicker.setDateFormat(Qt.TextDate)
calendarPicker.setDateFormat('yyyy-M-d')
```

------

#### **Dialog**

**Dialog** 是一个模态无边框对话框组件，通常用于消息提示、确认消息和提交内容。与传统的 `QDialog` 相比，`Dialog` 会中断用户操作，直到用户确认知晓后才可关闭。

**主要功能**：

- **替代组件**: `QDialog`
- **主要接口**: `exec()` 方法用于显示对话框并等待用户响应，`setText()` 用于设置按钮的文本。
- **自定义样式**: `setTitle()` 用于设置对话框标题，`setText()` 用于修改按钮文本，`hide()` 用于隐藏按钮。

**应用场景**：适用于需要阻止用户操作并要求其做出确认或选择的场合，如删除确认、保存提示等。

**示例代码**：

```python
w = Dialog("标题", "这是一条消息通知", window)

if w.exec():
    print('确认')
else:
    print('取消')

# 修改按钮文本
w.yesButton.setText("来啦老弟")
w.cancelButton.setText("但是我拒绝")

# 隐藏确定按钮
w.yesButton.hide()
w.buttonLayout.insertStretch(0, 1)

# 隐藏取消按钮
w.cancelButton.hide()
w.buttonLayout.insertStretch(1)
```

------

#### **MessageBox**

**MessageBox** 是一个模态遮罩对话框，功能类似于 `QMessageBox`。使用时，最好将对话框的父级设置为主窗口，以确保遮罩的尺寸与主窗口保持一致。

**主要功能**：

- **替代组件**: `QMessageBox`
- **主要接口**: `exec()` 方法用于显示对话框并等待用户响应。
- **自定义样式**: `setTitle()` 用于设置对话框标题，`setText()` 用于修改按钮文本。

**应用场景**：适用于需要显示信息并等待用户确认的场合，如错误提示、信息确认等。

**示例代码**：

```python
w = MessageBox("标题", "这是一条消息通知", window)

if w.exec():
    print('确认')
else:
    print('取消')
```

------

#### **MessageBoxBase**

**MessageBoxBase** 是一个基于 `MessageBox` 的自定义对话框组件。通过继承 `MessageBoxBase` 并向 `viewLayout` 垂直布局中添加自定义组件，可以创建符合特定需求的对话框。这种灵活性使其适用于复杂场景，如输入表单或包含多个控件的对话框。

**主要功能**：

- **替代组件**: 无直接替代。

- 主要接口

  :

  - `exec()`：用于显示对话框并等待用户响应。
  - `viewLayout.addWidget()`：用于向对话框中添加自定义组件。

- 自定义样式

  :

  - 继承 `MessageBoxBase` 并在子类中添加自定义组件和布局。
  - `setMinimumWidth()`：用于设置对话框的最小宽度。

**应用场景**：适用于需要在对话框中包含复杂自定义内容的场合，例如包含多个输入框、选择器的高级对话框。

**示例代码**：

```python
class CustomMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL')
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)

def showMessage(window):
    w = CustomMessageBox(window)
    if w.exec():
        print(w.urlLineEdit.text())
```

------

#### **ColorDialog**

**ColorDialog** 是一个用于选择颜色的对话框组件。当用户选择的颜色发生变化时，会发送 `colorChanged(color: QColor)` 信号。它是 `QColorDialog` 的替代组件，并提供类似的接口。

**主要功能**：

- **替代组件**: `QColorDialog`
- **主要接口**: `colorChanged` 信号用于响应颜色改变事件，`exec()` 方法用于显示对话框并等待用户选择颜色。
- **自定义样式**: `setColor()` 用于设置初始颜色，`enableAlpha()` 用于启用或禁用透明度选择。

**应用场景**：适用于需要用户选择颜色的场合，如选择背景色、前景色或其他颜色属性。

**示例代码**：

```python
w = ColorDialog(QColor(0, 255, 255), "Choose Background Color", window, enableAlpha=False)
w.colorChanged.connect(lambda color: print(color.name()))
w.exec()
```

------

#### **Flyout**

**Flyout** 是一个可关闭的弹出窗口组件，可以收集用户的输入、显示项目的更多详细信息或要求用户确认操作。与对话框不同的是，`Flyout` 可以通过点击空白位置来轻松关闭。

**主要功能**：

- **替代组件**: `QDialog` 或自定义弹出组件
- **主要接口**: `Flyout.create()` 方法用于创建并显示弹出窗口，`Flyout.make()` 方法用于自定义弹出内容并显示。
- **自定义样式**: 支持添加图标、标题、内容、自定义组件等，并通过 `aniType` 设置动画类型。

**应用场景**：适用于需要展示详细信息或要求用户输入但不强制中断用户操作的场合，如轻量级的提示、快速操作确认等。

**示例代码**：

```python
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = PushButton("Click Me", self)
        self.button.clicked.connect(self.showFlyout)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.resize(600, 500)

    def showFlyout(self):
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title='Lesson 4',
            content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
            target=self.button,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP
        )

# 在弹出窗口中显示图片
Flyout.create(
    image="/path/to/image.png",
    title='Lesson 4',
    content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
    target=self.button,
    parent=self,
    isClosable=False
)

# 向弹出窗口中添加自定义组件
view = FlyoutView(
    title='Lesson 5',
    content="最短的捷径就是绕远路，绕远路才是我的最短捷径。",
    image='/path/to/image.png',
    isClosable=True
)

# 添加按钮
button = PushButton('Action')
button.setFixedWidth(120)
view.addWidget(button, align=Qt.AlignRight)

# 显示弹出窗口
w = Flyout.make(view, self.button, self)
view.closed.connect(w.close)
```

------

#### **FlyoutViewBase**

**FlyoutViewBase** 是 `Flyout` 的基础类，用于自定义弹出窗口的内容。通过继承 `FlyoutViewBase` 并向其中添加自定义组件，可以创建符合特定需求的弹出窗口。

**主要功能**：

- **替代组件**: 自定义弹出组件
- **主要接口**: 继承 `FlyoutViewBase` 并在子类中添加自定义布局和组件，`Flyout.make()` 方法用于显示自定义弹出窗口。
- **自定义样式**: 支持添加复杂布局和自定义内容，适用于需要高定制化的弹出窗口。

**应用场景**：适用于需要展示复杂自定义内容的弹出窗口场合，如详细操作提示、复杂信息输入等。

**示例代码**：

```python
class CustomFlyoutView(FlyoutViewBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = BodyLabel('这是一场「试炼」，我认为这就是一场为了战胜过去的「试炼」，\n只有战胜了那些幼稚的过去，人才能有所成长。')
        self.button = PrimaryPushButton('Action')

        self.button.setFixedWidth(140)

        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.button)

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = PushButton("Click Me", self)
        self.button.clicked.connect(self.showFlyout)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.resize(600, 500)

    def showFlyout(self):
        Flyout.make(CustomFlyoutView(), self.button, self)
```

------

#### **TeachingTip**

**TeachingTip** 是一个用于显示教学提示、信息或确认操作的气泡弹窗组件。与 `Flyout` 类似，`TeachingTip` 可以包含图标、标题、内容以及自定义组件，并且支持自动消失功能。

**主要功能**：

- **替代组件**: `QDialog` 或自定义弹出组件
- **主要接口**: `TeachingTip.create()` 方法用于创建并显示气泡弹窗，`TeachingTip.make()` 方法用于自定义内容并显示。
- **自定义样式**: 支持设置图标、标题、内容、自动消失时间等，并可添加自定义组件。

**应用场景**：适用于需要轻量级提示、快速信息展示或简单确认操作的场合，如操作引导、提示信息等。

**示例代码**：

```python
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = PushButton("Click Me", self)
        self.button.clicked.connect(self.showTeachingTip)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.resize(600, 500)

    def showTeachingTip(self):
        TeachingTip.create(
            target=self.button,
            icon=InfoBarIcon.SUCCESS,
            title='Lesson 4',
            content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
            isClosable=True,
            tailPosition=TeachingTipTailPosition.BOTTOM,
            duration=2000,
            parent=self
        )

# 在气泡弹窗中显示图片
TeachingTip.create(
    target=self.button,
    image="/path/to/image.png",
    title='Lesson 4',
    content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
    isClosable=True,
    tailPosition=TeachingTipTailPosition.BOTTOM,
    duration=2000,
    parent=self
)

# 在气泡弹窗中添加自定义组件
position = TeachingTipTailPosition.BOTTOM
view = TeachingTipView(
    icon=None,
    title='Lesson 5',
    content="最短的捷径就是绕远路，绕远路才是我的最短捷径。",
    image='/path/to/image.png',
    isClosable=True,
    tailPosition=position,
)

# 添加组件
button = PushButton('Action')
button.setFixedWidth(120)
view.addWidget(button, align=Qt.AlignRight)

w = TeachingTip.make(
    target=self.button,
    view=view,
    duration=-1,    # 关闭自动消失
    tailPosition=position,
    parent=self
)
view.closed.connect(w.close)
```

------

#### **CustomTeachingTip**

**CustomTeachingTip** 是 `TeachingTip` 的一个扩展应用，允许将内部的 `bubble.view` 替换为 `FlyoutViewBase` 子类的实例，以实现自定义窗口内容。它使得 `TeachingTip` 更加灵活，适用于复杂的提示或操作界面。

**主要功能**：

- **替代组件**: 自定义弹出组件
- **主要接口**: 继承 `FlyoutViewBase` 并在子类中添加自定义布局和组件，`TeachingTip.make()` 方法用于显示自定义气泡弹窗。
- **自定义样式**: 支持添加复杂布局和自定义内容，适用于需要高定制化的气泡弹窗。

**应用场景**：适用于需要展示复杂自定义内容的提示或操作界面，如详细操作引导、复杂信息提示等。

**示例代码**：

```python
class CustomFlyoutView(FlyoutViewBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = BodyLabel('这是一场「试炼」，我认为这就是一场为了战胜过去的「试炼」，\n只有战胜了那些幼稚的过去，人才能有所成长。')
        self.button = PrimaryPushButton('Action')

        self.button.setFixedWidth(140)
        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.button)

    def paintEvent(self, e):
        # 不绘制边框和背景
        pass

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = PushButton("Click Me", self)
        self.button.clicked.connect(self.showTeachingTip)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.resize(600, 500)

    def showTeachingTip(self):
        TeachingTip.make(
            target=self.button,
            view=CustomFlyoutView(),
            tailPosition=TeachingTipTailPosition.RIGHT,
            duration=2000,
            parent=self
        )
```

------

#### **FlowLayout**

**FlowLayout** 是一个自适应视口宽度的流式布局组件，当内部组件超出视口宽度时自动换行。它适合用于布局大小不固定且需要动态调整的场景。

**主要功能**：

- **替代组件**: `QVBoxLayout`, `QHBoxLayout`
- **主要接口**: `setAnimation()` 方法可设置动画参数，`removeAllWidgets()` 方法可移除所有组件。
- **自定义样式**: 支持自定义间距、边距及动画效果。

**应用场景**：适用于需要灵活布局、自动换行的场合，如图片库、标签云等。

**示例代码**：

```python
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        layout = FlowLayout(self, needAni=True)  # 启用动画

        # 自定义动画参数
        layout.setAnimation(250, QEasingCurve.OutQuad)

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setVerticalSpacing(20)
        layout.setHorizontalSpacing(10)

        layout.addWidget(QPushButton('aiko'))
        layout.addWidget(QPushButton('刘静爱'))
        layout.addWidget(QPushButton('柳井爱子'))
        layout.addWidget(QPushButton('aiko 赛高'))
        layout.addWidget(QPushButton('aiko 太爱啦😘'))

        self.resize(250, 300)

# 在某些情况下，流式布局中的组件可能发生重叠，可使用下述方法强制刷新布局：

# 移除全部组件
flowLayout.removeAllWidgets()

# 重新添加组件
for w in widgets:
    flowLayout.addWidget(w)
```

------

#### **CardWidget**

**CardWidget** 是一个灵活的卡片组件，常用于以结构化和美观的方式展示各种类型的信息和内容。它是一个容器组件，可用于放置任意组件，并且支持点击事件。

**主要功能**：

- **替代组件**: 自定义实现
- **主要接口**: `setBorderRadius()` 方法可设置卡片的圆角大小，`clicked` 信号可响应点击事件。
- **自定义样式**: 支持自定义标题、内容、按钮等，适用于展示丰富信息的场景。

**应用场景**：适用于展示结构化信息的场合，如用户档案卡片、产品介绍卡片等。

**示例代码**：

```python
class AppCard(CardWidget):

    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton('Open', self)
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)

# 点击 CardWidget 会发送 clicked 信号
card = AppCard(
    icon=":/qfluentwidgets/images/logo.png",
    title="PyQt-Fluent-Widgets",
    content="Shokokawaii Inc."
)
card.clicked.connect(lambda: print("点击卡片"))

# 默认圆角大小为 5px，下述代码调整为 8px
card.setBorderRadius(8)
```

------

#### **SimpleCardWidget**

**SimpleCardWidget** 是 `CardWidget` 的子类，与 `CardWidget` 唯一的区别是 `SimpleCardWidget` 的背景不会随着鼠标进入或退出而变化。它适合用于不需要视觉反馈的场景。

------

#### **ElevatedCardWidget**

**ElevatedCardWidget** 是带阴影效果的卡片组件，当鼠标移入时，会显示阴影和上移动画。它常用于需要强调的内容展示场景。

**主要功能**：

- **替代组件**: 自定义实现
- **主要接口**: `setFixedSize()` 方法可设置卡片的固定大小，支持添加图标和标签。
- **自定义样式**: 支持阴影和动画效果，适用于突出展示的卡片内容。

**应用场景**：适用于需要在页面上突出展示的内容，如推荐产品、重要信息卡片等。

**示例代码**：

```python
class EmojiCard(ElevatedCardWidget):

    def __init__(self, iconPath: str, name: str, parent=None):
        super().__init__(parent)
        self.iconWidget = ImageLabel(iconPath, self)
        self.label = CaptionLabel(name, self)

        self.iconWidget.scaledToHeight(68)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.iconWidget, 0, Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.setFixedSize(168, 176)
```

------

#### **HeaderCardWidget**

**HeaderCardWidget** 是带标题的卡片组件，通常用于替代 `QGroupBox`。它内置了水平布局，用户只需将组件添加到 `viewLayout` 中即可完成布局。

**主要功能**：

- **替代组件**: `QGroupBox`
- **主要接口**: `setTitle()` 方法可设置卡片标题，支持自定义布局和内容。
- **自定义样式**: 支持标题、内容和按钮等自定义，适用于展示带标题的结构化信息。

**应用场景**：适用于展示带标题的分组信息，如系统要求、功能模块等。

**示例代码**：

```python
class SystemRequirementCard(HeaderCardWidget):
    """ System requirements card """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('系统要求')

        self.infoLabel = BodyLabel('此产品适用于你的设备。具有复选标记的项目符合开发人员的系统要求。', self)
        self.successIcon = IconWidget(InfoBarIcon.SUCCESS, self)
        self.detailButton = HyperlinkLabel('详细信息', self)

        self.vBoxLayout = QVBoxLayout()
        self.hBoxLayout = QHBoxLayout()

        self.successIcon.setFixedSize(16, 16)
        self.hBoxLayout.setSpacing(10)
        self.vBoxLayout.setSpacing(16)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.hBoxLayout.addWidget(self.successIcon)
        self.hBoxLayout.addWidget(self.infoLabel)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.detailButton)

        self.viewLayout.addLayout(self.vBoxLayout)
```

------

#### **GroupHeaderCardWidget**

**GroupHeaderCardWidget** 是一个带有分组功能的卡片组件，允许用户通过 `addGroup()` 方法将组件添加到新分组中。分组会被存放在垂直布局 `vBoxLayout` 中，适用于展示多层次的结构化信息。

**主要功能**：

- **替代组件**: 自定义实现
- **主要接口**: `addGroup()` 方法可添加分组内容，支持自定义分组标题和内容。
- **自定义样式**: 支持多分组展示和自定义布局，适用于展示复杂信息的场景。

**应用场景**：适用于展示分层次的设置选项或信息，如应用设置、分步骤操作指南等。

**示例代码**：

```python
class SettinsCard(GroupHeaderCardWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("基本设置")
        self.setBorderRadius(8)

        self.chooseButton = PushButton("选择")
        self.comboBox = ComboBox()
        self.lineEdit = SearchLineEdit()

        self.hintIcon = IconWidget(InfoBarIcon.INFORMATION)
        self.hintLabel = BodyLabel("点击编译按钮以开始打包 👉")
        self.compileButton = PrimaryPushButton(FluentIcon.PLAY_SOLID, "编译")
        self.openButton = PushButton(FluentIcon.VIEW, "打开")
        self.bottomLayout = QHBoxLayout()

        self.chooseButton.setFixedWidth(120)
        self.lineEdit.setFixedWidth(320)
        self.comboBox.setFixedWidth(320)
        self.comboBox.addItems(["始终显示（首次打包时建议启用）", "始终隐藏"])
        self.lineEdit.setPlaceholderText("输入入口脚本的路径")

        # 设置底部工具栏布局
        self.hintIcon.setFixedSize(16, 16)
        self.bottomLayout.setSpacing(10)
        self.bottomLayout.setContentsMargins(24, 15, 24, 20)
        self.bottomLayout.addWidget(self.hintIcon, 0, Qt.AlignLeft)
        self.bottomLayout.addWidget(self.hintLabel, 0, Qt.AlignLeft)
        self.bottomLayout.addStretch(1)
        self.bottomLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.bottomLayout.addWidget(self.compileButton, 0, Qt.AlignRight)
        self.bottomLayout.setAlignment(Qt.AlignVCenter)

        # 添加组件到分组中
        self.addGroup("resource/Rocket.svg", "构建目录", "选择 Nuitka 的输出目录", self.chooseButton)
        self.addGroup("resource/Joystick.svg", "运行终端", "设置是否显示命令行终端", self.comboBox)
        group = self.addGroup("resource/Python.svg", "入口脚本", "选择软件的入口脚本", self.lineEdit)
        group.setSeparatorVisible(True)

        # 添加底部工具栏
        self.vBoxLayout.addLayout(self.bottomLayout)
```

------

#### **RoundMenu**

**RoundMenu** 是一个用于提供一系列动作供用户选择的菜单组件，使用方式与 `QMenu` 类似。支持自定义菜单项、子菜单，并可以添加自定义组件。

**主要功能**：

- **替代组件**: `QMenu`
- **主要接口**: `addAction()` 方法添加菜单项，`addMenu()` 方法添加子菜单，`addSeparator()` 方法添加分割线。
- **自定义样式**: 支持自定义菜单项图标、子菜单和自定义组件。

**应用场景**：适用于需要提供一系列可选操作的场合，如右键菜单、工具栏菜单等。

**示例代码**：

```python
menu = RoundMenu()

# 逐个添加动作，Action 继承自 QAction，接受 FluentIconBase 类型的图标
menu.addAction(Action(FluentIcon.COPY, '复制', triggered=lambda: print("复制成功")))
menu.addAction(Action(FluentIcon.CUT, '剪切', triggered=lambda: print("剪切成功")))

# 批量添加动作
menu.addActions([
    Action(FluentIcon.PASTE, '粘贴'),
    Action(FluentIcon.CANCEL, '撤销')
])

# 添加分割线
menu.addSeparator()

menu.addAction(QAction('全选', shortcut='Ctrl+A'))

# 添加子菜单
submenu = RoundMenu("添加到", self)
submenu.setIcon(FluentIcon.ADD)
submenu.addActions([
    Action(FluentIcon.VIDEO, '视频'),
    Action(FluentIcon.MUSIC, '音乐'),
])

menu.addMenu(submenu)
```

**添加自定义组件**：

```python
class ProfileCard(QWidget):
    """ Profile card """

    def __init__(self, avatarPath: str, name: str, email: str, parent=None):
        super().__init__(parent=parent)
        self.avatar = AvatarWidget(avatarPath, self)
        self.nameLabel = BodyLabel(name, self)
        self.emailLabel = CaptionLabel(email, self)
        self.logoutButton = HyperlinkButton('https://qfluentwidgets.com/', '注销', self)

        self.setFixedSize(307, 82)
        self.avatar.setRadius(24)

class Demo(QWidget):

    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e) -> None:
        menu = RoundMenu(parent=self)

        # add custom widget
        card = ProfileCard('resource/shoko.png', '硝子酱', 'shokokawaii@outlook.com', menu)
        menu.addWidget(card, selectable=False)

        menu.addSeparator()
        menu.addActions([
            Action(FluentIcon.PEOPLE, '管理账户和设置'),
            Action(FluentIcon.SHOPPING_CART, '支付方式'),
            Action(FluentIcon.CODE, '兑换代码和礼品卡'),
        ])
        menu.addSeparator()
        menu.addAction(Action(FluentIcon.SETTING, '设置'))
        menu.exec(e.globalPos())
```

------

#### **CheckableMenu**

**CheckableMenu** 是一个支持勾选功能的菜单组件，通常与 `QActionGroup` 一起使用，以提供多选或单选功能。

**主要功能**：

- **替代组件**: `QMenu` + `QActionGroup`
- **主要接口**: `addAction()` 方法添加可选动作，支持设置勾选状态。
- **自定义样式**: 支持设置单选和多选菜单项的图标和行为。

**应用场景**：适用于需要提供多选或单选菜单选项的场合，如文件排序、视图过滤器等。

**示例代码**：

```python
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.createTimeAction = Action(FluentIcon.CALENDAR, "创建日期", checkable=True)
        self.shootTimeAction = Action(FluentIcon.CAMERA, "拍摄日期", checkable=True)
        self.modifiedTimeAction = Action(FluentIcon.EDIT, "修改日期", checkable=True)
        self.nameAction = Action(FluentIcon.FONT, "名字", checkable=True)

        self.ascendAction = Action(FluentIcon.UP, "升序", checkable=True)
        self.descendAction = Action(FluentIcon.DOWN, "降序", checkable=True)

        # 将动作添加到动作组
        self.actionGroup1 = QActionGroup(self)
        self.actionGroup1.addAction(self.createTimeAction)
        self.actionGroup1.addAction(self.shootTimeAction)
        self.actionGroup1.addAction(self.modifiedTimeAction)
        self.actionGroup1.addAction(self.nameAction)

        self.actionGroup2 = QActionGroup(self)
        self.actionGroup2.addAction(self.ascendAction)
        self.actionGroup2.addAction(self.descendAction)

    def contextMenuEvent(self, e):
        menu = CheckableMenu(parent=self, indicatorType=MenuIndicatorType.RADIO)

        menu.addActions([
            self.createTimeAction, self.shootTimeAction,
            self.modifiedTimeAction, self.nameAction
        ])
        menu.addSeparator()
        menu.addActions([self.ascendAction, self.descendAction])

        menu.exec(e.globalPos(), aniType=MenuAnimationType.DROP_DOWN)
```

------

#### **SystemTrayMenu**

**SystemTrayMenu** 是一个用于系统托盘的菜单组件，通常与 `QSystemTrayIcon` 一起使用，为用户提供快捷操作入口。

**主要功能**：

- **替代组件**: `QSystemTrayIcon`
- **主要接口**: `addAction()` 方法添加菜单项，`setContextMenu()` 方法设置托盘菜单。
- **自定义样式**: 支持自定义菜单项的图标和行为，适用于托盘快捷操作。

**应用场景**：适用于需要在系统托盘中提供快捷操作入口的场合，如应用控制菜单、快捷设置菜单等。

**示例代码**：

```python
class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setIcon(parent.windowIcon())

        self.menu = SystemTrayMenu(parent=parent)
        self.menu.addActions([
            Action('🎤   唱'),
            Action('🕺   跳'),
            Action('🤘🏼   RAP'),
            Action('🎶   Music'),
            Action('🏀   篮球', triggered=self.ikun),
        ])
        self.setContextMenu(self.menu)

    def ikun(self):
        print("""巅峰产生虚伪的拥护，黄昏见证真正的使徒 🏀

                       ⠰⢷⢿⠄
                   ⠀⠀⠀⠀⠀⣼⣷⣄
                   ⠀⠀⣤⣿⣇⣿⣿⣧⣿⡄
                   ⢴⠾⠋⠀⠀⠻⣿⣷⣿⣿⡀
                   ⠀⢀⣿⣿⡿⢿⠈⣿
                   ⠀⠀⠀⢠⣿⡿⠁⠀⡊⠀⠙
                   ⠀⠀⠀⢿⣿⠀⠀⠹⣿
                   ⠀⠀⠀⠀⠹⣷⡀⠀⣿⡄
                   ⠀⠀⠀⠀⣀⣼⣿⠀⢈⣧
        """)

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())
        self.label = QLabel('Right-click system tray icon', self)
        self.layout().addWidget(self.label)

        self.resize(500, 500)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))

        self.systemTrayIcon = SystemTrayIcon(self)
        self.systemTrayIcon.show()
```

------

#### **CommandBar**

**CommandBar** 是一个水平排列的动作栏，当动作过多以至于视口容纳不下时，CommandBar 会自动隐藏超出视口的动作到下拉菜单中。它是 QToolBar 的替代组件，提供类似的接口，并且支持更灵活的自定义。

**主要功能**：

- **替代组件**: QToolBar
- **主要接口**: `addAction()` 方法用于添加单个动作，`addActions()` 方法用于批量添加动作，`addSeparator()` 方法用于添加分隔符，`addHiddenAction()` 方法用于添加始终隐藏的动作。
- **自定义样式**: `setToolButtonStyle()` 方法可以设置按钮样式，支持图标与文本的排列方式。
- **应用场景**: 适用于需要提供多个操作按钮的场合，尤其是在空间有限的界面上，可以有效地管理超出空间的动作。

**示例代码**：

```python
commandBar = CommandBar()

# 逐个添加动作
commandBar.addAction(Action(FluentIcon.ADD, '添加', triggered=lambda: print("添加")))

# 添加分隔符
commandBar.addSeparator()

# 批量添加动作
commandBar.addActions([
    Action(FluentIcon.EDIT, '编辑', checkable=True, triggered=lambda: print("编辑")),
    Action(FluentIcon.COPY, '复制'),
    Action(FluentIcon.SHARE, '分享'),
])

# 添加始终隐藏的动作
commandBar.addHiddenAction(Action(FluentIcon.SCROLL, '排序', triggered=lambda: print('排序')))
commandBar.addHiddenAction(Action(FluentIcon.SETTING, '设置', shortcut='Ctrl+S'))

# 命令行可以添加自定义组件
button = TransparentDropDownPushButton(FluentIcon.MENU, 'Menu')
button.setFixedHeight(34)
setFont(button, 12)

menu = RoundMenu(parent=self)
menu.addActions([
    Action(FluentIcon.COPY, 'Copy'),
    Action(FluentIcon.CUT, 'Cut'),
    Action(FluentIcon.PASTE, 'Paste'),
    Action(FluentIcon.CANCEL, 'Cancel'),
    Action('Select all'),
])
button.setMenu(menu)

# 添加自定义组件
commandBar.addWidget(button)

# 默认情况下 CommandBar 只显示动作的图标，如需修改显示模式：
# 图标右侧显示文本
commandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# 图标底部显示文本
commandBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
```

------

#### **CommandBarView**

**CommandBarView** 是 CommandBar 的变体，通常与 Flyout 一起使用。它继承了 CommandBar 的大部分功能和接口，同时更适合在弹出窗口或侧边栏中显示。CommandBarView 提供了与 CommandBar 类似的接口，使得开发者可以轻松在弹出窗口中集成操作栏。

**主要功能**：

- **替代组件**: 传统工具栏和自定义操作栏。
- **主要接口**: `addAction()`、`addActions()`、`addHiddenAction()` 等方法与 CommandBar 一致，用于添加和管理动作。
- **自定义样式**: `resizeToSuitableWidth()` 方法可以自动调整 CommandBarView 的宽度以适应内容，确保界面布局美观。
- **应用场景**: 适用于在 Flyout 或其他弹窗中展示一系列操作按钮，如工具面板、快捷操作栏等。

**详细描述**：

- **添加动作**: 可以使用 `addAction()` 或 `addActions()` 方法将多个动作添加到 CommandBarView 中。每个动作可以通过 `FluentIcon` 设置图标，并且可以指定快捷键。
- **隐藏动作**: `addHiddenAction()` 方法允许将某些动作添加为隐藏状态，只有在特定条件下才会显示。
- **宽度调整**: `resizeToSuitableWidth()` 方法用于根据内容自动调整 CommandBarView 的宽度，确保在不同视口尺寸下的显示效果。
- **与 Flyout 的集成**: CommandBarView 通常与 Flyout 一起使用，可以通过 `Flyout.make()` 方法将 CommandBarView 嵌入到 Flyout 中，实现悬浮在页面上的操作栏。

**示例代码**：

```python
commandBar = CommandBarView()

# 添加操作按钮
commandBar.addAction(Action(FluentIcon.SHARE, 'Share'))
commandBar.addAction(Action(FluentIcon.SAVE, 'Save'))
commandBar.addAction(Action(FluentIcon.DELETE, 'Delete'))

# 添加隐藏的操作按钮
commandBar.addHiddenAction(Action(FluentIcon.APPLICATION, 'App', shortcut='Ctrl+A'))
commandBar.addHiddenAction(Action(FluentIcon.SETTING, 'Settings', shortcut='Ctrl+S'))

# 自动调整宽度以适应内容
commandBar.resizeToSuitableWidth()

# 创建目标按钮
target = PushButton("Click Me")

# 使用 Flyout 将 CommandBarView 嵌入弹窗中
Flyout.make(commandBar, target=target, parent=target, aniType=FlyoutAnimationType.FADE_IN)
```

**总结**：

CommandBarView 是一个灵活的操作栏组件，非常适合在弹出窗口或侧边栏中使用。通过与 Flyout 的无缝集成，它可以轻松在不同的界面中展示一系列操作按钮，满足复杂界面布局的需求。

------




