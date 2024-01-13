"""! @brief  Исполнитель сценариев. 
Всеядный исполнитель. Ему достаточно отдать на растеразание инстанс поставщика - он все вытащит сам из файлов настроек.
Кроме того - он гибкий в сборе различных сценариев в рамках одного потсващика. Подробней о каждом способе описано в функциях
`run_scenario_files(), run_scenario_file(), run_scenarios(), run_scenario()` в модуле `executor`



 @section libs imports:
  - .executor (local)


"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .executor import run_scenario_files, run_scenario_file, run_scenarios, run_scenario
