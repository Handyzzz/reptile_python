#!/Users/handyzzz/.venv/p352/bin python

import douban_group
from douban_group import splider_data
import write_to_file
from write_to_file import write_file


data_dic = douban_group.splider_data()

write_to_file.write_file(data_dic)

