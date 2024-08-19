import Modules.Note_modules as Note_modules
from Modules.Note_modules import CreateNote, WriteToNote, RenameNote, ChangeLinks, NoteConnection
import Modules.Summarization_module as Sum_module
import Modules.Keywords as Keywords
from datetime import datetime
start=datetime.now()

Keywords.keywordss("""Российские военные отразили три штурмовые атаки в направлении сел Ольговка, Русское и Черкасское Поречное. Там войска противника потеряли танк, боевую машину пехоты, две боевые бронированные машины и более 25 человек. Четырех украинских военнослужащих взяли в плен, отметили в Минобороны.""")

print(datetime.now()-start)