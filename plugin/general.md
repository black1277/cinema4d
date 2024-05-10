## Общие сведения о плагинах в Cinema 4D

 Каждый плагин должен иметь суффикс ```.pyp``` или ```.pypv``` (для зашифрованных файлов). Когда Cinema 4D запускается, она находит в этой папке все файлы, заканчивающиеся на ```.pyp``` или ```.pypv``` , и запускает плагин.
Для того чтобы плагин мог взаимодействовать с программой и пользователем в нем нужно зарегистрировать хуки.
Все хуки плагинов построены на классах данных, полученных из [BaseData][1].  Эти классы данных содержат набор методов, вызываемых Cinema 4D. Пример из [MessageData][2]:
```python
class SampleData(plugins.MessageData):

    def CoreMessage(self, id, bc):
        pass
```
Для регистрации плагина в программе существует целый класс функций [Register*()][3] каждая из которых регистрирует свой тип плагина:
```python
c4d.plugins.RegisterBitmapLoaderPlugin(id, str, info, dat) # Регистрирует BitmapLoaderData плагин.

c4d.plugins.RegisterBitmapSaverPlugin(id, str, info, dat, suffix) # Регистрирует BitmapSaverData плагин.

c4d.plugins.RegisterCommandPlugin(id, str, info, icon, ...) # Регистрирует CommandData плагин.

c4d.plugins.RegisterDescription(id, str[, res]) # Регистрирует описание для идентификатора плагина.

c4d.plugins.RegisterFalloffPlugin(id, str, info, g, ...) # Регистрирует FalloffData плагин.

c4d.plugins.RegisterHiddenToken(key, help, example, hook) # Эта функция регистрирует скрытый токен, который не отображается в настройках рендеринга.

c4d.plugins.RegisterManagerInformation(id, str, info) # Регистрирует информацию менеджера для использования при регистрации ярлыков с помощью AddShortcut().

c4d.plugins.RegisterMessagePlugin(id, str, info, dat) # Регистрирует MessageData плагин.

c4d.plugins.RegisterNodePlugin(id, str, info, g, icon) # Регистрирует NodeData плагин.

c4d.plugins.RegisterObjectPlugin(id, str, g, ...[, ...]) # Регистрирует ObjectData плагин.

c4d.plugins.RegisterPluginHelpCallback(pluginid, callback) # Регистрирует обратный вызов для справочной поддержки плагина.

c4d.plugins.RegisterPreferencePlugin(id, g, name, ...) # Регистрирует новую настройку в диалоговом окне настроек Cinema 4D.

c4d.plugins.RegisterSceneLoaderPlugin(id, str, g, info, ...) # Регистрирует SceneLoaderData плагин.

c4d.plugins.RegisterSceneSaverPlugin(id, str, g, info, ...) # Регистрирует SceneSaverData плагин.

c4d.plugins.RegisterSculptBrushPlugin(id, str, info, icon, ...) # Регистрирует SculptBrushToolData.

c4d.plugins.RegisterShaderPlugin(id, str, info, g, ...) # Регистрирует ShaderData плагин.

c4d.plugins.RegisterTagPlugin(id, str, info, g, ...) # Регистрирует плагин TagData:

c4d.plugins.RegisterToken(key, help, example, hook) # Регистрирует новый токен, который можно использовать в имени файла рендеринга. Токен отображается в настройках рендеринга и может быть выбран пользователем.

c4d.plugins.RegisterToolPlugin(id, str, info, icon, ...) # Регистрирует ToolData плагин.
```
Типы плагинов:
```
    c4d.plugins.BasePlugin
    c4d.plugins.BaseData
        c4d.plugins.BitmapLoaderData
        c4d.plugins.BitmapSaverData
        c4d.plugins.CommandData
        c4d.plugins.FalloffData
        c4d.plugins.MessageData
        c4d.plugins.ToolData
        c4d.plugins.SculptBrushToolData
        c4d.plugins.NodeData
            c4d.plugins.TagData
            c4d.plugins.ObjectData
            c4d.plugins.ShaderData
            c4d.plugins.SceneLoaderData
            c4d.plugins.SceneSaverData
            c4d.plugins.PreferenceData
    c4d.plugins.BaseDrawHelp
    c4d.plugins.GeResource
    c4d.plugins.PriorityList
```

