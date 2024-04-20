# coding=utf-8
# 参数上下文
class Context:
    _store = "sport"
    _isHeadless = "是"
    _page = 1
    _configDir = ""

    def __init__(self, store, isHeadless, page, configDir):
        self._store = store
        self._is_headless = isHeadless
        self._page = page
        self._configDir = configDir

    def check_browser_headless(self):
        return self._is_headless == "是"

    def getStoreCode(self):
        return self._store

    def getConfigDir(self):
        return self._configDir

    def getPage(self):
        return self._page