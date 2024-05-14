from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):
    fronEnd = State()
    backEnd = State()
    grafikDizayn = State()


class BackButtonStates(StatesGroup):
    level1 = State()
    level2 = State()
    level3 = State()