Пример регистрации плагина для NodeData:
```python
class SampleData(plugins.ObjectData):
    def GetVirtualObjects(self, op, hierarchyhelp):
        pass

plugins.RegisterObjectPlugin(id=PLUGIN_ID, str="PluginName",
                             g=SampleData, description="", icon=None,
                             info=c4d.OBJECT_GENERATOR)
```
Здесь:
 - ```PLUGIN_ID``` - уникальный номер плагина, который нужно получить зарегистрировавшись здесь - https://plugincafe.maxon.net/ Вводите в поле ввода название своего плагина и жмете кнопку GeneratePluginID
 - ```str``` - название вашего плагина
 - ```g``` - производный класс
 - ```description``` - имя файла ресурса описания, который будет использоваться для вашего плагина без расширения .res , например Oobjectname . Имя должно быть уникальным
 - ```icon``` - иконка плагина, может быть None
 - ```info``` - настройки плагина в виде флагов
Для загрузки иконки можно использовать функцию:
```python
def load_icon(fn):
    fn = os.path.join(os.path.dirname(__file__), fn)
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp.InitWith(fn)[0] == c4d.IMAGERESULT_OK:
        return bmp
    return None

PLUGIN_ICON = load_icon("res/icon.tif")
```

### Структура каталогов
```
myPlugin/
    myPlugin.pyp
    ...
    res/
        c4d_symbols.h
        description/
            myDescription.h
            myDescription.res
            ...
        dialogs/
            myDialog.res
            ...

        strings_en-US/
            c4d_strings.str
            description/
                myDescription.str
                ...
            dialogs/
                myDialog.str
                ...
            strings_de-DE/
            strings_ja-JP/
            ...
    myIcon.tif
```
Основной файл — ```myPlugin.pyp``` , в котором регистрируются перехватчики. Каталог ```res``` содержит ресурсы плагина, которые содержат диалоги, описания и строки. Для каждого описания существует файл ```.res``` с описанием и файл ```.h``` с перечислениями констант, используемых в описании. Каждый диалог содержится в отдельном файле ```.res```. Файл ```c4d_symbols.h``` должен содержать перечисления констант, используемых в файлах ```.res```.
Затем должен быть каталог с именем strings_xx-XX для каждого языка, который поддерживает плагин, согласно стандарту ISO 639-1 :
```
  Арабский: ar-AR
  Китайский: zh-CN
  Чешский: cs-CZ
  Немецкий: de-DE
  Итальянский: it-IT
  Корейский: ko-KR
  Японский: ja-JP
  Польский: pl-PL
  Русский: ru-RU
  Испанский: es-ES
  Французский: fr-FR
  Английский: en-US
```
Каждый из языковых каталогов должен содержать файл ```.str``` для каждого диалога и файл ```c4d_strings.str``` для других строк ресурсов.
Наконец, в папке плагина можно хранить любые другие файлы, например значки или логотипы. Доступ к ним можно легко получить с помощью ```__file__``` :
```python
dir, file = os.path.split(__file__)
```
Плагинам нужна специальная структура ресурсов, например, папка ```res``` , файл ```c4d_symbols.h``` и т. д., даже если эти файлы пусты или не содержат ничего полезного.



[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d.plugins/BaseData/index.html#c4d.plugins.BaseData
[2]: https://developers.maxon.net/docs/py/23_110/modules/c4d.plugins/BaseData/MessageData/index.html#c4d.plugins.MessageData
[3]: https://developers.maxon.net/docs/py/23_110/modules/c4d.plugins/index.html